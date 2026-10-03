---
date: "{{DATE}}"
timezone: "Europe/Berlin"
status: open
started_at: null
closed_at: null
updated_at: null
sessions: 0
active_session_id: null
---

# Study day — {{DATE}}

Copy only when days/{{DATE}}.md does not exist. Replace {{DATE}} with the actual Berlin date. Remove template guidance from the actual log. Same-date reopen appends to the existing file.

## Starting state

- Numbered verbs introduced / target (supplemental entries excluded):
- Latest requested activity and whether it is pending or completed:
- Historical source: live session / Backfilled from prior conversation.
- For backfill only: exact times and original session count may be unknown; do not fabricate them. Record a historical summary separately from live session sections. sessions counts the actual live sections, not estimated historical sessions.


- Verbs introduced and group statuses:
- Current grammar focus:
- Vocabulary snapshot and active mistakes:
- Continuation from previous day, including pending prompts:

## Sessions

Append once actual study starts:

### Session {{N}} — {{DATE}}-S{{NN}}

- Mode: full review / targeted review / continue / new session
- Status: active / paused / completed
- Started at:
- Ended at:
- Topics and material:
- New numbered verbs (batch of 10) / grammar / vocabulary actually introduced:
- Supplemental entries (excluded from numbered total):
- Old material reused in cumulative review:
- New vocabulary included in this review:
- Preferences changed:
- Next action:

| Exercise ID | Prompt | Learner's full answer | Correct full sentence | Explanation | Hint used? | Result / evidence |
| --- | --- | --- | --- | --- | --- | --- |

Use stable IDs; update an existing result rather than duplicate it on retry. Never insert example solutions as submitted learner answers.

## Pending exercises and continuation

- Unanswered prompts with IDs:
- Exact next step:
- Relevant curriculum or evidence references:

## Events

| Timestamp | Type | Details |
| --- | --- | --- |

Append open, continuation, pause, reopen, rollover, checkpoint, and close events as applicable. Preserve previous closures after reopening.

## End-of-day summaries

Append one summary per closure after new work:

### Closure {{N}}

- Closed at:
- Sessions included:
- Actual study completed:
- New material:
- Strengths evidenced:
- Mistakes and changes:
- Remaining practice:
- Next session starting point:
- Files updated (day, curriculum, mistakes, preferences if changed, CURRENT_STATE, progress.json, README dashboard if changed) and persistence result:

On closing set status: closed and preserve this summary. When actual study resumes on the same date, set reopened, append the next session, and preserve previous closures. Do not create a second date file. Repeating a close without new work must not duplicate this summary.

## Save status

Record whether local updates and remote saving succeeded; keep failed saves explicitly pending.
