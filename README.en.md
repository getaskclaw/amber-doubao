[简体中文](README.md) · English

# amber-doubao

> ⚠️ **Correction (2026-10-02, second)**: one defense-axis case, A-d511f9e8, is now NA on every lane (the exam room did not grade the file the candidate delivered, and the grader asks for something the task text does not say). The denominator and the **number of passed cases do not change**; every lane's total now carries `'`. In this repo's issue tables, read that cell as NA. Everything else stays as published; the [correction notice](https://github.com/getaskclaw/amber/blob/main/docs/corrections-2026-10-02-a-d511f9e8.en.md) governs.

> **2026-10-07 update**: A-cdc3d11a (review): On one review case the grader counted every sub-point of a well-formed finding as a separate unproven claim and treated real defects outside its short answer list as false alarms, so a correct, well-formatted review could not reach the passing line; the case is held on every lane, denominator unchanged, until the grader and exam room are repaired and the case is re-sat. This lane (doubao-seed-evolving @ Volcengine Ark Agent Plan) the cell goes from a loss to NA (held); the case moves from a loss to NA on 27 lanes and no sitting is re-run. The pass count is unchanged (17'/24 on the board); losses go 4→3 and NA 3→4; the review axis stays 1/2 with 1 NA. The cell is updated in the [W38 issue](results/2026-W38.md). See the [amber spec repo correction of 2026-10-07 (A-cdc3d11a)](https://github.com/getaskclaw/amber/blob/main/docs/corrections-2026-10-07-a-cdc3d11a.en.md).

Public AMBER benchmark results for Doubao models on Volcengine Ark — cases private, results public.
中文：[README.md](README.md)

## Scoreboard

<!-- scoreboard:start -->

![amber-doubao scoreboard: cases passed per axis for doubao-seed-evolving](results/assets/scoreboard.en.png?v=20261009)

| Group | Axis | What it tests | doubao-seed-evolving · [W38](results/2026-W38.md) |
|---|---|---|:-:|
| Building | Coding | Implement the spec correctly | 5/6 |
|  | Delivery | Done means handed in | 3/3 |
|  | Ops | Follow the runbook | 6/6 |
|  | Requirements | Ship A when A was asked | 1/1 |
|  | Convergence | Finish, don't spin | 1/1 |
| Judging | UI | Build the page to the mock | 0/1 |
|  | Vision | Spot defects in screenshots | 0/1 |
|  | Defense | Plug every hole in the validator | 0/2 · 2 NA |
|  | Attribution | Pin defects to their root cause | 0/1 · 1 NA |
|  | Review | Inspect someone else's work | 1/2 · 1 NA |
|  | **Total** |  | **17'/24** |

Each cell = cases passed / cases on that axis (a case is one scored task). NA = the case was voided or put on hold; it counts as neither a pass nor a fail, and a total carrying `'` contains at least one NA. Most axes hold only 1–2 cases, so one case moves the reading: do not over-read small gaps. All columns are from the same week (W38) and the test dates may differ; every number is a snapshot.

<!-- scoreboard:end -->

## What this is

- A 'lane' is one vendor's shop/API for a model name; a 'case' is one task, a 'run' is one sitting (a multi-variant case has several runs).

- One report per issue in `results/YYYY-Www.md`: same paper set, same harness (the program that runs the exam and scores it), full-library runs (23 cases / 26 papers).
- Each issue pins: library size and hashes, per-case scores and pass/fail, terminal states (how the run process exited), token usage and latency, environment fingerprint, and qualitative verdicts written under an evidence discipline.
- Cases, oracles, transcripts (full answer logs)s and intermediate artifacts are **never published** (see "Publication discipline").
- Sister repos: [amber-crof](https://github.com/getaskclaw/amber-crof), [amber-commandcode](https://github.com/getaskclaw/amber-commandcode), [amber-deepseek](https://github.com/getaskclaw/amber-deepseek), [amber-devin](https://github.com/getaskclaw/amber-devin), [amber-goldenpotato](https://github.com/getaskclaw/amber-goldenpotato), [amber-gpt](https://github.com/getaskclaw/amber-gpt), [amber-kimi](https://github.com/getaskclaw/amber-kimi), [amber-ollama](https://github.com/getaskclaw/amber-ollama), [amber-opencode](https://github.com/getaskclaw/amber-opencode), [amber-stepfun](https://github.com/getaskclaw/amber-stepfun), [amber-workbuddy](https://github.com/getaskclaw/amber-workbuddy).

## Publication discipline (red lines)

1. Published: scores and aggregates, token usage, speed, qualitative verdicts.
2. Never published: case content, oracles/scorers, transcripts, candidate workspaces, any intermediate that could reconstruct a paper.
3. Every issue pins: model ID, effort band (the thinking-effort setting), date (UTC), harness version, per-case content hash (bundle_sha (per-case content-hash fingerprint)), cross-checkable against the public hash index in [getaskclaw/amber](https://github.com/getaskclaw/amber).
4. Case identities stay private: public results reference cases only by stable aliases (A-xxxxxxxx, hash-derived) plus bundle hashes — internal case IDs, variant names and case descriptions never appear.
5. Tone: this is a community measurement, not an attack on the vendor. Data talks; wording stays restrained.

## Lane note

This repo benches the **Volcengine Ark Agent Plan** (subscription) lane. The plan's model catalog differs from pay-as-you-go: no version-pinned IDs; the only Doubao 2.1-pro-class entry is `doubao-seed-evolving` (officially synced to the latest version on release day). Scores are attributed to the exact wire name measured.

## A methodological caveat

Same model name, same provider, two runs can still score differently — sampling parameters, load and server-side versions drift; an `evolving` channel can even change brains when the vendor ships. Every conclusion here carries a date and a band. A single day's number is a snapshot, not a law.

## Results index

| Issue | Content | Verdict |
|---|---|---|
| [2026-W38](results/2026-W38.md) | doubao-seed-evolving (≡ 2.1-pro-0915, official sync) @ high, full-library debut | Case-level 16/23 ties the best published lane; build/text/ops/req-drift 97.9% top-tier, review/vision/ui-build net −2 liability, verify trio walled in the main sweep but all delivered under the 3600s makeup (addendum 1) |
| [Wire identity probe](docs/model-identity-wire-probe-2026-09.en.md) | Final verdict on the "doubao ≈ ds-flash re-badge" hypothesis | Falsified: template fingerprints 47/31/84 pairwise-distinct, encrypted_content on doubao only; score similarity = capability convergence, not a re-label |
| [2026-W38 correction notice](results/2026-W38-correction.en.md) | W38 full-library review: 0 cells reversed · 1 held here | 1 W38 main-table vision cell held |

## Disclaimer

Not affiliated with or sponsored by Volcengine/ByteDance. Scores are snapshots of a specific date and effort band, not purchasing advice.
