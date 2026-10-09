# AfriTune roadmap

This roadmap is a **plan**, not a claim that the listed experiments have been completed.

## Phase 1 — Public baseline documentation

- [x] Publish English notebook and original Fon NER results.
- [x] Document model, data splits, training parameters, and limitations.
- [x] Add original charts and evaluation reports.
- [x] Identify an immutable upstream dataset reference and integrity checks.
- [x] Document the notebook's unresolved dependency mismatch.
- [x] Publish contributor guidance and repository citation instructions.

## Phase 2 — Verification and governance

- [ ] Confirm the original experiment's dataset commit and complete environment.
- [ ] Verify the notebook in a fresh GPU environment when compute is available.
- [ ] Add an exact dependency lockfile based on an executed environment.
- [ ] Review and select a code license with the rights holder.
- [ ] Verify upstream dataset/model terms before redistribution.
- [ ] Agree on maintainers, release policy, and citation metadata.
- [ ] Introduce automated static checks and non-GPU tests.

## Phase 3 — Scientific expansion

- [ ] Evaluate several random seeds and report variation.
- [ ] Perform qualitative error analysis with representative examples.
- [ ] Compare with appropriately selected baselines under the same evaluation protocol.
- [ ] Investigate additional African languages and transfer learning.
- [ ] Publish model artifacts only after rights, provenance, and release checks.

## Release gates

Do not label a release as *fully reproducible* without an independently executed clean-environment test. Do not claim state-of-the-art performance without a valid comparable benchmark.
