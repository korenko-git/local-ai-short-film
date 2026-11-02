# Audio source and early synthesis records

## Sea recording

Joseph Sardin, "Sea Waves", BigSoundBank recording 0698, CC0: https://bigsoundbank.com/sea-waves-s0698.html . The waves are a field recording, not neural generation. Stable Audio was not used for this version; its large downloads were stopped and no wave-generation model was installed.

Music attribution and source metadata are in `music-source-metadata.json` and the root `CREDITS.md`. Current reusable voice references and exact transcripts are in `shared/refs/audio/`; performance directions are in `VOICE-DIRECTION.md`.

## Early Chatterbox experiment (historical)

An early local ComfyUI narration test used Chatterbox Multilingual with audio from the supplied `IMG_5233.MP4` as its reference. It was synthesized speech, not the original actor recording. Model: https://huggingface.co/ResembleAI/chatterbox ; integration: https://github.com/filliptm/ComfyUI_Fill-ChatterBox . Drama 3 later became the selected speech tool; the dossier uses the supplied completed recording as documented in its scene.

The original workflow was `matvey-narration-workflow.json`; rerunning that historical workflow required `matvey-narrator-reference.wav` in ComfyUI input. Language: Russian (`ru`). Text was split into short fragments for stability. Exact current scene scripts stay in Russian quotation marks in their English READMEs.

The old extension setup recorded diffusers 0.27.2 → 0.32.2 for huggingface_hub compatibility, numpy 2.2.6 and onnx 1.17.0, while protobuf remained 4.25.8. A pre-existing MediaPipe/numpy-2.x conflict was noted, and the complete third-party extension set was not validated. These are historical installation observations, not instructions to change a working environment.
