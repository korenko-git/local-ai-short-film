# 08. Ingenuity: water puzzle

## Current state and full-film revisions

The complete scene v1 was accepted on 2 November 2026, including the voices and achievement: `output/scene08-ingenuity-gate-v1.mp4`. It matches `work/scene08-full-preview-v1.mp4` by SHA-256. The original accepted edit is 56.21 s, 1344 x 768, 24 fps.

The later full-film revision `work/scene08-montage-v3.mp4` awaits separate review. In v2, six frames were trimmed from each side of shared poses; the line "Первая попытка оказалась ошибочной" moved to 16.667 s, after the wrong turn, and short speech overlaps were removed. Filter: `work/scene08-montage-v2-filter.txt`. In v3 a further 2.5 s hold at the end of the wheel approach was removed: the source tail trim is 66 frames instead of six. Wheel movement and the door opening/closing were retained, with all following voices and the badge shifted with picture. Source clips, voices, prompts and parameters were unchanged. The v3 change followed feedback at full-film 2:11–2:13, 3:17–3:19 and 3:37–3:39.

## Story and mechanism

The character exits scene 7's vines onto a stone platform. The camera rises and turns toward an overhead view, revealing disconnected channels, two rotating discs, a waterwheel and a closed door. Preserve the same face, costume and map; show where the map is put before both hands are needed. This replaces an older branch-and-lever-ring/grille concept.

There is one winding route without branches. Each circular disc has an L-shaped channel and turns 90 degrees around its central axis; other stones remain fixed. Initially the water hits the north wall of disc A. Turn A 90 degrees counterclockwise: water reaches the south wall inside disc B. Turn B 90 degrees clockwise: water reaches the wheel, turns it and opens both door leaves.

The character first puts the map on dry stone, turns A incorrectly, and tries turning the wheel by hand. The door opens during the effort but immediately closes when he lets go to wipe sweat. He then solves the two discs, retrieves the map and walks through. Water must visibly flow within its current reachable route. Until the correct second turn, the wheel and door must remain still except during the deliberate manual attempt.

### Earlier staging proposals, not blanket approvals

The proposed sequence included a splash on the nose, a resolute wipe, a stiff first turn suddenly giving way with a comic balance-recovery step, and a raised finger followed by a hop onto a dry edge before incoming water. Only the stiff-turn/balance action was explicitly carried into the approved first-turn v3. The initial extra gags remained proposals; do not assume acceptance from the overall scene description. The achievement is "СМЕКАЛКА — ИСПЫТАНИЕ 3 ИЗ 4", with the character line "Смекалка — есть!".

## Channel diagrams and image versions

The diagrams are schematics, not film keyframes. Keep their source, door, wheel, fixed channels and camera aligned; do not transfer service letters/colour labels into a generated shot. They were originally awaiting their own assessment.

| Record | Purpose |
|---|---|
| `refs/channels-01-start.svg` | Initial obstruction at A |
| `refs/channels-02-first-move.svg` | Correct A, obstruction at B |
| `refs/channels-03-solved.svg` | Correct A/B, wheel supplied and door open |
| `refs/channels-overview.svg` | Side-by-side comparison |
| `refs/draw_channels.py` | Diagram source |
| `refs/archive/square-turntables-v1/` | Previous square-tile PNG previews |

GPT Image v1 had a useful composition but incorrect channels. The user requested round discs; v2 changed the composition and was not used. The start frame v3 was accepted. The accepted linked image sequence is:

- `frames/approved/scene08-puzzle-start-gpt-image-v3.png`: initial puzzle.
- `frames/approved/scene08-puzzle-entry-gpt-image-v1.png`: character approaching from a distance.
- `frames/approved/scene08-first-turntable-action-gpt-image-v2.png`: correct first turn; later v3 adds the requested sudden release/balance recovery and was accepted too. Task: `workflows/images/scene08-gpt-image-turn-1-v3/`.
- `frames/approved/scene08-second-turntable-thinking-gpt-image-v2.png`: thought at B; preserve correct A and water stopping inside B.
- `frames/approved/scene08-puzzle-solved-gpt-image-v2.png`: both discs aligned, water at the rotating wheel, both door leaves open, character seated by B. Task: `workflows/images/scene08-gpt-image-solved-v2/`.

The user also accepted four preparation/failure frames: `scene08-puts-map-down-gpt-image-v1.png`, `scene08-first-disc-wrong-turn-gpt-image-v1.png`, `scene08-manual-wheel-test-gpt-image-v1.png`, `scene08-door-closes-when-wheel-stops-gpt-image-v1.png`, all in `frames/approved/`.

Qwen 2.1 trials remain in `frames/drafts/` and `workflows/images/scene08-water-channel-keyframes-v1/`. They copied service letters from diagrams and had inaccurate water routing; do not use them as the selected clip inputs. Prompts, references and settings for GPT Image variants are in their `workflows/images/` packages.

The first Qwen batch produced two saved results; its third run was cancelled when the image tool changed. Initial GPT Image v1 supplied start/first-move/solved states, but feedback noted that the solution did not show water through the second channel or the character's turning action. The round-disc correction retained the useful first composition. Before v2 correction, the first disc was crooked and water failed to reach the internal south wall of the second; both states were regenerated. The user accepted the resulting five images, then requested the manual-wheel failure and explicit map-down/wrong-turn ordering; all four additional states and the revised first-turn v3 were separately shown and accepted before video.

## Accepted video sequence

Originals remain in `video/raw/`. Accepted copies use these names in `output/clips/`:

| Order | Clip | Seed | Action |
|---|---|---:|---|
| 1 | `scene08-approach-v2.mp4` | 11080102 | Approach the platform |
| 2 | `scene08-map-down-v1.mp4` | 11080103 | Crouch and put down the map |
| 3 | `scene08-wrong-turn-reset-v1.mp4` | 11080104 | Wrong turn, then edited reverse back to the original state |
| 4 | `scene08-approach-wheel-v3.mp4` | 11080108 | Approach/touch the stationary wheel |
| 5 | `scene08-manual-wheel-v3.mp4` | 11080110 | Manual effort, door opens then closes after release |
| 6 | `scene08-correct-first-turn-v1.mp4` | 11080111 | Correct A, water reaches B |
| 7 | `scene08-correct-second-turn-v1.mp4` | 11080112 | Correct B, water drives the wheel and opens the door |
| 8 | `scene08-enter-door-v1.mp4` | 11080113 | Retrieve the rolled map and pass through |

Later working clips use 1344 x 768, 24 fps, 16 steps and about 6.58 s each. Early Max trials used 20 steps; keep the per-task parameters as the authority. Every package retains prompt, media, inputs, seed and settings.

## Iteration journal: approach and wrong turn — 1 November 2026

- Replaced the grille story with the two-disc water puzzle; recorded the proposed gags without starting generation or claiming approval. The accepted images were then prepared and shown individually. The first-turn v3 retained the requested sudden release and balancing action.
- First approach v1 was rejected for an almost static river and low quality; render/artifacts remain in `video/drafts/rejected/`. v2 strengthened the continuous-water-motion prompt and used FreeVideo Max, 20 steps, one pass, seed 11080102. The accepted approach v2 is in `video/raw/scene08-approach-v2.mp4` and `output/clips/`; package `workflows/video/scene08-approach-v2/`.
- The map-down clip completed in FreeVideo Max at 1344 x 768, 6.58 s, 24 fps, seed 11080103, and was explicitly accepted. Package: `workflows/video/scene08-map-down-v1/`.
- Wrong-turn v1 used reference mode with a separate portrait plus start/end images as additional references, seed 11080104, Max 20 steps, 6.58 s (6.5 s requested). This mode did not lock endpoints as precisely as first/last. v2 used only the accepted first/last frames and the same seed; the portrait was omitted at the user's request.
- The selected result is an edit of wrong-turn v2: hold the wrong orientation for 0.4 s, reverse the 3.5–6.583 s turning segment including its sound, giving 10.08 s total at 1344 x 768 / 24 fps. The user accepted it; original v1/v2 remain unchanged. Command/source/settings/media: `workflows/video/scene08-wrong-turn-reset-v1/`. This choice closes the v1/v2 comparison; earlier pending-comparison text is superseded.

## Iteration journal: getting to the wheel — 1 November 2026

1. The user requested a separate transition before the manual test. An initial pair and task `workflows/video/scene08-approach-wheel-v1/` (seed 11080106) were prepared, with visible water. Before rendering, an attempt failed because `source_approved_frames` is not a supported `media.json` field; the failed record is `work/scene08-approach-wheel-v1-run-attempt01-failed.json`. The manifest was corrected to the actual schema.
2. v1 rendered at 16 steps, 1344 x 768, 6.58 s, but the user rejected it: doors moved before the character touched the wheel. Its material is in `video/drafts/rejected/scene08-approach-wheel-v1/`.
3. A composite with closed doors and hands on the wheel was retained as `frames/approved/scene08-wheel-touch-doors-closed-v2.png`. The user then requested the closed door specifically from the beginning of the source. v8 copied that region to the ending. v9 moved/extended it 25 px left; v10 moved another 25 px, for 50 px total, final edge x=1120 and width 224 px, removing the glowing edge. Draft v8/v9/v10 PNGs remain in `frames/drafts/`; v10's task is `workflows/video/scene08-wheel-touch-doors-closed-v10/`. These image-compositing steps did not themselves start video.
4. The user accepted v10 and authorized video. FreeVideo approach v2 (seed 11080107, 16 steps, 1344 x 768, 24 fps, 6.58 s) opened the door by itself around 2.6 s. The source is in `video/drafts/rejected/scene08-approach-wheel-v2-source/`. An edit locked the initial closed door throughout while retaining water/character movement: `video/drafts/scene08-approach-wheel-v2-door-lock-v1.mp4`, with its task package. The user rejected that edit because near-identical pixel regions discouraged the intended motion; it moved into `video/drafts/rejected/scene08-approach-wheel-v2-door-lock-v1/`.
5. GPT Image supplied a more distinct endpoint: character shifted to the wheel with both hands. The first endpoint incorrectly showed water reaching the wheel and was rejected. The user required water to stop at the first disc. v2, `frames/drafts/scene08-wheel-touch-final-gpt-image-v2.png`, keeps all later channels dry, the wheel still and the door closed. Packages: `workflows/images/scene08-wheel-touch-final-v1/` and `scene08-wheel-touch-final-v2/`.
6. The accepted endpoint drove FreeVideo approach v3: seed 11080108, 16 steps, 1344 x 768, 24 fps, 6.58 s. The prompt explicitly keeps water visibly moving only up to A's wall; the character only approaches and lightly touches the rim. Checks at 0, 2.6, 5.2 and 6.4 s confirmed movement with the wheel/door unchanged. The user accepted it; `output/clips/scene08-approach-wheel-v3.mp4` is the accepted copy.

## Iteration journal: manual effort and solution — 1 November 2026

- The next pair started from the actual last frame of approach v3. An early ending showed release of a still wheel and a forehead wipe, with water still limited to A. Preparation packages: `workflows/video/scene08-manual-wheel-v2/` and `workflows/images/scene08-manual-wheel-end-v2/`.
- The user initially specified `frames/approved/scene08-manual-wheel-test-gpt-image-v1.png` (hands turning, door open) as the endpoint. The prompt described door leaves moving with the wheel. That FreeVideo v2 run was cancelled before a result; no completed clip exists. Its exact pair remains in `workflows/video/scene08-manual-wheel-v2/inputs/`, run record `work/scene08-manual-wheel-v2-run.json`.
- After cancellation the user selected `frames/drafts/scene08-manual-wheel-end-gpt-image-v2.png`. Manual v3 is one continuous effort/open/release/close shot, seed 11080110, 16 steps, 1344 x 768, 24 fps, 6.58 s. Water stays before A. Checked at 0, 2.6, 3.9, 5.2 and 6.4 s; explicitly accepted and copied to `output/clips/scene08-manual-wheel-v3.mp4`.
- Correct-first-turn v1 starts at the actual manual-v3 ending, returns to A and turns it a quarter-turn. Water reaches B's wall; wheel and door remain still. Seed 11080111, 16 steps, 1344 x 768, 24 fps, 6.58 s. Checked at 0, 2.6, 5.2, 6.4 s and explicitly accepted. Package: `workflows/video/scene08-correct-first-turn-v1/`.
- Correct-second-turn v1 starts at the previous actual ending and targets the accepted solved v2 image. Water crosses both discs, turns the wheel and then opens the door. Seed 11080112, same 16-step/1344 x 768/24 fps/6.58 s settings and check times. Explicitly accepted; task `workflows/video/scene08-correct-second-turn-v1/`.
- The exit pair combines that solved ending with `frames/drafts/scene08-enters-open-door-gpt-image-v1.png`. The character picks up the rolled map from dry ground and goes through while water/wheel continue and the door remains open. FreeVideo exit v1: seed 11080113, same working settings/check times. Explicitly accepted; packages `workflows/video/scene08-enter-door-v1/` and `workflows/images/scene08-enters-open-door-v1/`.
- All eight clips were accepted. Next came full-scene assembly and narration, rather than another trial or scene.

## Exact Russian speech

Drama 3 generated nine narrator lines and one character achievement in a single local workflow, prompt ID `59a436bf-e05b-4178-b81b-472c066f2239`, seeds `11080121–11080130`. The following cue windows were provisional before the later edit; use the montage record for current timing.

| # | Speaker / exact text | Original window | Duration |
|---|---|---|---:|
| 1 | Narrator: "На пути Матвея ждала каменная головоломка." | 00:01–00:05 | 3.48 s |
| 2 | Narrator: "Он положил карту и стал разбираться в каналах." | 00:07–00:11 | 2.46 s |
| 3 | Narrator: "Первая попытка оказалась ошибочной." | 00:14–00:18 | 2.37 s |
| 4 | Narrator: "Вода не доходила до колеса." | 00:24–00:28 | 1.90 s |
| 5 | Narrator: "Матвей попробовал открыть проход силой." | 00:30–00:32 | 2.55 s |
| 6 | Narrator: "Стоило отпустить колесо — дверь сразу закрылась." | 00:35–00:36 | 3.48 s |
| 7 | Narrator: "Тогда он повернул первый диск. Вода дошла до второй преграды." | 00:37–00:42 | 5.25 s |
| 8 | Narrator: "Ещё один поворот направил поток к колесу." | 00:43–00:47 | 3.20 s |
| 9 | Narrator: "Забрав карту, Матвей шагнул в открытый проход." | 00:50–00:55 | 3.11 s |
| 10 | Character: "Смекалка — есть!" | Achievement | 1.67 s |

Files: `audio/voice/drafts/`. Texts, references, individual seeds/settings: `workflows/voice/scene08-voiceover-v1/`. Initially these awaited listening; acceptance was later recorded as part of the complete scene, not inferred from generation.

## Assembly, acceptance and tasks

The v1 review edit used the eight accepted clips in the order above, retaining their original sound and adding all ten voice lines. The SVG badge "СМЕКАЛКА / ИСПЫТАНИЕ 3 ИЗ 4" appears upper-right for the last 4.5 s; its spoken line starts at 53 s. Clip order, audio timing, encodings and result hash: `workflows/montage/scene08-assembly-v1/`.

On 2 November the user accepted the complete v1, including narration and badge. Accepted clip copies were then moved from the `output/` root into `output/clips/`, leaving only the complete scene in the root. Originals and the complete edit were unchanged; README/metadata links were updated.

Completed tasks include the diagrams, round-disc states, all accepted preparation/failure frames, stiff first-turn v3, reverse edit, closed-door composites and their rejection/replacement, eight clip approvals, voice/badge assembly and accepted-output transfer. Historical unchecked items about reviewing approach v3 are superseded by its explicit later acceptance. Proposed extra gags were never automatically approved. Remaining work is review of the later full-film montage revision and its continuity/sound, not regeneration of an already accepted sequence.


## Material layout

`frames/approved/` contains selected keyframes; `frames/drafts/` alternatives. Scene-specific references are in `refs/`. Original FreeVideo clips stay in `video/raw/`; rejected attempts in `video/drafts/rejected/`. `workflows/images/`, `workflows/video/` and `workflows/voice/` keep the API workflows or generation tasks, prompts, media, seeds and settings. `audio/voice/` contains scene lines, `audio/sfx/` exact effects. Keep one current accepted complete scene in the `output/` root, accepted clip copies in `output/clips/`, and older complete edits in `work/archive/`.

Shared identity/costume references: `../../shared/refs/images/`; shared voice references: `../../shared/refs/audio/`. Empty directories do not imply that material exists. Read [the scene workflow](../../docs/SCENE-WORKFLOW.md) and [Comfy MCP guide](../../docs/COMFY-MCP-LLM.md) before new work. Paths refer to production records; raw media is retained separately from the published source.

## Additional recorded artifact locations

These supplementary records belong to the versions described above; their presence is not an approval.

- `frames/drafts/scene08-first-turntable-action-gpt-image-v1.png`
- `frames/drafts/scene08-second-turntable-thinking-gpt-image-v1.png`
- `video/raw/scene08-wrong-turn-v1.mp4`
- `frames/drafts/scene08-wheel-touch-doors-closed-v8.png`
- `frames/drafts/scene08-wheel-touch-doors-closed-v9.png`
- `frames/drafts/scene08-wheel-touch-doors-closed-v10.png`
- `work/scene08-montage-v2.mp4`
- `frames/approved/scene08-first-turntable-action-gpt-image-v3.png`
- `video/raw/scene08-wrong-turn-v2.mp4`

## Documentation maintenance

- 2026-11-02: consolidated the complete production decisions, version history, artifact references and speech directions into this English README. Russian spoken/onscreen text is retained in quotation marks. No render or approval state changed.
