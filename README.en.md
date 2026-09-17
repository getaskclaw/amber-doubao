# amber-doubao

Public AMBER benchmark results for Doubao models on Volcengine Ark — cases private, results public.
中文：[README.md](README.md)

## What this is

- One report per issue in `results/YYYY-Www.md`: same paper set, same harness, full-library runs (23 cases / 26 papers).
- Each issue pins: library size and hashes, per-case scores and pass/fail, terminal states, token usage and latency, environment fingerprint, and qualitative verdicts written under an evidence discipline.
- Cases, oracles, transcripts and intermediate artifacts are **never published** (see "Publication discipline").

## Publication discipline (red lines)

1. Published: scores and aggregates, token usage, speed, qualitative verdicts.
2. Never published: case content, oracles/scorers, transcripts, candidate workspaces, any intermediate that could reconstruct a paper.
3. Every issue pins: model ID, effort band, date (UTC), harness version, per-case content hash (bundle_sha), cross-checkable against the public hash index in [getaskclaw/amber](https://github.com/getaskclaw/amber).
4. Case identities stay private: public results reference cases only by stable aliases (A-xxxxxxxx, hash-derived) plus bundle hashes — internal case IDs, variant names and case descriptions never appear.
5. Tone: this is a community measurement, not an attack on the vendor. Data talks; wording stays restrained.

## Lane note

This repo benches the **Volcengine Ark Agent Plan** (subscription) lane. The plan's model catalog differs from pay-as-you-go: no version-pinned IDs; the only Doubao 2.1-pro-class entry is `doubao-seed-evolving` (officially synced to the latest version on release day). Scores are attributed to the exact wire name measured.

## A methodological caveat

Same model name, same provider, two runs can still score differently — sampling parameters, load and server-side versions drift; an `evolving` channel can even change brains when the vendor ships. Every conclusion here carries a date and a band. A single day's number is a snapshot, not a law.

## Results index

| Issue | Content | Verdict |
|---|---|---|
| [2026-W38](results/2026-W38.md) | doubao-seed-evolving (≡ 2.1-pro-0915, official sync) @ high, full-library debut | Case-level 16/23 ties the best published lane; build/text/ops/req-drift 97.9% top-tier, review/vision/ui-build net −2 liability, all three verify cases zero-delivery at the harness wall |

## Disclaimer

Not affiliated with or sponsored by Volcengine/ByteDance. Scores are snapshots of a specific date and effort band, not purchasing advice.
