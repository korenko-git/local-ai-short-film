# Generating a short film locally

Editable content: `content/en.json`, `content/ru.json`, `content/uk.json`. All editions use the filmmaker's first-person voice. English is the default; the film itself retains Russian speech/lettering.

From the repository root:

```text
python scripts/build-article.py
python scripts/build-site.py
python scripts/preview-site.py
```

Open <http://127.0.0.1:8765/> to preview the site. No Python packages are required.

JSON files are the editable text sources. The builder creates `index.html`, `ru.html` and `uk.html` for browsers; these generated files are ignored by Git. Edit the JSON, rather than the HTML, so rebuilding preserves changes. GitHub Actions generates the pages before publishing them to Pages.

Use `--offline` on the article builder for single-file HTML exports; video remains external.

Selected public stills and eight web videos live in `assets/`: the film, bridge orbit, curiosity POV, wind in the hair (scene 4), first channel turn/water motion (scene 8), accepted dynamic sprint v5 (scene 9), and short final-film excerpts of the hourglass and unintelligible speech. The sprint discussion includes the supplied anime-reference contact sheet and its camera/sound iteration history. Provenance: `assets.json`, `web-media.json` and `artifact-assets.json`. Recreate the original viewing copies with `scripts/prepare-web-media.py` only when the local production media and FFmpeg are available. Originals are preserved.

Artifact examples compare supplied keyframes with film frames and show puzzle development attempts. Galleries open images in the existing lightbox; small crops retain their natural size. The hourglass discussion distinguishes the supplied timer state from the bell-contact image actually used as the last frame in the video task. Proposed causes and manual keyframe cleanup remain hypotheses, not tested fixes.

Timecodes in paragraphs, image/video captions and tables link to the corresponding moment in the main film. A range seeks to its start; fractional seconds are supported. Seeking pauses other example videos and does not start playback automatically. Full artifact galleries remain expanded.

The article builder also copies the canonical achievement SVG template and Python renderer from `shared/graphics/`, fills a Russian first-trial SVG preview using only the standard library, and includes their download links and template source in the editing section. It does not execute the Pillow renderer. Offline exports embed the SVG preview; downloadable source files remain external.

The Pages builder copies only referenced public files into `work/site-dist`, excluding content sources, local notes, chats, private inputs and machine inventories. See [general scene workflow](../SCENE-WORKFLOW.md) and [sources](SOURCES.md).
