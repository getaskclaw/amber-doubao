# Wire-level identity probe: the doubao re-badge question, final verdict (2026-09-17)

中文：[model-identity-wire-probe-2026-09.md](model-identity-wire-probe-2026-09.md)

## Background

In the AMBER W38 full-library run, `doubao-seed-evolving` (Volcengine Ark Agent Plan; officially version-synced with Doubao-Seed-2.1-pro-0915) produced a nine-axis score fingerprint closest to the deepseek-flash family (all top-4 z-cosine neighbours were ds lanes). Score similarity proves behavioural resemblance only — it can neither prove nor rule out re-badging (the same model sold under a new name). This probe settles the question at the wire level.

## Method

Same subscription key, same endpoint (`/api/plan/v3`), same minimal request (`hi`), one call per model. We inspect the envelope, never the answer:

1. **Template-offset fingerprint**: `prompt_tokens` of a tiny request ≈ the fixed overhead of that model's chat template. Stable per model family; reproducible.
2. **Schema signature**: presence of `encrypted_content` in the response message (Volcengine Seed-family encrypted-reasoning mark).
3. **Alias echo**: request model X, read `response.model` — a gateway silently rewriting (you ask A, it serves B) shows up here.

Repro script: [model-identity-wire-probe-2026-09.py](model-identity-wire-probe-2026-09.py) (stdlib only; key via env var, never printed).

## Results

| requested model | echo (response.model) | prompt_tokens (`hi`) | encrypted_content |
|---|---|---|---|
| doubao-seed-evolving | doubao-seed-evolving (no rewrite) | 47 | **yes** |
| deepseek-v4.1-flash | deepseek-v4-1-flash | 31 | no |
| deepseek-v4-flash | deepseek-v4-flash-ga-260731 | 84 | no |

Stability re-run (`hi` → `hello there`): doubao 47/48, ds-v4.1 31/32 — offsets stable, each +1 token for the extra word.

## Verdict

**Re-badging: falsified.** Template fingerprints differ pairwise (47/31/84); `encrypted_content` is carried by doubao only; echoes report their true names. On the Ark endpoint, doubao-seed-evolving and its deepseek-flash offerings are different models. The tight AMBER score-fingerprint match is genuine capability-profile convergence (or similar training recipes), not a re-label.

Side observations: Ark's `deepseek-v4-flash` echo leaks the underlying build (`ga-260731`); plan-tier ds models are marked preview and intermittently 429 under load.

## Methodological lesson

Score-shape similarity ≠ identity. A cosine nearest-neighbour table can only raise suspicion; four cheap calls (template offset + schema field + echo) settle it. Run wire probes first, then decide whether a full-library head-to-head is worth the quota.
