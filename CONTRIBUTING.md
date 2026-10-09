# Contributing to AfriTune

Thank you for helping improve transparent NLP research for African languages.

## Before contributing

Read the [README](README.md), [reproducibility guide](docs/reproducibility.md), and [notebook audit](docs/notebook_audit.md). AfriTune currently documents **one** Fon NER training run; its published scores have not been independently reproduced.

## Suggested contributions

- Improve English documentation, code readability, and notebook portability.
- Identify methodological issues with a reproducible example.
- Improve dataset provenance, checksums, or environment reporting.
- Add carefully documented evaluation scripts or tests.
- Propose additional languages or experiments **without** representing them as completed results.

## Workflow

1. Open an issue describing the change and its scientific motivation.
2. Fork the repository and create a focused branch.
3. Make a small, reviewable change and document how it was checked.
4. Open a pull request using the repository template.
5. Clearly distinguish static inspection from executed tests.

Do not commit model weights, access tokens, private Drive paths, downloaded datasets, or large checkpoints. Do not change published metrics without traceable evaluation evidence. Never present illustrative or hard-coded values as new measurements.

## Research integrity

Report seeds, split definitions, dataset revision, hardware, package versions, evaluation protocol, and any deviation from the baseline. Preserve the original reported results; document new runs separately. Credit upstream dataset and model creators and respect their terms.

## License status

A repository license has **not yet been selected**. Public visibility alone does not grant permission to reuse or redistribute copyrighted material. Please discuss rights and contribution terms with the maintainers before submitting substantive code.
