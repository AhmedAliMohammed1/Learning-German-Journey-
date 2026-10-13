# Repository health and reconciliation

**Verified:** 2026-10-13 (Europe/Berlin). This is **repository maintenance only**, not another learner attempt, study session, mastery promotion or end-of-day event. The canonical live state is [progress.json](progress.json); raw study history remains under [days/](days/).

## Verified invariants

| Check | Result |
| --- | --- |
| JSON parses | **Pass** |
| Unified verb rows `curriculum/verbs.md` vs progress.json | **147 = 147**, sequential IDs 1–147 |
| Vocabulary rows `curriculum/vocabulary.md` vs progress.json | **171 = 171**, sequential V001–V171 |
| Duplicate verb lemmas or registered vocabulary labels | **None detected** |
| Exact ID, lemma, and status for each inventory row | **All rows match structured JSON** |
| Study day logs | **14 files**, dated 2026-09-30 through 2026-10-13 |
| Missing day frontmatter | **None** after normalizing Oct10–12 |
| Session sections and day-level `sessions` fields | **31 matching documented sessions** |
| `progress.sessions_recorded` | **31**, reconciled from day files |
| Day status and current session | **2026-10-13 open, S02 active**, matching day metadata |
| Next unanswered selected-review exercise | **2026-10-13-S02-E02**, still pending |
| Paused previous session | **2026-10-13-S01-E03**, still pending |
| Other dated unanswered exercises | Preserved; no completions manufactured |
| Current summaries and instructions | README, CURRENT_STATE, START_HERE, LEARNING_PROFILE and AGENTS point to the same state |
| Skills | Reading practicing; speaking, conversation and listening unassessed (no audio inferred) |

## Reconciliation performed

1. Replaced the long rolling README and CURRENT_STATE dashboards with **one live snapshot**, while preserving every old paragraph in [archive/README_before_2026-10-13_reconciliation.md](archive/README_before_2026-10-13_reconciliation.md) and [archive/CURRENT_STATE_before_2026-10-13_reconciliation.md](archive/CURRENT_STATE_before_2026-10-13_reconciliation.md). These archived snapshots are historical, not current instructions.
2. Updated START_HERE and AGENTS to read structured/daily evidence first; corrected the old handoff from paused S01 to active S02, the vocabulary tally from 170 to **171**, and the next task from S01-E03 to **S02-E02**.
3. Removed obsolete **100/100** and **supplemental verb** language from *current* policy and template. Text inside the historical Oct8 day log is annotated as superseded without rewriting learner history.
4. Aligned LEARNING_PROFILE and the MISTAKE_PATTERNS preamble to structured current statuses: weak **M32 / M34**, improving **M08 / M28**, stable **M13**. Older status labels below the preamble remain archival evidence.
5. Added `wenn` and `obwohl` to the grammar topic map; corrected `bevor` from introduced/pending to **practicing** after actual Oct12 written evidence.
6. Normalized YAML metadata for Oct10–12, added explicit historical session headings for Oct8 and Oct12, and cleared stale Oct9 `active_session_id` after rollover. Historical day statuses **open/reopened** were **not** fabricated as `closed`. Missing original timestamps stay `null`.
7. Reconciled `progress.sessions_recorded` to **31** documented session IDs and refreshed secondary stale fields `latest_study_date`, `latest_study_state`, `current_review_scope`, `last_verified_study_*`, and `next_suggested_action` from the already recorded Oct13 E01 study evidence.
8. Preserved all existing original learner answers and corrections. The current Oct13 E01 remains **not fully correct**: `sei` is a spelling slip for `sie` and `ihrem Kollegen` is required for “لزميلها”; Perfekt and verb-second were correct.

## Limits of older records (not silently repaired)

- Some old `progress.exercise_results` entries lack an `exercise_id` or a full raw answer, while `completed_exercise_ids` records dated completion. Do **not** generate artificial result objects or declare those attempts uncompleted. Use dated logs and explicit learner reports as the provenance.
- Sep30–Oct2 are **backfilled summaries**, not individually timed live sessions; their `sessions: 0` and null original times are expected. Oct8-S01 is a **documented historical session** with incomplete raw individual answers, so its session header is retained but no attempt scores invented.
- A historical archived README, archived CURRENT_STATE, or a section inside a daily log may say “latest” as of *its own date*; only the new top-level live dashboard and structured/daily state govern future continuation.
- Previous closed sessions within a later reopened day are a real history, not reason to close that day again. Do not create a new session just to run audits.

## Repeatable checks

Run the optional standard-library checker: `python scripts/validate_repo.py` from the checkout. It checks JSON, inventory counts/IDs/statuses, day metadata and section IDs, session totals, and the exact current exercise pointer.

When new study work is actually performed, synchronize `progress.json`, `days/YYYY-MM-DD.md`, `CURRENT_STATE.md`, curriculum/mistakes as needed, and the short README dashboard. If no study has happened, only update maintenance documentation; no new exercise ID is generated by maintenance.
