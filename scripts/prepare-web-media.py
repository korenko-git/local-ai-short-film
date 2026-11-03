"""Create web copies from preserved local footage. Requires FFmpeg."""
import json,subprocess,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];DEST=ROOT/'article/assets'
SOURCES={
    'film.mp4':'output/assemblies/film-scenes-01-12-review-v3.mp4',
    'bridge-camera.mp4':'scenes/06-courage-bridge/output/clips/scene06-orbit-hq.mp4',
    'curiosity-camera.mp4':'scenes/07-shell-dead-end/output/clips/scene07-deadend-pov-v1.mp4',
    'hair-wind.mp4':'scenes/04-map/output/scene-04-matvey-gets-map-v4.mp4',
    'water-first-turn.mp4':'scenes/08-ingenuity-gate/video/raw/scene08-correct-first-turn-v1.mp4',
    'speed-dynamic.mp4':'scenes/09-speed/output/clips/scene09-speed-camera-approved-v5.mp4',
}
records=[]
for filename,relative in SOURCES.items():
    src=ROOT/relative;out=DEST/filename
    assert src.is_file(),f'Local production file required: {relative}'
    if not out.exists():subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',str(src),'-map_metadata','-1','-c:v','libx264','-preset','fast','-crf','25','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-movflags','+faststart',str(out)],check=True)
    records.append({'asset':'assets/'+filename,'source':relative,'purpose':'public viewing copy','video':'H.264 CRF 25','audio':'AAC 128 kbps'})
for name,source,seconds in [('water-first-turn','scenes/08-ingenuity-gate/video/raw/scene08-correct-first-turn-v1.mp4',4.5),('speed-dynamic','scenes/09-speed/output/clips/scene09-speed-camera-approved-v5.mp4',2.5)]:
    out=DEST/(name+'.jpg')
    if not out.exists():subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-ss',str(seconds),'-i',str(ROOT/source),'-frames:v','1','-map_metadata','-1','-q:v','2',str(out)],check=True)
    records.append({'asset':'assets/'+out.name,'source':source,'seconds':seconds,'purpose':'clip poster extracted without retouching'})
reference='scenes/09-speed/refs/speed-camera/contact.jpg'
if not (DEST/'speed-reference.jpg').exists():shutil.copy2(ROOT/reference,DEST/'speed-reference.jpg')
records.append({'asset':'assets/speed-reference.jpg','source':reference,'purpose':'supplied anime motion-reference contact sheet; reference imagery, not a film render'})
(DEST.parent/'web-media.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print('Ready:',len(SOURCES),'web videos and',len(records)-len(SOURCES),'supporting images; originals preserved')
