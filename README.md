<div align="center">

<a href="https://github.com/korenko-git/local-ai-short-film/raw/refs/heads/main/docs/article/assets/film.mp4">
  <img src="docs/article/assets/cover.jpg" alt="A sailing ship approaching a tropical island — watch the film" width="100%">
</a>

<h1>Generating a Short Film Locally</h1>

<p><em>One island. Four trials. A birthday adventure made with AI.</em></p>

<p><strong>4:10</strong> &nbsp;·&nbsp; <strong>12 scenes</strong> &nbsp;·&nbsp; <strong>24 fps</strong> &nbsp;·&nbsp; <strong>16 GB VRAM</strong></p>

<p>
  <a href="https://github.com/korenko-git/local-ai-short-film/raw/refs/heads/main/docs/article/assets/film.mp4"><strong>▶ Watch the film</strong></a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#about-the-project">Behind the scenes</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="#tools-and-hardware">Tools &amp; hardware</a>
</p>

<p><sub>Russian dialogue · MP4, 71 MB · Article in English / Українська / Русский</sub></p>

</div>

---

## About the project

I made a four-minute birthday adventure using image, speech and video generation. This repository contains the production notes, prompts, workflows and an [illustrated article](docs/article/README.md) about how it came together.

The character arrives on an island, crosses a suspension bridge, finds a hidden path, solves a water puzzle and races through a closing gate. A chest, a talking parrot and a night-time zipline lead to the birthday ending.

The finished edit runs **4 minutes 10 seconds**, with **12 scenes at 1344 × 768 and 24 fps**. I generated images, speech and video separately, then assembled the scenes with FFmpeg. Codex helped prepare workflows, organize the material and carry out editing changes.

The article follows the actual attempts: camera moves guided by a reference, wind moving the character's hair, convincing water motion, a talking parrot, failed hourglass animation and the revisions needed to turn separate clips into a film.

## Tools and hardware

| Task | Tools |
|---|---|
| Keyframes | Qwen Image 2.1; GPT Image for some water-puzzle frames |
| Speech | Drama 3 |
| Video | MiniMax H3 through FreeVideo; an early experiment with Wan 2.2 |
| Workflow assistance | Codex and ComfyUI MCP |
| Editing and audio mixing | FFmpeg |

I used an RTX 5070 Ti with 16 GB of VRAM. Video generation took roughly 1.5 minutes per second of footage in my setup. During one speech-generation run, occupied system RAM reached about 52 GB. The article describes the memory optimizations and community tools that made this workflow possible.

## Explore the repository

- [Scene index](scenes/README.md) — story, scene notes and production history.
- [Production workflow](docs/SCENE-WORKFLOW.md) — keyframes, generation and editing.
- [ComfyUI MCP guide](docs/COMFY-MCP-LLM.md) — setup and working with the local tools.
- [Generation notes](docs/GENERATION-LEGACY.md) — model files, settings and earlier experiments.
- [Article source](docs/article/README.md) — translations, assets and build instructions.
- [Credits](CREDITS.md) — tools, music and source attribution.

Selected footage and stills are included with the article. Raw generations, rejected takes, personal reference photographs and model weights are excluded. Shared voice references are in [shared/refs/audio](shared/refs/audio/README.md).

## Preview the article locally

With Python 3 installed, run these commands from the repository root. No additional Python packages are needed.

```sh
python scripts/build-article.py
python scripts/build-site.py
python scripts/preview-site.py
```

Open <http://127.0.0.1:8765/>. Edit the text in `docs/article/content/en.json`, `uk.json` or `ru.json`, then rebuild the pages.
