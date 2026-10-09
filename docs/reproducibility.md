# Reproducibility guide (work in progress)

## Scope

This guide describes how to prepare an environment for the published [Fon NER Colab notebook](../AfriTune_Fon_NER_Public_English.ipynb). **The repository has not yet passed an end-to-end clean-environment reproduction test.** Reported validation and test scores come from one original training run, not from rerunning these instructions.

## Environment

1. Open the notebook in Google Colab and select a GPU runtime (the original run used a Tesla T4).
2. Execute the notebook's installation cell, or install the dependencies in [requirements.txt](../requirements.txt).
3. Restart the runtime if package changes require it, then run the environment-check cell and record the resolved package versions.
4. Execute the notebook in order. The dataset is downloaded from the MasakhaNER repository; no dataset files are redistributed here.

## Important version discrepancy

The notebook currently requests `transformers>=4.55,<5` and `datasets>=3,<5`. The original experiment metadata instead records `transformers==5.18.0`, `datasets==4.8.5`, `torch==2.11.0+cu130`, and `numpy==2.1.3`. **These are not an equivalent or verified set of environment constraints.** The requirements file reflects the notebook installation cell, not a reconstruction of the original environment. Do not describe it as a lockfile.

## Known methodological details

- Model: `FacebookAI/xlm-roberta-base`
- Dataset: MasakhaNER 2.0, Fon
- Splits: 4,343 training / 623 validation / 1,228 test sentences
- Random seed: 42
- Three training epochs; learning rate 2e-5; per-device batch size 4; gradient accumulation 4; FP16
- Best checkpoint selected by validation entity-level F1
- Held-out test entity-level micro-F1: 0.791324

## Before claiming exact reproducibility

- [ ] Resolve the recorded-versus-installed Transformers version mismatch.
- [ ] Pin the source dataset to a specific immutable revision and record checksums.
- [ ] Capture the full resolved dependency set and Python/CUDA environment.
- [ ] Confirm all notebook cells run sequentially in a fresh runtime.
- [ ] Compare newly produced validation/test metrics to the original reports.
- [ ] Review notebook paths, output artifacts, and English-language comments.

The original numerical evaluation files are in [results](../results/).
