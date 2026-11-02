# 11. Night-time zipline

## Current state and full-film revisions

The user confirmed acceptance of the complete scene `output/scene11-final-v2.mp4` (32.04 s). It contains selected clips 1, 2, 3 and unchanged clip 5; clip 4 had already been removed. Accepted clip copies are in `output/clips/`; original renders stay in `video/raw/`. Shared frame duplication at joins 1–2 and 2–3 was removed and sound/picture joins smoothed.

For the full film, montage v3 removed clip 5 (the separate first ride), leaving the descent followed by scene 12. File `work/scene11-montage-v3.mp4`, filter `work/scene11-montage-v3-filter.txt`. Current review revision v4, `work/scene11-montage-v4.mp4`, also removes 5.500–7.750 s (2.25 s) of waiting after packing so the character immediately turns away from the chest. Mission and descent remain. This follows full-film feedback at 2:11–2:13, 3:17–3:19 and 3:37–3:39. Source media/settings were untouched; no new generation. These later revisions have no separate recorded approval.

## Story, continuity and exact speech

Continue from scene 10's daylight gift reveal. Clip 1 keeps that lighting and ends by the chest. Clip 2 uses its actual last rendered frame and turns the camera toward the high night-time cliff. The folded grey scooter travels in a case. The character descends to the beach holding a bar beneath a suspended trolley with both hands. Preserve the single sloping cable and geography of the beach below. Night continues through the finale.

Narrator, not parrot, using Drama 3 and the scene-10 narrator reference:

> "Капитан Матвей, вам поручается новое задание — покорять дороги, открывать маршруты и не забывать о шлеме."

The requested setup originally placed the composed character near the chasm at night for this mission. The later selected plan mixes it into the descent. Earlier ice axes were explicitly replaced with the trolley handle; keep both hands overhead on the grip and the scooter in its case. A proposed greeting during the first ride was replaced by the separate starry scene 12. The earlier ride shows a foot push on a firm beach-side path, helmet fastened; it remains part of accepted scene v2 but is excluded from the latest full-film revision.

## Selected shot plan v2

| Clip | Inputs / action | Result |
|---|---|---|
| 1 | Scene-10 accepted reveal → sunset departure v5. Collect folded scooter/helmet and end beside the chest. No sunset speech. Preserve mountains, bay, camera and vegetation. | `video/raw/scene11-01-departure-v2.mp4`, seed 11110136, 6.6 s, accepted |
| 2 | Exact actual last frame of clip 1 → accepted night cliff frame 3 v5. Walk directly toward the cliffs visible behind the chest; follow and smoothly pan/turn to the high launch point. Do not use the blue-hour still. | `video/raw/scene11-02-cliff-approach-v2.mp4`, seed 11110137, 8.0 s actual / 7.3 s requested, AAC present, accepted |
| 3 | Exact actual last frame of clip 2; no separate descent frame 4. Reach overhead, hold the trolley bar with both hands and descend toward the beach. Show waves continuously advancing and retreating. No ice axes. | `video/raw/scene11-03-night-zipline-descent-v2.mp4`, seed 11110138, 10.125 s; separately mixed review `video/drafts/scene11-03-night-zipline-descent-v2-review.mp4`; accepted before full-scene acceptance |
| 4 | Omitted at user's request | No new separate clip |
| 5 | Retain existing `frames/approved/scene11-02-beach-first-ride-v1.png` and beach-ride shot | Original `scene11-05-beach-first-ride-v1`, unchanged in accepted scene v2; later omitted in full film |

Current generation packages: `workflows/video/scene11-01-departure-v2/`, `scene11-02-cliff-approach-v2/`, `scene11-03-night-zipline-descent-v2/`; selected plan `workflows/video/PLAN-v2.md`. Original plan v1 is historical, not current. Original numbering intentionally jumps from 3 to 5.

## Keyframes and geometry

Qwen Image 2.1, 28 steps, Euler. Selected copies are in `frames/approved/`, originals/drafts in `frames/drafts/`; per-image seeds, prompts, input copies, workflows and prompt IDs are in `workflows/images/scene11-keyframes-v1/` and `workflows/images/scene11-transition-v1/`.

Use `../../shared/refs/images/Matvey_story_master_matvey_00001_.png` and accepted scene-10 `../10-chest-gift/frames/approved/scene10-02-gift-reveal-v3.png` for identity/costume/landscape.

| State/version | Record and outcome |
|---|---|
| Night cliff v1 | `frames/drafts/scene11-01-night-cliff-v1.png`, seed 11110101; made before case/ice-axe choice, superseded |
| Night cliff v2 | `frames/drafts/scene11-01-night-cliff-v2.png`, seed 11110103; rejected later |
| First beach ride | `frames/drafts/scene11-02-beach-first-ride-v1.png`, seed 11110102; approved copy used later |
| Blue hour | `frames/drafts/scene11-01-blue-hour-arrival-v1.png`, seed 11110106; omitted from selected clip 2 |
| Sunset v4 | Seed 11110109, prompt ID `82b34557-40f2-4881-bb3e-8a019448a615`; dense foliage, back view/horizon after earlier wrong direct gaze, but rejected later for shifted mountains |
| Sunset v5 | `frames/drafts/scene11-00-sunset-departure-v5.png`, seed 11110134, prompt ID `e3aa9e2a-ff00-498c-b2ba-db11f8ac3b67`; derived directly from scene 10 with fixed camera/mountains/bay/beach/vegetation and sunset light; standalone assessment initially pending, subsequently used in accepted departure clip |
| Accepted frame 3 v5 | `frames/approved/scene11-01-night-cliff-v5.png`, seed 11110131, prompt ID `16668c40-ab4f-4064-8619-dc2b78106c2f`; very high cliff, beach distant below, explicitly accepted |
| Descent frame 4 v4 | Seed 11110133, prompt ID `1a41ee2c-7f6c-4b9a-a724-28524f58b9c6`; trolley above, both hands on bar, straight cable. Rejected and stored as `frames/drafts/rejected/scene11-02-zipline-descent-v4-rejected-user-feedback.png` |

The first sunset trial duplicated scooter/helmet and failed internal inspection. Sunset v2 reduced vegetation and had the character look at camera; v3 restored foliage but retained the gaze. Both were rejected and removed from approved frames into rejected drafts. v4 changed the mountains and was rejected after a later comparison with scene 10. v5 corrected that using the original composition.

The user objected to a cable running sideways without visible supports, then required a higher cliff and smaller/distant beach. Descent frame v3 had a kinked rope and was rejected. Descent v1–v4 did not yield an accepted dedicated frame; the user proposed omitting frame 4 rather than forcing it. The older rendered descent using ice axes was a separate historical video result, not approval of the rejected still.

## Speech, music and sound

Narration: `audio/voice/scene11-narrator-mission-v1.flac`, Drama 3, seed 11110111, 8.22 s, prompt ID `67def388-5d83-4c51-a0b3-415b9ea5c2b3`, established narrator from scene 10. It initially awaited listening, then was included in the accepted scene. The full text is quoted above.

FreeVideo prompts request an original instrumental closing-adventure theme and island ambience: daylight birds/leaves becoming evening insects, wind and surf. Historical descent v1 includes rope/ice-axe Foley; selected v2 replaces that with trolley sounds. The beach ride adds scooter wheels and a foot push. Inspect actual sound rather than inferring quality from an AAC track's presence. The review of selected clip 3 adds Drama 3 over FreeVideo sound while preserving the raw original.

## Historical five-clip render v1

Initial agent preflight returned `no_token`, so no video/sound was generated at that stage. After the user's direct instruction, Drama 3 was unloaded from ComfyUI, then the project FreeVideo CLI rendered the five shots sequentially. Original plan: `workflows/video/PLAN-v1.md`.

| Historical task | Seed | Duration |
|---|---:|---:|
| `scene11-01-sunset-transition-v1` | 11110120 | 6.583 s |
| `scene11-02-blue-hour-transition-v1` | 11110121 | 7.300 s |
| `scene11-03-night-briefing-v1` | 11110122 | 8.708 s |
| `scene11-04-zipline-descent-v1` | 11110123 | 7.300 s |
| `scene11-05-beach-first-ride-v1` | 11110124 | 7.300 s |

Each raw H.264/AAC clip remains under `video/raw/`, with its prompt/media/parameters task. The draft assembly `video/drafts/scene11-review-v1.mp4` was 37.285 s (rounded 37.29 s), with re-encoded H.264/AAC and corrected monotonic audio timestamps. It is historical, not accepted/current; the archived full copy is `work/archive/scene11-review-v1.mp4`.

Contact sheets: `work/scene11-review-v1-contact.jpg` and the individual `work/scene11-01-sunset-transition-v1-contact.jpg` through `work/scene11-05-beach-first-ride-v1-contact.jpg`. Each clip/container was inspected and sheets shown. After v1, the user revised the keyframes/shot structure rather than accepting the obsolete ice-axe/blue-hour version.

## Journal and outstanding tasks

- **1 November 2026:** scene material organized with its existing status.
- **2 November, early planning:** after cancelling the scroll/port detour, considered treasure-to-beach descent and gift staging. An earlier scene-16→12 renumbering preceded the final three-scene ending. The user restored the full gift/greeting text, assigned the joke to the pirate parrot, and reserved introduction/mission/greeting for the narrator. The shared 7–9-shot / 65–80 s ending target was provisional until speech timing.
- **2 November, image work:** drafted linked night start/descent/ride states; initially selected ice axes and scooter case. Added day/sunset/blue-hour/night continuity after feedback. Showing/accepting a structure did not imply acceptance of later renders.
- **2 November, v1 generation:** initial preflight failed; after explicit direction unloaded Drama and generated the five clips/music/nature ambience. The 37.285 s draft awaited review and was not moved into accepted output.
- **2 November, revisions:** corrected sunset gaze/vegetation, cable supports/height and trolley grip; rejected the kinked/unsuccessful descent still and omitted it. Rejected changed mountain geography and created sunset v5 from scene 10. No automatic rerenders were started merely by making replacement images.
- **2 November, selected clips:** user specified departure without sunset speech, exact-last-frame continuation to cliff, combined mission/descent, no clip 4 and unchanged clip 5. Departure v2 was rendered/accepted; its actual ending seeded cliff-approach v2, also accepted. Its ending seeded descent v2, with moving surf and separate Drama mix, then accepted. Completed v2 was explicitly confirmed accepted as a whole.
- **2 November, full-film edits:** removed clip 5 for v3, then removed 2.25 s post-packing wait for v4. Those later review revisions retain original accepted media and require their own assessment.

Remaining work: review montage v4 in the full-film context, especially night geography, sound, wave motion and the transition to scene 12. Do not restore the obsolete ride/ice-axe/scroll plan without a new instruction.


## Material layout

`frames/approved/` contains selected keyframes; `frames/drafts/` alternatives. Scene-specific references are in `refs/`. Original FreeVideo clips stay in `video/raw/`; rejected attempts in `video/drafts/rejected/`. `workflows/images/`, `workflows/video/` and `workflows/voice/` keep the API workflows or generation tasks, prompts, media, seeds and settings. `audio/voice/` contains scene lines, `audio/sfx/` exact effects. Keep one current accepted complete scene in the `output/` root, accepted clip copies in `output/clips/`, and older complete edits in `work/archive/`.

Shared identity/costume references: `../../shared/refs/images/`; shared voice references: `../../shared/refs/audio/`. Empty directories do not imply that material exists. Read [the scene workflow](../../docs/SCENE-WORKFLOW.md) and [Comfy MCP guide](../../docs/COMFY-MCP-LLM.md) before new work. Paths refer to production records; raw media is retained separately from the published source.

## Additional recorded artifact locations

These supplementary records belong to the versions described above; their presence is not an approval.

- `work/scene11-01-departure-v2-run.json`
- `media.json`

## Documentation maintenance

- 2026-11-02: consolidated the complete production decisions, version history, artifact references and speech directions into this English README. Russian spoken/onscreen text is retained in quotation marks. No render or approval state changed.
