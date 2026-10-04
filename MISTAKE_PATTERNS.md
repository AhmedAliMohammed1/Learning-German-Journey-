# Adaptive mistake tracking

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
