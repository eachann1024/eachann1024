"""《小王子》黄昏沙丘风格的共用场景层：渐变天空、太阳、星光、流云、飞鸟、沙丘。"""

PALETTE = {
    "ink": "#33465A",
    "body": "#4C5E6E",
    "muted": "#64788A",
    "quote": "#8A7B66",
    "accent": "#C4622B",
    "accentSoft": "#E0863F",
    "paper": "#FFFBF2",
    "line": "#D9C4A2",
    "sand": "#6A5B47",
    "sky": "#7D8FA0",
}

CSS = """
  .serif{font-family:Georgia,"Iowan Old Style","Palatino Linotype","Times New Roman",serif}
  .sans{font-family:ui-sans-serif,-apple-system,"Helvetica Neue",Helvetica,Arial,sans-serif}
  .mono{font-family:ui-monospace,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace}
  .cjk{font-family:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans SC",sans-serif}

  .tw{animation:tw 4.4s ease-in-out infinite}
  .a1{animation-delay:.5s}.a2{animation-delay:1s}.a3{animation-delay:1.6s}
  .a4{animation-delay:2.2s}.a5{animation-delay:2.9s}.a6{animation-delay:3.5s}
  .rise{animation:rise 9s ease-in-out infinite}
  .halo{transform-box:fill-box;transform-origin:center;animation:halo 7s ease-in-out infinite}
  .drift{animation:drift 30s linear infinite}
  .drift2{animation:drift 42s linear infinite;animation-delay:-11s}
  .birds{animation:fly 22s linear infinite}
  .flap{transform-box:fill-box;transform-origin:center;animation:flap 1.1s ease-in-out infinite}

  .cape{transform-box:fill-box;transform-origin:78% 8%;animation:cape 4.6s ease-in-out infinite}
  .scarf{transform-box:fill-box;transform-origin:4% 86%;animation:scarf 3.2s ease-in-out infinite}
  .tuft{transform-box:fill-box;transform-origin:14% 96%;animation:tuft 3.8s ease-in-out infinite}
  .tail{transform-box:fill-box;transform-origin:6% 82%;animation:tail 2.9s ease-in-out infinite}
  .ear{transform-box:fill-box;animation:ear 5.4s ease-in-out infinite}
  .nod{transform-box:fill-box;animation:nod 5.6s ease-in-out infinite}
  .bloom{transform-box:fill-box;animation:bloom 6.2s ease-in-out infinite}
  .blink{animation:blink 5.6s steps(1,end) infinite}

  .caret{animation:caret 1.1s steps(1,end) infinite}
  .typing{animation:typing 4.4s ease-in-out infinite}
  .pulse{transform-box:fill-box;transform-origin:center;animation:pulse 3s ease-in-out infinite}
  .dash{stroke-dasharray:6 8;animation:dash 6s linear infinite}
  .ride{animation:ride 7.5s ease-in-out infinite}
  .bar{transform-box:fill-box;transform-origin:center bottom;animation:bar 2.6s ease-in-out infinite}

  @keyframes tw{0%,100%{opacity:.18}50%{opacity:1}}
  @keyframes rise{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}
  @keyframes halo{0%,100%{transform:scale(1);opacity:.72}50%{transform:scale(1.07);opacity:1}}
  @keyframes drift{from{transform:translateX(-170px)}to{transform:translateX(1370px)}}
  @keyframes fly{from{transform:translate(-130px,26px)}to{transform:translate(1330px,-44px)}}
  @keyframes flap{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.42)}}
  @keyframes cape{0%,100%{transform:rotate(-4deg) skewX(0)}50%{transform:rotate(5deg) skewX(-4deg)}}
  @keyframes scarf{0%,100%{transform:rotate(-8deg)}50%{transform:rotate(10deg)}}
  @keyframes tuft{0%,100%{transform:rotate(-6deg)}50%{transform:rotate(7deg)}}
  @keyframes tail{0%,100%{transform:rotate(-8deg)}50%{transform:rotate(11deg)}}
  @keyframes ear{0%,90%,100%{transform:rotate(0)}94%{transform:rotate(-10deg)}}
  @keyframes nod{0%,100%{transform:rotate(0)}48%{transform:rotate(6deg)}}
  @keyframes bloom{0%,100%{transform:scale(1)}50%{transform:scale(1.07)}}
  @keyframes blink{0%,93%{opacity:1}94%,97%{opacity:0}98%,100%{opacity:1}}
  @keyframes caret{0%,49%{opacity:1}50%,100%{opacity:0}}
  @keyframes typing{0%{transform:scaleX(.08)}55%,100%{transform:scaleX(1)}}
  @keyframes pulse{0%,100%{opacity:.4;transform:scale(.88)}50%{opacity:1;transform:scale(1)}}
  @keyframes dash{to{stroke-dashoffset:-140}}
  @keyframes ride{0%,100%{transform:translateX(0)}50%{transform:translateX(118px)}}
  @keyframes bar{0%,100%{transform:scaleY(.45)}50%{transform:scaleY(1)}}

  @media(prefers-reduced-motion:reduce){
    .tw,.rise,.halo,.drift,.drift2,.birds,.flap,.cape,.scarf,.tuft,.tail,.ear,.nod,
    .bloom,.blink,.caret,.typing,.pulse,.dash,.ride,.bar{animation:none}
  }
"""


def defs(w, h, uid=""):
    return f"""<defs>
    <linearGradient id="dusk{uid}" x1="0" y1="0" x2="0.12" y2="1">
      <stop offset="0" stop-color="#DCEBF6"/>
      <stop offset="0.4" stop-color="#F1E6EF"/>
      <stop offset="0.7" stop-color="#FCEBDC"/>
      <stop offset="1" stop-color="#FDF4E4"/>
    </linearGradient>
    <radialGradient id="sun{uid}" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#FFF6DE"/>
      <stop offset="0.6" stop-color="#FBD98E"/>
      <stop offset="1" stop-color="#F3BE65"/>
    </radialGradient>
    <radialGradient id="sunHalo{uid}" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0.38" stop-color="#FBD98E" stop-opacity=".5"/>
      <stop offset="1" stop-color="#FBD98E" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="hillFar{uid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#CBDCEB"/><stop offset="1" stop-color="#DEE9F2"/>
    </linearGradient>
    <linearGradient id="hillMid{uid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#F3DAB7"/><stop offset="1" stop-color="#EDC99A"/>
    </linearGradient>
    <linearGradient id="hillNear{uid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#E4B786"/><stop offset="1" stop-color="#D7A471"/>
    </linearGradient>
    <linearGradient id="card{uid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FFFDF7"/><stop offset="1" stop-color="#FDF3E3"/>
    </linearGradient>
    <filter id="soft{uid}" x="-45%" y="-45%" width="190%" height="190%"><feGaussianBlur stdDeviation="12"/></filter>
    <filter id="drop{uid}" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#B98A5C" flood-opacity=".22"/>
    </filter>
    <filter id="paper{uid}" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="4" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
    <clipPath id="frame{uid}"><rect x="0" y="0" width="{w}" height="{h}" rx="20"/></clipPath>
  </defs>"""


def sky(w, h, sun=None, uid=""):
    out = [f'<rect width="{w}" height="{h}" fill="url(#dusk{uid})"/>']
    if sun:
        cx, cy, r = sun
        out.append(
            f'<g transform="translate({cx} {cy})">'
            f'<circle class="halo" r="{r * 1.95:.0f}" fill="url(#sunHalo{uid})"/>'
            f'<circle class="rise" r="{r}" fill="url(#sun{uid})"/></g>'
        )
    return "\n    ".join(out)


def stars(points, crosses):
    out = ['<g fill="#C79B52">']
    for i, (x, y, r) in enumerate(points):
        out.append(f'<circle class="tw a{i % 6}" cx="{x}" cy="{y}" r="{r}"/>')
    out.append("</g>")
    out.append('<g stroke="#C79B52" stroke-width="1.3" stroke-linecap="round" fill="none">')
    for i, (x, y, s, full) in enumerate(crosses):
        d = f"M0-{s}V{s}M-{s} 0H{s}"
        if full:
            o = round(s * 0.68, 1)
            d += f"M-{o}-{o} {o} {o}M{o}-{o}-{o} {o}"
        out.append(f'<g class="tw a{(i + 2) % 6}" transform="translate({x} {y})"><path d="{d}"/></g>')
    out.append("</g>")
    return "\n    ".join(out)


def clouds(y1, y2):
    return f"""<g fill="#FFFFFF">
      <g class="drift" opacity=".72"><ellipse cx="0" cy="{y1}" rx="64" ry="15"/><ellipse cx="42" cy="{y1 - 7}" rx="44" ry="19"/><ellipse cx="-40" cy="{y1 + 4}" rx="34" ry="11"/></g>
      <g class="drift2" opacity=".5"><ellipse cx="0" cy="{y2}" rx="52" ry="12"/><ellipse cx="35" cy="{y2 - 5}" rx="35" ry="15"/></g>
    </g>"""


def birds(y=0, opacity=".5"):
    return f"""<g class="birds" transform="translate(0 {y})" stroke="#8C7A5C" stroke-width="1.6" fill="none" stroke-linecap="round" opacity="{opacity}">
      <path class="flap" d="M0 0q7-6 13 0q6-6 13 0"/>
      <path class="flap" style="animation-delay:.3s" transform="translate(36 17)" d="M0 0q6-5 11 0q5-5 11 0"/>
      <path class="flap" style="animation-delay:.6s" transform="translate(-28 25)" d="M0 0q5-4 9 0q4-4 9 0"/>
    </g>"""


def hills(h, far, mid, near, uid=""):
    return f"""<path d="M0 {far}c152-44 252 8 374-18s214-62 352-34 290 70 474 34v{h}H0Z" fill="url(#hillFar{uid})" opacity=".92"/>
    <path d="M0 {mid}c168-52 286 16 420-10s240-50 388-16 266 58 392 26v{h}H0Z" fill="url(#hillMid{uid})"/>
    <path d="M0 {near}c180-40 330 18 486-4s268-36 420-8 196 28 294 14v{h}H0Z" fill="url(#hillNear{uid})"/>"""


def grass(items):
    d = "".join(f"M{x} {y}c4-12 10-16 14-{s}" for x, y, s in items)
    return f'<g stroke="#C08D52" stroke-width="1.6" stroke-linecap="round" opacity=".45" fill="none"><path d="{d}"/></g>'


def grain(w, h, uid="", o=".05"):
    return f'<rect width="{w}" height="{h}" filter="url(#paper{uid})" opacity="{o}"/>'
