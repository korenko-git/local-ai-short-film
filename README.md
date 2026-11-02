# Generating a short film locally

A personal birthday adventure made with local image, speech and video generation: **12 scenes, four trials, 4:10.250**, assembled at 1344 x 768 / 24 fps. This repository documents the production and contains a three-language article ready for GitHub Pages.

Read the article: [English](docs/article/index.html) · [Українська](docs/article/uk.html) · [Русский](docs/article/ru.html). Open the HTML files locally, or build a self-contained site for Pages. The film keeps its original Russian audio and lettering.

## The experiment

I used Qwen Image 2.1 for most keyframes, GPT Image for some water-puzzle states, Drama 3 for speech and MiniMax H3 through FreeVideo for video. Codex and ComfyUI MCP helped orchestrate workflows and keep prompts, seeds and results organized; FFmpeg handled editing. My first Wan 2.2 attempt was faster but did not meet the quality I wanted.

The workstation had an RTX 5070 Ti with 16 GB VRAM. I observed roughly 52 GB of occupied system RAM during a speech run. Video took approximately 1.5 minutes of generation per output second in the working setup. These are project observations, not benchmark guarantees.

The article covers camera changes, wind in hair, surprisingly good water motion, degraded detail from some GPT Image inputs, a convincing parrot and less convincing hourglass sand, plus the final edit fixes.

## Build and preview the site

Python 3, standard library only:

```text
python scripts/build-article.py
python scripts/build-site.py
python scripts/preview-site.py
```

Then open `http://127.0.0.1:8765/`. Use `--offline` with `build-article.py` for single-file HTML exports; video remains external. Selected public stills and smaller web videos are in `docs/article/assets/`. Regenerating web copies from the private production workspace requires FFmpeg and `python scripts/prepare-web-media.py`.

The GitHub Actions workflow stages only the website. To use it, select **Settings > Pages > Source > GitHub Actions** in the GitHub repository. It runs on pushes to `main` or manual dispatch.

## Production navigation

- [Scene index](scenes/README.md): current plot, outputs and approval states.
- [Agent instructions](AGENTS.md): repository rules.
- [General scene workflow](docs/SCENE-WORKFLOW.md): directing, connected frames, editing and handoffs.
- [Comfy MCP guide](docs/COMFY-MCP-LLM.md): correct interpreter, API checks and memory management.
- [Historical generation workflow](docs/GENERATION-LEGACY.md): earlier layouts, model files and production procedure.
- [Credits](CREDITS.md): tools, music and source attribution.

```text
docs/article/              public article, translations and selected assets
scenes/NN-name/            scene notes, workflows and local production material
shared/                   shared graphics, identity, voices and music
scripts/                  generation launchers and website builders
output/assemblies/        local full-film assemblies (ignored)
work/                     local edits/history and staged site (ignored)
```

Scene-specific frames, dialogue, SFX and workflows stay with their scene. Shared identity/costume/voice references stay in `shared/`. Each shot keeps prompt, media, seed and settings. Originals stay in `video/raw/`; accepted clip copies go in `output/clips/`; the current accepted whole scene is the only full edit in its `output/` root. Previous full edits go in `work/archive/`.

## What is intentionally local

Raw/rejected media, local logs, private reference photographs, model weights and inventories are excluded by `.gitignore`; they are not deleted. The approved reusable voice clips, transcripts and small voice encodings are public under [shared/refs/audio](shared/refs/audio/README.md). Finished music/ambience remain in `shared/audio/`. Upstream FreeVideo is installed separately. A public clone does not include the private identity photographs or promise one-command reproduction of historical edits.

Scene READMEs contain the complete English production notes, version history, settings and remaining tasks. Exact Russian dialogue and on-screen labels remain quoted. Film v3 is still marked pending full-film review in the production timeline; acceptance of individual scenes is recorded separately.

## Generation tasks and model files

New keyframes use Qwen Image 2.1 through local ComfyUI/Comfy MCP; speech uses Drama 3 and is saved in the scene's `audio/voice/`. API-format workflows must have their LoadImage/LoadAudio files uploaded and validated before running. The local input inventory is `COMFY-INPUTS.json`; reusable voice references are under `shared/refs/audio/`.

New video uses FreeVideo only. Each `scenes/NN-name/workflows/video/TASK/` keeps `prompt.txt`, `media.json` and inputs. Frame paths inside media are relative to that media file. FreeVideo may generate sea/birds/leaves with the video; intelligible speech is separate Drama 3 and exact impacts/mechanisms can be separate `audio/sfx/`. Inspect sound after rendering rather than treating an audio stream as proof of quality. Sync suspense music in the edit.

```powershell
./scripts/Generate-Video.ps1 -Scene 06 -Task scene06-orbit -OutName orbit-new -Seconds 6.5 -Seed 11070233
```

The new raw clip remains pending review. The historical baseline is 1344 x 768, one pass, 16 steps. Unload idle ComfyUI models before video; bridge escape keyframes are already mirrored and must not be mirrored again.

Install/cache/runtime paths are configurable launcher arguments, not repository-owned model installations. Required model filenames and the earlier runtime/input workflow are documented in `docs/GENERATION-LEGACY.md`. Models were not duplicated into the project; legacy assembly scripts require adapting former paths rather than promising a one-command exact rebuild.
