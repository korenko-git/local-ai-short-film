param(
    [Parameter(Mandatory=$true)][string]$LogDir,
    [int]$TimeoutSeconds=120,
    [string]$ComfyRoot='D:\AI\ComfyUI_windows_portable\ComfyUI',
    [string]$ComfyPython=''
)
$ErrorActionPreference='Stop'
if (!$ComfyPython) {$ComfyPython=Join-Path (Split-Path $ComfyRoot -Parent) 'python_embeded/python.exe'}
$endpoint='http://127.0.0.1:8188/system_stats'
$LogDir=[IO.Path]::GetFullPath($LogDir)
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
function Get-ComfyHealth {
    try { return Invoke-RestMethod -Uri $endpoint -TimeoutSec 3 }
    catch {
        if ($_.Exception.ToString() -match '10013|forbidden by its access permissions|Access is denied|Permission denied|доступ.*запрещ') {
            throw 'Sandbox denied localhost access. Run this script through exec_command with sandbox_permissions=require_escalated. Do not change firewall or install packages.'
        }
        return $null
    }
}
$health=Get-ComfyHealth
if($health){
    [pscustomobject]@{ready=$true;reused=$true;url=$endpoint;python=$health.system.python_version;comfy=$health.system.comfyui_version} | ConvertTo-Json
    exit 0
}
if(!(Test-Path -LiteralPath $comfyPython) -or !(Test-Path -LiteralPath (Join-Path $comfyRoot 'main.py'))){throw 'Portable ComfyUI installation not found.'}
$stamp=Get-Date -Format 'yyyyMMdd-HHmmss'
$outLog=Join-Path $LogDir "comfy-$stamp-stdout.log"
$errLog=Join-Path $LogDir "comfy-$stamp-stderr.log"
$recordPath=Join-Path $LogDir "comfy-$stamp-process.json"
$comfyProc=Start-Process -WindowStyle Hidden -PassThru -FilePath $comfyPython -ArgumentList @('-u','main.py','--listen','127.0.0.1','--port','8188') -WorkingDirectory $comfyRoot -RedirectStandardOutput $outLog -RedirectStandardError $errLog
$record=@{pid=$comfyProc.Id;started=$comfyProc.StartTime.ToString('o');executable=$comfyPython;arguments='-u main.py --listen 127.0.0.1 --port 8188';stdout=$outLog;stderr=$errLog;status='starting'}
$record | ConvertTo-Json | Set-Content -LiteralPath $recordPath -Encoding utf8
$deadline=(Get-Date).AddSeconds($TimeoutSeconds)
do {
    Start-Sleep -Seconds 2
    $health=Get-ComfyHealth
    if($health){
        $record.status='api_ready'
        $record | ConvertTo-Json | Set-Content -LiteralPath $recordPath -Encoding utf8
        [pscustomobject]@{ready=$true;reused=$false;pid=$comfyProc.Id;url=$endpoint;record=$recordPath;python=$health.system.python_version;comfy=$health.system.comfyui_version} | ConvertTo-Json
        exit 0
    }
    $comfyProc.Refresh()
    if($comfyProc.HasExited){break}
} while((Get-Date) -lt $deadline)
$record.status='api_not_ready'
$record | ConvertTo-Json | Set-Content -LiteralPath $recordPath -Encoding utf8
Get-Content -LiteralPath $errLog -Tail 35
throw "Comfy API not ready. Inspect $outLog and $errLog. Do not start another instance blindly."
