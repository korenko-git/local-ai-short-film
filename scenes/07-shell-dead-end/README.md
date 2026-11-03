# 07. Curiosity: shell and dead end

## Current state and full-film revision

The complete scene `output/scene-07-curiosity-final-v1.mp4` (31.84 s) was accepted. The later `work/scene07-montage-v2.mp4`, used in full-film v2/v3, is a review revision and has no separately recorded approval. Its filter is `work/scene07-montage-v2-filter.txt`.

At joins between clips 3–6, six frames were removed from each side of the common pose. The earlier head trim of the last clip was retained and extended by six frames. Narration and achievement timing follow the new edit. Source footage, voices, prompts, seeds and generation settings were preserved; no regeneration was required.

## Story and shot sequence

1. Continue from the bridge along the island trail.
2. Show the empty dead end, sign and shell from the character's viewpoint. The narrator explains that the way is blocked and asks what to do.
3. The character enters, scratches his head, notices the blinking shell and says "О!". This line is already present in the video.
4. He approaches and physically turns the arrow board.
5. The arrow points into the former dead end; the vines part simultaneously. Preserve the visible cause and effect.
6. He walks away into the passage, seen from behind, carrying the map. He does not hold the branches apart.
7. The achievement appears during the last 4.5 s: "ЛЮБОЗНАТЕЛЬНОСТЬ — ИСПЫТАНИЕ 2 ИЗ 4". After it appears, the character says "Любознательность — есть!".

## Accepted edit and audio

- Accepted complete scene: `output/scene-07-curiosity-final-v1.mp4`, copied from `work/scene07-full-preview-v6.mp4`; SHA-256 matched.
- Edit record: `work/scene07-full-preview-v6.json`.
- Previous v4 picture was copied bit-for-bit into v6; the original clips and updated badge did not change. Only the audio was revised.
- Clip 6 has a 0.7 s head trim. Narration starts at 11.758 s; the achievement line starts at 27.9 s.
- Narration: `audio/voice/scene07-narrator-deadend.flac`.
- Character achievement: `audio/voice/scene07-achievement-curiosity-v1.flac`, Drama 3, seed `11070331`, established character reference.
- Voice task packages: `workflows/voice/scene07-dialogue/` and `workflows/voice/scene07-achievement-curiosity-v1/`.
- The separate generated "О!" track was removed because that line was already in the video.
- `audio/sfx/scene07-curiosity-achievement.wav` is a superseded procedural chime, not part of the accepted edit. In v5 it lasted 2.2 s and entered at 27.9 s; v6 replaced it with speech.
- Voice-only preview: `work/scene07-achievement-line-preview-v1.wav`. Badge check: `work/scene07-full-preview-v5-last.png`.

## Clips and keyframes

Article note, 3 November 2026: the filmmaker supplied a rejected duplicate-character image illustrating an appearance reference inserted into the edited scene. It accompanies the bridge third-hand discussion about overreliance on agent checks. This scene's `workflows/images/scene07-linked-keyframes-v1/run-arrival.json` also records `rejected_duplicate_character`; no exact run identity is inferred for the supplied image. Production media and approval states are unchanged.

Article note, 3 November 2026: added the filmmaker-supplied review contact sheet for `scene07-curiosity-v2-raw.mp4`, with seven frames from 6.583333 s using `fps=1,scale=448:256,tile=4x2`. It illustrates Luna's post-generation inspection in the editing section. No footage or approval state changed.

Originals remain in `video/raw/`; copies with the same filenames are in `output/clips/`:

| Order | Filename | Action |
|---|---|---|
| 1 | `scene07-bridge-arrival-v4.mp4` | Arrival from the bridge |
| 2 | `scene07-deadend-pov-v1.mp4` | Dead end from the character's viewpoint |
| 3 | `scene07-enter-scratch-v7.mp4` | Entry and head scratch |
| 4 | `scene07-oh-approach-v1.mp4` | Notice the shell, then approach |
| 5 | `scene07-sign-turn-v1.mp4` | Turn the sign |
| 6 | `scene07-enter-passage-v1.mp4` | Leave through the passage |

Prompts, input media, seeds and parameters are in the corresponding `workflows/video/scene07-*/` packages. The ordered Qwen Image 2.1 draft sequence was: `frames/drafts/1c511a7d_000.png` (arrival), `7b9b8712_000.png` (frame 1.5, same dead end without the character), `scene07-deadend-start.png` (blocked path), `f37c37c5_000.png` (shell/reaction), `ea636fe5_000.png` (approach), `d2ba2425_000.png` (turn), `9b29bb27_000.png` (open passage), `72088fc7_000.png` (exit). The draft-frame list was not independently approved simply by being listed; the complete edit later received explicit acceptance.

Shared badge design: `../../shared/graphics/trial-achievement-template.svg`; scene render: `work/achievement-2-of-4.svg` and `work/achievement-2-of-4.png`.

## Production journal

- **1 November 2026:** v3 was a review edit with the old label "ИСПЫТАНИЕ 2 ИЗ 8". A shared SVG template was created; scenes 6 and 7 were updated to "ИСПЫТАНИЕ 1 ИЗ 4" and "ИСПЫТАНИЕ 2 ИЗ 4". v4 retained earlier v3 versions.
- **1 November:** the requested short achievement chime produced v5 with unchanged v4 picture and re-encoded audio. The user then requested spoken "Любознательность — есть!" instead. Drama 3 generated the line; v6 replaced the chime at 27.9 s while preserving the video stream/SHA-256.
- **1 November:** the user accepted the edit and authorized its transfer to `output/`. The source and accepted copy hashes matched; original clips remained unchanged.
- **1 November, resource management:** with an empty queue, ComfyUI models/cache were unloaded and the verified idle portable process was stopped. Recorded free RAM increased from 8.1 to 51.0 GB; free VRAM before stopping increased from 7.7 to 15.6 GB. Use the documented portable launcher before future generation, and verify the actual process rather than reusing a historical PID.
- **2 November:** organized the accepted output as one complete scene plus six clip copies in `output/clips/`; originals stayed in `video/raw/`.
- **2 November:** created the later montage revision described above; it awaits review.

## Remaining work

Review the full-film montage revision for identity, costume, map continuity, timing, sound and joins. The original checklist's frame-preparation, voice-generation, v6 assembly and accepted-output transfer tasks are completed; its old pending-review checkboxes predate the recorded acceptance and must not undo it.


## Material layout

`frames/approved/` contains selected keyframes; `frames/drafts/` alternatives. Scene-specific references are in `refs/`. Original FreeVideo clips stay in `video/raw/`; rejected attempts in `video/drafts/rejected/`. `workflows/images/`, `workflows/video/` and `workflows/voice/` keep the API workflows or generation tasks, prompts, media, seeds and settings. `audio/voice/` contains scene lines, `audio/sfx/` exact effects. Keep one current accepted complete scene in the `output/` root, accepted clip copies in `output/clips/`, and older complete edits in `work/archive/`.

Shared identity/costume references: `../../shared/refs/images/`; shared voice references: `../../shared/refs/audio/`. Empty directories do not imply that material exists. Read [the scene workflow](../../docs/SCENE-WORKFLOW.md) and [Comfy MCP guide](../../docs/COMFY-MCP-LLM.md) before new work. Paths refer to production records; raw media is retained separately from the published source.

## Additional recorded artifact locations

These supplementary records belong to the versions described above; their presence is not an approval.

- `work/scene07-full-preview-v4.mp4`
- `work/scene07-full-preview-v5.mp4`

## Documentation maintenance

- 2026-11-02: consolidated the complete production decisions, version history, artifact references and speech directions into this English README. Russian spoken/onscreen text is retained in quotation marks. No render or approval state changed.
