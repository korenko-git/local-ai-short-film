# Generating a short film locally

Editable content: `content/en.json`, `content/ru.json`, `content/uk.json`. All editions use the filmmaker's first-person voice. English is the default; the film itself retains Russian speech/lettering.

From the repository root:

```text
python scripts/build-article.py
python scripts/build-site.py
```

No Python packages are required. Pages: `index.html`, `ru.html`, `uk.html`. Use `--offline` on the article builder for single-file HTML exports; video remains external.

Selected public stills and three web videos live in `assets/`: the film, the bridge orbit and the curiosity POV. Provenance: `assets.json` and `web-media.json`. Recreate viewing copies with `scripts/prepare-web-media.py` only when the local production media and FFmpeg are available. Originals are preserved.

The Pages builder copies only referenced public files into `work/site-dist`, excluding content sources, local notes, chats, private inputs and machine inventories. See [general scene workflow](../SCENE-WORKFLOW.md) and [sources](SOURCES.md).
