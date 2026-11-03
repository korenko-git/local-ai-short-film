# 09. Speed: closing gate

## Current state

The user explicitly accepted the complete v3 scene on 2 November 2026. `output/scene09-full-v3.mp4` is 28.83 s and matches the review edit by SHA-256. Five used segments are in `output/clips/`. There are no mandatory tasks outstanding for this accepted version. Earlier pending/rejected notes below are version history, not the current state.

## Agreed story and continuity

1. Exit scene 8's stone passage into a straight jungle corridor. Establish the whole distance, with a closed wooden gate far away and a bell/large hourglass near the start.
2. Ring the bell: the glass chambers flip and the gate opens. The character leans toward the sand, briefly admires the mechanism, then realizes that time is already running.
3. Put the map behind the waistband at the right hip, then sprint along the obstacle-free route. Alternate the run, decreasing sand and slowly closing gate.
4. Accelerate on the last metres and pass through a still-wide-enough opening. The gate shuts behind, with a brief wooden impact and pause.
5. Catch breath, look back and smile. Character line: "Скорость — есть!". Badge: "СКОРОСТЬ — ИСПЫТАНИЕ 4 ИЗ 4".
6. Retrieve the map from the same right-hand storage location and check the route to the treasure. The user cancelled map stamps: simply reach the indicated place. This supersedes early TODOs about a fourth stamp.

Maintain face, glasses, costume, map hand/storage and the scene-8 exit geography. Do not treat a gate-approach image as a completed threshold crossing. Review/show connected frames before FreeVideo unless the user explicitly authorizes an alternative, as happened for this scene's final shots.

## Keyframe development — 1 November 2026

All Qwen Image 2.1 packages below retain full prompts, media, seeds, parameters and prompt IDs. Baseline: 28 steps, Euler/simple, CFG 1. References include `refs/scene08-exit-continuity.png`, copied from scene 8's door-exit keyframe, and the shared character master.

| Version | Images / seeds | Assessment and result |
|---|---|---|
| Initial v1 | `scene09-01-establish-v1.png`, `scene09-02-timer-v1.png`; 11090101–11090102; `workflows/images/scene09-keyframes-v1/` | Gate taller than intended, apparent distance shorter than 20 m, hourglass axis unclear. Map changed from right hand to left; settle the hand or show the transfer. The first pair was shown but not accepted. |
| Revised v2/v4 | `scene09-01-establish-v2.png`, `scene09-02-timer-v4.png`; 11090111 and 11090114; `workflows/images/scene09-keyframes-v2/` | Longer straight road, low slatted gate, brass side pivots, sand mostly in the upper chamber after starting. Hand continuity improved, but no bell contact/clear lean; stone exit became a tree. Rejected by user after review. |
| Intermediate failures | 11090112 and 11090113 | Duplicate child in one image; closed gate and sand already below in the other. Rejected by agent and retained. |
| Accepted v3/v6 | `scene09-01-establish-v3.png`, `scene09-02-timer-v6.png`; 11090121 and 11090123; `workflows/images/scene09-keyframes-v3/` | Solid gate in a cross-wall, continuous high side walls so it cannot be bypassed, restored stone exit at left, stable opening/masonry/camera. Initial sand below, then above after flipping. User accepted this pair. |
| Intermediate v5 | seed 11090122, `frames/drafts/650998be_000.png` | Extra hand and too much sand; rejected by agent. |

The user specifically objected to gates jumping between frames, looking like a pen that could be walked around, and more sand appearing after the timer started. v3/v6 addressed those points. The hourglass remained very large and the route looked shorter than the intended 25 m. Sand quantities looked broadly comparable but exact volume conservation was not guaranteed. Bell contact and the curious lean were deliberately handled in later action frames, not claimed from the unchanged initial pose.

The accepted pair was copied to `frames/approved/scene09-01-establish-v3.png` and `scene09-02-timer-v6.png`. The proposed right-waistband map storage was subsequently accepted explicitly.

### Action and running keyframes

- `scene09-03-bell-v1.png`: left hand touching the bell, looking at the timer, map in right hand, gate open and sand moving. `scene09-04-map-stow-v1.png`: storing the map at the right hip. Both derive from accepted mechanism v6; task `workflows/images/scene09-actions-v1/`, seeds 11090131–11090132. One character/two hands, face/costume and architecture checked; user accepted both. Copies are in `frames/approved/`.
- `scene09-05-run-v1.png`: run away from camera with free hands and map behind right waistband. `scene09-06-gate-approach-v1.png`: nearer the partly closing gate, most sand below. Task `workflows/images/scene09-run-v1/`, seeds 11090141–11090142. First derives from map-stow, second from run.
- Sand in the run image remained closer to its starting state instead of half depleted. The user accepted it as-is and explicitly cancelled that correction. The second image stops before the threshold; the map appears nearer the right rear waistband, which required continuity checks. Six keyframes were accepted, without implying approval of an unmade crossing/ending.
- The user directly authorized video without additional threshold/finale keyframes. No video was launched during the earlier image-review stages.

## Initial FreeVideo clips and preview

Tasks `scene09-start-v1`, `scene09-map-stow-v1`, `scene09-sprint-v1`, `scene09-pass-v1` each contain prompt, media, inputs and parameters under `workflows/video/`. Initial requests: 1344 x 768, 6.5 s, 16 steps, no two-pass. First three use first/last; passage uses first only under explicit authorization.

| Clip | Raw file | Seed | Observed action |
|---|---|---:|---|
| Start | `video/raw/scene09-start-v1.mp4` | 11090151 | Bell contact, glass chambers flip, then gate opens |
| Map | `video/raw/scene09-map-stow-v1.mp4` | 11090152 | Look toward gate and store map behind right waistband |
| Sprint | `video/raw/scene09-sprint-v1.mp4` | 11090153 | Continuous run toward gate, map retained |
| Passage | `video/raw/scene09-pass-v1.mp4` | 11090154 | Pass through, disappear beyond the leaves, then gate closes |

Each completed clip is 1344 x 768, 24 fps, 158 frames, about 6.58 s. Run records are `work/scene09-...-v1-run.json`; engine artifacts remain beside raw media. Start completed on 1 November; subsequent shots completed sequentially on 2 November. Beginning a run was never recorded as a finished/accepted clip.

`work/scene09-clips-preview-v1.mp4` (26.36 s) concatenates the four originals without picture re-encoding, retaining original sound; it had no Drama 3 or badge and was not the final output. Concat list and SHA-256 records: `workflows/montage/scene09-clips-preview-v1/`. Contact sheets are `work/start-v1-contact.jpg`, `map-stow-v1-contact.jpg`, `sprint-v1-contact.jpg`, `pass-v1-contact.jpg`.

Half-second checks of passage show the gate reached around 2–3 s, then the character hidden by a leaf and closure around 4–5 s; no far-side shot existed yet. The camera pulls back slightly. Sand in the sprint sometimes thickens visibly. These checks used decoded frames/metadata, not a guarantee of subjective sound quality.

## Far-side finale and superseded full edit v2 — 2 November 2026

The user asked to continue. `video/raw/scene09-finale-v1.mp4` uses reference mode, seed 11090201, 16 steps, 1344 x 768, 24 fps, 6.58 s; task `workflows/video/scene09-finale-v1/`. From beyond the gate, the character runs toward camera, looks back at the closed leaves, smiles, retrieves the map from the right and unfolds it. No stamps. `work/finale-v1-contact.jpg` confirms the single character/costume and unfolding map; the retrieval is partly occluded by hand/body. Its start repeats passage action, accounted for in editing. No exact lip-sync to the separate voice was claimed.

The user cancelled stamps and requested these narrator lines with the scene-8 reference:

| Exact Russian line | File in `audio/voice/drafts/` | Seed |
|---|---|---:|
| "Матвей, быстрее!" | `scene09-narrator-faster-v1.flac` | 11090212 |
| "Твоё любопытство сыграет с тобой злую шутку!" | `scene09-narrator-curiosity-v1.flac` | 11090213 |
| Character: "Скорость — есть!" | `scene09-speed-achievement-v1.flac` | 11090211 |

Drama 3 task: `workflows/voice/scene09-achievement-v1/`; prompt ID `4b41bcca-11e2-4d2b-b611-b6566313d78a`. These first awaited listening; later full-scene acceptance settled their status.

Superseded `work/scene09-full-preview-v2.mp4` is 28.87 s, five clips, passage trimmed to 2.5 s before the reverse view. Original cue positions: warning 4.5 s, faster 12 s, achievement speech 25.5 s, badge "СКОРОСТЬ / ИСПЫТАНИЕ 4 ИЗ 4" from 25.3 s. H.264 CRF18/AAC192k, original background gain 0.65 and separately mixed voices. Manifest, filter, timing/hashes: `workflows/montage/scene09-full-preview-v2/`; font/text check `work/preview-v2-badge-check.png`. v1 was retained. At that stage the scene remained pending, and later scenes were not launched.

## Dynamic camera insert: versions 1–3

The user supplied a 16.07 s anime motion reference and requested expressive running, camera turns, blurred background and golden sparks beneath the shoes. Local source: `refs/speed-camera/user-speed-reference.mp4`; contact sheet `refs/speed-camera/contact.jpg`. Preserve the photorealistic character/costume and map behind the right waistband; borrow motion rather than anime appearance.

- **v1:** seed 11090221, 1344 x 768, 6.5 s requested, 16 steps/no two-pass; character master plus accepted running frame, silent motion guide from source 9.5–16.0 s. Planned low shoes → front three-quarter face → side track, rapid background and contact sparks. Interrupted with Ctrl+C before a result when the user refined the direction; do not count as completed.
- **Revision:** after opening the gate, move the camera from behind around to the side/profile, then use the full reference's effects/angles. At the beginning, add Drama 3 "Стой!" with upper/lower speed lines, corresponding to the contact sheet's first four frames.
- **v2:** seed 11090222, full 0–16.07 s video guide, 6.5 s output requested. Rejected by agent after completion: it transferred the anime/source character instead of the intended character. Kept in `video/drafts/rejected/scene09-speed-camera-v2/`; sheet `work/speed-camera-v2-contact.jpg`.
- **v3:** seed 11090224, only character/corridor photo references; the full motion reference informed the written direction but was not supplied directly as a video guide. Output `video/raw/scene09-speed-camera-v3.mp4`, 1344 x 768, 24 fps, 6.58 s, 16 steps/no two-pass; package `workflows/video/scene09-speed-camera-v3/`.

At 0.5 s intervals, v3 shows surprised face/speed streaks, turn, rear tracking, side profile, blurred walls and shoe sparks around 4–5 s. Identity, glasses and costume remain. Large gate leaves appear at the side near the ending, requiring geography review at the join; the very low sole-level view is weaker than requested. Sheet: `work/speed-camera-v3-contact.jpg`. Streaks/sparks came from FreeVideo, not an added graphic layer.

Drama 3 "Стой!": `audio/voice/drafts/scene09-stop-v1.flac`, seed 11090223, narrator `synthetic-voice-a`, prompt ID `ba7bbca0-20b3-401a-ae0d-0313a0062e8c`, task `workflows/voice/scene09-stop-v1/`. It was prepared while video ran but generated after the video stage to avoid GPU contention. `video/drafts/scene09-speed-camera-v3-with-stop.mp4` (6.59 s) copies picture, retains background at 0.65 and adds the 0.60 s cue at 0.05 s. Edit/hash record: `workflows/montage/scene09-speed-camera-v3/`. v3 was first shown pending review, not automatically accepted from technical completion.

## Dynamic insert v4: new cue, then v5: restored music

The user accepted v3's picture but requested "Бежи!" instead of "Стой!" and reported nonsense FreeVideo voices near its end. Keep that exact approved Russian wording, rather than silently correcting the script.

Drama 3 "Бежи!": `audio/voice/drafts/scene09-run-cue-v1.flac`, seed 11090225, narrator `synthetic-voice-a`, prompt ID `d28e393f-5951-4381-b168-4b2f19bb1d83`, task `workflows/voice/scene09-run-cue-v1/`.

v4 `video/drafts/scene09-speed-camera-v4-run-clean.mp4` (6.58 s) copied the accepted picture and explicitly mapped only the new speech, at 0.05 s. All original FreeVideo audio was removed, including the unwanted voices but also music, footsteps, wind and sparks. The rest was silent; this was an intentional intermediate result, with no added SFX. Its filter/settings/SHA-256 are in `workflows/montage/scene09-speed-camera-v4/`. Original and stop-cue versions were retained, no video regenerated/global model settings changed.

The user requested music back and removal of only the voices. Because the soundtrack was almost mono (channel correlation 0.9971), simple centre cancellation would also remove music. Existing torchaudio `HDEMUCS_HIGH_MUSDB_PLUS` ran on CPU with two threads. 319 MB weights were downloaded into `work/audio-model-cache/torchaudio/models/`; no extra package installation was required and the process/model did not remain in memory afterward.

Source audio: `work/speed-source.wav`. The separated outputs are `audio/sfx/scene09-speed-instrumental-v1.wav` (drums+bass+other) and `audio/sfx/scene09-speed-vocals-removed-v1.wav` (isolated vocals). Script/settings: `workflows/audio/scene09-vocal-removal-v1/`.

v5 `video/drafts/scene09-speed-camera-v5-music-no-vocals.mp4` copies picture, uses separated background at 0.9 and Drama 3 "Бежи!" at 0.05 s, duration 6.58 s. Record: `workflows/montage/scene09-speed-camera-v5/`. Separation can leave faint speech or alter effects; its subjective quality required listening. v3/v4 were preserved. The user accepted v5 and requested the complete assembly; the accepted insert is `video/raw/scene09-speed-camera-approved-v5.mp4`.

During this audio work, the verified task-owned portable ComfyUI process still held 19,004,411,904 bytes of working set after model unloading. It was stopped only after executable/start-time verification against `work/comfy-20261102-091030-process.json`; unrelated applications were not stopped. The historical record reports 51.96 GiB free RAM afterward. Check host RAM as well as VRAM after speech jobs; do not reuse a historical PID as authority to terminate a current process.

## Accepted full scene v3

`work/scene09-full-preview-v3.mp4` is 28.83 s, 1344 x 768, 24 fps, H.264 CRF18/AAC192k. Order: bell/timer → map stow → dynamic running with cue/streaks/sparks/restored music → 2.5 s passage → far-side finale/map. The new run replaces the static sprint; it is not a second repeated run.

Warning stays at 4.5 s; "Матвей, быстрее!" moves to 10.6 s to avoid the insert's "Бежи!" at 13.22 s. "Скорость — есть!" starts at 25.5 s; badge at 25.3 s. No map stamps. The cleaned insert mix is not attenuated again; other backgrounds use 0.65. No FreeVideo/ComfyUI generation or additional resident model was needed for this edit.

Inputs, filter, cue times, settings and SHA-256: `workflows/montage/scene09-full-preview-v3/`. Accepted segment copies:

- `output/clips/scene09-start-v1.mp4`
- `output/clips/scene09-map-stow-v1.mp4`
- `output/clips/scene09-speed-camera-approved-v5.mp4`
- `output/clips/scene09-pass-v1-cut.mp4`
- `output/clips/scene09-finale-v1.mp4`

Checks: `work/full-v3-contact.jpg`, `work/full-v3-speed-cut-check.jpg`, `work/full-v3-pass-cut-check.jpg`, duration/codecs and picture/audio presence. Side-running to the gate wide shot is a direct cut, not a continuous camera move. The user then accepted the entire v3; it was copied unchanged to `output/scene09-full-v3.mp4` with matching SHA-256. Output organization left only that complete file in the root and five segments in `output/clips/`. Original media and earlier edits were retained. Later scenes were not started as a side effect.


## Material layout

`frames/approved/` contains selected keyframes; `frames/drafts/` alternatives. Scene-specific references are in `refs/`. Original FreeVideo clips stay in `video/raw/`; rejected attempts in `video/drafts/rejected/`. `workflows/images/`, `workflows/video/` and `workflows/voice/` keep the API workflows or generation tasks, prompts, media, seeds and settings. `audio/voice/` contains scene lines, `audio/sfx/` exact effects. Keep one current accepted complete scene in the `output/` root, accepted clip copies in `output/clips/`, and older complete edits in `work/archive/`.

Shared identity/costume references: `../../shared/refs/images/`; shared voice references: `../../shared/refs/audio/`. Empty directories do not imply that material exists. Read [the scene workflow](../../docs/SCENE-WORKFLOW.md) and [Comfy MCP guide](../../docs/COMFY-MCP-LLM.md) before new work. Paths refer to production records; raw media is retained separately from the published source.

## Documentation maintenance

- 2026-11-03: article artifact review covers the failed hourglass flip at 02:34–02:36, unintelligible speech at 02:58–03:01 and altered/viewer-facing map at 03:01–03:03. Checked the start-v1 prompt/media/parameters: explicit horizontal-pivot flip, fixed stand, establish-v3 first and bell-v1 last (not timer-v6), 6.5 s requested. Missing intermediate orientation and concurrent actions are hypotheses, not proven causes. Existing footage and approvals are unchanged; excerpts retain final-film sound.
- 2026-11-02: added the accepted v5 camera insert and `refs/speed-camera/contact.jpg` to all three article editions. The accompanying account follows the chat history: rejected style transfer, character photo references with written staging, the revised "Бежи!" cue, and vocal separation to retain music. Original media and approval states are unchanged.
- 2026-11-02: consolidated the complete production decisions, version history, artifact references and speech directions into this English README. Russian spoken/onscreen text is retained in quotation marks. No render or approval state changed.
