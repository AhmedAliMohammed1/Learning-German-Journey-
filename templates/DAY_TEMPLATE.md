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

- Mode: full_review / targeted_review / continue_previous_session / start_new_study_day / speaking / conversation / reading / listening
- Status: active / paused / completed
- Started at:
- Ended at:
- Topics and material:
- New numbered verbs (batch of 10) / grammar / vocabulary actually introduced:
- Supplemental entries (excluded from numbered total):
- Old material reused in cumulative review:
- New vocabulary included in this review:
- Preferences changed:
- Selected skill activity ID and reason for this difficulty:
- Available modalities: text / received audio / delivered audio; pronunciation assessment capability:
- Next action:

| Exercise ID | Prompt | Learner's full answer | Correct full sentence | Explanation | Hint used? | Result / evidence |
| --- | --- | --- | --- | --- | --- | --- |

Use stable IDs; update an existing result rather than duplicate it on retry. Never insert example solutions as submitted learner answers.

## Skill activities — append only when actually practised

### Activity {{ACTIVITY_ID}} — {{MODE}}

- Target and essential communicative/comprehension goals:
- Familiar verb/vocabulary IDs and grammar topic/mistake IDs:
- New vocabulary actually introduced and reused:
- Scenario / passage / Arabic prompts:
- Listening source content, delivery modality, and whether transcript was visible before the answer:
- Received response modality and whether original audio was actually assessed:
- Status: active / paused / completed.
- Immediate independent success:
- Delayed retention confirmed:
- Next action / remaining goals:

| Attempt / exercise ID | Learner response | Dimension | Result | Hints / replays / model shown | Correction and observed evidence |
| --- | --- | --- | --- | --- | --- |

Dimensions: comprehension, German production, grammar, vocabulary, pronunciation, fluency, or turn-taking as relevant. Results: independent_correct / correct_with_support / needs_retry / not_assessed. A transcript cannot supply pronunciation evidence; a silent text cannot supply listening evidence. An Arabic comprehension answer and an assisted German answer have separate results.

- Fresh transfer check after correcting:
- Mode-specific status/trend and evidence-linked reason:
- Review queue entry ID / target_key:
- Next due_on date (Europe/Berlin) and interval_index:
- Remaining activity preserved on mode switch or pause:

Use progress.skill_tracking and progress.review_queue. Keep one queue entry per mode + target; repeated saves reuse its ID. Initial delayed review schedule is next day, then 3 and 7 days after successful retests. Log failed or assisted retests honestly and adapt.

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
- Remaining practice and unfinished skill activities:
- Separate comprehension vs German production and audio-only assessment results:
- Skill review_queue dates, statuses, and reasons:
- Next session starting point:
- Files updated (day, curriculum, mistakes, preferences if changed, CURRENT_STATE, progress.json, README dashboard if changed) and persistence result:

On closing set status: closed and preserve this summary. When actual study resumes on the same date, set reopened, append the next session, and preserve previous closures. Do not create a second date file. Repeating a close without new work must not duplicate this summary.

## Save status

Record whether local updates and remote saving succeeded; keep failed saves explicitly pending.
