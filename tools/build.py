#!/usr/bin/env python3
"""生成 README 的《小王子》黄昏沙丘风格动画 SVG。

    python3 tools/build.py          # 写入 assets/
    python3 tools/build.py --png    # 额外导出预览 PNG（需 Chrome）
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import figures as F  # noqa: E402
import scene as S  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
P = S.PALETTE


def svg(w, h, body, uid="", label=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}" preserveAspectRatio="xMidYMid meet">
  {S.defs(w, h, uid)}
  <style>{S.CSS}</style>
  <g clip-path="url(#frame{uid})">
{body}
    {S.grain(w, h, uid)}
  </g>
</svg>
"""


# ---------------------------------------------------------------- hero
def hero():
    w, h, u = 1200, 620, "H"
    body = f"""    {S.sky(w, h, sun=(900, 286, 106), uid=u)}
    {S.stars([(150,120,2.1),(330,76,1.8),(1096,118,2.2),(610,150,1.7),(468,196,1.6),(1012,74,1.8),(214,252,1.5)],
             [(240,196,9,True),(700,92,7,False),(1148,206,8,True),(396,120,6,False)])}
    {S.clouds(138, 236)}
    {S.birds(0)}
    {S.hills(h, 452, 508, 566, uid=u)}

    <!-- 小王子与狐狸站在沙丘脊上 -->
    <g transform="translate(806 554)">{F.prince(1.3)}</g>
    <g transform="translate(906 560)">{F.fox(1.2, delay=0.4)}</g>
    <g transform="translate(716 558)">{F.rose(0.82, delay=1.1)}</g>

    {S.grass([(118,598,24),(140,600,20),(1046,596,24),(1068,598,20),(330,604,24)])}

    <text class="mono" x="56" y="58" font-size="11.5" letter-spacing="3.4" fill="{P['sky']}">E / 1024</text>
    <text class="mono" x="1144" y="58" font-size="11.5" letter-spacing="3.4" text-anchor="end" fill="{P['sky']}">INDEPENDENT SOFTWARE</text>

    <text class="serif" x="56" y="256" font-size="108" font-weight="700" letter-spacing="-1.5" fill="{P['ink']}">Eachann</text>
    <path d="M60 288h132" stroke="{P['accentSoft']}" stroke-width="3" stroke-linecap="round"/>
    <text class="sans" x="58" y="336" font-size="23" font-weight="600" fill="{P['body']}">Tools for a more considered workflow.</text>
    <text class="cjk" x="58" y="380" font-size="16" fill="{P['quote']}">“只有用心才能看得清。”</text>
    <text class="mono" x="58" y="424" font-size="11" letter-spacing="2.4" fill="{P['muted']}">DESKTOP APPS · PI EXTENSIONS · LOCAL FIRST</text>

    <g class="mono" font-size="12" letter-spacing="2.6" fill="{P['sand']}">
      <text x="56" y="588"><tspan fill="{P['accent']}" font-weight="700">02</tspan> FLAGSHIP</text>
      <text x="600" y="588" text-anchor="middle"><tspan fill="{P['accent']}" font-weight="700">03</tspan> PI PACKAGES</text>
      <text x="1144" y="588" text-anchor="end"><tspan fill="{P['accent']}" font-weight="700">12</tspan> PROJECTS</text>
    </g>"""
    return svg(w, h, body, u, "Eachann — tools for a more considered workflow")


# ---------------------------------------------------------------- notes
def notes():
    w, h, u = 1200, 420, "N"
    lines = "".join(
        f'<rect class="typing" style="transform-box:fill-box;transform-origin:left center;animation-delay:{d}s" '
        f'x="26" y="{y}" width="{wd}" height="5" rx="2.5" fill="#B9CBD9"/>'
        for y, wd, d in ((70, 196, 0.2), (86, 158, 0.6), (102, 180, 1.0), (118, 120, 1.4))
    )
    body = f"""    {S.sky(w, h, sun=(1028, 150, 64), uid=u)}
    {S.stars([(120,74,1.8),(340,54,1.6),(900,62,1.8),(612,96,1.5),(232,128,1.4)],
             [(176,112,7,True),(764,56,6,False),(1150,120,7,True)])}
    {S.clouds(92, 162)}
    {S.hills(h, 282, 322, 360, uid=u)}

    <!-- 纸张：层叠的笔记卡片 -->
    <g transform="translate(636 92)" filter="url(#drop{u})">
      <g transform="rotate(-5)" opacity=".55">
        <rect x="18" y="10" width="250" height="160" rx="12" fill="url(#card{u})" stroke="{P['line']}"/>
      </g>
      <g transform="translate(36 -4) rotate(3)" opacity=".8">
        <rect x="18" y="10" width="250" height="160" rx="12" fill="url(#card{u})" stroke="{P['line']}"/>
      </g>
      <g transform="translate(74 6)">
        <rect width="264" height="168" rx="12" fill="url(#card{u})" stroke="{P['line']}"/>
        <path d="M0 34h264" stroke="{P['line']}" opacity=".7"/>
        <g fill="{P['accentSoft']}" opacity=".85"><circle cx="20" cy="18" r="3.4"/><circle cx="33" cy="18" r="3.4" fill="#E6B45A"/><circle cx="46" cy="18" r="3.4" fill="#8FAE7F"/></g>
        <text class="mono" x="244" y="22" text-anchor="end" font-size="8.5" letter-spacing="1.8" fill="{P['muted']}">MARKDOWN</text>
        <rect x="26" y="50" width="96" height="7" rx="3.5" fill="{P['accentSoft']}" opacity=".75"/>
        {lines}
        <rect class="caret" x="150" y="115" width="2" height="11" fill="{P['accent']}"/>
        <g stroke="{P['line']}" fill="none"><rect x="26" y="136" width="60" height="18" rx="9"/><rect x="94" y="136" width="44" height="18" rx="9"/></g>
        <text class="mono" x="56" y="148" text-anchor="middle" font-size="7.5" letter-spacing="1.4" fill="{P['muted']}">CAPTURE</text>
        <text class="mono" x="116" y="148" text-anchor="middle" font-size="7.5" letter-spacing="1.4" fill="{P['muted']}">AI</text>
      </g>
    </g>

    <!-- 小王子与羊 -->
    <g transform="translate(566 378)">{F.prince(1.06)}</g>
    <g transform="translate(486 384)">{F.sheep(0.9, delay=0.7)}</g>
    <g transform="translate(662 384)">{F.rose(0.72, delay=1.2)}</g>
    {S.grass([(150,402,20),(170,404,16),(1058,400,20),(1080,402,16)])}

    <text class="mono" x="56" y="48" font-size="11" letter-spacing="3.2" fill="{P['sky']}">01 / A SPACE FOR THOUGHT</text>
    <text class="serif" x="56" y="166" font-size="62" font-weight="700" letter-spacing="-1" fill="{P['ink']}">Goose Note</text>
    <path d="M58 190h92" stroke="{P['accentSoft']}" stroke-width="3" stroke-linecap="round"/>
    <text class="sans" x="58" y="228" font-size="19" font-weight="600" fill="{P['body']}">Leave room for the next idea.</text>
    <text class="mono" x="58" y="262" font-size="10.5" letter-spacing="2.4" fill="{P['muted']}">LOCAL MARKDOWN · QUICK CAPTURE · AI</text>"""
    return svg(w, h, body, u, "Goose Note — local markdown, quick capture, AI")


# ---------------------------------------------------------------- herdr
def herdr():
    w, h, u = 1200, 420, "R"

    def pane(x, y, wd, hd, title, active=False):
        stroke = P["accentSoft"] if active else P["line"]
        rows = "".join(
            f'<rect x="16" y="{ry}" width="{rw}" height="4" rx="2" fill="#B9CBD9" opacity=".8"/>'
            for ry, rw in ((46, int(wd * 0.52)), (58, int(wd * 0.38)), (70, int(wd * 0.46)))
        )
        return f"""<g transform="translate({x} {y})" filter="url(#drop{u})">
        <rect width="{wd}" height="{hd}" rx="11" fill="url(#card{u})" stroke="{stroke}"/>
        <path d="M0 26h{wd}" stroke="{P['line']}" opacity=".7"/>
        <circle class="pulse" cx="{wd - 16}" cy="13" r="3.4" fill="{P['accentSoft'] if active else '#8FAE7F'}"/>
        <text class="mono" x="14" y="17" font-size="8.5" letter-spacing="1.8" fill="{P['muted']}">{title}</text>
        <text class="mono" x="16" y="38" font-size="10" fill="{P['accent']}">›</text>
        <rect class="caret" x="26" y="30" width="16" height="2" fill="{P['accent']}"/>
        {rows}
      </g>"""

    body = f"""    {S.sky(w, h, sun=(506, 68, 44), uid=u)}
    {S.stars([(128,70,1.8),(352,52,1.6),(884,58,1.8),(606,104,1.5),(250,136,1.4)],
             [(196,106,7,True),(748,62,6,False),(1152,112,7,True)])}
    {S.clouds(96, 170)}
    {S.birds(-18, ".42")}
    {S.hills(h, 282, 322, 360, uid=u)}

    {pane(596, 92, 182, 126, "LOCAL")}
    {pane(790, 74, 196, 150, "REMOTE", active=True)}
    {pane(998, 96, 170, 120, "WORKSPACE")}
    <g stroke="{P['accentSoft']}" fill="none" opacity=".7">
      <path class="dash" d="M778 150h12"/><path class="dash" d="M986 150h12"/>
    </g>

    <g transform="translate(566 378)">{F.prince(1.06, flip=True)}</g>
    <g transform="translate(644 384)">{F.fox(0.96, delay=0.6)}</g>
    {S.grass([(158,400,20),(180,402,16),(1046,402,20),(1068,404,16)])}

    <text class="mono" x="56" y="48" font-size="11" letter-spacing="3.2" fill="{P['sky']}">02 / NATIVE WORKSPACE</text>
    <text class="serif" x="56" y="166" font-size="62" font-weight="700" letter-spacing="-1" fill="{P['ink']}">Goose Herdr</text>
    <path d="M58 190h92" stroke="{P['accentSoft']}" stroke-width="3" stroke-linecap="round"/>
    <text class="sans" x="58" y="228" font-size="19" font-weight="600" fill="{P['body']}">A place for every session.</text>
    <text class="mono" x="58" y="262" font-size="10.5" letter-spacing="2.4" fill="{P['muted']}">RUST · GPUI · SSH · SPLIT PANES</text>"""
    return svg(w, h, body, u, "Goose Herdr — sessions, SSH, split terminals")


# ---------------------------------------------------------------- pi
def pi():
    w, h, u = 1200, 420, "P"

    def card(x, no, name, sub, art):
        return f"""<g transform="translate({x} 152)" filter="url(#drop{u})">
        <rect width="336" height="156" rx="14" fill="url(#card{u})" stroke="{P['line']}"/>
        <text class="mono" x="22" y="30" font-size="9.5" letter-spacing="2.4" fill="{P['accent']}">{no}</text>
        <text class="serif" x="22" y="62" font-size="25" font-weight="700" fill="{P['ink']}">{name}</text>
        <text class="mono" x="22" y="84" font-size="9.5" letter-spacing="1.8" fill="{P['muted']}">{sub}</text>
        <path d="M22 98h292" stroke="{P['line']}" opacity=".8"/>
        {art}
      </g>"""

    route = f"""<g transform="translate(22 110)">
          <path d="M0 14h292" stroke="{P['line']}"/>
          <path class="dash" d="M0 14h292" stroke="{P['accentSoft']}" opacity=".8" fill="none"/>
          <g class="ride"><circle cx="18" cy="14" r="6" fill="{P['accentSoft']}"/><circle cx="18" cy="14" r="2.4" fill="#FFF6E8"/></g>
          <g fill="#FFFDF7" stroke="{P['line']}"><circle cx="18" cy="14" r="4"/><circle cx="155" cy="14" r="4"/><circle cx="292" cy="14" r="4"/></g>
        </g>"""
    reply = "".join(
        f'<rect class="typing" style="transform-box:fill-box;transform-origin:left center;animation-delay:{d}s" '
        f'x="22" y="{y}" width="{wd}" height="6" rx="3" fill="{c}"/>'
        for y, wd, d, c in ((112, 250, 0.1, "#B9CBD9"), (126, 196, 0.5, "#B9CBD9"), (140, 142, 0.9, P["accentSoft"]))
    )
    bars = "".join(
        f'<rect class="bar" style="animation-delay:{i * 0.12:.2f}s" x="{22 + i * 17}" y="110" width="7" height="34" rx="3.5" '
        f'fill="{P["accentSoft"] if i % 3 == 0 else "#B9CBD9"}" opacity=".9"/>'
        for i in range(17)
    )

    body = f"""    {S.sky(w, h, sun=(602, 78, 46), uid=u)}
    {S.stars([(140,64,1.8),(362,48,1.6),(878,52,1.7),(760,96,1.5)],
             [(214,96,7,True),(698,46,6,False),(1156,104,7,True)])}
    {S.clouds(74, 128)}
    {S.hills(h, 300, 336, 368, uid=u)}

    {card(24, "01", "Jev Route", "THE RIGHT MODEL FOR THE TASK", route)}
    {card(432, "02", "Jev Reply", "LESS NOISE, MORE CLARITY", reply)}
    {card(840, "03", "Mini Mode", "LESS NOISE, MORE FOCUS", bars)}

    <g transform="translate(170 396)">{F.sheep(0.88, delay=0.3)}</g>
    <g transform="translate(1036 400)">{F.fox(0.84, delay=1.2)}</g>
    {S.grass([(268,404,18),(286,406,14),(922,404,18),(940,406,14)])}

    <text class="mono" x="56" y="48" font-size="11" letter-spacing="3.2" fill="{P['sky']}">03 / THE PI COLLECTION</text>
    <text class="mono" x="1144" y="48" text-anchor="end" font-size="11" letter-spacing="2.2" fill="{P['muted']}">3 PACKAGES · 10K+ DOWNLOADS</text>
    <text class="serif" x="56" y="112" font-size="48" font-weight="700" letter-spacing="-1" fill="{P['ink']}">Extensions for Pi</text>"""
    return svg(w, h, body, u, "The Pi collection — 3 packages, 10K+ downloads")


TARGETS = {"hero": hero, "notes": notes, "herdr": herdr, "pi": pi}


def main():
    ASSETS.mkdir(exist_ok=True)
    for name, fn in TARGETS.items():
        out = ASSETS / f"{name}.svg"
        out.write_text(fn(), encoding="utf-8")
        print(f"{out.relative_to(ROOT)}  {out.stat().st_size / 1024:.1f}KB")
    if "--png" in sys.argv:
        for name in TARGETS:
            src = ASSETS / f"{name}.svg"
            size = "1200,620" if name == "hero" else "1200,420"
            subprocess.run(
                [CHROME, "--headless", "--disable-gpu", f"--screenshot=/tmp/{name}.png",
                 f"--window-size={size}", "--hide-scrollbars", f"file://{src}"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False,
            )
            print(f"/tmp/{name}.png")


if __name__ == "__main__":
    main()
