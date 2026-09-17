#!/usr/bin/env python3
"""Wire-level model identity probe (Volcengine Ark Agent Plan, 2026-09-17).

Sends one tiny request per model to the same endpoint and fingerprints the
envelope, not the answer:
  1. template offset   — prompt_tokens of a tiny request (chat-template overhead,
                         stable per model family)
  2. schema signature  — presence of message.encrypted_content (Seed-family mark)
  3. alias echo        — response.model vs requested model (gateway rewrite check)

Usage: ARK_PLAN_API_KEY=... python3 model-identity-wire-probe-2026-09.py
The key is read from the environment and never printed.
"""
import json, os, sys, urllib.request, urllib.error

BASE = "https://ark.cn-beijing.volces.com/api/plan/v3"
MODELS = ["doubao-seed-evolving", "deepseek-v4.1-flash", "deepseek-v4-flash"]

key = os.environ.get("ARK_PLAN_API_KEY")
if not key:
    sys.exit("set ARK_PLAN_API_KEY")

for m in MODELS:
    payload = {"model": m, "messages": [{"role": "user", "content": "hi"}], "max_tokens": 4}
    req = urllib.request.Request(BASE + "/chat/completions", method="POST",
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
        data=json.dumps(payload).encode())
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            d = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(m, "HTTP", e.code, e.read().decode()[:200]); continue
    msg = d.get("choices", [{}])[0].get("message", {})
    print(json.dumps({
        "requested": m,
        "echo": d.get("model"),
        "prompt_tokens": d.get("usage", {}).get("prompt_tokens"),
        "has_reasoning_content": bool(msg.get("reasoning_content")),
        "has_encrypted_content": bool(msg.get("encrypted_content")),
    }, ensure_ascii=False))
