# Scene production and handoff guide

This model-independent guide replaces the former scene-7 handoff addressed to a particular agent. It applies to any scene. The current scene README and latest user instruction take precedence over historical snapshots.

## Establish the actual state

Read `AGENTS.md`, `scenes/README.md` and the scene README. Identify the accepted edit, pending revisions, rejected material and exact next task. A rejected whole clip may contain a useful transition, but that does not make the clip accepted. Never automatically restart an interrupted render mentioned in an old handoff.

## Make the action understandable

Break the action into problem, observation, reaction, physical action and visible result. A single overloaded interpolation can skip the important movement. Show a blocked path from the character's point of view before the sign turns; show a disconnected water channel before water reaches the wheel.

Define the camera movement for each shot: follow, orbit, POV turn, close-up or reveal. Preserve screen direction, attachments and geography across angles. A bridge orbit must reveal height while keeping its ropes plausible.

## Build connected keyframes

Use Qwen Image 2.1 with established scene and character references. Derive later states from the same base rather than reinventing the location. Preserve people, costume, props, light and camera where continuity requires it. Show who moves a lid, sign or wheel. Track where a map is placed before the character needs both hands.

Inspect identity, hands, extra people, geometry, mechanisms, closed/open states and movement direction. Save alternatives in `frames/drafts/` and API workflows/parameters in `workflows/images/`. Show the ordered frames to the user and wait for the response before video.

## Generate manageable shots

Use FreeVideo only for new video. Store `prompt.txt`, `media.json`, inputs, seed, settings and run status in `workflows/video/TASK/`. Paths in `media.json` are relative to it. Use the actual last frame of a previous clip when a continuous transition needs it; a rendered ending may differ from its reference.

Describe relevant continuous movement explicitly: flowing water, waves, wind in hair, swaying ropes. Also specify what stays still. A wheel must not turn before the water reaches it. The historical baseline is 1344 x 768, single-pass, 16 steps; change it only for a justified task need.

## Voice, ambience and editing

Use Drama 3 and existing voice references for intelligible speech. Save lines and settings inside the scene. Inspect emotional/pronunciation tags for truncated or duplicated words. Keep useful FreeVideo ambience; add exact effects separately when needed.

Watch the video in motion and listen to the whole mix. A valid MP4/audio stream does not establish quality. Check unexpected speech, action completion, synchronization, pauses and camera continuity. Add achievements and text as editable overlays.

Trim duplicate held poses at first/last-frame joins. Show a reward after the completed action. Move narration with the picture edits. Keep original footage, graphics and speech tracks separate.

## Save and hand off

- Keep originals in `video/raw/`.
- Save failed alternatives to `video/drafts/rejected/` (ignored by Git).
- Keep only the current accepted complete scene in the root of `output/`.
- Put copies of accepted clips in `output/clips/`.
- Keep superseded complete edits in `work/archive/`.
- Update the scene README and main index with files, settings, feedback, tasks and a short journal.
- Record approval only when given. Approval of a plan is not approval of future frames or renders.

For runtime/memory diagnostics read [COMFY-MCP-LLM.md](COMFY-MCP-LLM.md). Old PIDs and process logs are historical evidence only. Do not start the next scene while organizing files.
