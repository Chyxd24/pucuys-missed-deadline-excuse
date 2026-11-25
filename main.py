"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one excuse (<=200 chars) to /output/entry.txt.
Stdlib only, no network, deterministic.
"""
import os

EXCUSE = (
    "Sorry I missed the deadline — I finished it, then re-ran the tests 400 times "
    "to be sure, and they've been green for 3 hours. I just liked watching them pass."
)

path = "/output/entry.txt"
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as fh:
    fh.write(EXCUSE)
with open(path, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == EXCUSE, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")