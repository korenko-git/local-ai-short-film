# Working on this film

Read `scenes/README.md` and the selected scene README before production work. Keep episode-specific material in `scenes/NN-name`; shared identity, costume, voice references, music and graphics belong in `shared/`.

Read `docs/COMFY-MCP-LLM.md` before Comfy MCP. Portable ComfyUI Python and the MCP service use different environments. Do not fix a wrong interpreter by installing ComfyUI dependencies one by one into the MCP environment. First prepare and show connected keyframes, wait for the user's response, then start FreeVideo.

After a result, update the scene README and `scenes/README.md`: result paths, status, feedback, remaining tasks and a short journal. Interrupted/rejected renders are not complete results. Record approval only if the user gave it. Do not automatically generate following scenes during file organization or documentation work.

Use Qwen Image 2.1 for new keyframes, Drama 3 for clear speech, and exclusively FreeVideo for new video. Historical GPT Image/Wan experiments remain historical. Keep each shot's prompt, media, seed and parameters beside the task. Failed alternatives belong in `video/drafts/rejected/`.

Keep only the current accepted complete scene in the root of its `output/`. Keep copies of accepted individual clips in `output/clips/`; never move originals out of `video/raw/`. Save older full edits in `work/archive/`. Preserve consistent identity, costume, voices, props and geography.

FreeVideo may create ambience with video. Use Drama 3 for intelligible speech, and separate `audio/sfx/` files for precise effects when needed. Do not change global model settings without a concrete need.

## Public article

Edit `article/content/{en,ru,uk}.json`, then run `python scripts/build-article.py`. English is the default; translations must have matching sections. Write in the filmmaker's first person and call the protagonist the character (or the translation), rather than naming the child throughout the article. Do not invent approvals or measurements.

Run `python scripts/build-site.py` to stage and validate GitHub Pages files. Public pages must not link to private/local production directories. Exclude raw chats, local inventories, private reference inputs, weights and process logs. Preserve original footage when preparing smaller web copies. Preparation does not authorize a Git push or deployment.

The user explicitly approved publishing shared voice references. Their canonical directory is `shared/refs/audio/`, including transcripts and small encoded voice references. This exception does not include personal reference photographs or arbitrary per-workflow input snapshots. Keep finished music/ambience in `shared/audio/`. Public PNGs must not embed generation prompts, workflow JSON or EXIF; retain generation settings in separate workflow files and keep unmodified image backups local.

General scene workflow: `docs/SCENE-WORKFLOW.md`. Scene READMEs contain the complete English production record. Keep exact Russian speech in quotation marks when editing its English directions.
