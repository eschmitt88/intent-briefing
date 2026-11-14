#!/usr/bin/env python3
"""Check docs/writing-guide.md for internal consistency.

The guide states each principle twice: once as a short rule, once with its
evidence. This check fails if the two copies disagree on the evidence tag,
or if a principle is missing from either section. Exit 1 on any mismatch.
"""
import pathlib, re, sys

text = pathlib.Path(__file__).resolve().parent.parent.joinpath("docs/writing-guide.md").read_text()
TAG = r"`\[(strong|moderate|weak|provisional|in-house)\]`"
try:
    rules = text.split("## The rules", 1)[1].split("\n## ", 1)[0]
    evidence = text.split("## Evidence", 1)[1].split("\n## ", 1)[0]
except IndexError:
    sys.exit("writing-guide.md: missing '## The rules' or '## Evidence' section")

def tags(section, item_re):
    out = {}
    for block in re.split(r"\n(?=\d+\. \*\*)", section):
        m = re.match(item_re, block.strip())
        if m:
            t = re.search(TAG, block)
            out[m.group(1)] = t.group(1) if t else None
    return out

rule_tags = tags(rules, r"\d+\. \*\*(P\d+):")
ev_tags = tags(evidence, r"(\d+)\. \*\*")
ev_tags = {f"P{k}": v for k, v in ev_tags.items()}

errors = []
for p in sorted(set(rule_tags) | set(ev_tags), key=lambda x: int(x[1:])):
    r, e = rule_tags.get(p, "MISSING"), ev_tags.get(p, "MISSING")
    if r != e or r is None:
        errors.append(f"{p}: rules={r} evidence={e}")
for e in errors:
    print(f"writing-guide mismatch: {e}")
print(f"checked {len(rule_tags)} rules / {len(ev_tags)} evidence entries")
sys.exit(1 if errors else 0)
