# 10. Chest and gift

## Current state and full-film revisions

The complete scene v1, `output/scene10-chest-gift-v1.mp4` (31.32 s), was explicitly accepted, including the four video segments and approved voices. It is the unchanged picture/sound of `work/scene10-voiced-preview-v2.mp4`.

Later review-only revisions are `work/scene10-montage-v2.mp4` and current `work/scene10-montage-v3.mp4`. v2 shortened the reaction before the parrot to one second by removing the original 14.167–19.750 s interval; filter `work/scene10-montage-v2-filter.txt`. v3 restores the parrot flight and a short character reaction (+1.75 s relative to v2), using original v1 intervals 0–13.167, 14.500–17.250 and 19.750–end. Both narrator/parrot lines remain complete. This responds to full-film feedback at 2:11–2:13, 3:17–3:19 and 3:37–3:39. The latest revision awaits separate assessment; sources/settings were preserved and no regeneration performed.

## Story, props and shot plan

After scene 9, the character checks the map, reaches the stone platform above the bay, finds the chest, puts the map away and says "Вот ты где!". He opens it himself. Arrival and gift reveal were merged into one scene with approval. Additional locks, seals and another trial were cancelled. The canonical chest has a convex lid, two brass bands and a round lock.

The rejected scroll text was "ВАШЕ СУДНО ОЖИДАЕТ В ПОРТУ"; do not restore the port detour. After the treasure, a taut sloping cable provides a Tomb Raider-style descent directly to the beach. The folded grey two-wheel scooter goes into a carrying case for that descent; the final trolley grip is described in scene 11, replacing earlier ice-axe ideas.

Four segments cover three actions: arrive; open/reveal; parrot reaction followed by a close-up speaking insert. The accepted reveal frame v3 is the common endpoint/startpoint of clips 2 and 3. Alternate the parrot, scooter and character reaction; do not stretch approach or packing. The parrot's full 11.16 s voice fits its own insert. The narrator's mission belongs at the night zipline in scene 11. The former separate-arrival README is retained locally at `work/archive/scene10-arrival-before-merge/README.md`.

## Exact Russian dialogue and performance

| Speaker | Exact line | Direction |
|---|---|---|
| Character | "Вот ты где!" | On finding the chest, after putting the map away |
| Narrator | "Перед нами новейшее достижение мирового кораблестроения." | Reveal introduction; preserve established narrator |
| Parrot, pirate voice | "Два колеса, один руль, ни одной пушки. Зато какая скорость!" | The parrot says only this joke |
| Narrator, separate pending cue | "Молодец!" | For the proposed gold achievement, not yet accepted |

Use Drama 3. The parrot dozes on a branch beside the chest, not inside it, startles at the lid creak and launches into a memorized speech. Roll the Russian consonant in "руль" and "скорость", pause after "ни одной пушки", then end excitedly. v2 phonetic hints "р-р-руль" and "скор-р-рость" stretch only those consonants; do not add new canonical words. The narrator retains introduction, mission and full birthday greeting.

| Voice version | File / seed | Status |
|---|---|---|
| Narrator introduction v2 | `audio/voice/scene10-narrator-shipbuilding-v2.flac`; 11101003; `synthetic-voice-a.mp3` | Explicitly accepted |
| Parrot v3 | Drama 3; 11101005; `synthetic-pirate-ref.wav`; `workflows/voice/scene10-voiceover-v3/` | Source take for the selected edit |
| Parrot v4 | `audio/voice/scene10-parrot-scooter-v4.flac`, 11.16 s | Explicitly accepted |
| Character chest line | `audio/voice/scene10-matvey-found-chest-v1.flac`; 11101006; `synthetic-voice-b.mp3` | Accepted within voiced preview v2 |
| Narrator praise | `audio/voice/scene10-narrator-molodec-v1.flac`; 11101007; narrator reference | Awaiting separate listening |

Parrot v4 is an edit: first 2.00 s of the squawk from parrot v1, then v3 from 0.50 s to the end. Recipe/source/settings: `workflows/audio/scene10-parrot-scooter-v4-edit/`. In narrator v1 the phrase repeated; parrot v2 cut off halfway. v1's inarticulate frightened cry was useful, but that did not mean the whole v1 take was accepted. User acceptance applies to narrator v2 and parrot v4; their workflow packages retain tags/prompts/parameters/prompt IDs.

## Proposed gold achievement — still pending

`work/achievement-gold-molodec.svg` uses SMIL animation. Start from the existing dark "СКОРОСТЬ — ИСПЫТАНИЕ 4 ИЗ 4" state; over 1.35 s a gold fill wipes left to right over it, then black "МОЛОДЕЦ" lettering appears. The user specifically requested an animated transformation, not an unrelated static badge. The animation and separately generated narrator "Молодец!" await assessment and are not included in accepted scene v1.

## Qwen keyframes

The user accepted reveal replacement v3 and authorized video using the linked storyboard, then accepted the four-segment voiced preview. Do not infer acceptance of unrelated draft stills outside that edit.

| Frame | Description / record |
|---|---|
| `frames/drafts/scene10-01-arrival-no-matvey-v1.png` | Same first view without the character, preserving the existing left-hand entrance and composition |
| `frames/drafts/scene10-01-arrival-v1.png` | Character at closed chest, parrot, distant cliff, taut cable and beach; costume matches reference. Visible metal trim may differ from chest canon and required review. |
| `frames/approved/scene10-02-gift-reveal-v3.png` | Character holds the open lid with both hands and looks inside in surprise; scooter/helmet inside. Replaces v2, where he merely stood by a chest that seemed to open itself. Draft copy retained. |
| `frames/drafts/scene10-03-parrot-reaction-v2.png` | Closer parrot with open beak; character appears only once at edge; gift stays in open chest |

Initial package: `workflows/images/scene10-keyframes-v1/`; successful seeds 11100101, 11100103, 11100105; Qwen Image 2.1, 1024, 28 steps, Euler/simple, CFG 1. Reveal v3 has its own `workflows/images/scene10-02-gift-reveal-v3/` package, seed 11100110, same image settings, prompt ID `ebfc4e61-ecc9-4e3e-b2b5-7fd4f3fef2e5`.

Removing the character from the first frame used `workflows/images/scene10-01-arrival-no-matvey-v1/`, seed 11100107, same Qwen settings and the identical first frame supplied as all three references. The earlier `scene10-00-empty-entrance-v1.png` incorrectly invented a second passage and was rejected. `e67b2589_000.png` and `cb49186e_000.png` duplicated the character and remain drafts. Two new map/platform images, seeds 11100108–11100109, were rejected as unrelated to the established storyboard and moved to `frames/drafts/rejected/`; their workflows are historical only.

Use the shared character master and accepted scene-9 ending for identity/costume/geography. Keep daylight here; night belongs to scene 11. Early stills presented the scooter/helmet layout, chest trim and parrot model as visual proposals, not independent approval of packaging. The case was not shown in those stills. Subsequent case transport and day/sunset/blue-hour/night transition were developed for scene 11; its first historical five-clip assembly was 37.29 s and was not this scene's accepted edit.

## FreeVideo segments

| Shot | Raw file | Seed | Transition / measured result |
|---|---|---:|---|
| 1 | `video/raw/scene10-01-arrival-v1.mp4` | 11100121 | Empty platform → character at closed chest; 6.58 s |
| 2 | `video/raw/scene10-02-open-chest-v1.mp4` | 11100122 | Closed chest → character holding lid; 6.58 s |
| 3 | `video/raw/scene10-03-parrot-reaction-v1.mp4` | 11100123 | Accepted reveal v3 → branch reaction; 6.58 s |
| 4 | `video/raw/scene10-04-parrot-lipsync-v1.mp4` | 11100125 | Close-up beak movement using parrot v4 audio reference; 11.55 s |

All are 1344 x 768 at 24 fps. Task packages in `workflows/video/` retain prompt/media/inputs/settings; run reports and engine artifacts remain with raw clips. Copies with the same filenames are in `output/clips/`.

The initial dialogue-free sequence `work/scene10-clips-preview-v1.mp4` was 19.78 s. The accepted voiced preview is `work/scene10-voiced-preview-v2.mp4`, copied unchanged to `output/scene10-chest-gift-v1.mp4` (31.32 s). Clip 1 contains the accepted character line, clip 2 the narrator, clip 4 parrot v4. Contact sheets: `work/scene10-01-arrival-v1-contact.jpg`, `scene10-02-open-chest-v1-contact.jpg`, `scene10-03-parrot-reaction-v1-contact.jpg`, `scene10-04-parrot-lipsync-v1-contact.jpg`.

`scene10-03-parrot-lipsync-v2` was rejected during continuity inspection because the chest closed mid-shot; it is in `video/drafts/rejected/`. The selected close insert is the new clip-4 v1, not that rejected version.

## Production history and remaining work

- **1 November:** moved material into the scene folder, retaining the then-current plan status.
- **2 November, ending design:** removed the port scroll, considered a rope descent after treasure, restored the complete scooter-introduction/birthday text, and divided roles between narrator and pirate parrot. The old scene 15→11 renumbering was an intermediate stage before arrival/reveal merged into current scene 10. Final structure became three scenes (chest/gift, night zipline, starry greeting), with an initial 7–9-shot / 65–80 s target to be refined after speech. Structural approval did not approve future renders.
- **2 November, images:** prepared three connected Qwen drafts and retained duplicate-character failures. An empty establishing image first added an unwanted extra entrance; it was replaced by removing the character from the actual first frame. No video ran merely from those image preparations.
- **2 November, voices:** generated narrator/parrot v1, then v2 with single-utterance/pause tags and more comic pirate delivery. Narrator v2 accepted; truncated parrot v2 rejected. Generated parrot v3, assembled v4 with the earlier cry as requested, then received explicit acceptance of v4.
- **2 November, arrival/achievement:** added the map/chest action, character line and draft gold achievement. The two unrelated new map frames were rejected. Revised the badge to the requested animated dark-to-gold state and generated the separate praise cue; both remain pending.
- **2 November, video/acceptance:** accepted reveal v3 replaced the self-opening-lid appearance; four FreeVideo segments were assembled with the selected voices. The user accepted voiced preview v2 including the character line and later confirmed the resulting complete v1. Saved one full output and four accepted clip copies. Gold praise badge/cue were not included.
- **2 November, later editing:** v2 shortened reaction, v3 restored flight/reaction as described at the top; both are review revisions, with original media untouched.

Remaining: assess the proposed gold badge and narrator praise independently, and review the latest full-film montage. Preserve the accepted v1 and its clips; do not silently promote unreviewed standalone drafts or cancelled endings.


## Material layout

`frames/approved/` contains selected keyframes; `frames/drafts/` alternatives. Scene-specific references are in `refs/`. Original FreeVideo clips stay in `video/raw/`; rejected attempts in `video/drafts/rejected/`. `workflows/images/`, `workflows/video/` and `workflows/voice/` keep the API workflows or generation tasks, prompts, media, seeds and settings. `audio/voice/` contains scene lines, `audio/sfx/` exact effects. Keep one current accepted complete scene in the `output/` root, accepted clip copies in `output/clips/`, and older complete edits in `work/archive/`.

Shared identity/costume references: `../../shared/refs/images/`; shared voice references: `../../shared/refs/audio/`. Empty directories do not imply that material exists. Read [the scene workflow](../../docs/SCENE-WORKFLOW.md) and [Comfy MCP guide](../../docs/COMFY-MCP-LLM.md) before new work. Paths refer to production records; raw media is retained separately from the published source.

## Documentation maintenance

- 2026-11-02: consolidated the complete production decisions, version history, artifact references and speech directions into this English README. Russian spoken/onscreen text is retained in quotation marks. No render or approval state changed.
