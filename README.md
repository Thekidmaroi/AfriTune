# AfriTune 🌍

**Reproducibility-focused NLP research for African languages.**

AfriTune's first experiment fine-tunes **XLM-RoBERTa Base** for **Fon Named Entity Recognition** using the Fon portion of **MasakhaNER 2.0**.

## Experimental results

| Model | Validation entity-level F1 | Held-out test entity-level F1 |
|---|---:|---:|
| XLM-RoBERTa Base | 85.61% | **79.13%** |

Test entity-level micro-precision: **77.40%**; micro-recall: **80.95%**. The results come from **one training run** (seed 42), not a state-of-the-art comparison.

| Entity type | Test F1 |
|---|---:|
| DATE | 67.71% |
| LOC | 85.68% |
| ORG | 73.85% |
| PER | 88.40% |

## Method

- **Data:** 4,343 train / 623 validation / 1,228 test sentences.
- **Labels:** BIO tagging for DATE, LOC, ORG, and PER (nine tags including O).
- **Backbone:** `FacebookAI/xlm-roberta-base`.
- **Tokenization:** first-subtoken labeling; other subtokens and special tokens ignored (`-100`).
- **Maximum length:** 256 subtokens.
- **Training:** 3 epochs, learning rate 2e-5, batch size 4, gradient accumulation 4, weight decay 0.01, FP16 on Tesla T4.
- **Checkpoint selection:** highest validation entity-level F1; test evaluated separately.

## Documentation

See [the preliminary scientific report](docs/scientific_report.md) for the methodology, results, error analysis, and limitations.

## Release status

**Initial documentation release.** The reviewed, fully English Colab notebook, dependency lockfile, verified dataset revision, and figures are being prepared. The model weights (~1.05 GiB) and training checkpoints are not hosted in this repository. The absence of these assets means that end-to-end reproduction has **not yet been verified** from this repository.

This is a baseline from one experiment, not a benchmark ranking or claim of novelty. Dataset redistribution and licensing terms will be reviewed before any datasets or model weights are published.
