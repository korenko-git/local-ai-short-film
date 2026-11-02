# Comfy MCP: working guide for LLM agents

Revised 2 November 2026. This documents one verified local setup and its failure modes, not a guarantee for every machine. Inspect current MCP schemas before using the tool names below.

## 1. Read the context

Read `AGENTS.md`, `scenes/README.md` and the scene README. Keyframes: Qwen Image 2.1. Speech: Drama 3. Show connected keyframes and wait for the user's response before FreeVideo. Keep API workflows, prompts, inputs, outputs, seeds and run records in the scene. Preserve previous attempts.

## 2. Check the actual API

Call `server_info({})`, then `system_stats({})`. The original workstation uses `127.0.0.1:8188` and RTX 5070 Ti 16 GB VRAM. A successful CUDA response from `system_stats` means the API is reachable. `server_info.running=false` alone does not prove that a manually launched server is down. Reuse a healthy instance.

## 3. Launch the correct portable interpreter

From the checkout root:

```powershell
./scripts/Start-ComfyPortable.ps1 -LogDir './scenes/07-shell-dead-end/work'
```

For another installation, pass `-ComfyRoot` and `-ComfyPython`. The historical defaults point to `D:\AI\ComfyUI_windows_portable\ComfyUI` and its adjacent `python_embeded/python.exe`.

The launcher first checks `/system_stats`, reuses a healthy server, starts the portable interpreter in a hidden window on loopback, records PID/start time/executable and logs, and waits up to 120 seconds for the actual API. A PID is not readiness. If a command returns a session ID, wait for completion.

In the original Codex sandbox, localhost, temp files or installations outside the workspace sometimes required normal platform escalation. Use that mechanism for an observed permission error; do not change firewall, ACL, MCP registration, CORS or LAN listening. Do not repeat an identically denied launch blindly.

Do not use MCP `launch_comfyui` blindly: it previously selected the MCP service interpreter instead of portable ComfyUI. These are separate environments. A missing `filelock` or `PIL` import is a reason to inspect the executable, not to install ComfyUI packages one by one into MCP's Python. Inspect fresh stdout/stderr and timestamps; an old log is not current process state.

## 4. Upload the inputs

Check every `LoadImage`/`LoadAudio` reference in the API-format JSON. Restore real local files and call `upload_file({paths:[...], overwrite:true})` with absolute paths derived from the current checkout. Overwrite only known inputs for the current task.

Inspect `uploads[].cloud_name` and `subfolder`; update the workflow if names changed. Never substitute a rejected duplicate-character image or an unrelated costume. Private source photos stay excluded. Approved shared voice-reference files are available in `shared/refs/audio/`; use its transcripts and upload the referenced file before running a workflow.

## 5. Validate, enqueue and record

Call `validate_workflow({workflow_path:...})` and current `system_stats`. Continue only with valid inputs and available models/nodes. Use dependency discovery for missing node types rather than guessing packages. Release memory only after checking that no other generation is running.

Call `run_workflow({workflow_path:...,wait:false})`. Save `prompt_id`, model, seed, inputs, settings and status beside the workflow immediately. Queued does not mean completed.

## 6. Wait, retrieve, inspect

Use `job({action:"status",prompt_id:...})` or bounded waits such as `job({action:"wait",prompt_id:...,timeout_seconds:25})`. A timeout is not failure: do not enqueue a duplicate. On an error read job details and fresh logs.

After completion use `fetch_outputs` into the scene directory. Inspect identity, costume, hands, number of people, props, geography and motion direction. Show the actual frames in order and wait for feedback. A successful render is not approval.

## 7. Video and handoff

Unload idle ComfyUI models before heavy FreeVideo jobs: both tools compete for GPU and host memory. Do not stop unrelated processes. Use `scripts/Generate-Video.ps1` with a new output name, only after the user has responded to the connected frames unless a later explicit instruction changes that workflow. Historical baseline: 1344 x 768, one pass, 16 steps.

Watch video in motion and listen to all sound. Follow [SCENE-WORKFLOW.md](SCENE-WORKFLOW.md) for editing, acceptance and documentation.

## Verified historical example

On 1 November 2026 portable startup reached `api_ready=true`; upload and validation succeeded without warnings; Qwen Image 2.1 completed the scene-7 sign image at seed `11070107`, 28 steps. Local workflow: `scenes/07-shell-dead-end/workflows/images/scene07-linked-keyframes-v1/scene07-same-sign.json`. Its run record and logs are retained locally. The evidence paths and API-format examples below complete the original production record.

## Diagnostic boundaries

- Verify executable and start time before stopping a process; an old PID is insufficient.
- Never delete FreeVideo engine locks to bypass ownership.
- Use API/interpreter diagnostics for localhost/Python failures, not browser automation.
- Respect denied application control; do not route around it with another UI tool.
- Do not replace models/global settings to work around an unverified launch issue.
- Keep planned, queued, interrupted, rejected, rendered, reviewed and accepted states distinct.

## Original successful run records

The verified Qwen task returned prompt ID `ea636fe5-71e0-4d4d-88e4-987ba154210d`, seed 11070107, 28 steps, completed on 1 November 2026. Retrieved image: `scenes/07-shell-dead-end/frames/drafts/ea636fe5_000.png`. Workflow: `scenes/07-shell-dead-end/workflows/images/scene07-linked-keyframes-v1/scene07-same-sign.json`; sibling run record: `run-at-shell.json`. Successful portable logs: `scenes/07-shell-dead-end/work/comfy-authorized-stdout.log` and `comfy-authorized-stderr.log`.

The original tool calls used these shapes (resolve placeholder paths from the current checkout):

```javascript
mcp__comfy_mcp__upload_file({paths: ["ABSOLUTE_SCENE_FRAME", "ABSOLUTE_CHARACTER_REFERENCE"], overwrite: true})
mcp__comfy_mcp__validate_workflow({workflow_path: "ABSOLUTE_WORKFLOW_JSON"})
mcp__comfy_mcp__run_workflow({workflow_path: "ABSOLUTE_WORKFLOW_JSON", wait: false})
mcp__comfy_mcp__job({action: "status", prompt_id: "RETURNED_ID"})
mcp__comfy_mcp__job({action: "wait", prompt_id: "RETURNED_ID", timeout_seconds: 25})
mcp__comfy_mcp__job({action: "error", prompt_id: "RETURNED_ID"})
mcp__comfy_mcp__fetch_outputs({prompt_id: "RETURNED_ID", out_dir: "ABSOLUTE_SCENE_FRAMES_DRAFTS", inline_images: false})
```

For a permission-denied portable launch from a managed agent, the documented command used the platform's normal `sandbox_permissions: "require_escalated"` mechanism with justification: "Start the documented local portable ComfyUI and verify its localhost API for the authorized Qwen image generation." Do not treat that historical successful launch as permission to change network or machine-wide settings. If investigating old MCP launch logs, specify port 8188 and compare timestamps with the portable process; stale logs can describe another interpreter/run.
