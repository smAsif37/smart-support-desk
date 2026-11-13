"""Fine-tune DistilBERT as the ticket classifier (11 Bitext categories + OTHER).

Colab (free T4 GPU):
    !git clone https://github.com/<you>/smart-support-desk && cd smart-support-desk
    !pip install -q -r training/requirements-train.txt
    !python -m training.train_classifier --out ticket-classifier --push_to_hub <hf-user>/ticket-classifier
(for --push_to_hub log in first: from huggingface_hub import notebook_login; notebook_login())
"""
import argparse
import json
import time

import numpy as np
import torch
from datasets import Dataset
from sklearn.metrics import accuracy_score, f1_score
from transformers import (AutoModelForSequenceClassification, AutoTokenizer, DataCollatorWithPadding,
                          Trainer, TrainingArguments, set_seed)

from .data import build_splits

BASE = "distilbert-base-uncased"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="ticket-classifier")
    ap.add_argument("--epochs", type=int, default=3)
    ap.add_argument("--lr", type=float, default=3e-5)
    ap.add_argument("--batch", type=int, default=32)
    ap.add_argument("--max_length", type=int, default=128)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--push_to_hub", default="", help="e.g. username/ticket-classifier")
    a = ap.parse_args()

    set_seed(a.seed)
    labels, train, val, test = build_splits(a.seed)
    print(f"labels={labels}\ntrain={len(train)} val={len(val)} test={len(test)}")

    tok = AutoTokenizer.from_pretrained(BASE)
    def to_ds(rows):
        d = Dataset.from_dict({"text": [t for t, _ in rows], "label": [l for _, l in rows]})
        return d.map(lambda b: tok(b["text"], truncation=True, max_length=a.max_length), batched=True)
    d_tr, d_va = to_ds(train), to_ds(val)

    model = AutoModelForSequenceClassification.from_pretrained(
        BASE, num_labels=len(labels),
        id2label={i: l for i, l in enumerate(labels)}, label2id={l: i for i, l in enumerate(labels)})

    def metrics(p):
        pred = p.predictions.argmax(-1)
        return {"accuracy": accuracy_score(p.label_ids, pred),
                "macro_f1": f1_score(p.label_ids, pred, average="macro")}

    args = TrainingArguments(
        output_dir="outputs", num_train_epochs=a.epochs, learning_rate=a.lr,
        per_device_train_batch_size=a.batch, per_device_eval_batch_size=64,
        eval_strategy="epoch", save_strategy="epoch", load_best_model_at_end=True,
        metric_for_best_model="macro_f1", save_total_limit=1, weight_decay=0.01,
        fp16=torch.cuda.is_available(), seed=a.seed, report_to="none", logging_steps=50)
    trainer = Trainer(model=model, args=args, train_dataset=d_tr, eval_dataset=d_va,
                      processing_class=tok, data_collator=DataCollatorWithPadding(tok), compute_metrics=metrics)
    t0 = time.time()
    trainer.train()
    secs = time.time() - t0

    trainer.save_model(a.out)
    tok.save_pretrained(a.out)
    json.dump({"base_model": BASE, "labels": labels, "train": len(train), "val": len(val), "test": len(test),
               "epochs": a.epochs, "lr": a.lr, "batch": a.batch, "max_length": a.max_length, "seed": a.seed,
               "train_seconds": round(secs, 1), "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu",
               "log_history": trainer.state.log_history}, open(f"{a.out}/training_summary.json", "w"), indent=2)
    print(f"Saved to {a.out} in {secs:.0f}s. Now run: python -m training.evaluate_classifier --model {a.out}")
    if a.push_to_hub:
        model.push_to_hub(a.push_to_hub)
        tok.push_to_hub(a.push_to_hub)
        print("Pushed to https://huggingface.co/" + a.push_to_hub)


if __name__ == "__main__":
    main()
