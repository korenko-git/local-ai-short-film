# Shared voice references

This is the canonical location for reusable audio references. The filmmaker approved keeping these references in the public repository on 2 November 2026. Personal source photographs and general ComfyUI upload snapshots remain excluded.

| File | Purpose |
|---|---|
| `synthetic-voice-a.mp3` | Narrator reference |
| `synthetic-voice-b.mp3` | Character voice reference |
| `synthetic-pirate.mp3` | Synthetic pirate voice sample |
| `synthetic-pirate-ref.wav` | Extracted pirate reference used for generation |
| `narrator-encoded.safetensors` | Small encoded narrator reference, not model weights |
| `pirate-encoded.safetensors` | Small encoded pirate reference, not model weights |
| `voice-reference-transcripts.json` | Exact speech-reference transcripts and source |

The source noted in the production records is the [ComfyUI-Drama3 demo](https://pedromarinhodev.github.io/ComfyUI-Drama3/). The notes describe these as synthetic demo voices. Preserve upstream attribution; including a reference here does not create a new blanket license for it.

Use [the voice-direction guide](../../audio/docs/VOICE-DIRECTION.md) for performance instructions. Finished music and ambience remain under `shared/audio/`; scene dialogue/effects stay in their scene folders.

## Migration journal

- 2026-11-02: consolidated the former `shared/voices/references` files and reference transcripts here; removed the byte-identical duplicate narrator MP3 from local ComfyUI input snapshots. File hashes were verified during migration. Updated scene links, including previously incorrect relative paths. Original files are preserved in the ignored local cleanup archive.
