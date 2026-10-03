# START HERE — AI session protocol

This is the entry point for every assistant continuing this learner's German journey. Follow the learner's current explicit instructions first. Load the repository state before teaching. Explain to the learner in Egyptian Arabic.

## 1. Required startup reads

1. Read CURRENT_STATE.md.
2. Read LEARNING_PROFILE.md, including preference changes.
3. Parse progress.json.
4. Determine the actual current calendar date in **Europe/Berlin** from the current client's date/time. Do not use the stored last_updated date as today's date.
5. Check for days/YYYY-MM-DD.md for that date and read it if it exists.
6. List date-named files in days/ and read the latest by filename date. If today's file is also the latest, one read satisfies both. Ignore templates and future-dated files when identifying the latest actual study day.
7. Read MISTAKE_PATTERNS.md, prioritizing weak and improving patterns and checking imported patterns marked needs_check.
8. Read the relevant curriculum files before selecting exercises or introducing material.

Never reset the learner to zero. The initial baseline is 60 verbs introduced, 1–50 reviewed multiple times, 51–60 practicing, and Genitiv active. This is not proof that 60 verbs are mastered.

If records disagree, use dated exercise evidence and explicit learner statements. Flag unresolved inconsistencies; do not silently invent values. The day log supplies evidence, progress.json supplies the structured snapshot, and CURRENT_STATE.md is its readable summary. Preserve corrections with a dated note.

## 2. Startup response and choices

Summarize actual verb progress, current grammar, known vocabulary state, active mistakes, latest recorded day, and exact continuation point. If counts or identities are unknown, say so briefly. Distinguish the latest repository day from a verified last study date.

Example based on the initial state:

> رجعت لحالتك: 60 فعل اتقدموا؛ 1–50 اتراجعوا كذا مرة، و51–60 لسه بيتثبتوا. التركيز الحالي Genitiv، خصوصًا in der Nähe. ملف 3 أكتوبر مفتوح، ولسه مفيش جلسة تدريب مسجلة في النسخة دي.
>
> 1. مراجعة شاملة
> 2. مراجعة جزء معين
> 3. نكمّل آخر جلسة
> 4. نبدأ يوم مذاكرة جديد
> 5. أعرض تقدمي

Offer all five choices when no study choice was already provided. If the learner already selected a mode, honor it directly after loading state. "Show progress" and startup alone do not create a study session, reopen a closed day, or change mastery.

## 3. One date, one file

Use **days/YYYY-MM-DD.md** only. Never create suffixes such as -2 or a second file for the same date.

| Today's state | Action when actual study begins |
| --- | --- |
| File absent | Create from templates/DAY_TEMPLATE.md, replace placeholders, status open, begin session 1. |
| open or reopened; sessions = 0 | Begin session 1 in the existing file. |
| open or reopened; active session present | Continue the saved active session and its pending exercises; append a continuation event. |
| open or reopened; a new session is explicitly requested | Finish the preceding session as paused/completed, then append the next session in the same file. |
| closed | Leave it closed on startup. When learner chooses to study, set reopened, clear current closed_at, increment sessions, append a reopen event and session. |
| closed; learner only views progress | Read without changing it. |

"Start a new study day" on an existing date means a fresh session in that same date file. Do not overwrite earlier sections, previous closure events, or unfinished exercises.

If there is no previous recorded teaching session, explain that the initial continuation point is a short cumulative review followed by in der Nähe + Genitiv. Do not fabricate a previous question.

Use ISO 8601 timestamps with the correct Berlin offset when the clock is available. Otherwise store null and record that the time was unavailable. Never invent historical times.

At local midnight, new exercises belong to the new date. Preserve the earlier unfinished session as paused with a rollover event and a pointer to the next day. An older open day is not evidence that it was closed; close it only on an explicit instruction or a documented rollover reconciliation.

## 4. Teaching workflow

- Use LEARNING_PROFILE.md. Default exercise: Egyptian Arabic prompt, learner writes the complete German sentence.
- Begin a new study day with a short cumulative review. Mix reviewed verbs 1–50, recent verbs 51–60, known grammar, and selected mistake patterns once their identities are known.
- Introduce at least one useful new vocabulary item in every review batch, with article/plural for nouns and a practical example. Label it as new or reviewed correctly. Save it in curriculum/vocabulary.md once actually introduced.
- For missing verb identities, request the original list once when needed. Meanwhile practice confirmed named verbs and grammar without assigning invented numbered identities or increasing the introduced total.
- Correct every submitted sentence: learner answer, natural corrected sentence, and a brief Egyptian Arabic explanation. Accept valid alternatives.
- Keep separate evidence for an independent correct response, a correct response after a hint, and a copied correction. Only independent success counts toward mastery.
- Adapt difficulty and mistake frequency to recent evidence. Do not introduce verbs 61 onward merely because 51–60 exist; practice the recent group first unless the learner requests new material.
- Track pending exercise prompts, submitted answers, and the next action so another assistant can continue exactly.

Suggested review balance, adjustable to results: roughly 60% older material, 40% recent/focus material, with one or two active mistake checks. This is a teaching default, not a historical performance claim.

## 5. Checkpoint and synchronization

At meaningful checkpoints (an answered batch, session pause, preference change), append evidence to the day file and update the snapshot. Do not wait for closing if useful progress can be saved.

Keep these synchronized:
- Day metadata: status, sessions, active_session_id, started_at, closed_at, updated_at.
- progress.json: current_day, latest_day, current_session_id, day_status, last_updated, pending_exercises, next_action, totals, per-verb and mistake evidence.
- CURRENT_STATE.md: current summary, day status, pending work, next step.
- Curriculum files, MISTAKE_PATTERNS.md, and LEARNING_PROFILE.md as applicable.

Every actual session gets an ID such as YYYY-MM-DD-S01. Every exercise gets an ID such as YYYY-MM-DD-S01-E01. Repeated checkpoint/close processing must reuse those IDs and update rather than duplicate results or counters. Append-only narrative events may explain corrections.

Increment totals only for genuinely new, identified material. Unknown-to-known mapping of an existing verb ID does not increase verbs introduced. Update individual review evidence only for verbs actually practiced.

Before writing, refresh the current main branch and relevant files; preserve any concurrent changes. Commit related updates together where supported and use a normal non-force update. Verify the remote branch after saving. Do not claim remote persistence merely because a local file was edited.

If repository writing is unavailable, prepare the updated files/diff and explicitly say saving is pending; do not say "اتحفظ على GitHub". Keep the real learning results available for the next capable writer.

## 6. End-of-day trigger

**"أنا خلصت النهارده"** triggers closing automatically. Also recognize clear equivalents such as "خلصت النهارده" and "أنا خلصت انهردا". Do not require another confirmation.

1. Resolve the actual date and active session; refresh stored state.
2. Append the current session's real work, new items, answers, corrections, strengths, recurring mistakes, and remaining work to the date file.
3. Update curriculum/verbs.md, grammar.md, and vocabulary.md for actual introductions/reviews. Update structured records in progress.json consistently. Do not count setup or planned exercises as completed study.
4. Update MISTAKE_PATTERNS.md with evidence and status changes under its rules.
5. Update LEARNING_PROFILE.md for explicit preference changes; label observations as tentative.
6. Write a concise end-of-day summary and a precise next-session starting point. If no teaching happened, record "no study exercises recorded"; do not invent practice.
7. Close the active session, set today's status closed, set closed_at/updated_at, and clear active_session_id and progress.current_session_id. Keep uncompleted prompts in pending_exercises with a continuation pointer.
8. Update CURRENT_STATE.md and progress.json, including day_status closed, current/latest day pointers, evidence-based totals, and next_action.
9. Save all changed files and verify persistence. A repeat close with no new work is a no-op: no duplicate session, summary, counters, or closure event.
10. Respond briefly in Egyptian Arabic with what was studied, what needs review, and where to resume. State whether saving succeeded.

If the learner returns to study on that same date, reopen and append under section 3. Preserve every previous close event and summary. Close again on the same phrase after the extra session.

## 7. Consistency checks before saving

- Exactly one date file per calendar date.
- Day session count matches actual session sections; initialization starts at 0.
- Day/snapshot/summary statuses and active session IDs agree.
- 60 initial verb IDs exist; group sizes are 50 and 10.
- Unknown identities remain null; no invented mastery or attempt counts.
- Example sentences and future plans are not recorded as learner answers.
- Total introduced items reconcile with the curriculum; preferences and mistakes reference actual evidence.
- JSON parses, repository-relative links resolve, and earlier history remains intact.
