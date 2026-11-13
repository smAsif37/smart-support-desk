"""Dataset preparation shared by training and evaluation (guarantees identical splits).

Improvements over the first notebook:
  * near-duplicate removal BEFORE splitting (Bitext is template-generated; duplicates leak into test)
  * extra OTHER class for out-of-scope messages
  * noisy copies (typos, lowercase, filler) of 30% of TRAIN examples for realism
  * proper 70/15/15 train/validation/test split, stratified and seeded
"""
import random
import re
from typing import List, Tuple

from .oos_data import build_oos, split_oos_cores

DATASET = "bitext/Bitext-customer-support-llm-chatbot-training-dataset"
OOS_LABEL = "OTHER"
FILLERS_PRE = ["hi, ", "hello team, ", "pls help: ", "hey ", "urgent - ", "sir/madam, ", "hi support, "]
FILLERS_POST = [" thanks", " please help", "!!", " asap", " ???", " regards"]


def norm_key(text: str) -> str:
    t = re.sub(r"\{\{[^}]*\}\}", " ", text.lower())
    t = re.sub(r"\d+", " ", t)
    return " ".join(re.sub(r"[^a-z ]", " ", t).split())


def dedupe(pairs: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    seen, out = set(), []
    for text, label in pairs:
        k = norm_key(text)
        if k and k not in seen:
            seen.add(k)
            out.append((text, label))
    return out


def add_noise(text: str, rng: random.Random) -> str:
    t = text.lower() if rng.random() < 0.6 else text
    words = t.split()
    for _ in range(rng.choice([0, 1, 1, 2])):
        if not words:
            break
        i = rng.randrange(len(words))
        w = words[i]
        if len(w) > 3:
            j = rng.randrange(len(w) - 1)
            op = rng.choice(["swap", "drop", "dup"])
            w = (w[:j] + w[j + 1] + w[j] + w[j + 2:] if op == "swap" else
                 w[:j] + w[j + 1:] if op == "drop" else w[:j] + w[j] + w[j:])
            words[i] = w
    t = " ".join(words)
    if rng.random() < 0.5:
        t = re.sub(r"[.,!?]", "", t)
    if rng.random() < 0.35:
        t = rng.choice(FILLERS_PRE) + t
    if rng.random() < 0.35:
        t = t + rng.choice(FILLERS_POST)
    return t


def build_splits(seed: int = 42, noise_frac: float = 0.3, n_oos: int = 600):
    """Returns (labels, train, val, test) where each split is a list of (text, label_id).

    Out-of-scope (OTHER) sentences are split by WHOLE SENTENCE, so validation/test OTHER examples are unseen.
    """
    from datasets import load_dataset
    from sklearn.model_selection import train_test_split
    rng = random.Random(seed)
    ds = load_dataset(DATASET, split="train")
    pairs = dedupe([(r["instruction"], r["category"]) for r in ds])
    labels = sorted({l for _, l in pairs} | {OOS_LABEL})
    l2i = {l: i for i, l in enumerate(labels)}
    texts = [t for t, _ in pairs]
    y = [l2i[l] for _, l in pairs]
    x_tr, x_tmp, y_tr, y_tmp = train_test_split(texts, y, test_size=0.30, stratify=y, random_state=seed)
    x_va, x_te, y_va, y_te = train_test_split(x_tmp, y_tmp, test_size=0.50, stratify=y_tmp, random_state=seed)

    groups, share, o = split_oos_cores(seed), {"train": 0.70, "val": 0.15, "test": 0.15}, l2i[OOS_LABEL]
    oos = {k: [(t, o) for t, _ in dedupe([(t, OOS_LABEL) for t in build_oos(int(n_oos * share[k]), seed, groups[k])])]
           for k in groups}
    tr = list(zip(x_tr, y_tr)) + oos["train"]
    noisy = [(add_noise(t, rng), l) for t, l in tr if rng.random() < noise_frac]
    train = tr + noisy
    rng.shuffle(train)
    return labels, train, list(zip(x_va, y_va)) + oos["val"], list(zip(x_te, y_te)) + oos["test"]
