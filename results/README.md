# Experimental results

These are the **original entity-level NER reports** exported by the AfriTune Fon XLM-RoBERTa experiment, not reconstructed values.

| Split | Precision (micro) | Recall (micro) | F1 (micro) | Entity support |
|---|---:|---:|---:|---:|
| Validation | 0.837050 | 0.876122 | **0.856140** | 557 |
| Test | 0.773958 | 0.809487 | **0.791324** | 1,307 |

## Held-out test by entity

| Entity | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| DATE | 0.655696 | 0.700000 | 0.677124 | 370 |
| LOC | 0.821429 | 0.895377 | 0.856810 | 411 |
| ORG | 0.746667 | 0.730435 | 0.738462 | 230 |
| PER | 0.879599 | 0.888514 | 0.884034 | 296 |

## Files

- [`ner_validation_report.csv`](ner_validation_report.csv): original validation entity-level metrics.
- [`ner_test_report.csv`](ner_test_report.csv): original held-out test entity-level metrics.

Metrics are from **one experiment**, not an average over multiple seeds. The test split was held out from model selection. Figures and other artifacts will be added after verifying their provenance and suitability for public release. Model checkpoints and raw datasets are not included.
