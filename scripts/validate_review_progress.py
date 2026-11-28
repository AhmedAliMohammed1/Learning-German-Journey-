#!/usr/bin/env python3
"""Validate comprehensive review v2 separately from legacy progress."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
def read(path):
    return json.loads((root / path).read_text(encoding="utf-8"))
index = read("review_progress/index.json")
order = read(index["order_path"])
plan = read(index["day_plan"])
assert sorted(order["verb_ids"]) == list(range(1, index["inventory"]["verbs"]+1))
assert sorted(order["vocabulary_ids"]) == [f"V{i:03d}" for i in range(1,index["inventory"]["vocabulary"]+1)]
assert index["session_id"] == plan["session_id"]
assert set(plan["verb_ids"]) <= set(order["verb_ids"])
assert set(plan["vocabulary_ids"]) <= set(order["vocabulary_ids"])
if index["active_batch"]:
    batch = read(index["active_batch"])
    assert batch["session_id"] == index["session_id"]
    assert batch["batch_id"] in plan["issued_batches"]
    assert len({p["exercise_id"] for p in batch["prompts"]}) == len(batch["prompts"])
    assert all(p["item_id"] in plan["verb_ids"] + plan["vocabulary_ids"] for p in batch["prompts"])
print("PASS: review v2 inventory and active checkpoint")
