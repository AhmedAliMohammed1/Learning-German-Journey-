# Adaptive mistake tracking

## Latest update —2026-10-18
- M28 fronted-element V2 now **stable**:6 dated post-error independent successes across Oct11-S03, Oct12-S02 and Oct18-S01. Reduce drill frequency; light retention.
- Latest18-S01-E01: M02 improving with deinem→seinen (possessor and governed Akk), M34 weak with missing er; both post-error streaks reset. Previous correct ihrem Kollegen/subject evidence retained. M28 stable unchanged: finite position after danach correct, subject omission distinct. Kollegen noun ending already correct.


## Current status index — 2026-10-13

The **live, canonical pattern statuses** are in `progress.json.mistake_patterns`. The old headings below (“Active/weak”, “Improving”, “Stable”, “needs_check”) are **2026-10-03 historical backfill snapshots**, not today's status. Preserve evidence but do not use old labels for current scheduling.

- **Weak now:** **M32** (word order after `und`); **M34** (preserve intended subject in follow-up clause).
- **Improving:** **M08** (`ihn/sie/es`) and **M28** (V2 after fronted phrase). **Stable:** **M13** Genitiv adjective ending.
- **S02-E01:** learner `sei` is a written typo for `sie`, not proven wrong grammatical case. `dem Kollegen` is valid Dativ but `ihrem Kollegen` is necessary for `لزميلها`.
- See `CURRENT_STATE.md` for the exact current exercise and `days/2026-10-13.md` for actual responses.

---


**Backfilled from prior conversation**, based on the learner's supplied assessment on 2026-10-03. These status labels represent reported historical progress; they are not calculated from invented exercise counts.

## Active / weak — deliberate retesting

- **M01 — darf vs darfst; incorrect darft**: ich/er/sie/es darf; du darfst; ihr dürft
- **M05 — sitzen vs setzen**: Das Kind sitzt auf dem Stuhl. Ich setze das Kind auf den Stuhl.
- **M11 — Genitiv article and noun ending selection**: in der Nähe des Bahnhofs; in der Nähe der Schule
- **M12 — nested Genitiv phrases**: in der Nähe des Hauses meiner Freundin
- **M13 — Genitiv adjective ending**: des öffentlichen Parks

## Improving — cumulative spaced practice

- **M02 — mein / meinen / meinem**: Mein Bruder kommt. Ich sehe meinen Bruder. Ich helfe meinem Bruder.
- **M03 — deshalb + verb + subject**: Deshalb suche ich ihn.
- **M08 — ihn / sie / es by noun gender**: der Schlüssel → ihn; die Tasche → sie; das Handy → es
- **M09 — modal verb + final infinitive**: Ich muss morgen arbeiten.
- **M14 — Akk vs Dat after specific verbs**: Ich sehe meinen Bruder. Ich helfe meinem Bruder.
- **M15 — Dat person + Akk thing**: Ich gebe meiner Schwester ein Geschenk.
- **M16 — warten auf + Akk**: Ich warte auf den Bus.
- **M17 — um ... zu**: Ich gehe zum Supermarkt, um Milch zu holen.
- **M18 — anfangen / aufhören + zu**: Ich fange an zu lesen. Ich höre auf zu arbeiten.
- **M19 — sentence-final verb with weil and wo**: weil ich kein Auto habe; Ich weiß, wo er wohnt.
- **M20 — eine Tasse Wasser / Kaffee for intended quantity**: eine Tasse Kaffee, rather than Kaffeetasse for a quantity of coffee
- **M21 — capitalized nouns; lowercase ordinary pronouns mid-sentence**: Ich helfe ihr. Ich schreibe eine Nachricht. Polite Sie/Ihnen stay uppercase.

## More stable than before — lighter maintenance checks

- **M04 — wissen vs kennen**: Ich weiß die Antwort. Ich kenne diesen Mann.
- **M06 — helfen + Dat**: Ich helfe meinem Bruder.
- **M07 — denken an + Akk**: Ich denke an meine Mutter.
- **M22 — danken + Dat**: Ich danke meinem Bruder.
- **M23 — antworten + Dat**: Ich antworte meinem Lehrer.
- **M24 — suchen + Akk**: Ich suche den Schlüssel.
- **M25 — kennen + Akk**: Ich kenne diesen Mann.
- **M26 — sehen / hören + Akk**: Ich sehe meinen Bruder. Ich höre die Musik.

"Stable" means more reliable than earlier according to the history, not permanently mastered. Continue sampling these naturally.

## Previous diagnostic retained

**M10 — anfangen conjugation** remains needs_check: ich fange an; du fängst an; er/sie fängt an. The earlier record flagged it, and the current backfill supplies the correct forms but no separate reliability assessment. It is distinct from M18, the improving anfangen/aufhören + zu construction.

Active verb contrast liegen/legen/stellen also needs continued practice. Do not label it a repeated-error pattern until an actual error or explicit learner report supports that classification.

## Minor spelling issues — separate, low priority

- SP01: **Nachricht**
- SP02: **antworten**
- SP03: **helfen**
- SP04: **erklären**
- SP05: **Regel**
- SP06: **Freund**
- SP07: **Vater**
- SP08: **Kaffee**
- SP09: **Restaurant**
- SP10: **Kirche**

These spellings were reported as previously troublesome. Individual improvement and frequencies are unknown; "improving" here is a low-priority practice label, not a measured streak. Correct them briefly without treating them as severe grammar weaknesses.

## Future adaptive evidence rules

- A new relevant error after needs_check makes the pattern weak; fresh independent correct use can make it improving.
- weak → improving after at least 2 independent correct uses in different sentences after the latest error.
- improving → stable after at least 4 independent correct uses across at least 2 actual sessions after the latest error.
- stable → improving after a new relevant error; repeated errors return it to weak.
- A hint, copied solution, or repeated corrected answer does not advance an independent success streak.
- Imported statuses remain the baseline. Do not reset them because fresh in-repository counters start at 0.
- Adjust the thresholds when useful and record why. Use high priority for weak, medium for improving, and occasional checks for stable.
- Retest in fresh full sentences with useful new vocabulary, not repeated identical questions.

## Evidence and provenance

Individual original answers, error frequencies, independent-success counts, and exact times were not supplied. Historical counts are **unknown**. Fresh recorded counters begin at **0**, meaning no post-backfill measured attempts, not no prior practice.

The reference sentences above are correct forms or historical study examples; they are not raw learner answers. Future evidence must include date, session/exercise ID, original answer, correction, hint status, independent success/error, and status change reason. Mirror the same IDs/statuses in progress.json.mistake_patterns and keep spelling in its separate spelling_patterns list.

## Import changes

- Initialization retained ten reported patterns with needs_check because their reliability was unknown.
- 2026-10-03 backfill supplies current weak/improving/stable assessments, adds Genitiv and other historical patterns, and preserves M10 as a diagnostic without inventing new observations.


## Fresh live evidence — 2026-10-03 — S01 Batch 1

- M01 remains weak: E01 used **darfst** correctly once.
- M05 moved **weak -> improving**: E04 used **sitzt** correctly and E05 used **setze** correctly.
- M11 remains weak: Genitiv ownership/endings were wrong in E02, E03, and E04; E10 did correctly form **des Parks**.
- M12 remains weak: E04 needs **des Eingangs der Schule**.
- M13 remains weak: E10 needs **des öffentlichen Parks**.
- M16 remains improving: E06 correctly used **warten auf meinen Freund**.
- M10 moved **needs_check -> improving**: E07 used **ich fange an** correctly.
- M18 remains improving with a fresh error: E07 omitted **zu** before *lesen*.
- M06 remains stable: E08 correctly used **helfen + Dativ**.
- M24 moved **stable -> improving**: E08 used an incorrect object construction with **suchen**.
- M03 and M09 remain improving: E09 correctly used **deshalb + verb-second** and modal + final infinitive.


## Fresh live evidence — 2026-10-03 — S01 Batch 2

- **M01 improving:** E11 used **Mein Bruder darf ... schließen** correctly; second fresh independent success, weak -> improving.
- **M11 weak:** E12 and E16 still show Genitiv possessor-ending problems.
- **M12 weak:** E16 got **des Hauses** right but failed the second possession layer.
- **M18 improving:** E17 correctly used **aufhören + zu arbeiten**.
- **M19 improving:** E18 indirect **wo** clause wrong; E20 **weil** clause word order correct.
- **M17 improving:** E19 correctly used **um ... zu holen**.
- **M21 improving:** capitalization errors in **Arbeiten** and **wasser**.
- **M27 weak — new live pattern:** stationary location takes Dativ, destination takes Akkusativ with two-way prepositions. E13 used **im Kühlschrank** after **stellen**; correct is **in den Kühlschrank**. E15 correctly used **auf den Tisch**.


## Fresh live evidence — 2026-10-03 — S01 Batch 3

- **M01 improving:** E21 again used **darf ... öffnen** correctly; article error was separate.
- **M11 weak:** E22 still had a wrong possessor form; E25/E26 showed some correct Genitiv endings.
- **M12 weak:** E25 correctly formed **des Hauses des Chefs**; one fresh success after the latest error.
- **M13 weak:** E26 again needs **des öffentlichen Parks**.
- **M19 improving:** E27 correctly placed the verb at the end of the indirect **wo** clause; subject case was the remaining problem.
- **M18 improving:** E28 failed **aufhören + zu + Infinitiv** and needs another retest.
- **M17 improving:** E30 used **weil** instead of **um ... zu** for same-subject purpose.
- **M21 improving:** E29 wrote **arbeit** lowercase.
- **M27 improving:** E23 correctly used **auf den Schreibtisch** for destination and E24 **auf dem Schreibtisch** for location; weak -> improving.
- **M28 weak — new live pattern:** after a fronted phrase, the finite verb must remain second: **Nach der Arbeit treffe ich ...**. E29 repeated the earlier V2 issue.


## Fresh live evidence — 2026-10-03 — S01 Batch 4

- **M11 improving:** E33 still missed the masculine Genitiv noun ending (**des Vaters**), then E34 and E35 independently produced correct Genitiv forms (**des Eingangs des Krankenhauses**, **des öffentlichen Parks**). Two fresh successes after the latest error -> weak to improving.
- **M12 improving:** E34 correctly formed **des Eingangs des Krankenhauses**; together with E25 **des Hauses des Chefs**, this gives two independent correct nested-Genitiv uses after the latest error -> weak to improving.
- **M13 weak:** E35 correctly used **des öffentlichen Parks** once after the latest error. Keep weak until another independent success.
- **M27 improving:** E31 correctly used destination **in den Rucksack** and E32 stationary **im Rucksack**.
- **M28 weak:** E36 correctly used **Nach der Arbeit gehe ich ...** after the latest error. One fresh success; keep weak pending another.
- **M19 improving:** E37 correctly used the indirect **wo** clause with the verb at the end; only the comma was missing.
- **M18 improving:** E38 correctly used **aufhören + zu kochen**.
- **M17 improving:** E39 correctly used **um ... zu** for same-subject purpose; add **ihn** to match the explicit object and add the comma.
- **M15 improving:** E33 correctly used **meiner Schwester das Handy** (Dat person + Akk thing); the remaining error belonged to Genitiv ownership.

## Cross-mode evidence and pronunciation rules — 2026-10-03 configuration

Use the latest structured statuses and dated live checkpoints, not the old backfill classification. Retest a known grammar pattern in speaking/conversation/reading/listening using its existing M ID; retain the mode, exercise/activity ID, modality, and support flags on new evidence.

Pronunciation is a separate category, created only after a reliably heard issue in actually assessable original audio. Record the word/sound, observed issue, relevant audio/attempt reference where accessible, correction, independent retry, and later retest. Do not infer sound errors from a transcript, spelling error, speech-recognition output, or accent alone. If audio is unclear, ask for a repeat; mark the dimension not_assessed when assessment is unavailable.

Keep minor spelling separate. Arabic fallback can demonstrate reading/listening comprehension while German production still needs assistance. A corrected repeat does not raise independent-success counters.

At skill checkpoints, update progress.skill_tracking and its review_queue as well as grammar/vocabulary/mistake evidence. No new observed mistake, pronunciation assessment, or counter was created by adding the modes.


## Fresh live evidence — 2026-10-03 — S02 Batch 1

- M13 improving: E02 used **des öffentlichen Parks** correctly again.
- M28 improving: E01 kept verb-second after **Nach der Arbeit**.
- M27 stable: E03 **auf den Stuhl** and E04 **auf dem Stuhl** were both correct.
- M19 stable: E09 had correct indirect-**wo** word order; only the comma was missing.
- M18 remains improving after the E07 anfangen + zu error.
- M14 remains improving after E10 needs **meinen Freund** with treffen.
- M21 remains improving after E08 used **Ihrem** instead of **ihrem**.
- M15, M16, M17 and M10 had fresh correct evidence.

Latest live weak set: none. Continue spaced checks of improving patterns.


## Fresh live evidence — 2026-10-03 — S02 Batch 2

- **M29 weak — new live pattern:** E13 correctly used **stellen** for placement, but E14 used **stellt** for a stationary object. Correct contrast: **Ich stelle den Koffer neben die Tür. / Der Koffer steht neben der Tür.**
- **M28 stable:** E11 and E15 again kept the finite verb second after fronted phrases. Post-error evidence now spans enough fresh uses across two sessions.
- **M11 improving:** E12 got **des neuen** right but needs **Restaurants** with Genitiv -s.
- **M16 improving:** E15 omitted **auf** in **warten auf den Lehrer**.
- **M18 improving:** E11 still needs the standard **Ich fange ... an, etwas zu lesen** structure; E17 then correctly used **aufhören + zu schreiben**.
- **M15 improving:** E16 correctly used the Dativ recipient **meiner Mutter**; the Autoschlüssel article error is separate.
- **M19 stable:** E18 was fully correct.
- **M06 stable:** E19 correctly used **hilft ihrer Schwester**.
- **M24 improving:** E19 correctly used **das Handy suchen**.
- **M17 improving:** E20 was fully correct with **um Milch zu kaufen**.


## Fresh live evidence — 2026-10-03 — verbs 61–70 first practice

- **M28 stable:** E33 correctly used verb-second after **Nach der Arbeit** with separable **anrufen**.
- **M21 improving:** E33 wrote **arbeit**; nouns remain capitalized: **Arbeit**.
- No new weak grammar pattern was created from E31–E40.
- All numbered verbs 61–70 were independently correct in their first practice. This supports **practicing**, not mastery.


## Fresh live evidence — 2026-10-03 — S02 E41–E50

- M29 stehen/stellen: E48 correctly used **steht neben der Tür**. One fresh success after the latest error; keep weak until another independent success.
- M16 warten auf + Akk: E49 fully correct; remains improving.
- M18 anfangen/aufhören + zu: E50 fully correct; remains improving.
- M14 verb-specific case: E42 used Dativ with **anrufen**; correct is **ihre Freundin anrufen** (Akk) and separable **an**.
- Repeated temporal case error: E42 and E46 used **nach dem Arbeit**; correct is **nach der Arbeit**.
- E47 needs **mit + Dativ plural: mit unseren Freunden**.

### M30 — nach + Dativ in temporal phrases
- Status: improving
- Priority: medium
- Reference: **nach der Arbeit**, **nach dem Essen**
- Fresh evidence: S02 E42 and E46.
- Policy: embed this in new-verb practice; do not block progression.


## Fresh live evidence — 2026-10-04 — S01 Batch 1

- **M29 improving:** E02 used **stellen** correctly for placement and E03 used **stehen** correctly for a stationary object. The Koffer article/number errors were separate.
- **M13 stable:** E04 again used **des öffentlichen Parks** correctly. Post-error independent success now spans more than one live session.
- **M11 improving:** E04 correctly used **des ... Parks**; broader Genitiv endings still need spaced review.
- **M15 improving:** E05 correctly used **meiner Schwester den Autoschlüssel**.
- **M19 stable:** E06 kept the verb at the end of the indirect **wo** clause; capitalization of **weiß** was separate.
- **M30 improving:** E01 correctly used **nach der Arbeit** after the previous repeated error.
- Minor form targets from the batch: **der/den Koffer**, **Das Hotel ist**, lowercase **weiß**, and **mein Zimmer**.


## Fresh live evidence — 2026-10-04 — S01 Batch 2

- **M30 improving:** E14 correctly used **nach der Arbeit** again.
- **M19 stable:** E19 used correct verb-final order after **weil**; comma and lowercase article were separate surface errors.
- **M11 improving:** E20 used **der Eingangs**; correct masculine Genitiv is **des Eingangs**. Reset the fresh success streak for this target.
- **M12 improving:** E20 needs the nested phrase **des Eingangs der Hochschule**. The second layer **der Hochschule** was correct, but the first layer was not.
- New verb-form retest targets: **ausziehen = ziehe ... aus** and **umziehen = nach + place + um**. These are currently verb-specific learning targets, not separate mistake IDs yet.


## Fresh live evidence — 2026-10-04 — S01 Batch 3

- **M11 improving, priority high:** E24 repeated the masculine Genitiv error. Correct: **des Eingangs**.
- **M12 improving, priority high:** E24 still needs the nested phrase **des Eingangs des Krankenhauses**; the second Genitiv layer was correct.
- **M16 improving:** E25 omitted **auf** again in **warten auf meinen Bruder**.
- **M15 improving:** E26 kept the Dativ-recipient + direct-object pattern structurally correct.
- **M27 stable:** E27/E28 correctly contrasted **liegen + Dativ** and **legen + Akkusativ**.
- **M30 improving:** E30 used **nach der Termin**; correct is **nach dem Termin**. The learner is reliable with **nach der Arbeit**, but masculine Dativ articles still need practice.
- Verb-specific retest: E23 used **auf** instead of **aus** with **ausfüllen**.


## Fresh live evidence — 2026-10-05 — new-day diagnostic

- **M11 improving:** E03 correctly used **des Eingangs** after the latest errors.
- **M12 improving:** E03 correctly formed **des Eingangs des Krankenhauses**.
- **M16 improving:** E02 correctly used **warten auf meine Schwester**.
- **M30 improving:** E04 correctly used **nach dem Termin**; the later Mietvertrag article error is separate.
- **M27 stable:** E05 correctly used destination **in den Rucksack**; **legen** is more natural than *stellen* for a flat Ausweis.
- Verb-specific target 79 **ausfüllen** repeated the prefix error in E01: **fülle ... aus**, not *auf*.


## Fresh live evidence — 2026-10-05 — verbs 81–90

- **M28 stable:** E11 and E15 kept verb-second after **Nach der Arbeit** with separable verbs.
- **M15 improving:** E12 used **zu meinem Freund** with zurückgeben; natural structure is **Ich gebe meinem Freund das Buch zurück** — Dativ recipient directly, without *zu*.
- **M14 improving:** E13 showed a fresh object-case issue with **der Reisepass**; the object of mitbringen is Akkusativ: **meinen Reisepass**.
- Time-expression form needs maintenance after E08: **nächsten Monat**, not *nächster Monat*.
- Article/case maintenance from the batch: **mein Handy**, **ein Zimmer**, **in einem Hotel**, **das Wochenende**, **das Paket**, **zum Termin**.
- E15 correctly formed separable **absagen** but omitted the explicit object; use **den Termin absagen** when the thing being cancelled is stated.
- Do not create a new weak pattern from these one-off surface errors yet; embed them in future new-material practice and promote only if repeated evidence supports it.


## Fresh live evidence — 2026-10-06 — Full review Batch 2

- **Dativ recipient + Akk thing:** E13 was fully correct: **meiner Schwester die Quittung**.
- **warten auf + Akk:** E14 was fully correct: **auf meinen Bruder**.
- **Wo/Wohin contrast:** E15 **auf den Schreibtisch** and E16 **auf dem Schreibtisch** were both correct.
- **aufhören + zu:** E17 was fully correct.
- **indirect wo clause:** E18 was fully correct.
- **anrufen:** E19 used the verb and Akkusativ object correctly, but the prompt required **nach dem Termin**, not **nach der Arbeit**.
- **Genitiv adjective ending:** E20 correctly used **des öffentlichen Parks**.
- No new broad weak pattern is created from the Hotel/Restaurant or office/desk lexical mismatches.


## Review-selection persistence rule — 2026-10-06

- Weak/improving/needs_check patterns remain review candidates regardless of age.
- Introducing newer verbs never removes an older unresolved pattern from the candidate pool.
- Targeted unresolved review should weight high-priority and long-unseen patterns more strongly, while rotating across the full history.
- Stable patterns may be sampled lightly for retention; they should not crowd out unresolved patterns.
- Whenever possible, combine a mistake target with a not-yet-strong verb in a natural full sentence and include useful new vocabulary.


## Fresh live evidence — 2026-10-06 — S02 history-wide review

- **M01 improving:** correct **darf ... öffnen**.
- **M05 active:** learner used **stellen** instead of **setzen** for seating a child; **sitzen** itself was correct in the next sentence.
- **M18 active:** learner again omitted separable **an** in **anfangen ... an zu lesen**.
- **M16 improving:** **warten auf meinen Freund** was correct.
- **M14 improving:** **treffen + Akk** and the Akkusativ object with **mitbringen** were correct.
- **M15 improving:** **meinem Freund ... das Buch zurückgeben** was correct.
- **M30 improving:** **nach dem Termin** was correct.
- Surface-form maintenance: **neben der Tür** and **nächsten Monat**.
- Vocabulary: **Fahrplan** recalled correctly; **Schalter** was replaced by *Fenster* and needs a fresh retest.


## Fresh live evidence — 2026-10-06 — S02 Batch 2

- M14: E12 repeated object-case trouble with **sehen**; use **meinen Bruder**.
- M05/M27: E13 chose **setzen** correctly but used location Dativ instead of destination Akkusativ; use **auf den Stuhl**.
- M18: E14 again omitted separable **an** in **anfangen ... an + zu**.
- M15: E16 used **meinen Chef**; recipient with **schicken** needs Dativ **meinem Chef**.
- M17: E18 needs **um ... zu** for same-subject purpose.
- M21: E13 wrote **stuhl**; noun capitalization remains a light maintenance target.
- Fresh success: modal + infinitive, helfen + **ihm**, treffen + Akk, ausziehen, verlieren + **ihn**, and V2 after **danach**.


## Fresh live evidence — 2026-10-06 — S02 E21–E30

- M27/M29: fresh independent success on **liegen / stellen / stehen** and Wo/Wohin contrast; reduce review frequency.
- M11/M12: fresh independent success on **des Eingangs des Bahnhofs**; reduce review frequency but keep spaced checks.
- M30: fresh error **nach der Termin**; correct **nach dem Termin**.
- M15: **meiner Mutter ... ihr** correct.
- M14: **anrufen + Akk** was correct in E27; E28 used **meinem Freund** with besuchen, correct **meinen Freund**.
- M17: **um ... zu** structure itself was correct in E28.
- M19: two fresh weil-clause errors in E29/E30; status returns to improving.
- Current higher-frequency targets: temporal Dativ, verb-specific Akk/Dat, separable word order, and weil clauses.


## Fresh live evidence — 2026-10-06 — S02 E31–E40

- M14: E32 correct **sehen + Akk**; E36 correct **treffen + Akk**.
- M15: E32 correct **ihm den Schlüssel**.
- M18: E34 correct **anfangen ... an zu lesen**.
- M22/M23: E35 correct Dativ with **antworten** and **danken**.
- M17: E36 correct **um ... zu**.
- M19: E33/E37 still need subject + final verb after **weil**; E40 had correct final-verb order.
- M04: E38 correctly distinguished **kennen** vs **wissen**; negation placement was the remaining issue.
- M03: E39 correctly used **deshalb + V2**.
- Current higher-frequency target: **nicht** placement and complete weil clauses.


## Fresh live evidence — 2026-10-06 — S02 E41–E50

- M27: E41 used stationary **im Briefkasten** instead of destination **in den Briefkasten**.
- M19: E45 still needs explicit subject in a weil clause; E50 was fully correct.
- M16: E44 kept **warten auf + Akk** correct.
- M14/M15: E43 correctly used sehen + Akk and helfen + Dat pronoun.
- M17: E46 **um ... zu** correct.
- M03: E47 **deshalb + V2** correct.
- M02/M08: E49 needs masculine possessive **seinen Namen**.
- Current higher-frequency targets: destination/location case, possessives, complete weil clauses, and article/case around feminine Dativ.


### M31 — einsteigen / aussteigen with transport
- Status: improving.
- Pattern:
  - **in + Akk + einsteigen**: in den Zug / in den Bus einsteigen.
  - **aus + Dat + aussteigen**: aus dem Zug / aus dem Bus aussteigen.
  - In Perfekt, both normally use **sein** in these movement uses.
- Evidence:
  - 2026-10-07 S02 E19: auxiliary correct, but **in + Akk** omitted.
  - E20: auxiliary correct; **vom Zug** used instead of **aus dem Zug**.
  - E26: wrong auxiliary and missing **in + Akk**.
  - E27: **aus dem Bus** correct, auxiliary still wrong.
  - E33: auxiliary improved to **bin**, but **in + Akk** still omitted.
  - E34: **bin ... aus dem Zug ausgestiegen** correct.
- Next action: retest both directions in fresh bus/train sentences; reduce frequency after repeated independent success.


## Fresh live evidence — 2026-10-07 — Perfekt S02 E41–E48

- **M31 improving, priority high:** E41 repeated the missing **in + Akk** pattern with **einsteigen**. Correct: **an der Haltestelle in den Bus eingestiegen**.
- **M31 improving, priority high:** E42 replaced **aussteigen aus + Dat** with *aufsteigen auf + Akk*. Correct: **aus dem Zug ausgestiegen**.
- Keep transport entry/exit in fresh Perfekt sentences until both directions succeed independently more than once.
- Separate new lexical/construction targets: **jemanden zum Essen einladen**, **an einem Kurs teilnehmen**, and stationary **am Schalter**.


## Fresh live evidence — 2026-10-07 — S03 E11–E20

- **M31 improving:** E11 correctly produced **in den Bus eingestiegen**; the remaining error was **an der Haltestelle**, not the vehicle-entry phrase.
- **M18 improving:** E12 and E20 independently produced **anfangen ... an + zu** correctly in Präsens and Perfekt. Reduce frequency and retest later.
- **M30 improving:** E18 regressed to *nach der Termin*; correct **nach dem Termin**. Keep in active rotation.
- **M27 / destination-location maintenance:** E16 used *im Rucksack* for a destination and also missed Perfekt. Correct **in den Rucksack gelegt**.
- **M01 dürfen:** E19 needs **Ich darf das Fenster öffnen.** Keep a fresh modal retest.
- Possessive/case maintenance: E13 needs feminine **seine Adresse**.
- Stationary preposition maintenance: E14 needs **vor dem Krankenhaus**, not *vom Krankenhaus*.


## Authoritative latest checkpoint — 2026-10-09

Earlier headings are imported/datetimed assessments; current structured statuses and the notes here take precedence.

### M19 — sentence-final verb with weil and wo
- Status: **improving**; priority low.
- Reference: weil ich kein Auto habe; Ich weiß, wo er wohnt.
- 2026-10-09-S02-E05: error — Missing finite ist in weil clause.

### M31 — einsteigen in + Akk / aussteigen aus + Dat
- Status: **improving**; priority high.
- Reference: in den Zug eingestiegen; aus dem Zug ausgestiegen
- 2026-10-09-S01-E03: independent correct — In den Zug einsteigen correctly used with modal Perfekt.

### M32 — Word order after und
- Status: **weak**; priority high.
- Reference: und ich habe ihn ...; or und ihn ...
- 2026-10-09-S01-E02: error — Und does not itself occupy the first position of the following main clause.

### M33 — haben auxiliary agreement
- Status: **improving**; priority high.
- Reference: ich habe; mein Bruder/er hat
- 2026-10-09-S01-E10: error — Hab mein Bruder needs hat mein Bruder.
- 2026-10-09-S01-E11: independent correct — Third-person auxiliary hat correctly formed; subject/detail problems are distinct.
- 2026-10-09-S02-E02: independent correct — Third-person auxiliary hat correctly formed; subject/detail problems are distinct.
- 2026-10-09-S02-E04: independent correct — Third-person auxiliary hat correctly formed; subject/detail problems are distinct.
- 2026-10-09-S02-E06: independent correct — Third-person auxiliary hat correctly formed; subject/detail problems are distinct.

### M34 — Preserve the intended subject in a follow-up clause
- Status: **weak**; priority high.
- Reference: Danach hat sie es gebucht. Deshalb hat er meine Schwester angerufen.
- 2026-10-09-S01-E09: error — Subject sie omitted after danach; es is the object.
- 2026-10-09-S02-E06: error — Ich changes brother to learner as caller; target er.

- M08: S02 E04 **sie sie** is valid subject+object reference to sister and bag.
- M03: S02 E06 deshalb V2 is correct; the wrong caller is M34.
- M28: S01 E09 needs **Gestern hat meine Schwester ...**; returned to improving.
- Missing gestern/zu Hause recorded as full-translation omissions, separate from successful dass order.
- S02 E06 **hab ich** is colloquial habe ich; do not invent an agreement failure from it. The required subject is **hat er**.
- dass has six correct written clause-order applications; keep grammar practicing rather than creating a false mistake pattern.


## Fresh live evidence — 2026-10-09 — S03 recent-material review

- **M19 weil/wo:** E01 already had correct final **ist** in the weil clause; E06 independently produced a complete **weil ... ist** clause. Positive fresh evidence; keep improving with reduced frequency.
- **M34 preserve intended subject:** E04 omitted **sie** after *danach*; fresh retest E08 changed the subject to **ich** instead of **sie**. E09 then independently preserved **mein Bruder → er** after *danach*. Keep **weak / high priority** until another varied independent success.
- **sich entscheiden für + Akk:** E01 missed **für**; E06 independently succeeded. Treat as a recent verb-specific target, not a new broad mistake pattern.
- **dass + Perfekt:** E03 omitted clause-final auxiliary; E07 independently succeeded with **vergessen hat**. Keep overall grammar practicing.


## End-of-day fresh evidence — 2026-10-09 — S04

- Requested tense control: Perfekt was used for a Präsens prompt with **kündigen**; retest tense labels.
- Third-person Präsens: **Meine Schwester verlängere** → **Meine Schwester verlängert**.
- **beantragen + Akk** directly: **ein/das Visum beantragen**, not *auf der Visum*.
- Object case/article: **den Mietvertrag**.
- Vocabulary form: **die Jacke** (repeated repair).
- Positive evidence: **erledigen** correct in fresh Präsens; **umtauschen** and **verlängern** Perfekt structures were understood.

## October 10 — wenn and als review
- E01 missed subject ich; E02 direction nach Hause and tense; E05 and E07 confused wenn with als for one-off past event.
- E08: separable present bereitet ... vor. E03, E04 and E06 were independently correct.
- Recognition quiz: 3/4, future conditional incorrectly classified as als. Retest before mastery.

## 2026-10-10 Reading: Das verlorene Paket
- Independent errors: niemand instead of niemanden in Akkusativ; der Nachbarn rather than der Nachbar as subject; seinen Nachbarin rather than seinen Nachbarn; nicht after geantwortet; omitted nicht in a transfer sentence; incorrect modal/infinitive construction; pronoun order; spelling Paket.
- Initially used in die Tasche for static location. Final fresh independent response used in die Tasche for movement and in der Tasche for static location correctly; only typo gester instead of gestern. Treat Wo/Wohin as improving, not mastered; schedule later retention check.


## 2026-10-11 targeted review: 17 independent written exercises
- Clear improvement: **als** one-off past and **wenn** conditional, in der Tasche vs in die Tasche, modal Perfekt independent follow-up **hat ... kaufen können**, and masculine Dativ **meinem Bruder / seinem Freund** after earlier case confusion. Do not promote to mastered after one session.
- Active remaining: **nach + Dativ** (nach dem Mietvertrag; nach den Unterlagen), **sich entscheiden für + Akk**, **niemanden** Akk, Perfekt double infinitives on first attempt, V2 after fronted Gestern, Dativ recipient vs Akk item, location phrase, plural Unterlagen, and object-pronoun ordering **es ihm** vs **ihm es**. E17 correct with es + Dativ noun; E18 two-pronoun test still unanswered.
- Written-only attempts; do not update oral dimensions. Reference: 2026-10-11-S01-E01–E17, days/2026-10-11.md.

## Checkpoint 2026-10-11 S03-E02
S03-E02: M28 correct V2 after obwohl and correct reparieren Perfekt; hat gestern mein Bruder is grammatical. M08: der Fahrrad / ihn needs das Fahrrad / es; previously unexplained gender, not failed lexical recall. Retest later, no mastery promotion.

## Checkpoint 2026-10-11 S03-E03
S03-E03: correct Dativ dem Vermieter and Perfekt habe ... überwiesen. Lexical/form distinction die Miete versus die Mieter; no new broad case/order error. Retest later.

## Checkpoint 2026-10-11 S03-E04
S03-E04 ausgeben: er gibt, not gebt; viel Geld (uncountable), für + Akk. Separable aus produced. First item-specific error, no invented broad repeated-error pattern; fresh transfer E05 before moving on.

## Checkpoint 2026-10-11 S03-E05
S03-E05 fresh independent success on ausgeben third-person gibt, viel Geld, für + Akk and final aus after E04. Only spelling Miet → Miete; reduce immediate drilling and advance to verdienen, keep delayed retest 2026-10-12.

## Checkpoint 2026-10-11 S03-E09
S03-E09 correct temporal feminine Dativ nach der Arbeit, main-clause V2 and packt ... aus. Remove unnecessary comma after phrase; Packet → Paket spelling. Do not treat as failure of verb use or as mastery of masculine/plural temporal Dativ.

## Checkpoint 2026-10-11 S03-E10
S03-E10 correct obwohl/V2 and verbessern. Few/quantity form repair wenige Zeit → wenig Zeit, comparable to E04 viele Geld → viel Geld; light embedded maintenance, not a word-order error. Ich → ich capitalization. Continue progression.

## Checkpoint 2026-10-11 S03-E11
S03-E11: er verspricht (e → i), not verspreche; repeated das Fahrrad gender target (den incorrect). mir and dass-final repariert correct. Neutral order dass er morgen; marked dass morgen er not automatically a syntactic failure. Embed gender and third-person form in later fresh work; progression continues.

## Checkpoint 2026-10-11 S03-E12
S03-E12 used Präsens erlaubt instead of requested Perfekt hat ... erlaubt after model. Dativ mir and zu-infinitive correct with support. Retest tense in one new permission sentence; no independent mastery evidence.

## Checkpoint 2026-10-11 S03-E13 and progression
S03-E13: fresh correct erlauben Perfekt and Dativ meiner Schwester. Feminine Meine Mutter and the natural infinitive group das Auto zu benutzen need repair. Progress to next batch; embed possessive gender, tense and infinitive-group review, not extended review blockage.

## Reading S05-E02 — 2026-10-11
- zeigen recipient + Dativ: original mit einem Kollege needs ihrem Kollegen for intended recipient; even mit einem requires Kollegen (-n). Related existing M15; no new pattern ID. Perfekt hat ... gezeigt correct.
- Text-detail Datei versus Unterlagen repaired again; comprehension/lexical selection separate from Perfekt grammar. Next fresh transfer S05-E03.

## Reading S05-E03 — 2026-10-11
- Fresh transfer correctly uses zeigen + Dativ recipient without mit: seinem Freund das Bild. Positive M15 evidence after E02; one success does not promote mastery. Kollege form not produced (Freund substituted), gestern omitted; keep semantic detail separate from correct grammar.

## Oct 12 S02 real attempt evidence
- M08 pronoun: S02-E06 er was used as Akk object for die Datei (should sie); S02-E07 es for das Fahrrad independently correct. Mixed evidence; continue retest of feminine reference.
- M15: S02-E02 lacked the thing sent and recipient needed ihrem Kollegen, including weak masculine -n; S02-E07 independently correct es meiner Schwester gezeigt. Individual n-form still unresolved.
- M19: S02-E04 correct weil ... gefunden hat; S02-E05 missing final hat. Do not mark as mastered.
- M28: S02-E06 correctly used deshalb hat sie; subsequent main-clause V2 also correct. Older error history remains intact.
- Specific repairs: noch nicht (E01); hat verglichen and ins Internet, omitted gestern (E03); darin einen Fehler independently correct after prior repair (E05); lexical Datei vs Unterlagen; spelling Programm. No new mistake IDs or imagined pronunciation evidence.

## 2026-10-12 S03 new grammar tense adherence
- E01: clause-final verb and main V2 correct; tense mismatch: subordinate geschickt hat (Perfekt) instead of schickt (Präsens). Do not register a new structural-word-order mistake.
- E02: independently correct feminine die Datei -> sie and mit der alten Datei + Dativ in a new bevor context, positive contextual evidence for old M08 and case patterns. Single success is not proof of global mastery.


## E04/E05 before-clause review: Oct 12 close
- S03-E04: learner wrote dem Kollege, corrected to ihrem Kollegen (possessive Dativ and weak-masculine ending -n). Bevor within the sentence was capitalized incorrectly. Correct Perfekt in subordinate and main clauses.
- S03-E05: independently correct seinem Kollegen (Dativ -n) and es for das Bild; also correct subordinate-final verb and main V2. This is one successful fresh transfer, not definitive mastery.
- Five independent full sentences with bevor, three fully correct; S03-E01 needed Präsens instead of Perfekt, S03-E04 needed capitalization and Dativ corrections.
- Pending review S03-E06 concerns plural Unterlagen -> sie, before + Perfekt and Dativ. Historic unresolved items preserved.

## October 13 inserted image direction error
- 2026-10-13-S01-E01 independent: 'Mein Bruder fügt das Bild in der Datei ein, danach speichert er sie'. Correct 'Mein Bruder fügt das Bild in die Datei ein. Danach speichert er sie.' This is a directional two-way-preposition error: einfügen in + Akk (Wohin?) rather than stationary in + Dat (Wo?).
- Correct separately: fügt ... ein separable, danach V2 speichert er, Akk object sie for die Datei. One specific case error does not negate independent success for verb form.
- 2026-10-12-S04-E01 answered after midnight and independently fully correct: 'Meine Schwester kopiert die Datei, danach bearbeitet sie sie.' Positive contextual evidence on feminine pronoun and V2.
- Fresh test next E02 with in die Datei after inserting feminine die Kopie. Do not automatically mark the directional preposition issue mastered after reading model; preserve older cases/mistake IDs.

## Oct 13 E02 missing object sie after insertion
- Independent learner: Meine Schwester hat gestern eine Kopie erstellt, danach hat sie in die Datei eingefügt.
- Corrected: Meine Schwester hat gestern eine Kopie erstellt. Danach hat sie sie in die Datei eingefügt.
- Correct Perfekt of erstellen and einfügen, in + Akk direction. Missing direct object sie referring to die Kopie. Review existing M08, do not create new mistake ID. E03 new verbs exercise pending.

## 2026-10-13 final handoff after E02 — M08 evidence
- Persisted Oct13 S01-E02 independent result into progress.json: correct 'hat erstellt', 'hat eingefügt', 'in die Datei', but missing direct Akk pronoun 'sie' for die Kopie in second clause. Counts as another fresh M08 pronoun omission, not failure of Perfekt or preposition.
- E01 had 'in der Datei' instead of 'in die Datei' for insertion; E02 correct in die Datei is positive same-session repair, not delayed mastery. Further independent retests due under review queue.
- Status: Oct13 S01 paused for new-chat transition, not day close. Next E03 exact Arabic: أختي بتختار المرفق، وبعد كده بتضيفه للرسالة. For that sentence test masculine accusative ihn (der Anhang) and Dativ der Nachricht, as well as separable verbs.
- Existing error pattern IDs M08 and directional two-way-preposition category retained. No invented pronunciation or oral evidence.

## 2026-10-13 S02-E01 — typo versus grammar
- Raw: `Gestern hat meine Schwester die Bestätigung geprüft, danach hat sie sei dem Kollegen geschickt`. Natural: `Gestern hat meine Schwester die Bestätigung geprüft. Danach hat sie sie ihrem Kollegen geschickt.`.
- **sei → sie** is plausibly a spelling/metathesis slip, not established incorrect feminine case/gender; no new M08 grammar-error count. Delayed fresh check remains appropriate.
- **dem Kollegen** has correct Dativ and weak masculine -n; however intended **لزميلها** requires possessive **ihrem Kollegen**. Preserve this as a semantic/possessive issue, not a Dativ failure.
- Correct independent Perfekt of prüfen/schicken and main V2; full sentence still needed correction.

## 2026-10-13 S02-E02–E04 final written checkpoint and pause
- E02 raw: `Gester hat mein Bruder die Programm aktualisiert, danach hat er den Fehler aus der Datei gelöscht`. Correct lexical and case dimensions for `hat aktualisiert`, `den Fehler`, `aus der Datei`, and verb-second. Repair the orthographic `Gester` and neuter `das Programm`; treat `gelöscht` as valid in context but not as independent recall of `entfernen`.
- E03 raw: `Meine Schwester hat gestern den Anhang von der Nachricht entfernt, danach hat sie dem Kollegen eine Nachricht geschickt`. Correct Perfekt `hat entfernt`, masculine Akk `den Anhang`, Dativ `dem Kollegen`. `von der Nachricht` is possible; `aus der Nachricht` is more idiomatic. Definite **`die Nachricht`** required to preserve the same referent; **`ihrem Kollegen`** for her colleague (possessive).
- E04 raw: `Gestern hat meine Schwester die Datei ausgewählt, danach hat sie hinzu die Nachricht gefügt`. Correct `hat ausgewählt` / verb-second. `hinzugefügt` is a single Perfekt participle, second clause must include the feminine object pronoun `sie` and Dativ `der Nachricht`. Correct: `Danach hat sie sie der Nachricht hinzugefügt.`
- These are distinct observable spelling, noun gender, referential definiteness, separable-Partizip, pronoun and recipient-possession issues; do not relabel `von der Nachricht` as ungrammatical or invent a recurrent-error count from one answer. Preserve currently weak **M32/M34** and improving **M08** as per the structured status map.
- Learner explicitly paused after E04. **S02-E05 remains unanswered**, focused on `verschieben` Perfekt and Dativ `seiner Schwester`. The old S01-E03, other pending exercises and reviews remain saved. All evidence is written, not spoken or listening.

## 2026-10-14 S01-E03 — M08 object omission
- Original `Gestern hat mein Bruder das Fahrrad repariert, damit meine Schwester heute benutzen kann.`; corrected `Gestern hat mein Bruder das Fahrrad repariert, damit meine Schwester es heute benutzen kann.`. Omitted es for das Fahrrad. Main Perfekt correct; purpose/order had near-model support. Append to existing M08, remain improving; fresh die Datei/sie retest E04 pending.

## 2026-10-14 S01-E04 — M08 fresh transfer
- `Ich speichere die Datei, damit mein Bruder sie morgen drucken kann.` independently correct: sie refers to die Datei, Akk object. Fresh success after E03 omission, M08 remains improving; no delayed retention claim.

## 2026-10-14 S02-E02 — M08 direct-object omission
- Original `Meine Schwester hat gester den Vorschlag angeneommen,  danach hat sie ihrem Kollegen geschickt `; corrected `Meine Schwester hat gestern den Vorschlag angenommen. Danach hat sie ihn ihrem Kollegen geschickt.`. Missing ihn for masculine Vorschlag. Correct ihrem Kollegen Dativ, hat geschickt and V2 separate. Existing M08 retained improving; fresh transfer in E03 pending.

## 2026-10-14 S02-E03 — M08 fresh correct pronoun
- `Mein Bruder hat gestern den Vorschlag abgelehnt, danach eklärt er ihn seiner Schwester.` correctly uses ihn for Vorschlag and seiner Schwester Dativ. Second-clause tense/spelling error separate; M08 retained improving. Correction `Mein Bruder hat gestern den Vorschlag abgelehnt. Danach hat er ihn seiner Schwester erklärt.`.

## 2026-10-14 S02-E04 — M02 possessive Dativ
- `Obwohl meine Schwester gestern den Vorschlag abgelehnt, stimme ich heute meinen Kollegen zu  ` needs `Obwohl meine Schwester gestern den Vorschlag abgelehnt hat, stimme ich heute meinem Kollegen zu.`. zustimmen requires meinem Kollegen for one recipient; -n on Kollegen correct weak-noun form. Missing final hat is a separate auxiliary issue. M02 stays improving; main V2 and stimme ... zu correct.

## 2026-10-14 S02-E05 — M02 repeated singular Dativ
- `Mein Bruder hat gestern seinen Kollegen widersprochen, aber ich habe meinen Kollegen zugestimmt ` → `Mein Bruder hat gestern seinem Kollegen widersprochen, aber ich habe meinem Kollegen zugestimmt.`. Correct auxiliary/participle forms; recipient seinen/meinen needs seinem/meinem, as widersprechen and zustimmen both govern Dativ. Noun Kollegen correct. Continue embedding cases in new verbs; no broad regression or mastery inferred.

## 2026-10-14 S02-E06 — M02 fresh Dativ success
- Original `Mein Bruder vorschlagt seinem Kollegen einen Termin, danach bespricht er ihn die Vorschlag ` correctly contains seinem Kollegen and einen Termin. Corrected full sentence `Mein Bruder schlägt seinem Kollegen einen Termin vor. Danach bespricht er den Vorschlag mit ihm.`; vorschlagen separation/Umlaut, masculine den Vorschlag and mit ihm are separate corrections. Keep item evidence distinct.

## 2026-10-17 S01 —isolated123 recall only
-8 spelling repairs: verängern → verlängern; sich erinnenrn → sich erinnern; unterschrebien → unterschreiben; errichen → erreichen; anfengen → anfangen; aktulisieren → aktualisieren; duchen → duschen; wechslen → wechseln. Not evidence of grammatical case/order weakness.
- Distinctions: holen/mitbringen, dürfen/erlauben (both directions), sitzen/setzen (both directions), möchten/wollen. Complain requires sich beschweren.
- Broad-prompt mitnehmen and delivery-context mitbringen accepted alternatives; exact general nehmen/bringen recall unconfirmed. sich entscheiden accepted without für in infinitive-only task.106 other target forms correct. No contextual grammar/oral reassessment; existing M-pattern statuses unchanged. Repairs due2026-10-18, embedded in future requested sentences.

## 2026-10-17 S02-E01 —Nominativ subjects and wissen
- Original `Mein Schwester weißt nicht , ob ihrem Kollegen die Auskunft braucht` → `Meine Schwester weiß nicht, ob ihr Kollege eine Auskunft braucht.`.
- M02 improving baseline retained; new feminine meine before Schwester and masculine ihr Kollege as subordinate subject need Nominativ. Dativ ihrem Kollegen is not this subject. Same intended people preserved, so no new M34 error. sie weiß vs du weißt is a verb form repair.
- ob and final braucht independently correct. Auskunft identity/gender correct; eine vs die is intended indefinite meaning. Fresh E02 retest and delayed retestOct18; no global regression inferred.

## 2026-10-17 S03-E01 —relative grammar and static Dativ correct
- `Das ist der Drucker, der auf dem Tisch liegt ` has correct der relative, final liegt, and auf dem Tisch Dativ. M27 stable with fresh independent success.
- Preferred printer wording `Das ist der Drucker, der auf dem Schreibtisch steht.`: typical printer steht; liegt can describe lying orientation. Treat as contextual naturalness refinement, not incorrect conjugation/case or demonstrated stehen recall. Tisch general vs Schreibtisch specific. No subject identity/pronoun error or new M-pattern created.

## 2026-10-17 S03-E02 —fresh Dativ success
- `Das ist die Frau, die meinem Bruder hilft ` independently fully correct. M02: meinem Bruder after helfen singular Dativ; status improving retained alongside earlier Nominativ repairs. Final hilft and feminine relative die correct, no new error inferred.

## 2026-10-17 S03-E03 —written liest repair, relative success
- `Das ist das Kind, das die Anleitung list` → `Das ist das Kind, das die Anleitung liest.`. Correct neuter das and clause-final position. list→liest is a written present-form repair, not a relative-pronoun error, failed infinitive recall or assessed pronunciation. Retest fresh liest context later, dueOct18. No new grammar-error pattern/status change from this single occurrence.

## 2026-10-17 S03-E05 —possessive meaning, correct case
- `Nimm bitte den Reisepass mit!` → `Nimm bitte deinen Reisepass mit!` to retain «جواز سفرك». Den is correct masculine Akkusativ but lacks requested possession; do not record a false Akk/Dat or imperative error. nimm...mit independently correct. Existing M-pattern statuses unchanged; embed a later possessive-fidelity check.

## 2026-10-17 S03-E06 —Dativ correct, plural imperative repair
- `Hilft meinem Bruder bitte !` → `Helft meinem Bruder bitte!`. M02 fresh correct meinem Bruder after helfen; keep improving. Final bitte valid. ihr imperative Helft differs from third-singular hilft and du Hilf; no new case error or pronunciation inference.

## 2026-10-18 —source 2026-10-17-S04-E01, answered in 2026-10-18-S01
- `Meine Schwester hat gestern beim Kundendienst nachgefragt, danach hat sie ihrem Kollegen eine Nachricht geschickt` independently fully correct. M02 ihrem Kollegen Dativ; M28 danach hat sie; M34 sister preserved as sie.
- M28 promoted improving→stable using Oct11 three correct and Oct12 two correct records after Oct9 error plus today,6 across3sessions. Existing successful_session_ids with old pre-error dates retained as historical, rationale based explicitly on post-error evidence. M02/M34 statuses preserved; no pronunciation evidence.

## 2026-10-18 S01-E02 —fresh correct transfer
- ihren Kollegen Akk and explicit sie correct in a fresh Perfekt sentence; M02 improving/M34 weak remain with one success since latest errors. Gestern hat/ danach hat sie correct; M28 stable. Same-session transfer not delayed retention; earlier errors retained.

## 2026-10-18 S01-E03 —correct subjects and object pronoun
- M34 weak -> improving: two fresh independent explicit subjects since latest E01 error (E02 sie, E03 sie); M02 correct meiner Schwester and M08 correct es recorded. Missing mir is explicit recipient information omission, not wrong es/gender, wrong possessive case or grammatical invalidity. und sie bringt…zurück correct; M32 evidence in live JSON. Earlier errors retained.

## 2026-10-18 S01-E04 —und order distinct from subject identity
- M32 weak: und hat er -> und er hat. Correct er preserves brother, so M34 improving with fresh correct identity evidence; M08 improving with correct es for Buch. M28 stable unchanged, no fronted-adverb error. New participle aufbewahret -> aufbewahrt recorded in verb161 and delayed target; no invented generalized spelling pattern.
