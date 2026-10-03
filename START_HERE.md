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

Never reset the learner to zero. The current baseline is 60 / 100 numbered verbs introduced; 1–50 reviewed multiple times and generally retained (strong group baseline); 51–60 recent and practicing; Genitiv active and practicing. All numbered identities are now recovered from learner-supplied history. Supplemental verbs do not increase the numbered total. This is not proof that 60 verbs are mastered.

If records disagree, use dated exercise evidence and explicit learner statements. Flag unresolved inconsistencies; do not silently invent values. The day log supplies evidence, progress.json supplies the structured snapshot, and CURRENT_STATE.md is its readable summary. Preserve corrections with a dated note.

## 2. Startup response and choices

The five modes are **Full review**, **Targeted review**, **Continue previous session**, **Start a new study day**, and **Show progress**. Present them naturally in Egyptian Arabic as below.

Summarize actual verb progress, current grammar, known vocabulary state, active mistakes, latest recorded day, and exact continuation point. If counts or identities are unknown, say so briefly. Distinguish the latest repository day from a verified last study date.

Example based on the initial state:

> رجعت لحالتك: 60 من 100 فعل اتقدموا؛ 1–50 اتراجعوا كذا مرة ومحفوظين عمومًا، و51–60 لسه بيتثبتوا. التركيز Genitiv، خصوصًا in der Nähe والملكية المتداخلة. آخر مذاكرة يوم 3 أكتوبر؛ كنت طلبت مراجعة 1–60 مع Genitiv ووقفت عشان تجهيز الريبو. الملف مفتوح والمراجعة لسه مطلوبة.
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

If a historical day contains only a backfilled summary, read that summary as actual reported learning history even when sessions is 0. The count refers only to individually logged live session sections. The current continuation point is the requested cumulative verbs 1–60 + Genitiv review, paused for repository setup; it has not been completed. Do not fabricate a previous exact question. Offer the five choices before teaching unless a mode was already selected.

Use ISO 8601 timestamps with the correct Berlin offset when the clock is available. Otherwise store null and record that the time was unavailable. Never invent historical times.

At local midnight, new exercises belong to the new date. Preserve the earlier unfinished session as paused with a rollover event and a pointer to the next day. An older open day is not evidence that it was closed; close it only on an explicit instruction or a documented rollover reconciliation.

## 4. Teaching workflow

- Use LEARNING_PROFILE.md. Default exercise: Egyptian Arabic prompt, learner writes the complete German sentence.
- Begin a new study day with a short cumulative review. Mix reviewed verbs 1–50, recent verbs 51–60, known grammar, and selected mistake patterns once their identities are known.
- Introduce at least one useful new vocabulary item in every review batch, with article/plural for nouns and a practical example. Label it as new or reviewed correctly. Save it in curriculum/vocabulary.md once actually introduced.
- Use the exact recovered numbering in curriculum/verbs.md and progress.json. Introduce future numbered verbs in batches of 10, with old/new mixed exercises. Supplemental besuchen, erklären, vergessen, and mit jemandem sprechen stay outside the numbered total. Entry 31 remains möchten as supplied; its lexical base is mögen.
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
- Exact identities and numbering agree between verbs.md and progress.json. Never invent mastery percentages, historical attempts, or timestamps. Imported strong/improving/weak/stable assessments are reported baselines; zero fresh counters do not reset them.
- Example sentences and future plans are not recorded as learner answers.
- numbered_verbs_introduced equals verbs.introduced_total and the 60 numbered rows; numbered_verbs_target equals verbs.target (100). Keep group status keys, group records, and row statuses synchronized after new learning. Supplemental vocabulary is excluded from this total.
- Vocabulary registered_entries_count matches the deduplicated register; total_known is distinct and may remain null. Active mistake IDs match weak patterns.
- Total introduced items reconcile with the curriculum; preferences and mistakes reference actual evidence.
- JSON parses, repository-relative links resolve, and earlier history remains intact.

## 8. Backfilled historical memory

The learner supplied the original numbered list, grammar/vocabulary coverage, mistake assessments, and daily summaries on 2026-10-03. The earlier missing-identity state is superseded; do not ask for the same list again.

Read all four historical day summaries when broader context is needed: 2026-09-30, 2026-10-01, 2026-10-02, and 2026-10-03. Earlier days were administratively archived as closed at backfill, with original_closure_status unknown and null times. This is not proof that the learner issued a close command.

Backfilled summaries preserve learning without pretending to reconstruct exact sessions or scored attempts. Day sessions and progress.sessions_recorded count individually logged live session sections only; historical_session_count is null. Do not treat 0 live sessions as 0 historical learning.

Current weak priorities: darf/darfst, sitzen/setzen, Genitiv article/noun endings, nested Genitiv, and Genitiv adjective endings. Practice liegen/legen/stellen too. Maintain improving topics and lightly sample stable ones; minor spelling is separate. Fresh evidence changes these baselines adaptively.

Keep CURRENT_STATE, README dashboard, progress.json, numbered rows, curriculum, and day logs aligned. Before the closing save, update the README progress dashboard if its figures or current focus changed.
