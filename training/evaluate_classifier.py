"""Full evaluation of the fine-tuned classifier. Produces everything the report needs.

    python -m training.evaluate_classifier --model ticket-classifier              # core metrics
    python -m training.evaluate_classifier --model ticket-classifier --baseline   # + zero-shot comparison (slow)

Outputs in reports/: metrics.json, classification_report.txt, confusion_matrix.png,
confidence_vs_accuracy.png, errors.txt   (+ markdown tables printed to the console).
"""
import argparse
import json
from pathlib import Path

import numpy as np
import torch
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report, f1_score
from transformers import pipeline

from .data import build_splits

HERE = Path(__file__).parent
DESCRIPTIONS = {  # natural-language label names for the zero-shot baseline
    "ACCOUNT": "account login, registration or password", "CANCEL": "cancellation fees", "CONTACT": "contacting customer service",
    "DELIVERY": "delivery options and delivery time", "FEEDBACK": "complaint or review", "INVOICE": "invoice or bill",
    "ORDER": "tracking, changing or cancelling an order", "PAYMENT": "payment methods or payment problems",
    "REFUND": "refund request or refund policy", "SHIPPING": "shipping address", "SUBSCRIPTION": "newsletter subscription",
    "OTHER": "unrelated to customer support"}


def predict(clf, texts, bs=64):
    out = clf(texts, batch_size=bs, truncation=True, max_length=128)
    return [o["label"] for o in out], np.array([o["score"] for o in out])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="ticket-classifier")
    ap.add_argument("--outdir", default="reports")
    ap.add_argument("--baseline", action="store_true")
    ap.add_argument("--baseline_n", type=int, default=300)
    a = ap.parse_args()
    out = Path(a.outdir); out.mkdir(exist_ok=True)

    labels, _, _, test = build_splits()
    texts, gold = [t for t, _ in test], [labels[i] for _, i in test]
    DEV = 0 if torch.cuda.is_available() else -1  # use the Colab GPU when present
    clf = pipeline("text-classification", model=a.model, device=DEV)
    pred, conf = predict(clf, texts)
    acc, f1 = accuracy_score(gold, pred), f1_score(gold, pred, average="macro")
    print(f"TEST accuracy={acc:.4f} macro-F1={f1:.4f} (n={len(gold)})")
    (out / "classification_report.txt").write_text(classification_report(gold, pred, digits=3))

    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(9, 8))
    ConfusionMatrixDisplay.from_predictions(gold, pred, labels=labels, xticks_rotation=60, ax=ax, colorbar=False)
    plt.tight_layout(); plt.savefig(out / "confusion_matrix.png", dpi=150); plt.close()
    errs = [f"gold={g} pred={p} conf={c:.2f} | {t}" for t, g, p, c in zip(texts, gold, pred, conf) if g != p]
    (out / "errors.txt").write_text("\n".join(errs) or "no errors")

    # messy, hand-written realistic messages (NOT from the synthetic dataset)
    messy = json.loads((HERE / "messy_test_set.json").read_text())
    mp, mc = predict(clf, [m[0] for m in messy])
    mg = [m[1] for m in messy]
    m_acc = accuracy_score(mg, mp)
    print(f"MESSY-SET accuracy={m_acc:.3f} (n={len(mg)})")
    for (t, g), p, c in zip(messy, mp, mc):
        if g != p:
            print(f"  wrong: gold={g} pred={p} conf={c:.2f} | {t[:80]}")

    # confidence calibration on the messy set + test set: choose the human-review threshold
    all_conf = np.concatenate([conf, mc]); all_ok = np.array([g == p for g, p in zip(gold + mg, pred + mp)])
    rows = []
    print("\n| Threshold | Auto-handled share | Accuracy of auto-handled | Sent to human |\n|---|---|---|---|")
    for th in [0.5, 0.6, 0.7, 0.8, 0.9]:
        keep = all_conf >= th
        r = (th, keep.mean(), all_ok[keep].mean() if keep.any() else float("nan"), 1 - keep.mean())
        rows.append(r); print(f"| {th:.1f} | {r[1]:.1%} | {r[2]:.1%} | {r[3]:.1%} |")
    plt.figure(figsize=(5, 3.5)); plt.plot([r[0] for r in rows], [r[2] for r in rows], marker="o", label="accuracy of auto-handled")
    plt.plot([r[0] for r in rows], [r[1] for r in rows], marker="s", label="share auto-handled")
    plt.xlabel("confidence threshold"); plt.legend(); plt.tight_layout(); plt.savefig(out / "confidence_vs_accuracy.png", dpi=150); plt.close()

    metrics = {"test_n": len(gold), "test_accuracy": acc, "test_macro_f1": f1, "messy_n": len(mg), "messy_accuracy": m_acc,
               "threshold_table": rows}
    if a.baseline:  # zero-shot baseline vs fine-tuned, same samples
        zs = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=DEV)
        names = list(DESCRIPTIONS); inv = {v: k for k, v in DESCRIPTIONS.items()}
        def zpred(ts): return [inv[zs(t, list(DESCRIPTIONS.values()))["labels"][0]] for t in ts]
        idx = np.random.RandomState(0).choice(len(texts), min(a.baseline_n, len(texts)), replace=False)
        zt, zg = [texts[i] for i in idx], [gold[i] for i in idx]
        z_acc = accuracy_score(zg, zpred(zt)); f_acc = accuracy_score(zg, [pred[i] for i in idx])
        zm = accuracy_score(mg, zpred([m[0] for m in messy]))
        print("\n| Model | Test sample acc | Messy-set acc |\n|---|---|---|")
        print(f"| Zero-shot BART-MNLI (no training) | {z_acc:.1%} | {zm:.1%} |\n| Fine-tuned DistilBERT | {f_acc:.1%} | {m_acc:.1%} |")
        metrics.update({"zero_shot_sample_acc": z_acc, "zero_shot_messy_acc": zm, "finetuned_sample_acc": f_acc})
    json.dump(metrics, open(out / "metrics.json", "w"), indent=2)
    print(f"\nSaved artefacts in {out}/  (screenshot the console tables + PNGs for the report)")


if __name__ == "__main__":
    main()
