param(
    [Parameter(Mandatory=$true)][ValidatePattern('^\d{2}$')][string]$Scene,
    [Parameter(Mandatory=$true)][ValidatePattern('^[a-zA-Z0-9_-]+$')][string]$Task,
    [Parameter(Mandatory=$true)][ValidatePattern('^[a-zA-Z0-9_-]+$')][string]$OutName,
    [ValidateRange(0.1,600)][double]$Seconds=6.5,
    [int]$Seed=11070233,
    [string]$FreeVideoRoot='D:\AI\FreeVideo-Matvey',
    [string]$CachePath='',
    [string]$FreeVideoCli=''
)
$ErrorActionPreference='Stop'
$project=Split-Path $PSScriptRoot -Parent
$matchesScene=@(Get-ChildItem -LiteralPath (Join-Path $project 'scenes') -Directory | Where-Object {$_.Name.StartsWith($Scene+'-')})
if ($matchesScene.Count -ne 1) {throw 'Expected exactly one matching scene directory.'}
$sceneFolder=$matchesScene[0].FullName
$job=Join-Path $sceneFolder ('workflows/video/'+$Task)
$prompt=Join-Path $job 'prompt.txt';$media=Join-Path $job 'media.json'
if (!(Test-Path -LiteralPath $prompt) -or !(Test-Path -LiteralPath $media)) {throw 'Task is missing prompt.txt or media.json.'}
$output=Join-Path $sceneFolder ('video/raw/'+$OutName+'.mp4')
if (Test-Path -LiteralPath $output) {throw 'Output already exists. Choose a new OutName.'}
$env:UV_HTTP_RETRIES='3';$env:UV_HTTP_TIMEOUT='120'
if (!$FreeVideoCli) {$FreeVideoCli=Join-Path $project 'tools/FreeVideo/freevideo.ps1'}
if (!$CachePath) {$CachePath=Join-Path $FreeVideoRoot 'prepared/edge-da37681f5a1f7015/int8-convrot/cache'}
if (!(Test-Path -LiteralPath $FreeVideoCli)) {throw 'Install the upstream FreeVideo CLI and pass -FreeVideoCli.'}
$cli=$FreeVideoCli
New-Item -ItemType Directory -Force -Path (Join-Path $sceneFolder 'work'),(Join-Path $sceneFolder 'video/raw') | Out-Null
$runInfo=@{scene=$Scene;task=$Task;seed=$Seed;seconds=$Seconds;width=1344;height=768;steps=16;two_pass=$false;output=$output;prompt=$prompt;media=$media;status='started'}
$record=Join-Path $sceneFolder ('work/'+$OutName+'-run.json')
$runInfo | ConvertTo-Json | Set-Content -LiteralPath $record -Encoding utf8
& $cli --root $FreeVideoRoot generate --prompt-file $prompt --media $media --cache $CachePath --width '1344' --height '768' --seconds ([string]$Seconds) --no-two-pass --base-steps '16' --seed ([string]$Seed) --out $output
if ($LASTEXITCODE -ne 0) {$runInfo.status='failed';$runInfo | ConvertTo-Json | Set-Content -LiteralPath $record -Encoding utf8;throw 'FreeVideo failed; inspect the task logs.'}
$runInfo.status='rendered_pending_review'
$runInfo | ConvertTo-Json | Set-Content -LiteralPath $record -Encoding utf8
