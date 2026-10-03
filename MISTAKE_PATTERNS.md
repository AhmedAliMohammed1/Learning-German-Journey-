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
