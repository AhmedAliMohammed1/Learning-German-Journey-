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

Never reset the learner to zero. Read the live learned-verb count from progress.json/CURRENT_STATE.md rather than relying on any historical milestone. The verb inventory is **open-ended**: there is no final target such as 100/100. All learned verbs belong to one continuous inventory in curriculum/verbs.md, and every new verb receives the next sequential ID. Historical IDs are preserved. Introduced never means mastered.

If records disagree, use dated exercise evidence and explicit learner statements. Flag unresolved inconsistencies; do not silently invent values. The day log supplies evidence, progress.json supplies the structured snapshot, and CURRENT_STATE.md is its readable summary. Preserve corrections with a dated note.

## 2. Startup response and choices

The nine choices are **Full review**, **Targeted review**, **Continue previous session**, **Start a new study day**, **Show progress**, **Speaking**, **Conversation**, **Reading**, and **Listening**. Keep choices 1–5 in their existing order and add 6–9 as below. Accept either the number, Arabic name, or English name.

Summarize actual verb progress, current grammar, known vocabulary state, active mistakes, latest recorded day, and exact continuation point. If counts or identities are unknown, say so briefly. Distinguish the latest repository day from a verified last study date.

Startup summary must come from the latest saved state, never a frozen example. Include the day status, exact pending work, current weak/improving areas, and any due skill retests. Do not infer oral skill from written answers.

> 1. مراجعة شاملة
> 2. مراجعة جزء معين
> 3. نكمّل آخر جلسة
> 4. نبدأ يوم مذاكرة جديد
> 5. أعرض تقدمي
> 6. التحدث — ترجمة جمل بصوتك
> 7. المحادثة — موقف وحوار بالألماني
> 8. القراءة — قطعة وفهم وترجمة
> 9. السماعي — تسمع موضوع وتجاوب

Offer all nine choices when no study choice was already provided. If the learner already selected a mode, honor it directly after loading state. "Show progress" and startup alone do not create a study session, reopen a closed day, or change mastery.

### New-study-day track choice — explicit learner preference 2026-10-07

When the learner selects **4. Start a new study day / نبدأ يوم مذاكرة جديد**, do **not** automatically default to new verbs and do not immediately create exercises. First offer exactly these two learning-track choices:

1. **قاعدة جديدة — New grammar rule**
2. **أفعال جديدة — New verbs**

Opening this two-choice submenu is navigation/configuration only. It does not itself create a new study session, introduce material, increment counters, or replace preserved pending work. Start/open the day's study session when the learner chooses one of the two tracks and actual study begins.

**If the learner chooses New grammar rule:**
- Inspect curriculum/grammar.md, progress.json, dated evidence, and current mistake patterns.
- Select a practical grammar topic that has **not already been taught as a main topic**. Do not relabel review of an old grammar weakness as a "new rule."
- Explain it in simple Egyptian Arabic, show a few clear German examples, then practise it primarily with Arabic → German full sentences.
- Mix familiar verbs/vocabulary with the new grammar, add useful vocabulary under the normal new-activity policy, and later recycle the rule in cumulative review.
- Track the rule in curriculum/grammar.md and the normal evidence files once actually introduced.

**If the learner chooses New verbs:**
- Follow the normal verb-progression workflow: introduce an appropriate new verb batch, then practise it with old material and active grammar/mistake targets.
- There is **no configured final verb target**. Add every genuinely new verb to the same unified verb inventory with the next sequential ID and increment the current learned count.

This new-day track choice overrides any older wording that says a new study day automatically moves to new verbs after a short diagnostic. A short diagnostic may still be used **after** the learner chooses a track when it is genuinely useful for selecting difficulty, but it must not decide the track for them.

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

If a historical day contains only a backfilled summary, read that summary as actual reported learning history even when sessions is 0. The count refers only to individually logged live session sections. For the live continuation point, use progress.pending_exercises and the newest saved checkpoint. At this feature update, E01–E40 are completed and corrected, while Batch 5 E41–E50 is pending. Preserve it if the learner chooses another mode; do not replace it with a generic review. Do not fabricate a previous exact question. Offer the nine choices before teaching unless a mode was already selected.

Use ISO 8601 timestamps with the correct Berlin offset when the clock is available. Otherwise store null and record that the time was unavailable. Never invent historical times.

At local midnight, new exercises belong to the new date. Preserve the earlier unfinished session as paused with a rollover event and a pointer to the next day. An older open day is not evidence that it was closed; close it only on an explicit instruction or a documented rollover reconciliation.

### Targeted review selection policy — learner preference 2026-10-06

When the learner selects **2. Targeted review / مراجعة جزء معين**, do not assume they mean the newest material. Offer targeted-review subchoices that include:

1. Review a specific verb range or named topic.
2. Review current grammar/mistake patterns.
3. Review recent material.
4. **Review all not-yet-secure material across the whole history** — every verb, grammar pattern, or vocabulary target that is not `strong/mastered`, plus any `weak`, `improving`, or `needs_check` mistake pattern, regardless of when it was introduced.
5. **Recall not-yet-secure/new/practicing verbs — Arabic → German**, one isolated verb at a time.
6. **Recall not-yet-secure/new/practicing vocabulary — Arabic → German**, one isolated entry at a time.

The fourth option is a core mode, not an edge case. Old unresolved material must not disappear merely because newer batches were introduced.

For sentence/grammar review modes (isolated recall follows its explicit scope exception below):
- Build the candidate pool from the **entire saved history**, not only the latest group.
- Include individual verbs whose status is not `strong/mastered`, even if their surrounding historical group has a strong baseline.
- Include older mistake patterns that are `weak`, `improving`, or `needs_check`, even when they relate to verbs from early numbered groups.
- Weight selection toward: high-priority mistakes, repeated errors, few/no independent correct attempts, overdue/long-unseen items, and not-yet-strong verbs. Recency may be one factor but must never dominate the pool.
- Randomize/rotate across eligible old and recent targets so consecutive review batches do not repeatedly sample only the newest material.
- Prefer a spread across multiple historical ranges when enough eligible material exists (for example early/middle/recent targets in the same batch).
- Embed the learner's real mistakes inside useful full sentences rather than drilling isolated forms.
- Add at least **1 genuinely new practical vocabulary item per review batch** (normally 1–2), with article/plural for nouns and a natural example, and reuse new vocabulary later.
- A review batch should normally mix unresolved verbs + unresolved grammar + useful vocabulary. Do not equate "latest" with "weakest".
- Stable/strong material may appear occasionally for retention, but must not crowd out unresolved material.
- Save the selection rationale so the next assistant knows why those targets were chosen.

### Review submenus and isolated recall — explicit learner preference 2026-10-06

These are additional choices inside main-menu **1 Full review** and **2 Targeted review**. Keep all nine main-menu choices and the existing sentence/grammar review available. Opening a submenu alone is configuration/navigation, not study.

**Full review / مراجعة شاملة** offers:
1. **كل الأفعال — عربي → ألماني**: recall every actually introduced numbered verb through the latest batch, including strong/mastered verbs.
2. **كل الكلمات — عربي → ألماني**: recall every deduplicated introduced entry in the vocabulary register through the latest batch, regardless of status.
3. **مراجعة بالجمل والقواعد**: the existing cumulative Arabic-to-German full-sentence review.

The full verb pool is rebuilt from the **entire unified learned-verb inventory** in curriculum/verbs.md/progress.json. The current count is a live value, not a frozen limit. Do not split verbs into numbered vs supplemental pools.

**Targeted review / مراجعة جزء معين** keeps subchoices 1–4 above and adds:
5. **الأفعال اللي لسه تحت التدريب أو جديدة — عربي → ألماني**.
6. **الكلمات اللي لسه تحت التدريب أو جديدة — عربي → ألماني**.

Targeted recall draws from the whole history, not only the latest batch: include individual entries whose status is not strong/mastered (introduced, practicing, improving, weak, needs_check, or unassessed/unknown), plus explicit item-level evidence that recall is unresolved. Group-level strength cannot hide an individually unresolved verb. A grammatical case/order error with a correctly recalled lemma does not by itself prove poor lexical recall. Do not treat an imported "introduced" vocabulary status as mastered.

**Recall activity workflow**
- Give the Egyptian Arabic meaning **one item at a time** and wait for the learner's German answer before revealing the German target or a model. Use the infinitive/registered form for verbs. Briefly specify the intended meaning/context if the Arabic prompt has several plausible translations, without exposing the German answer.
- Accept a typed or spoken German item according to the learner's actual output; a full sentence is not required. For nouns, invite the article; test a learned plural when useful. If the noun is right but the article is missing/wrong, record lexical recall and article/form accuracy separately. Non-nouns use their registered relevant form.
- Accept valid synonyms for the stated meaning. Record semantic success without claiming recall of a specific curriculum target that was not actually produced; clarify/retest that exact distinction later if useful.
- Correct each response in Egyptian Arabic. Separate independent recall, hinted recall, and a copied correction. Revisit errors in a fresh shuffled pass; one immediate success is not mastery.
- In a full recall activity, snapshot the eligible item IDs, shuffle/rotate, and persist coverage so every eligible item is eventually asked. Short rounds are allowed, but never call the entire review completed while any eligible IDs remain untested. Retry weak items without letting repeats crowd out unseen items.
- For targeted recall, weight unresolved/long-unseen items and rotate across historical ranges. Correct answers can reduce frequency only using actual comparable recall evidence.
- On actual selection, preserve and pause any prior activity and its exact prompts. Use the same date file and stable session/exercise/activity IDs under the normal session rules. Save recall type (verbs/vocabulary), scope (all/unresolved), pool IDs, tested/remaining/retry IDs, current item, support flags, original answers, corrections, evidence, and next action in progress.json and the day file. An interruption resumes the same coverage.
- Tag item evidence **isolated_recall**. It can support lexical-recall evidence but does not prove contextual use, grammatical mastery, pronunciation, listening, or fluency. Keep the four skill-mode records unchanged unless suitable actual mode-specific practice occurs.

**Explicit scope exception:** These isolated recall choices review already introduced material only. They do not require full sentences, embedded grammar, or new vocabulary per round. The existing new-vocabulary/full-sentence requirements still apply to sentence review and other new activities. No count, mastery status, session, attempt, or retest is created merely by adding these menu choices.

### Present + Perfekt verb policy — explicit learner preference 2026-10-07

This policy applies to all future verb teaching and verb review.

- When a **new verb** is introduced, teach and store it with:
  1. infinitive + Egyptian Arabic meaning,
  2. a useful **Präsens** reference form/sentence; include important irregular du/er forms when relevant,
  3. its **Perfekt** form as auxiliary **haben/sein + Partizip II**,
  4. separable/case/preposition notes when relevant.
- Unless the learner explicitly asks for another past tense, **"past" means Perfekt** in this learning system.
- Example format: **gehen — ich gehe / er geht — ist gegangen**; **anrufen — ich rufe ... an — hat angerufen**.
- The verb inventory is open-ended. New verbs are appended to the same unified list; there is no final target.
- Do not retroactively claim that an older verb's Perfekt form was already mastered merely because its Präsens/infinitive is strong. Backfill/store Perfekt reference forms as they are taught or reviewed.
- Track evidence separately for at least **present/context use** and **Perfekt use/form**. Success in one tense does not automatically prove the other.

**Full review and Targeted review**
- Verb review must no longer be present-only. Include exercises using introduced verbs in both **Präsens** and **Perfekt**.
- In full-sentence review batches, mix present and Perfekt sentences naturally; use evidence to weight the weaker tense rather than enforcing a fixed ratio.
- **Full review** of verbs covers both tense dimensions across the introduced verb inventory. Short rounds are allowed, but do not call tense coverage complete while eligible verbs remain untested in the required dimension.
- **Targeted review** treats tense as item-level evidence: a verb can be secure in Präsens but still eligible because its Perfekt is new/weak/unassessed, and vice versa.
- In isolated Arabic → German verb recall, specify the requested form before the learner answers. For Präsens recall, ask for the infinitive/registered present form as appropriate. For Perfekt recall, ask for the full reference form **haben/sein + Partizip II** (for example **ist gegangen**, **hat angerufen**), not only the participle.
- Record present-recall/present-context evidence separately from Perfekt-form/Perfekt-context evidence. A correct isolated Perfekt form does not by itself prove full sentence grammar, and a correct present lemma does not prove Perfekt recall.
- Existing vocabulary-only recall behavior is unchanged.

This preference update is configuration only: it creates no exercise attempt, mastery change, new session, or automatic completion of prior work. Preserve the current **2026-10-07-S02-E41–E48** continuation exactly.

## 4. Teaching workflow

- Use LEARNING_PROFILE.md. Full review offers all-verb recall, all-vocabulary recall, and sentence review; the default inside sentence review is Arabic → German written full sentences. Speaking requests oral full sentences; conversation uses interactive turns; reading and listening use comprehension and guided German responses. Apply the selected mode rather than forcing all practice into writing.
- Use a **progression-first** default. Before a new verb batch, use at most a short 3–5 sentence diagnostic when useful, then introduce new material. Do not require repeated full review batches before progression.
- Except for isolated recall of already introduced items, introduce at least one useful new vocabulary item in every sentence-review batch and each new activity in the four skill modes, with article/plural for nouns and a practical example. Reuse the new item in varied contexts; identical corrective retries need not introduce extra words. Label it as new or reviewed correctly. Save it in curriculum/vocabulary.md once actually introduced.
- Use the single continuous verb inventory in curriculum/verbs.md and progress.json. New verbs receive the next sequential ID; there is no final verb target. Entry 31 remains möchten as historically supplied; its lexical base is mögen.
- Correct every submitted sentence: learner answer, natural corrected sentence, and a brief Egyptian Arabic explanation. Accept valid alternatives.
- Keep separate evidence for an independent correct response, a correct response after a hint, and a copied correction. Only independent success counts toward mastery.
- Adapt difficulty and mistake frequency to evidence across the full saved history. Recent evidence matters, but older unresolved items remain eligible until strong/mastered. Once the current numbered group has had meaningful practice, continue to the next batch of 10. An isolated weak pattern does not block progression; embed it in new-material exercises. An explicit learner request for new verbs overrides review-heavy defaults.
- Track pending exercise prompts, submitted answers, selected mode, activity goals, evidence, and the next action so another assistant can continue exactly. Mode switching pauses the previous activity and preserves its prompts; it never marks it completed.

**Progression balance:** after a new numbered batch is introduced, aim for roughly **70% new-verb-centered practice and 30% old material / grammar / mistake retests**. Rotate older verbs instead of reviewing everything every time. Use long review-only batches only when the learner explicitly selects review or recent evidence shows broad regression that blocks progress.

### Progression gate

- Do not wait for every improving or weak item to become stable before teaching new numbered verbs.
- Before the next group of 10, ask: has the current group had meaningful practice, and is the learner able to continue? If yes, advance.
- If the learner explicitly asks for new verbs, advance unless they also ask to pause for review.
- Keep unfinished review exercises preserved as deferred work. Never silently mark them completed and never force them before the new batch.
- Let evidence control future frequency: repeated independent success reduces review frequency; repeated errors increase how often that pattern is embedded in future new-material exercises.
- A diagnostic before new material is normally 3–5 sentences maximum and can be skipped when recent evidence already provides enough signal.

## 5. Checkpoint and synchronization

At meaningful checkpoints (an answered batch, session pause, preference change), append evidence to the day file and update the snapshot. Do not wait for closing if useful progress can be saved.

Keep these synchronized:
- Day metadata: status, sessions, active_session_id, started_at, closed_at, updated_at.
- progress.json: current_day, latest_day, current_session_id, day_status, last_updated, pending_exercises, next_action, totals, per-verb and mistake evidence.
- CURRENT_STATE.md: current summary, day status, pending work, next step.
- Curriculum files, MISTAKE_PATTERNS.md, and LEARNING_PROFILE.md as applicable.
- progress.skill_tracking (independent mode/dimension evidence), progress.review_queue (dated retests), and progress.adaptive_learning decisions. README and CURRENT_STATE summarize actual changes.

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
8. Update CURRENT_STATE.md and progress.json, including day_status closed, current/latest day pointers, evidence-based totals, next_action, mode/dimension results, and review_queue. Save incomplete skill activities as paused; closing a day does not make them passed.
9. Save all changed files and verify persistence. A repeat close with no new work is a no-op: no duplicate session, summary, counters, or closure event.
10. Respond briefly in Egyptian Arabic with what was studied, what needs review, and where to resume. State whether saving succeeded.

If the learner returns to study on that same date, reopen and append under section 3. Preserve every previous close event and summary. Close again on the same phrase after the extra session.

## 7. Consistency checks before saving

- Exactly one date file per calendar date.
- Day session count matches actual session sections; initialization starts at 0.
- Day/snapshot/summary statuses and active session IDs agree.
- The original 60 baseline verb IDs remain intact, and later numbered batches append without renumbering. Current introduced count must match the actual numbered rows.
- Exact identities and numbering agree between verbs.md and progress.json. Never invent mastery percentages, historical attempts, or timestamps. Imported strong/improving/weak/stable assessments are reported baselines; zero fresh counters do not reset them.
- Example sentences and future plans are not recorded as learner answers.
- `verbs.learned_total` must equal the number of rows in the unified learned-verb inventory. There is no `numbered_verbs_target` and no separate supplemental-verb count. Keep item statuses/evidence synchronized after new learning.
- Vocabulary registered_entries_count matches the deduplicated register; total_known is distinct and may remain null. Active mistake IDs match weak patterns.
- Total introduced items reconcile with the curriculum; preferences and mistakes reference actual evidence.
- JSON parses, repository-relative links resolve, and earlier history remains intact.

## 8. Backfilled historical memory

The learner supplied the original numbered list, grammar/vocabulary coverage, mistake assessments, and daily summaries on 2026-10-03. The earlier missing-identity state is superseded; do not ask for the same list again.

Read all four historical day summaries when broader context is needed: 2026-09-30, 2026-10-01, 2026-10-02, and 2026-10-03. Earlier days were administratively archived as closed at backfill, with original_closure_status unknown and null times. This is not proof that the learner issued a close command.

Backfilled summaries preserve learning without pretending to reconstruct exact sessions or scored attempts. Day sessions and progress.sessions_recorded count individually logged live session sections only; historical_session_count is null. Do not treat 0 live sessions as 0 historical learning.

Derive current weak priorities from the latest mistake records, not the historical backfill list. At this update, M13 Genitiv adjective endings and M28 verb-second after a fronted phrase are weak; several older patterns are now improving. Continue rotating all introduced material. Maintain improving topics and lightly sample stable ones; minor spelling is separate. Fresh evidence changes these baselines adaptively.

Keep CURRENT_STATE, README dashboard, progress.json, numbered rows, curriculum, and day logs aligned. Before the closing save, update the README progress dashboard if its figures or current focus changed.

## 9. Four skill modes

Before an activity, inspect the exact current verb/vocabulary inventory, grammar statuses, recent answers/hints, weak patterns, mode-specific evidence, and due retests. Do not guess a CEFR level from the 60-verb count. Use a short diagnostic when that skill is unassessed. Select familiar practical topics and manageable novelty.

### 6 — Speaking / التحدث

1. Give one Egyptian Arabic sentence at a time. The learner says the full German sentence themselves; wait for the answer before showing a German model.
2. Build sentences from known verbs/grammar and one or two new useful words for the activity. Gradually include current weaknesses in practical contexts.
3. Correct grammar and, only when actually assessable audio is available, pronunciation. Quote the understood answer, provide the natural German version, and explain the main correction in Egyptian Arabic.
4. Address one pronunciation feature at a time: a specific sound, word stress, rhythm, or a short phrase. Demonstrate it through accessible audio if supported; ask the learner to say it again.
5. Follow a corrected repeat with a fresh Arabic sentence using the same rule/word. A copied repeat is supported practice, not independent transfer.
6. Record grammar and pronunciation separately; save the actual evidence and the next oral target.

**Audio evidence rule:** A transcript, dictation result, or typed German text supports text grammar correction but cannot prove pronunciation, accent, stress, or fluency. If no usable original audio or phonetic assessment capability is available, set pronunciation outcome not_assessed, explain briefly, and offer voice/audio practice if supported. Do not claim to have heard a mistake from spelling alone. With ambiguous audio, ask for a repeat before labeling it an error.

### 7 — Conversation / المحادثة

1. Choose a realistic situation matching current evidence: shopping, directions, an appointment, work, transport, or another familiar topic. Give a short role/goal in Egyptian Arabic; do not reveal a complete script to memorize.
2. Begin in German and take one turn at a time. Wait for the learner's reply and respond meaningfully to it; adapt the next turn to what they actually said.
3. Correct grammar and assessable pronunciation step by step. Keep the interaction moving, but pause for the main error, explain briefly, and request a corrected reply.
4. If the learner is blocked, provide an incremental cue or small phrase. Then ask them to produce the whole German reply. Fade help as they improve.
5. Stay with the situation until the learner can handle its essential goal independently. Check at least two fresh variations (different place/person/object) and an unprompted final turn. Immediate success is provisional; delayed testing checks retention.
6. If the learner stops or closes the day, respect that request and save the scenario as paused with remaining goals. Never manufacture success to finish it.
7. Schedule a later retest of the same communicative skill in a new situation. Do not assess pronunciation/fluency from text-only role-play. Text role-play is a valid conversation-production exercise with those dimensions unassessed.

### 8 — Reading / القراءة

1. Provide a short original German passage tailored to current verbs, grammar, weak patterns, and a small amount of new vocabulary. A starting guideline is 50–90 words, adjustable to evidence; this is not a CEFR claim.
2. Offer full translation, translation of a selected part, comprehension questions, or a mix. Choose a reasonable starting task and follow the learner's preference.
3. Ask questions one at a time, aiming for German answers. If necessary, accept an Arabic answer first to verify meaning.
4. Help the learner turn that meaning into a full German answer: cue vocabulary, a starter, or a relevant rule; let them complete it. Use a model only when needed, then request their own version.
5. Ask a fresh related question without the model visible. Distinguish independent comprehension from supported German production and from copying.
6. Adapt passage length and sentence complexity; reuse new vocabulary in another sentence and schedule later transfer/retention checks.

### 9 — Listening / السماعي

1. Check whether this interface can actually deliver audible German. If unavailable, keep listening unassessed and explain that real audio/voice is needed; offer another chosen mode. A displayed text read silently is not listening practice.
2. Choose a short level-appropriate topic grounded in known material, with manageable new words. Starting guideline: 30–60 seconds or 4–6 short German sentences at a clear natural pace.
3. Deliver the German topic **by voice/audio** in the supported conversation interface. Do not display its transcript, translation, or answer key before the first listening attempt. Explain the task briefly beforehand in Egyptian Arabic.
4. After finishing, ask comprehension questions one at a time and let the learner answer in German. Arabic fallback is allowed to confirm comprehension.
5. Support conversion to a full German answer, then use a fresh question or a shorter replay segment. Offer slower replay/repetition when needed; log replays and hints.
6. Use an unheard short variant to check independent transfer. Reveal the transcript after the initial attempt when useful for explaining difficulties.
7. Separate understanding of the audio from German answer production. A correct Arabic answer can demonstrate content comprehension; a model-assisted German repetition does not demonstrate independent German production.
8. Answer pronunciation is assessed only from usable learner audio. Record output modality, transcript visibility, replays, hints, and original content so another session can retest fairly.

## 10. Adaptive selection, evidence, and later retests

In sentence review and the four skill modes, mix familiar vocabulary/grammar with a small amount of genuinely new practical vocabulary. Isolated recall rounds cover only their already introduced inventory under section 3. Start with roughly 80% familiar vocabulary and 1–2 new items per short activity, then adjust; this is a default, not a measured score. Revisit new words in a later turn, a fresh context, and a later session. The existing 60/40 old/recent review balance still applies to review content, not a conflicting vocabulary quota.

Choose work from:
- The learner's chosen mode/interest.
- Recent comparable independent performance, hints and retries.
- Current weak/improving patterns and pending activities.
- New-word retention and the due review_queue.
- Actual available audio capabilities.

Keep evidence separate by mode and dimension. Written grammar success may guide topic selection, but cannot raise pronunciation or listening status. Comprehension, German production, grammar, vocabulary use, pronunciation, and dialogue turn-taking need their own evidence. Only rate fluency from actually assessable audio.

Default task assessment:
- not_assessed: no suitable observed attempts for this skill/dimension.
- practicing: actual attempts exist but support/errors remain.
- improving: at least two independent fresh variations meet the task's essential goals.
- strong: independent success across varied contexts and at least two sessions, including a successful delayed retest. One simple task does not make the entire skill strong.
- Track immediate success and retained success separately. Unassessed dimensions stay unassessed; do not hold text practice hostage to unavailable audio.

Compare the latest 3–5 comparable independent attempts with earlier comparable attempts before describing a trend. Fewer hints, correct new uses, and fewer recurring errors can justify improving; a difficult new task is not automatic regression. Save a short evidence-linked reason for the next teaching choice. No invented mastery percentages.

**Spaced retest policy:** After meaningful practice, upsert one review_queue entry per mode + activity/target. First retest due next Berlin calendar day; independent success advances to 3 days, then 7 days after that retest. Continued success at the last stage uses 7 days as a maintenance interval. Difficulty/hints/errors keep the target practicing, trigger a short fresh test later in the current session where appropriate, and make the next delayed test due the next day. These intervals are adjustable to actual learning evidence.

At each future study startup/checkpoint, inspect due/overdue items and briefly recommend a relevant retest. Keep the learner's chosen mode; offer at most 1–2 priority tests rather than replacing the requested activity. Do not start a lesson from progress-only mode. Do not schedule imaginary tests before any new-mode practice occurred.

Retests happen when a capable assistant reads the repository during study. A saved due date does not run a background job or send a reminder. Preserve a pending oral/reading/listening activity separately from existing E41–E50.

## 11. Persistence contract for skill activities

Use the existing day files and progress.json only; no separate parallel tracking files.

- An activity uses a stable ID such as YYYY-MM-DD-S02-A01 and a selected mode. Switching modes saves the prior activity's state and its continuation.
- Log prompts/passages/scenario, learner responses, corrected forms, assessed audio facts, mode/dimension outcomes, hints/replays, vocabulary IDs, grammar topics, mistake IDs, fresh transfer tests, and next action in the day file.
- progress.skill_tracking stores one record per mode and its dimension status/counters, activities, evidence, and pending_activity_id. Existing numbered learning state remains authoritative.
- Store task outcomes as independent_correct, correct_with_support, needs_retry, or not_assessed per dimension. Avoid a single outcome that hides correct comprehension but assisted output.
- A task record includes id, mode, target, goals, difficulty_basis, input/output modality, actual audio assessed, transcript visibility, attempts with stable exercise IDs, status active/paused/completed, immediate_independent_success, delayed_retention_confirmed, and continuation.
- Retest entries use id, target_key, mode, activity_id, target, due_on, interval_index, status scheduled/completed, last_result, and evidence_ids. Compute due/overdue from the current Berlin date. Upsert by target_key; repeating a save must not duplicate schedules or outcomes.
- Prompt changes, copied solutions, and replay-assisted responses retain their support flags; never count them as independent attempts.
- Reuse existing grammar mistake IDs when the same rule fails in a new mode. Create a pronunciation pattern only after genuine audio evidence; separate accent/style from intelligibility errors. Update vocabulary/grammar under the same existing registries.
- End-of-day processing updates skill evidence, review_queue, pending activities, CURRENT_STATE, preferences, and the day status along with the existing curriculum workflow.
- No mode has been assessed merely because its configuration was added. Keep all four new baselines not_assessed until actual training occurs.


## Open-ended unified verb inventory — explicit learner preference 2026-10-09

- There is **no final verb-count goal**.
- The displayed verb number means only **how many verbs have been introduced/learned so far**.
- All verbs use **one continuous table/inventory**. Do not create separate numbered/supplemental verb tables.
- Preserve historical IDs; assign each new verb the next sequential ID.
- Continue teaching new verbs for as long as useful; do not stop because a milestone such as 100 was reached.
- This policy supersedes older text about a 100-verb target or supplemental verbs outside the main count.

## Unified table formatting rule — 2026-10-10

Every vocabulary item V001 onward belongs in the single Markdown table in `curriculum/vocabulary.md` (no standalone per-item headings below the table). Every verb ID belongs in the single contiguous table in `curriculum/verbs.md`, without blank lines splitting rows. New additions must be placed as rows, with stable IDs and synced status/counts from `progress.json`. Detailed learner attempts and examples belong in dated day logs and structured evidence, not duplicate vocabulary sections. When editing tables validate contiguous IDs, pipe column counts, and header count against `progress.json` before pushing.
