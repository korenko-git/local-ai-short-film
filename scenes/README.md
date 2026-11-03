# Story, scenes and production status

The scene READMEs contain the production notes, version history and exact Russian dialogue. Latest montage timeline: `work/film-edit-v3/timeline.json`.

## Story

A nine-year-old adventurer sails to an island, receives a map, passes four trials (courage, curiosity, ingenuity, speed), finds a grey two-wheel scooter and helmet, descends to the beach by zipline and receives a birthday greeting beneath the stars. Only the dossier is illustrated; the other scenes preserve the photorealistic character identity.

| Scene | Title | Current state |
|---|---|---|
| 01 | [Ship and island](01-ship-island/README.md) | Assembled; check transitions/loudness in the full edit. |
| 02 | [Cabin and folder](02-cabin-folder/README.md) | Assembled; check transitions/loudness in the full edit. |
| 03 | [Illustrated dossier and stamp](03-dossier-stamp/README.md) | Assembled; the deliberately illustrated exception to the photorealistic film. |
| 04 | [Receiving the map](04-map/README.md) | v4 assembled; the revised four-trial voice line awaits separate assessment in the original notes. |
| 05 | [Landing on the island](05-landing/README.md) | Assembled; check transitions/loudness in the full edit. |
| 06 | [Courage: suspension bridge](06-courage-bridge/README.md) | Accepted scene v2 retained; montage v3 for the full film awaits review. |
| 07 | [Curiosity: shell and dead end](07-shell-dead-end/README.md) | Accepted complete scene retained; montage v2 for the full film awaits review. |
| 08 | [Ingenuity: water puzzle](08-ingenuity-gate/README.md) | Accepted scene retained; montage v3 for the full film awaits review. |
| 09 | [Speed: closing gate](09-speed/README.md) | Complete scene v3 explicitly accepted; 28.83 seconds, five accepted segments. |
| 10 | [Chest and gift](10-chest-gift/README.md) | Accepted complete scene retained; montage v3 for the full film awaits review. |
| 11 | [Night-time zipline](11-zipline/README.md) | Full scene v2 accepted; montage v4 for the full film awaits review. |
| 12 | [Birthday under the stars](12-birthday-finale/README.md) | Scene v1 explicitly accepted; original clip 17.208 seconds. |

## Full-film assembly

Latest source: `output/assemblies/film-scenes-01-12-review-v3.mp4`, 250.250 seconds, 1344 x 768, 24 fps, 48 kHz stereo. The original record says pending full-film review; do not infer global approval from accepted individual scenes. Previous assemblies are in local `work/archive/assemblies/`.

In v2 the bridge badge moved to the landing at 1:10, duplicate poses were trimmed, narration moved after the failed turn, the chest reaction shortened and the first-ride clip removed. In v3 another 2.5 s near the wheel and 2.25 s after packing were removed; 1.75 s of parrot flight/reaction were restored. Sources were preserved and their SHA-256 checks recorded.

The ending was simplified from earlier plans to three scenes: chest/gift, night-time zipline, birthday greeting. Removed trials and the port-scroll/seal ideas must not be restored automatically. The narrator handles introduction, mission and birthday speech; only the parrot says the two-wheels/no-cannons joke. The final zipline uses a two-hand trolley handle and a scooter case.

## Working rules

Read the selected scene README, [general workflow](../docs/SCENE-WORKFLOW.md), and [Comfy MCP guide](../docs/COMFY-MCP-LLM.md). Show connected frames before FreeVideo and wait for feedback. Update result paths, feedback, tasks, parameters and a short journal after work. Interrupted/rejected/unreviewed results are distinct from accepted ones. Never launch another scene while organizing files.

Public article: [English](../article/index.html), [Ukrainian](../article/uk.html), [Russian](../article/ru.html). The earlier local PDF in `output/pdf/` predates the multilingual rewrite.


## Ending development and continuity

On 2 November 2026, earlier scenes 10–13 were removed to reduce the generation workload; former scenes 14–17 were renumbered 10–13. The user then approved merging treasure arrival and reveal, yielding the current consecutive 01–12 structure. Do not restore the cancelled episodes. The final three scenes initially targeted 7–9 shots and 65–80 seconds, to be refined after speech. Keep the restored text complete and avoid stretching approach/packing.

After the gate, check the map, reach the platform above the bay, put away the map and say "Вот ты где!". Reveal frame v3 is the shared join between chest clips 2 and 3; it replaces a lid that seemed to open by itself. Two unrelated map images were rejected. Narrator v2, parrot v4 and the character's line were accepted within the four-segment voiced preview, saved as scene-10 v1. The proposed gold transformation from trial 4/4 to black "МОЛОДЕЦ" and the narrator "Молодец!" remain separate pending items.

The narrator says "Перед нами новейшее достижение мирового кораблестроения." The pirate parrot says only "Два колеса, один руль, ни одной пушки. Зато какая скорость!". The narrator also gives the night mission and complete birthday greeting; exact text is in scenes 11–12. The user cancelled map seals and the port scroll, proposing a taut sloping zipline directly to the beach. Ice axes were an early idea, later replaced by a suspended trolley handle held in both hands; folded scooter in a case.

Selected scene-11 clip 2 begins with clip 1's actual last frame and turns toward the approved high cliff. Clip 3 starts at clip 2's actual ending, mixes Drama 3 with the descent and requires visibly moving waves; actual duration 10.125 s, seed 11110138. Earlier pending notes were superseded by explicit acceptance of the full scene v2. The separate ride remained in that accepted scene but was removed by the later full-film revision. Keep one consistent face/costume, canonical chest and grey scooter throughout.

Storyboard: `../STORYBOARD.jpg`; the former `../STORYBOARD-OLD.jpg` is historical. The initial article/PDF edition was prepared from v3; the site now has equivalent English, Ukrainian and Russian first-person editions.

## Production journal

- 2026-11-03: moved the public article source to root `article/`, generated three Markdown editions in `docs/`, and updated README/video links and the Actions repository URL. Article/site builds validated; no production media or approval states changed.

- 2026-11-03: added a contact-sheet example of Luna's video inspection and the recorded rejection/retry of the scene-09 anime-like sprint to the article's editing section. All translations and generated pages updated; production footage and approval records unchanged.
- 2026-11-03: added the filmmaker's rejected duplicate-character example beside the article's missed third hand, explaining the risk of trusting successful agent checks too much. Viewing copy and all translations updated; production media and approval states unchanged.
- 2026-11-03: expanded the bridge artifact account with early Qwen attempts, supplied photographic references and the resulting anatomy/railing errors. All article translations and generated pages updated; production media unchanged.
- 2026-11-03: expanded the three-language article with the filmmaker's artifact review: map orientation/continuity, inherited third hand, puzzle keyframe development, uphill water, failed hourglass flip and unintelligible speech. Read the actual scene-09 prompt and endpoint references; proposed causes are labelled as hypotheses. Prepared metadata-stripped viewing copies and short final-film excerpts, preserving production media and approval records.
- 2026-11-02: expanded all three article editions with scene 04 wind, scene 08 water motion and scene 09's accepted dynamic-camera insert, supplied motion-reference contact sheet and production history. Web copies preserve the original scene files and approval states.
- 2026-11-02: assembled scenes 01–12 in order with common 1344 x 768 / 24 fps picture and 48 kHz stereo sound. Full-film review was not automatically recorded as acceptance.
- 2026-11-02: v2 was 253.208 s. Moved the bridge reward to the landing, trimmed repeated poses, moved failed-attempt narration after the turn, shortened chest reaction and removed the first-ride clip. Original files passed SHA-256 checks and the result decoded without errors. Edit parameters/timeline: `work/film-edit-v2/`.
- 2026-11-02: v3 is 250.250 s: removed another 2.5 s by the wheel, restored 1.75 s of parrot flight/reaction, removed 2.25 s after packing. Source hashes still matched the pre-v2 record; prior v2 moved to `work/archive/assemblies/`. Parameters/timeline: `work/film-edit-v3/`. Full-film approval remains unrecorded.
- 2026-11-02: consolidated production documentation into English, retaining exact Russian dialogue. No source render, edit or approval state changed.
