# Adaptive mistake tracking

Imported patterns were reported in the prior conversation. Exact learner answers, occurrence counts, and dates were not available. Initial status **needs_check** means reported and awaiting fresh evidence; it does not assert a measured weakness.

## Status and evidence rules

- needs_check → weak after an independently observed relevant error; or → improving after a fresh independent correct use.
- weak → improving after at least 2 independent correct uses in different sentences after the latest error.
- improving → stable after at least 4 independent correct uses across at least 2 actual sessions after the latest error.
- stable → improving after a new relevant error; repeated errors return it to weak.
- A hint or copied correction does not advance the independent success streak.
- These thresholds are adjustable defaults. Record dated reasons for changes; never fabricate historical counts.
- Prioritize weak patterns, include occasional improving checks, and sample stable patterns less often. Use fresh sentences and vocabulary.
- Examples below are tutor reference examples, not answers submitted by the learner.

| ID | Reported pattern | Rule / correct example | Status | Recorded errors | Independent correct | Last checked |
| --- | --- | --- | --- | --- | --- | --- |
| M01 | darf / darfst | ich/er/sie/es darf; du darfst. Mein Bruder darf zu Hause bleiben. | needs_check | 0 | 0 | unknown |
| M02 | meinem / meinen / mein; Akk/Dat | Ich helfe meinem Bruder. Ich sehe meinen Bruder. Mein Bruder kommt. | needs_check | 0 | 0 | unknown |
| M03 | deshalb word order | deshalb occupies position 1; finite verb position 2. Deshalb bleibe ich zu Hause. | needs_check | 0 | 0 | unknown |
| M04 | wissen / kennen | Ich weiß, wo er wohnt. Ich kenne diesen Mann. | needs_check | 0 | 0 | unknown |
| M05 | sitzen / setzen | Ich sitze auf dem Stuhl. Ich setze mich auf den Stuhl. | needs_check | 0 | 0 | unknown |
| M06 | helfen + Dativ | Ich helfe meiner Schwester. Perfekt: Ich habe ihr geholfen. | needs_check | 0 | 0 | unknown |
| M07 | denken an + Akkusativ | Ich denke an meinen Bruder. | needs_check | 0 | 0 | unknown |
| M08 | object pronouns with vergessen | Der Schlüssel: Ich habe ihn vergessen. Die Tasche: sie. Das Handy: es. | needs_check | 0 | 0 | unknown |
| M09 | infinitive after modal verbs | Ich muss heute arbeiten. Infinitive at the end. | needs_check | 0 | 0 | unknown |
| M10 | anfangen conjugation | Ich fange an. Du fängst an. Er fängt an. | needs_check | 0 | 0 | unknown |

Zero counts mean no attempts recorded in this repository, not zero historical mistakes.

## Current grammar diagnostic

Check in der Nähe + Genitiv naturally during practice. It is an active study focus, not yet an evidenced recurring mistake. Create a separate mistake pattern only if actual answers justify it.

## Evidence log

No fresh evidence at initialization. Append: date, session/exercise ID, learner answer, correction, error or independent success, hint status, and resulting status. Mirror counters and status into progress.json.mistake_patterns.
