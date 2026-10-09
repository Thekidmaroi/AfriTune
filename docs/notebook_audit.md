# Notebook audit — Fon NER baseline

This audit is based on the **published 60-cell notebook** in the repository. It is a static inspection, **not an execution or reproduction claim**.

## Confirmed configuration

- The notebook downloads Fon train/dev/test files from the `main` branch of `masakhane-io/masakhane-ner`; the dataset revision is **not pinned**.
- An exploratory tokenizer section uses `max_length=128`, but a later cell **rebuilds** `tokenized_dataset` with `MAX_LENGTH=256`. The training and final test evaluation use this later variable. The earlier 128-token section is an analysis stage, not evidence that training used 128 tokens.
- The training arguments specify 3 epochs, learning rate 2e-5, batch size 4, gradient accumulation 4, weight decay 0.01, `eval_strategy="epoch"`, `save_strategy="epoch"`, and best-model selection by validation F1.
- Test evaluation uses `trainer.predict(tokenized_dataset["test"])` after training.

## Issues to resolve before a clean run

1. **Package version mismatch (high priority).** The installation cell specifies `transformers>=4.55,<5`, while the original metadata reports Transformers 5.18.0. A fresh environment has not been tested with either version.
2. **Mutable dataset source (high priority).** The URL references the upstream `main` branch. Record an immutable commit SHA and file checksums.
3. **English cleanup (documentation).** Some code comments, print messages, and plot labels remain in French despite the English notebook filename. Translation should not change code behavior.
4. **Static figures and metrics (scientific clarity).** At least one exploratory plot uses hard-coded truncation percentages, and the notebook includes a hard-coded results summary. These should be clearly marked as previously observed results, not automatically recomputed measurements.
5. **Notebook execution (high priority).** Execute every cell in order on a fresh Colab GPU runtime, capture package versions and outputs, and compare evaluation reports against the original files.
6. **Drive backup (portability).** The backup cell depends on Google Colab Drive mounting; this is optional for model training and should be identified as such.

## Safe next actions

- Preserve the original notebook as the historical experiment artifact.
- Prepare a reviewed reproduction notebook with pinned environment and dataset revision.
- Run it end-to-end and report whether the published metrics are reproduced.
- Only after successful verification label the environment as reproducible.

See [reproducibility.md](reproducibility.md) for the setup checklist and [original evaluation reports](../results/).
