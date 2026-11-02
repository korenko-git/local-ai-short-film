# Voice direction and audio sources

Consult the selected scene README for the accepted take and exact Russian dialogue. This guide incorporates the original voice-direction notes.

The dossier uses the supplied completed voice recording with ticking clock and sea. Do not regenerate it or reuse its timbre for unrelated roles. Other speech uses Drama 3 with established shared references. Keep actual dialogue in its scene's `audio/voice/` and generation settings in `workflows/voice/`.

The narrator is a mature Russian male baritone: clear diction, solemn adventure delivery, warm dry humour and moderate pace. Use a warmer delivery for the birthday ending. The parrot uses a friendly, gruff theatrical pirate voice; rolled consonants and short pauses serve the two-wheels/no-cannons joke. The narrator handles the longer shipbuilding introduction, mission and greeting. Do not assign the whole ending to the parrot.

Use expressive tags only when they help the performance and inspect each result for truncation or repeated words. Preserve successful voice references across scenes; identical descriptions alone do not ensure identical timbre. Approved reference audio, encodings and exact transcripts are published together in `shared/refs/audio/`. Music and ambience belong in `shared/audio/`; concrete scene dialogue remains beside its scene.

The accepted parrot voice combines the first two seconds of an early squawk with a later speech take from 0.5 seconds onward (11.16 seconds total). This is a deliberate edit, not a new single generation.

FreeVideo may supply useful ambience/music, but intelligible dialogue belongs to Drama 3. Check for accidental nonsense voices before mixing. Keep precise effects separate where timing matters.

Ocean ambience: Joseph Sardin, Sea Waves, recording 0698, BigSoundBank, CC0: https://bigsoundbank.com/sea-waves-s0698.html . Music source metadata is in `music-source-metadata.json`; see the root `CREDITS.md` for attribution. The older Chatterbox setup described in AUDIO-SOURCES.md is an early experiment, not the current speech workflow.

## Performance examples and reference transcripts

Narrator description: `[mature male Russian baritone narrator, solemn adventure announcement, clear diction, warm dry humor]`. Use moderate pace, comic pauses before a reveal and no continuous shouting. For the birthday ending, soften and warm the same voice; finish "Полный вперёд!" energetically.

The original short pirate-announcement example used `[gruff friendly pirate captain, grand theatrical announcement]` and `[with delighted surprise]`, with a `[pause]` before the no-cannons joke. Preserve the chosen scene's canonical Russian text in quotes: "Два колеса, один руль, ни одной пушки. Зато какая скорость!". The long shipbuilding introduction remains the main narrator's line for clarity.

The integration notes describe free bracketed performance descriptions, `[pause]`, `[laughs]`, paired `<whisper>...</whisper>` and `<|speaker:0|>` speaker markers. Check the current integration and the rendered result; a repeated text description alone does not guarantee identical timbre. Lock successful takes/references rather than changing the voice between scenes.

Demo: https://pedromarinhodev.github.io/ComfyUI-Drama3/ ; sample descriptions: https://pedromarinhodev.github.io/ComfyUI-Drama3/samples.json . Initial synthetic A/B/pirate files were candidates, not automatically an accepted cast. Exact reference speech for Voice A/B was recorded as: "Hi there! I'm one of the voices this model can make up on its own, and I'm ready to read anything you write." Use `shared/refs/audio/voice-reference-transcripts.json` for the verified per-file transcription actually supplied to encoding.

Prop direction from the same notes: grey two-wheel scooter for a nine-year-old, no motor or seat; grey bicycle helmet fastened during riding. Only the dossier uses the supplied completed `drama3-take-2.wav` voice with clock/sea; do not resynthesize it or assign its timbre to other scenes.
