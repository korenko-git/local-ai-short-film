from pathlib import Path
import math

ROOT = Path(__file__).resolve().parent
TITLES = ['Начало · два разрыва', 'Первое движение · плитка А', 'Второе движение · путь открыт']
NOTES = ['А: повернуть на 90° против часовой стрелки', 'Б: повернуть на 90° по часовой стрелке', 'Вода проходит весь путь и запускает колесо']

def scene(state):
    a = 'M320 280 H356 Q380 280 380 256 V220' if state == 0 else 'M320 280 H356 Q380 280 380 304 V340'
    b = 'M560 400 H596 Q620 400 620 424 V460' if state < 2 else 'M560 400 H596 Q620 400 620 376 V340'
    fixed = ['M110 280 H320', 'M380 340 V376 Q380 400 404 400 H560', 'M620 340 V304 Q620 280 644 280 H766']
    water = ('M110 280 H356 Q380 280 380 256 V224' if state == 0 else
             'M110 280 H356 Q380 280 380 304 V376 Q380 400 404 400 H596 Q620 400 620 424 V456' if state == 1 else
             'M110 280 H356 Q380 280 380 304 V376 Q380 400 404 400 H596 Q620 400 620 376 V304 Q620 280 644 280 H766')
    s = ['<rect width="1000" height="760" rx="24" fill="#f4f0e5"/>',
         '<text x="50" y="57" font-family="Segoe UI, sans-serif" font-size="27" font-weight="700" fill="#243e3d">'+TITLES[state]+'</text>',
         '<text x="50" y="91" font-family="Segoe UI, sans-serif" font-size="17" fill="#66716b">Сцена 08 · схема каналов · вид сверху</text>',
         '<rect x="110" y="160" width="690" height="440" rx="24" fill="#aca58f" stroke="#8d8775" stroke-width="4"/>']
    for row in range(3):
        for col in range(5):
            x,y=200+col*120,220+row*120
            s.append(f'<rect x="{x}" y="{y}" width="120" height="120" rx="5" fill="{["#c6c0a9","#cec8b2","#c0bba4"][(row+col)%3]}" stroke="#a6a08b" stroke-width="2"/>')
    for x,y in [(320,220),(560,340)]:
        s.append(f'<circle cx="{x+60}" cy="{y+60}" r="57" fill="#e1d2aa" stroke="#b78643" stroke-width="4"/>')
    for p in fixed+[a,b]:
        s.append(f'<path d="{p}" fill="none" stroke="#847b63" stroke-width="38" stroke-linejoin="round"/>')
        s.append(f'<path d="{p}" fill="none" stroke="#5d655f" stroke-width="27" stroke-linejoin="round"/>')
    s.append(f'<path d="{water}" fill="none" stroke="#299ebd" stroke-width="25" stroke-linejoin="round"/>')
    s.append(f'<path d="{water}" fill="none" stroke="#a2e4e6" stroke-width="7" stroke-linejoin="round" opacity=".8"/>')
    # Source pool, wheel and gate remain at identical coordinates in every state.
    s += ['<ellipse cx="111" cy="280" rx="42" ry="43" fill="#299ebd" stroke="#7acdd6" stroke-width="7"/>',
          '<text x="57" y="354" font-family="Segoe UI" font-size="17" fill="#426363">РУЧЕЙ</text>',
          '<path d="M812 280 V195 H870" fill="none" stroke="#8c7857" stroke-width="9" stroke-dasharray="7 5"/>',
          '<rect x="850" y="154" width="104" height="66" rx="6" fill="#8c8776" stroke="#605f54" stroke-width="5"/>']
    if state < 2:
        s += ['<rect x="862" y="165" width="79" height="45" fill="#615e50"/>', '<path d="M901 166 V210" stroke="#a9a086" stroke-width="3"/>']
    else:
        s += ['<rect x="862" y="165" width="79" height="45" fill="#304943"/>', '<path d="M862 165 L850 158 V214 L862 210 M941 165 L953 158 V214 L941 210" fill="#b9b198" stroke="#605f54" stroke-width="3"/>']
    s += ['<text x="902" y="139" text-anchor="middle" font-family="Segoe UI" font-size="16" fill="#52605a">ДВЕРЬ</text>',
          '<circle cx="812" cy="280" r="44" fill="#ab8151" stroke="#654e35" stroke-width="7"/>']
    for i in range(8):
        ang = (i*45+(12 if state==2 else 0))*math.pi/180
        x,y=812+38*math.cos(ang),280+38*math.sin(ang)
        s.append(f'<path d="M812 280 L{x:.2f} {y:.2f}" stroke="#5b4932" stroke-width="7"/>')
    s += ['<circle cx="812" cy="280" r="10" fill="#e2c387"/>', '<text x="812" y="354" text-anchor="middle" font-family="Segoe UI" font-size="17" fill="#52605a">КОЛЕСО</text>']
    for label,x,y in [('А',380,280),('Б',620,400)]:
        s.append(f'<circle cx="{x+41}" cy="{y+41}" r="13" fill="#b78643"/><text x="{x+41}" y="{y+46}" text-anchor="middle" font-family="Segoe UI" font-size="14" font-weight="700" fill="white">{label}</text>')
    if state < 2:
        x,y = (380,224) if state==0 else (620,456)
        s.append(f'<path d="M{x-19} {y} H{x+19}" stroke="#b4593f" stroke-width="6"/>')
        s.append(f'<path d="M{x-10} {y-9} l-7 -10 M{x+10} {y-9} l7 -10" stroke="#a2e4e6" stroke-width="4"/>')
    s += [f'<text x="50" y="658" font-family="Segoe UI" font-size="22" font-weight="600" fill="#243e3d">{NOTES[state]}</text>',
          '<text x="50" y="696" font-family="Segoe UI" font-size="16" fill="#677269">Золото — поворотные плитки · голубой — вода · тёмный — сухой канал</text>',
          '<text x="50" y="725" font-family="Segoe UI" font-size="15" fill="#7c8176">Подписи и цветовые отметки служебные; в кадр фильма не переносить.</text>']
    return ''.join(s)

names=['channels-01-start','channels-02-first-move','channels-03-solved']
for i,name in enumerate(names):
    (ROOT/(name+'.svg')).write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="760" viewBox="0 0 1000 760">'+scene(i)+'</svg>',encoding='utf-8')
overview='<svg xmlns="http://www.w3.org/2000/svg" width="1500" height="380" viewBox="0 0 3000 760">'+''.join(f'<g transform="translate({i*1000} 0)">{scene(i)}</g>' for i in range(3))+'</svg>'
(ROOT/'channels-overview.svg').write_text(overview,encoding='utf-8')
print('Created three SVG states and overview in', ROOT)
