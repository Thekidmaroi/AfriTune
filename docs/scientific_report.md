# AfriTune — Fon NER Scientific Report

## Experimental setup

This preliminary single-run experiment fine-tunes `FacebookAI/xlm-roberta-base` on the Fon split of MasakhaNER 2.0. The training, validation and test splits contain 4,343, 623 and 1,228 sentences, respectively. The task uses BIO labels for DATE, LOC, ORG and PER.

Word-level labels are assigned to first subtokens; other subtokens are masked with `-100`. Maximum sequence length is 256. The model was trained for three epochs on a Tesla T4 with learning rate 2e-5, per-device batch size 4, gradient accumulation 4, weight decay 0.01, FP16, and seed 42. The best checkpoint was selected using validation entity-level F1.

## Results

| Metric | Value |
|---|---:|
| Validation entity-level micro-F1 | 0.856140 |
| Test entity-level micro-precision | 0.773958 |
| Test entity-level micro-recall | 0.809487 |
| Test entity-level micro-F1 | **0.791324** |
| Test token accuracy | 0.982038 |
| Test loss | 0.075865 |

| Entity | Test F1 |
|---|---:|
| DATE | 0.6771 |
| LOC | 0.8568 |
| ORG | 0.7385 |
| PER | 0.8840 |

Entity-level metrics were computed using `seqeval`. These are results from one run and are not a state-of-the-art claim.

## Limitations

Variance across random seeds, comparisons with other baselines, a pinned dataset revision, a dependency lockfile and a fresh-environment reproduction are not yet available. Model weights and training checkpoints are stored separately. Data and model redistribution rights must be reviewed before release.
