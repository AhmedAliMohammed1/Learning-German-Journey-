#!/usr/bin/env python3
"""Validate German Journey repository invariants (Python standard library only)."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

def read(path):
    p = ROOT / path
    if not p.is_file():
        errors.append(f"Missing file: {path}")
        return ""
    return p.read_text(encoding="utf-8")

def rows(text, pattern):
    return [line.split("|")[1:-1] for line in text.splitlines() if re.match(pattern, line)]

def cell(value):
    return value.strip()

try:
    progress = json.loads(read("progress.json"))
except (json.JSONDecodeError, ValueError) as exc:
    sys.exit(f"ERROR: invalid progress.json: {exc}")

verb_lines = [[cell(c) for c in r] for r in rows(read("curriculum/verbs.md"), r"^\|\s*\d+\s*\|")]
vocab_lines = [[cell(c) for c in r] for r in rows(read("curriculum/vocabulary.md"), r"^\|\s*V\d+\s*\|")]
verb_items = progress["verbs"]["items"]
vocab_items = progress["vocabulary"]["items"]

if len(verb_lines) != len(verb_items) or len(verb_lines) != progress["verbs"]["learned_total"]:
    errors.append("Verb table / JSON inventory / learned_total counts disagree")
if len(vocab_lines) != len(vocab_items) or len(vocab_lines) != progress["vocabulary"]["registered_entries_count"]:
    errors.append("Vocabulary table / JSON inventory / register count disagree")

for i, (row, item) in enumerate(zip(verb_lines, verb_items), start=1):
    if len(row) < 7 or row[0] != str(i) or item.get("id") != i:
        errors.append(f"Verb ID mismatch at {i}")
    elif row[1] != item.get("infinitive") or row[6] != item.get("study_status"):
        errors.append(f"Verb name/status mismatch at {i}")

for i, (row, item) in enumerate(zip(vocab_lines, vocab_items), start=1):
    expected_id = f"V{i:03d}"
    if len(row) < 6 or row[0] != expected_id or item.get("id") != expected_id:
        errors.append(f"Vocabulary ID mismatch at {i}")
    elif row[1] != item.get("german") or row[5] != item.get("status"):
        errors.append(f"Vocabulary name/status mismatch at {i}")

for name, entries in (("verbs", [r[1] for r in verb_lines]), ("vocabulary", [r[1] for r in vocab_lines])):
    if len(entries) != len(set(entries)):
        errors.append(f"Duplicate {name} lemma in table")

day_paths = sorted((ROOT / "days").glob("????-??-??.md"))
documented_sessions = 0
today_content = None
for day_path in day_paths:
    data = day_path.read_text(encoding="utf-8")
    day = day_path.stem
    match = re.match(r"^---\s*\n([\s\S]*?)\n---", data)
    if not match:
        errors.append(f"{day}: missing frontmatter")
        continue
    props = dict((m.group(1), m.group(2).strip().strip('"'))
                 for line in match.group(1).splitlines()
                 if (m := re.match(r"^([a-z_]+):\s*(.*)$", line)))
    if props.get("date") != day:
        errors.append(f"{day}: date field mismatch")
    headings = [line for line in data.splitlines() if re.match(r"^#{2,3}\s+Session\b", line, re.I)]
    ids = set()
    for heading in headings:
        found = re.search(r"\b" + re.escape(day) + r"-S\d{2}\b", heading)
        if not found:
            errors.append(f"{day}: section has no canonical session ID")
        else:
            ids.add(found.group())
    try:
        n = int(props.get("sessions", "-1"))
    except ValueError:
        n = -1
    if n != len(headings) or n != len(ids):
        errors.append(f"{day}: metadata {n} sessions != {len(headings)} section headings / {len(ids)} IDs")
    documented_sessions += max(n, 0)
    if props.get("status") == "closed" and props.get("active_session_id") != "null":
        errors.append(f"{day}: closed day has an active session")
    if day == progress.get("current_day"):
        today_content = data
        if props.get("status") != progress.get("day_status"):
            errors.append("Current day status differs between day metadata and progress.json")
        if props.get("active_session_id") != (progress.get("current_session_id") or "null"):
            errors.append("Current day active session differs between day metadata and progress.json")

if documented_sessions != progress.get("sessions_recorded"):
    errors.append(f"Total documented sessions {documented_sessions} != progress.sessions_recorded {progress.get('sessions_recorded')}")
if today_content is None:
    errors.append("Missing current day file")

pending = progress.get("pending_exercises", [])
pending_ids = [x.get("id") for x in pending]
if len(pending_ids) != len(set(pending_ids)):
    errors.append("Duplicate pending exercise IDs")
target = progress.get("repository_integrity", {}).get("current_pending_exercise_id")
if target and not any(x.get("id") == target and x.get("status") == "pending" for x in pending):
    errors.append(f"Current pending exercise {target} is missing or not pending")
if progress.get("last_updated") != progress.get("current_day"):
    warnings.append("last_updated and current_day dates differ (can be normal across midnight)")

legacy = sum(not r.get("exercise_id") for r in progress.get("exercise_results", []))
if legacy:
    warnings.append(f"{legacy} historical exercise_results have no exercise_id; preserve source data, do not fabricate")
print(f"Verbs: {len(verb_lines)}, vocabulary: {len(vocab_lines)}, day files: {len(day_paths)}, sessions: {documented_sessions}")
for note in warnings:
    print("WARN:", note)
for error in errors:
    print("FAIL:", error)
if errors:
    sys.exit(1)
print("PASS: repository structural invariants verified")
