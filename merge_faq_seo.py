# -*- coding: utf-8 -*-
"""Merge full FAQ + seoBlock into index.json for all locales missing them."""
import json

with open("index.json", "r", encoding="utf-8") as f:
    data = json.load(f)

de_keys = set(data["de"].keys())
required = [k for k in sorted(data["de"].keys()) if k.startswith("faq.") or k.startswith("seoBlock.")]

# For any locale missing these keys, use EN as fallback (full text, no cut)
en = data["en"]
for loc in data:
    if loc in ("en", "de"):
        continue
    miss = [k for k in required if k not in data[loc]]
    if not miss:
        continue
    for k in required:
        if k not in data[loc]:
            data[loc][k] = en[k]

with open("index.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Verify
for loc in data:
    if loc in ("en", "de"):
        continue
    still = [k for k in required if k not in data[loc]]
    if still:
        print(loc, "still missing", still)
print("Done. All locales now have", len(required), "FAQ+seoBlock keys.")
