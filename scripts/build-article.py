"""Generate three equivalent buildless pages. Python standard library only."""
import argparse,base64,html,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'docs/article'
FILES={'en':'index.html','ru':'ru.html','uk':'uk.html'}
TIMES=[0,8,15.292,38.583,46.583,56.708,73.458,103.667,153.833,182.667,210.167,233]
LABELS=['00:00','00:08','00:15','00:39','00:47','00:57','01:13','01:44','02:34','03:03','03:30','03:53']
def esc(v):return html.escape(str(v),quote=True)
TIMECODE=re.compile(r'(?<![\w:])([0-5]?\d):([0-5]\d)(?:[,.](\d+))?(?:[–—-][0-5]?\d:[0-5]\d(?:[,.]\d+)?)?(?![\d:])')

def timecoded(value,label):
    value=str(value);parts=[];end=0
    for match in TIMECODE.finditer(value):
        seconds=int(match[1])*60+int(match[2])
        if match[3]:seconds+=float('0.'+match[3])
        stamp=match[0]
        parts.append(esc(value[end:match.start()]))
        parts.append(f'<a class="timecode" href="#film" data-time="{seconds:g}" aria-label="{esc(label)}: {esc(stamp)}">{esc(stamp)}</a>')
        end=match.end()
    parts.append(esc(value[end:]))
    return ''.join(parts)

def render(d):
    ui=d['ui'];lang=d['lang']
    def text(value):return timecoded(value,ui['seek'])
    introduction=f'<p>{esc(d["introduction"])}</p>' if d.get('introduction') else ''
    def block(b):
        k=b[0]
        if k in ('p','h3'):return f'<{k}>{text(b[1])}</{k}>'
        if k=='note':return f'<p class="note">{text(b[1])}</p>'
        if k=='quote':return f'<blockquote><p>{text(b[1])}</p></blockquote>'
        if k=='code':return f'<pre><code>{esc(b[1])}</code></pre>'
        if k=='figure':
            width,height=b[4:6] if len(b)>=6 else (1344,768)
            return f'<figure><img src="assets/{esc(b[1])}.jpg" alt="{esc(b[3])}" width="{width}" height="{height}" loading="lazy"><figcaption>{text(b[2])}</figcaption></figure>'
        if k=='gallery':return '<div class="artifact-gallery">'+''.join(block(['figure',*item]) for item in b[1])+'</div>'
        if k=='clip':return f'<figure class="clip-example"><video controls playsinline preload="none" poster="assets/{esc(b[3])}.jpg" aria-label="{esc(b[2])}"><source src="assets/{esc(b[1])}.mp4" type="video/mp4"></video><figcaption>{text(b[2])}</figcaption></figure>'
        if k=='table':
            head=''.join(f'<th scope="col">{esc(c)}</th>' for c in b[2]);rows=''.join('<tr>'+''.join(f'<td>{text(c)}</td>' for c in r)+'</tr>' for r in b[3])
            return f'<div class="table-wrap"><table><caption>{esc(b[1])}</caption><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
        if k=='film':
            chapters=''.join(f'<li><button data-time="{t}">{label}</button> {esc(n)}</li>' for t,label,n in zip(TIMES,LABELS,ui['chapterNames']))
            return f'<video id="main-film" controls playsinline preload="metadata" poster="assets/cover.jpg" aria-label="{esc(ui["filmLabel"])}"><source src="assets/film.mp4" type="video/mp4"></video><p class="video-caption">{esc(ui["filmLabel"])} · <a href="assets/film.mp4">{esc(ui["openFilm"])} ↗</a></p><details><summary>{esc(ui["chapters"])}</summary><ol class="chapters">{chapters}</ol></details>'
        if k=='sources':return f'<details><summary>{esc(b[1])}</summary><p>{esc(b[2])}</p></details>'
        if k=='credits':return f'<details><summary>{esc(ui["sources"])}</summary><p>{esc(b[1])}</p><ul><li><a href="https://incompetech.filmmusic.io/song/8287-adventures-in-adventureland">Kevin MacLeod · Adventures in Adventureland</a> · <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a></li><li><a href="https://bigsoundbank.com/">Joseph Sardin · BigSoundBank</a></li><li><a href="https://github.com/FlashML-org/FreeVideo">FreeVideo / MiniMax H3</a></li><li><a href="https://github.com/PedroMarinhoDev/ComfyUI-Drama3">ComfyUI-Drama3</a></li></ul></details>'
        raise ValueError(k)
    sections=[];nav=[]
    for i,s in enumerate(d['sections'],1):
        sid=s['id'];nav.append(f'<a href="#{sid}">{i:02} / {esc(s["nav"])}</a>')
        sections.append(f'<section id="{sid}"><p class="section-no">{i:02} / {esc(s["nav"])}</p><h2>{esc(s["title"])}</h2>'+''.join(block(b) for b in s['blocks'])+'</section>')
    languages=''.join(f'<a href="{f}" lang="{c}" hreflang="{c}" data-language="{c}"'+(' aria-current="page"' if c==lang else '')+f'>{label}</a>' for c,f,label in [('en','index.html','EN'),('ru','ru.html','RU'),('uk','uk.html','UK')])
    alt=''.join(f'<link rel="alternate" hreflang="{c}" href="{f}">' for c,f in FILES.items())
    stats=''.join(f'<div><b>{esc(n)}</b><span>{esc(label)}</span></div>' for n,label in d['facts'])
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="{esc(d['subtitle'])}"><meta property="og:type" content="article"><meta property="og:title" content="{esc(d['title'])}"><meta property="og:description" content="{esc(d['subtitle'])}"><meta name="author" content="Dmytro Korenko"><title>{esc(d['title'])}</title>{alt}<link rel="stylesheet" href="style.css"></head>
<body data-enlarge="{esc(ui['enlarge'])}"><div class="progress" aria-hidden="true"></div><header class="masthead"><a href="#title">{esc(d['masthead'])}</a><nav class="languages" aria-label="{esc(ui['language'])}">{languages}</nav><span>{esc(d['date'])}</span></header>
<main><section class="hero" aria-labelledby="title"><img src="assets/hero-4k.webp" alt="{esc(d['eyebrow'])}" width="3840" height="2194" fetchpriority="high"><div class="hero-copy"><p class="eyebrow">{esc(d['eyebrow'])}</p><h1 id="title">{esc(d['title'])}</h1><p>{esc(d['subtitle'])}</p><a class="hero-link" href="#film">{esc(d['watch'])} ↗</a></div></section>
<div class="intro"><p class="eyebrow">{esc(d['byline'])}</p><p class="lead">{esc(d['lead'])}</p>{introduction}<div class="facts">{stats}</div></div><div class="layout"><nav class="contents" aria-label="{esc(d['contents'])}"><p>{esc(d['contents'])}</p>{''.join(nav)}</nav><article>{''.join(sections)}</article></div></main>
<footer><p>{esc(d['title'])}</p><span>Dmytro Korenko · 2026</span><a href="#title">{esc(ui['back'])} ↑</a></footer><dialog class="lightbox" aria-label="{esc(ui['enlarge'])}"><button class="close" aria-label="{esc(ui['close'])}">{esc(ui['close'])} ×</button><img alt=""><p></p></dialog><script src="script.js"></script></body></html>'''
def main():
    p=argparse.ArgumentParser();p.add_argument('--offline',action='store_true');args=p.parse_args()
    items=[json.loads((SITE/'content'/f'{c}.json').read_text(encoding='utf-8')) for c in FILES]
    expected=[s['id'] for s in items[0]['sections']]
    for d in items:
        assert [s['id'] for s in d['sections']]==expected
        assert len(d['ui']['chapterNames'])==len(TIMES)
        text=render(d);(SITE/FILES[d['lang']]).write_text(text,encoding='utf-8')
        if args.offline:
            text=text.replace('<link rel="stylesheet" href="style.css">','<style>'+(SITE/'style.css').read_text(encoding='utf-8')+'</style>')
            text=text.replace('<script src="script.js"></script>','<script>'+(SITE/'script.js').read_text(encoding='utf-8')+'</script>')
            text=re.sub(r'(src|poster)="(assets/[^\"]+\.(?:jpg|webp))"',lambda m:m[1]+'="data:image/'+('webp' if m[2].endswith('.webp') else 'jpeg')+';base64,'+base64.b64encode((SITE/m[2]).read_bytes()).decode()+'"',text)
            (SITE/f'local-short-film-{d["lang"]}.html').write_text(text,encoding='utf-8')
        print(FILES[d['lang']],len(d['sections']),'sections')
if __name__=='__main__':main()
