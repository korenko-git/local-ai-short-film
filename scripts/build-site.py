"""Stage a public whitelist, validate references; no dependencies/network."""
import json,shutil
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'docs/article';DEST=ROOT/'work/site-dist'
class Links(HTMLParser):
    def __init__(self):super().__init__();self.refs=[];self.ids=[]
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if k in ('src','href','poster') and v:self.refs.append(v)
            if k=='id':self.ids.append(v)
def main():
    resolved=DEST.resolve()
    assert resolved.parent==(ROOT/'work').resolve() and resolved.name=='site-dist'
    if DEST.exists():shutil.rmtree(DEST)
    DEST.mkdir(parents=True)
    allowed=['index.html','ru.html','uk.html','style.css','script.js']
    for name in allowed:
        assert (SOURCE/name).is_file(),f'Run build-article.py first: {name}'
        shutil.copy2(SOURCE/name,DEST/name)
    for name in allowed[:3]:
        p=Links();p.feed((DEST/name).read_text(encoding='utf-8'))
        assert len(p.ids)==len(set(p.ids)),f'Duplicate id: {name}'
        for ref in p.refs:
            parts=urlsplit(ref)
            if parts.scheme or parts.netloc:continue
            path=unquote(parts.path)
            if path.startswith('assets/'):
                asset=(SOURCE/path).resolve()
                assert asset.is_relative_to((SOURCE/'assets').resolve()),path
                assert asset.is_file(),f'Missing asset: {path}'
                assert asset.stat().st_size<100*1024**2,f'File exceeds Git limit: {path}'
                target=DEST/path;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(asset,target)
            elif path:assert path in allowed,f'Local production link: {ref}'
            if parts.fragment:
                target=DEST/path if path else DEST/name
                if target.suffix=='.html':
                    linked=Links();linked.feed(target.read_text(encoding='utf-8'))
                    assert parts.fragment in linked.ids,f'Missing anchor: {ref}'
    for name in ['cover.jpg','film.mp4','bridge-camera.mp4','curiosity-camera.mp4']:
        assert (DEST/'assets'/name).is_file(),name
    (DEST/'.nojekyll').write_text('',encoding='utf-8')
    files=[p for p in DEST.rglob('*') if p.is_file()]
    summary={'languages':['en','ru','uk'],'files':len(files),'bytes':sum(p.stat().st_size for p in files),'status':'validated'}
    (ROOT/'work/site-build.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps(summary));print(DEST)
if __name__=='__main__':main()
