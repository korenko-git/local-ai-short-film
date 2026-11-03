# Credits

Project and direction: Dmytro Korenko. The article uses the filmmaker's first-person voice. The film's original speech is Russian; the English and Ukrainian pages translate the article.

## Production tools

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI), local image/speech workflows.
- [FreeVideo](https://github.com/FlashML-org/FreeVideo), local MiniMax H3 inference, built on the OpenVDN / Video DeltaNet work documented by the project.
- [ComfyUI-Drama3](https://github.com/PedroMarinhoDev/ComfyUI-Drama3), the Drama 3 speech integration.
- Qwen Image 2.1, the principal keyframe model; GPT Image for some puzzle states.
- Codex and ComfyUI MCP, workflow orchestration and production assistance.
- FFmpeg, editing, sound mixing, extraction and web encoding.
- ReportLab, the earlier PDF edition.

Tools and models retain their upstream licenses. Model weights are not included.

## Audio and images

- Kevin MacLeod, **Adventures in Adventureland**, CC BY 4.0, used in early scenes and mixed/edited with speech and effects. [Source](https://incompetech.filmmusic.io/song/8287-adventures-in-adventureland), [license](https://creativecommons.org/licenses/by/4.0/). Production metadata: `shared/audio/docs/music-source-metadata.json`.
- Ocean sound: Joseph Sardin / BigSoundBank, CC0, as documented in `shared/audio/docs/AUDIO-SOURCES.md` and the production notes.
- Generated dialogue/environmental sound is documented in scene records. Reusable synthetic voice references are included under `shared/refs/audio/` with source notes and transcripts; the filmmaker approved their inclusion on 2 November 2026.

Article illustrations include v3 film frames, selected generated keyframes and filmmaker-supplied crops; timestamps/provenance are in `docs/article/assets.json` and `docs/article/artifact-assets.json`. The site build excludes personal reference photographs, chats, raw generation archives and process logs. Selected failed examples are included for the artifact discussion. No blanket license is claimed over third-party material or personal likenesses.
