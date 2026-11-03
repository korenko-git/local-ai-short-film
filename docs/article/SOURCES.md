# Sources and editorial boundaries

This is the filmmaker's first-person production account. The English, Russian and Ukrainian editions share the same sections and examples. Their original source is the local production record, not external model benchmarking.

## Evidence

- Scene READMEs: consolidated English plot, footage, prompts, parameters, feedback and approval history; exact Russian dialogue is quoted.
- Local v3 timeline: 12 scenes, 250.250 seconds, bridge achievement at 70 seconds.
- Provided production chats, 31 October–2 November 2026: original story, failed attempts, shot direction, organization and edit changes. Automated review sessions containing copies of context were not counted as creative conversations. Raw transcripts and account/process metadata are not published.
- The filmmaker's later additions: Wan 2.2 comparison, about 52 GB occupied RAM during speech, camera examples, wind in hair, source-image degradation, water behaviour, parrot and hourglass evaluation.
- Hardware configuration supplied by the filmmaker on 3 November 2026: NVIDIA GeForce RTX 5070 Ti with 16 GB VRAM, AMD Ryzen 7 9800X3D and 64 GB system RAM. The 52 GB figure describes occupied system RAM during the observed speech run, not isolated model memory. The account explicitly separates local generation from the GPT Image keyframes made through an external service.
- Local FreeVideo documentation and generation launcher: MiniMax H3/VDN-H3 relationship, memory planning, int8 ConvRot cache and historical 1344 x 768 / 24 fps / single-pass / 16-step settings.
- `assets.json` and `web-media.json`: still timestamps and video source paths, relative to the original workspace.
- Added viewing examples use scene-4 v4, `scene08-correct-first-turn-v1.mp4` and accepted `scene09-speed-camera-approved-v5.mp4`. The speed-reference image is the supplied scene-9 `refs/speed-camera/contact.jpg`; it illustrates the borrowed motion language, not project-generated film imagery. The scene-9 chat and production journal support the rejected full anime-guide attempt, photo-reference/text-staging revision, Russian cue replacement, and CPU vocal-separation edit.
- Audio source records and root `CREDITS.md`: music and sea attribution.
- Achievement example: `shared/graphics/trial-achievement-template.svg` and `render_trial_achievement.py`, read directly from the repository. The SVG template was created by GPT Luna, as confirmed by the filmmaker. The renderer substitutes template fields and separately draws a transparent PNG using Pillow at double resolution before downsampling; it is not an SVG rasterizer. The article build copies the original sources and creates a populated SVG preview without Pillow.
- The filmmaker's 3 November 2026 artifact review: map orientation at 00:50–00:52 and 03:01–03:03, a third hand inherited from the bridge keyframe at 00:56–00:58, water flowing uphill from inconsistent puzzle geometry, Qwen/GPT Image staging attempts, the hourglass at 02:34–02:36, and unintelligible speech at 02:58–03:01. `artifact-assets.json` records public viewing copies. Some supplied crops were no longer on disk; corresponding frames were extracted from the retained web film instead. Image metadata was stripped; originals were not edited.
- Hourglass analysis reads `scenes/09-speed/workflows/video/scene09-start-v1/prompt.txt`, `media.json` and `parameters.json`. The task explicitly requests a horizontal-axis flip with a fixed stand; actual endpoint images are establish-v3 and bell-v1, not timer-v6. Neither specifies an intermediate rotation. Endpoint ambiguity and multiple simultaneous actions are possible explanations, not established causes. Manual GPT Image cleanup is the filmmaker's untested suggestion.
- Further bridge examples supplied on 3 November 2026: four early local-Qwen attempts, two photographic bridge references and the resulting keyframe. The filmmaker confirms that the desired precarious span emerged only after those references, alongside the third hand and rope railing on only one side. New galleries distinguish generated attempts from real-bridge reference photographs; `artifact-assets.json` records the metadata-stripped copies. Repeated copies of the same final keyframe are shown only once.

## Boundaries

16 GB refers to RTX 5070 Ti VRAM, not installed system RAM. About 52 GB is a run observation, not independently isolated per-process profiling. Timing, quality differences, convincing water motion and weak hourglass rendering are personal observations. No physical fluid simulation or exact phoneme lip-sync is claimed.

GPT Image was used for some trial-three states; Qwen Image 2.1 was the main keyframe tool. The public account acknowledges degraded video detail after those GPT Image inputs. Water belongs to trial three in the final order; the second trial is the shell/dead end. The camera examples are the second bridge clip and second curiosity clip. Source speech and on-screen text stay Russian.

The v3 film timeline is still marked pending full-film review in the production history. No retrospective approval is invented. The previous PDF is an earlier edition. Site preparation does not publish or push the repository.
