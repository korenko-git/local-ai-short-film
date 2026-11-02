# 12. Birthday under the stars

## Current state

Scene v1 is explicitly accepted: `output/scene12-final-v1.mp4`, 17.208 s original result. Accepted clip copy: `output/clips/scene12-clip1-v1.mp4`; original remains `video/raw/scene12-birthday-finale-v1.mp4`. The accepted review copy is `video/drafts/scene12-birthday-finale-v1-review.mp4`.

## Staging and exact Russian greeting

At night, the character stands by the bay with the grey scooter and fastened helmet. Preserve scene 11's beach geography after the treasure-to-beach zipline. The entire greeting belongs to the narrator, using the same voice as scene 10's introduction and scene 11's mission; the parrot does not speak it. Do not shorten the restored text or add a duplicate character line:

> "Дорогой Матвей, сегодня тебе девять лет. Пусть впереди ждут великие открытия, невероятные приключения и верные друзья. Пусть смелости хватит на любые испытания, а самая большая мечта обязательно сбудется. С днём рождения, капитан! Полный вперёд"

Stars gradually light up. The direction requires a shooting star on "С днём рождения", linked to the finished voice, and the final image ends on "Полный вперёд". A wave of the character's hand is a visual action, not another spoken line. The production check describes the rendered star as appearing in the later greeting near the birthday words; do not invent frame-exact synchronization beyond that observation.

The accepted edit is a single continuous move from character/scooter toward a wide bay/starry-sky view. The full greeting is retained. Voice starts at the beginning; FreeVideo background is reduced in the mix.

## Voice and video settings

| Material | Technical record |
|---|---|
| Narrator | `audio/voice/scene12-narrator-birthday-v1.flac`; Drama 3, seed 12120111, about 17.00 s; shared `synthetic-voice-a.mp3` |
| Voice package | `workflows/voice/scene12-narrator-birthday-v1/`; prompt ID `66adb998-99b1-4527-b55e-36ab28135ac0`; text/prompt/media/workflow/parameters retained |
| FreeVideo | 17.0 s requested, 17.208 s actual, 1344 x 768, 24 fps, H.264 + AAC, seed 12120121, 16 steps, single-pass |
| Video package | `workflows/video/scene12-birthday-finale-v1/`; prompts/media/inputs/settings/run record/mix command; additional `work/scene12-birthday-finale-v1-run.json` |

The user accepted the review with "принял"; the used keyframes and speech track are accepted as part of that scene. Original video was not moved out of raw storage.

## Connected Qwen keyframes

Use accepted `../11-zipline/frames/approved/scene11-02-beach-first-ride-v1.png` and shared `../../shared/refs/images/Matvey_story_master_matvey_00001_.png` for continuity. Qwen Image 2.1: 1024, 28 steps, Euler, CFG 1. Inputs, workflow JSON, prompts, settings and IDs are under `workflows/images/scene12-keyframes-v1/`.

| Accepted frame | Description | Seed / prompt ID |
|---|---|---|
| `frames/approved/scene12-01-matvey-looks-at-stars-v1.png` | Slowed near the water, looking up | 12120101 / `29d432d7-75aa-4ca6-b638-5d930f70e821` |
| `frames/approved/scene12-02-birthday-final-wide-v1.png` | Wide ending, hand wave beside scooter, stars and shooting star | 12120102 / `0c76d2bd-b990-4fce-ad92-3af3d14862a5` |

Draft originals remain in `frames/drafts/`. Image workflows passed `validate_workflow` with no errors/warnings; image, speech and video generations completed.

## Production journal

- **1 November 2026:** material organized with its existing plan status.
- **2 November, planning:** linked the final bay to the proposed treasure-to-beach descent. Earlier scene 17→13 renumbering preceded the final twelve-scene structure. The user restored the complete gift/greeting text and reserved the parrot for the chest joke. Mission occurs at the night zipline; the whole greeting belongs here. The early ice-axe idea was later replaced in scene 11.
- **2 November, structure:** approved ending reduced from four scenes to three: chest/gift, night zipline, greeting under stars. Arrival/reveal merged; initial total target 7–9 shots / 65–80 s awaited voice timing. Approval of structure did not approve unmade frames or clips.
- **2 November, frames:** prepared two linked Qwen drafts as a precise night continuation of the accepted scene-11 beach; they were shown for assessment before video.
- **2 November, voice:** created the full 17.00 s Drama 3 greeting with the established narrator; it initially awaited listening and no video had yet run.
- **2 November, video:** after frames were shown and explicit authorization received, rendered FreeVideo v1 and mixed its review with Drama 3, retaining the source. The review initially awaited acceptance.
- **2 November, acceptance:** explicit acceptance completed frame/voice/video review. Saved the full v1 and its clip copy in the prescribed output locations. Identity, costume, props and action continuity were checked.

All originally listed production tasks for accepted v1 are completed. Keep the nighttime lighting and complete script intact when considering a later edit; no unrequested extra dialogue or following scene should be generated.


## Material layout

`frames/approved/` contains selected keyframes; `frames/drafts/` alternatives. Scene-specific references are in `refs/`. Original FreeVideo clips stay in `video/raw/`; rejected attempts in `video/drafts/rejected/`. `workflows/images/`, `workflows/video/` and `workflows/voice/` keep the API workflows or generation tasks, prompts, media, seeds and settings. `audio/voice/` contains scene lines, `audio/sfx/` exact effects. Keep one current accepted complete scene in the `output/` root, accepted clip copies in `output/clips/`, and older complete edits in `work/archive/`.

Shared identity/costume references: `../../shared/refs/images/`; shared voice references: `../../shared/refs/audio/`. Empty directories do not imply that material exists. Read [the scene workflow](../../docs/SCENE-WORKFLOW.md) and [Comfy MCP guide](../../docs/COMFY-MCP-LLM.md) before new work. Paths refer to production records; raw media is retained separately from the published source.

## Documentation maintenance

- 2026-11-02: consolidated the complete production decisions, version history, artifact references and speech directions into this English README. Russian spoken/onscreen text is retained in quotation marks. No render or approval state changed.
