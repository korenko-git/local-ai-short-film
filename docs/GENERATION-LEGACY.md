# Historical generation workflow

These records describe the older project layout and early production state. For current operation use [the project README](../README.md), [scene index](../scenes/README.md), [scene workflow](SCENE-WORKFLOW.md) and [Comfy MCP guide](COMFY-MCP-LLM.md). Historical paths below are references, not a second canonical output tree.

## Early state and layout

At this stage six working scenes lived in `output/scenes/`, with `output/assemblies/scenes-01-06.mp4` as the assembly. Only the dossier was illustrated. Scene 7's earlier attempts were rejected in `archive/rejected/scene07/`; an interrupted approach generation was not a finished result. The later scenes were plans. That is a historical snapshot, not the status of the current twelve-scene film.

| Former location | Purpose / current interpretation |
|---|---|
| `output/scenes` | Completed working scene edits; now scene-local `output/` |
| `output/assemblies` | Full-film assemblies |
| `frames/approved`, `frames/drafts` | Selected keyframes and alternatives; old chest/scooter variants are not canon |
| `frames/source-video` | Original FreeVideo clips for editing; now scene-local `video/raw/` |
| `refs/images` | Identity/costume/bridge/dossier references |
| `audio/voices` | Concrete Drama 3 lines and supplied dossier voice |
| `refs/audio` | Reusable voice references, clock and source voice; reusable voices now `shared/refs/audio/` |
| `audio/effects`, `audio/music` | Sea, stamp impact, plank crack, ambience and music |
| `workflows/images`, `workflows/voice` | API-format Qwen/Drama workflows |
| `workflows/video` | Real FreeVideo tasks with `prompt.txt`, `media.json`, inputs |
| `scripts`, `tools/FreeVideo` | Launchers and the separately installed upstream CLI |
| `archive` | Rejected/history material |
| `MANIFEST.json`, `SOURCE-INVENTORY.json` | Original material provenance/inventory, retained as local records |

Original pre-organization `../outputs` and `../work` were retained; they are not canonical current output. The former storyboard was saved as `STORYBOARD-OLD.jpg`; it records an earlier proposal, not accepted current scenes. Use `STORYBOARD.md` and `STORYBOARD.jpg` with the scene index.

## Runtimes and models

The original FreeVideo installation used its `envs/unified` environment, `models/` and prepared `edge-da37681f5a1f7015/int8-convrot/cache`. Its installer also supplied a separate Python runtime outside the checkout. Models were not duplicated into this project. The CLI's original source checkout was `../work/FreeVideo`; the working copy later became `tools/FreeVideo`. Current launchers expose install/cache/CLI paths as parameters.

Portable ComfyUI uses its own adjacent `python_embeded/python.exe`, distinct from the MCP service interpreter; local API is `127.0.0.1:8188`.

- Drama 3: `custom_nodes/ComfyUI-Drama3` from PedroMarinhoDev; `models/diffusion_models/drama3_w4a8experts_bf16.safetensors` and `models/vae/drama3_codec.safetensors`; source `fishaudio/drama-3`. FL ChatterBox was installed earlier, but Drama 3 became the preferred tool.
- Qwen Image 2.1: `models/diffusion_models/qwen_image_2.1_int8_convrot.safetensors`, `models/text_encoders/qwen3vl_8b_int8_convrot.safetensors`, `models/vae/qwen_image_2.1_vae_bf16.safetensors`.

Copying project files does not install these models or validate the machine's environment.

## Historical production procedure

1. Read the selected scene and split complex action into problem → search → physical action → result. Do not overload one static transition.
2. Qwen keyframes use ComfyUI API JSON, not UI node-layout JSON. Historical scene-7 drafts were `v3-scene07-qwen-approach.json` and `v3-scene07-qwen-open.json`; they were unfinished then, not accepted end-to-end workflows. Bridge image families were `v5-scene06-reference-rope-bridge.json`, `v6-scene06-escape-*.json` and `v7-scene06-orbit-*.json`. Upload the current `LoadImage` references and validate before running; update upload names on another machine.
3. Drama 3 speech templates included `workflows/voice/v3-scene06-voices.json`. Change text, seed and `filename_prefix` on Generate/SaveAudio. Narrator used `synthetic-voice-a.mp3` and its exact EncodeVoice transcript. The supplied dossier voice belongs only to that scene. At this early stage scene 7 still needed narrator speech about the dead end and the separate "О!" reaction; later scene records supersede that missing-audio snapshot.
4. Unload idle ComfyUI models before video, without stopping unrelated processes. Historical RTX 5070 Ti 16 GB baseline: 1344 x 768, one pass, 16 steps. The earlier 480 x 288 plus upscale mode was rejected.
5. New video uses FreeVideo CLI only, not a Wan/Comfy video workflow. A media file can use `{"version":1,"first":"inputs/frame.png","last":"inputs/frame-end.png"}` with optional `last`. Do not combine first/last mode and reference mode. Paths are relative to `media.json`.
6. Edit with FFmpeg, trim held poses, place speech/effects against the action and show the individual scene. Add labels/achievements as edit layers. Only explicit acceptance promotes a result into the selected complete sequence.

Example using the current launcher's required scene argument:

```powershell
./scripts/Generate-Video.ps1 -Scene 06 -Task scene06-orbit -OutName scene06-orbit-new -Seconds 6.5 -Seed 11070233
```

Selected bridge tasks were `scene06-sway-hq`, `scene06-orbit` and `scene06-escape`. Escape input frames are already mirrored; never mirror them again. Older `scene06` and non-HQ `bridge-trial` tasks are not the selected new-render source. Old Wan clips and script experiments are not evidence of accepted current scenes.

## Assembly, inputs and sound provenance

Legacy edit scripts in `archive/legacy/scripts` still reference the former `work/outputs` layout and require path adaptation. They were not claimed as a universal one-command, bit-identical rebuild. Originals were retained rather than broken by the reorganization.

`COMFY-INPUTS.json` maps workflows to their LoadImage/LoadAudio names. Available files were copied into the input-reference directory; it is now local `shared/refs/comfy-inputs/`, with approved reusable voice references consolidated in `shared/refs/audio/`. Upload with `overwrite:true` only for known current inputs, then validate/run. `available=false` requires restoring the missing input and is not a portable-ready workflow.

Early scenes 1–5 use Kevin MacLeod's Adventures in Adventureland, CC BY 4.0; sea is Joseph Sardin / BigSoundBank, CC0. Bridge suspense music and impact/crack effects were synthesized locally. See [credits](../CREDITS.md) and shared audio metadata for attribution. Old script/storyboard descriptions remain history; the current scene index controls the film.
