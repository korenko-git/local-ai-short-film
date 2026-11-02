"""Create web copies from preserved local footage. Requires FFmpeg."""
import json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];DEST=ROOT/'docs/article/assets'
SOURCES={'film.mp4':'output/assemblies/film-scenes-01-12-review-v3.mp4','bridge-camera.mp4':'scenes/06-courage-bridge/output/clips/scene06-orbit-hq.mp4','curiosity-camera.mp4':'scenes/07-shell-dead-end/output/clips/scene07-deadend-pov-v1.mp4'}
records=[]
for filename,relative in SOURCES.items():
    src=ROOT/relative;out=DEST/filename
    assert src.is_file(),f'Local production file required: {relative}'
    if not out.exists():subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',str(src),'-c:v','libx264','-preset','fast','-crf','25','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-movflags','+faststart',str(out)],check=True)
    records.append({'asset':'assets/'+filename,'source':relative,'purpose':'public viewing copy','video':'H.264 CRF 25','audio':'AAC 128 kbps'})
(DEST.parent/'web-media.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print('Ready:',len(records),'web videos; originals preserved')
