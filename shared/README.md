# Shared production material

```text
shared/
  refs/
    audio/          reusable voice clips, transcripts and encoded references
    images/         private identity/costume photographs (local only)
    comfy-inputs/   local upload snapshots (local only)
  audio/
    music/          finished music used in the edit
    ambience/       finished environmental recordings
    docs/           voice direction and audio-source documentation
  graphics/         shared editable achievement design
```

References describe or condition a generation. Finished music and ambience are edit assets. Keep those categories separate. Specific generated lines and exact SFX belong in their own scene, not here.

The user approved publishing reusable voice references. See [refs/audio/README.md](refs/audio/README.md). Private reference photographs and general upload snapshots remain ignored. Small voice embeddings are explicitly permitted; full model weights are not.

2 November 2026: consolidated the former voice-reference directory and reference transcripts under `refs/audio/`, verified file hashes and repaired scene-relative references. Unmodified originals and the cleanup manifest are retained in the ignored local archive.
