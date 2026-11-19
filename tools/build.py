#!/usr/bin/env python3
"""Generate Architectural Ma animated SVG plates for eachann1024/README.md.

    python3 tools/build.py
"""
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ICONS = Path(__file__).resolve().parent / "icons"

P = {
    "plaster": "#f3f1eb",
    "paper": "#faf9f5",
    "stone": "#eae6dc",
    "stoneDeep": "#e1dcd0",
    "border": "#dcd6c8",
    "rule": "#cfc8ba",
    "bronze": "#5e5446",
    "ink": "#191b20",
    "body": "#4a463f",
    "muted": "#676258",
    "iris": "#3b69c8",
    "irisSoft": "#e3eaf8",
    "irisInk": "#244899",
}

FONTS = """
  .serif{font-family:"Iowan Old Style","Palatino Linotype",Georgia,"Songti SC","STSong","Noto Serif SC",serif}
  .sans{font-family:"PingFang SC","Hiragino Sans GB",-apple-system,BlinkMacSystemFont,"Helvetica Neue","Microsoft YaHei",sans-serif}
  .mono{font-family:ui-monospace,"SF Mono","JetBrains Mono",Menlo,Consolas,monospace}
"""


def icon_b64(name: str) -> str:
    data = (ICONS / f"{name}.png").read_bytes()
    return "data:image/png;base64," + base64.b64encode(data).decode("ascii")


def arrow_ne(cx: float, cy: float, color: str = P["muted"], scale: float = 1.0) -> str:
    return (
        f'<g transform="translate({cx} {cy}) scale({scale})" '
        f'fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
        f'<path d="M-5 5 L5 -5 M-2 -5 H5 V2"/></g>'
    )


def embedded_icon(name: str, x: float, y: float, size: float, rx: float, uid: str) -> str:
    b64 = icon_b64(name)
    clip_id = f"ic{uid}"
    return (
        f'<defs><clipPath id="{clip_id}">'
        f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{rx}"/>'
        f'</clipPath></defs>'
        f'<image href="{b64}" x="{x}" y="{y}" width="{size}" height="{size}" '
        f'clip-path="url(#{clip_id})" preserveAspectRatio="xMidYMid slice"/>'
        f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{rx}" '
        f'fill="none" stroke="{P["border"]}" stroke-width="1"/>'
    )


def frame(w: int, h: int, uid: str, label: str, css: str, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}" preserveAspectRatio="xMidYMid meet">
  <defs>
    <clipPath id="fr{uid}"><rect x="0" y="0" width="{w}" height="{h}" rx="18"/></clipPath>
  </defs>
  <style>
{FONTS}{css}
  @media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
  </style>
  <g clip-path="url(#fr{uid})">
    <rect width="{w}" height="{h}" fill="{P['plaster']}"/>
{body}
  </g>
  <rect x="0.75" y="0.75" width="{w - 1.5}" height="{h - 1.5}" rx="17.25" fill="none" stroke="{P['border']}" stroke-width="1.5"/>
</svg>
"""


# ------------------------------------------------------------------ hero
def hero() -> str:
    css = """
  .ma-slab{animation:ma-slab 10s cubic-bezier(.37,0,.63,1) infinite}
  .ma-veil{animation:ma-veil 10s cubic-bezier(.37,0,.63,1) infinite}
  .ma-iris{transform-origin:968px 220px;animation:ma-iris 10s cubic-bezier(.37,0,.63,1) infinite}
  .ma-horizon{transform-origin:536px 268px;animation:ma-horizon 10s cubic-bezier(.37,0,.63,1) infinite}
  @keyframes ma-slab{0%,100%{transform:translate(0,0)}50%{transform:translate(-18px,-8px)}}
  @keyframes ma-veil{0%,100%{transform:translate(0,0)}50%{transform:translate(14px,10px)}}
  @keyframes ma-iris{0%,100%{transform:scale(1) translate(0,0);opacity:.92}50%{transform:scale(1.12) translate(-8px,-6px);opacity:1}}
  @keyframes ma-horizon{0%,100%{transform:scaleX(.8);opacity:.78}50%{transform:scaleX(1);opacity:1}}
"""
    body = f"""    <line class="ma-horizon" x1="536" y1="268" x2="1126" y2="268" stroke="#c4bdb0" stroke-width="1.5"/>

    <g class="ma-slab">
      <rect x="742" y="106" width="176" height="198" rx="4" fill="{P['ink']}"/>
      <rect x="770" y="142" width="76" height="6" rx="3" fill="{P['plaster']}" opacity=".88"/>
      <rect x="770" y="162" width="114" height="5" rx="2.5" fill="#6f7582"/>
      <rect x="770" y="178" width="90" height="5" rx="2.5" fill="#505561"/>
    </g>

    <g class="ma-veil">
      <rect x="878" y="76" width="178" height="150" rx="4" fill="{P['paper']}" fill-opacity=".93" stroke="{P['border']}" stroke-width="1.5"/>
      <line x1="904" y1="120" x2="1026" y2="120" stroke="#c5beb0" stroke-width="1.5"/>
      <line x1="904" y1="142" x2="996" y2="142" stroke="#d9d3c7" stroke-width="1.5"/>
      <line x1="904" y1="164" x2="1012" y2="164" stroke="#d9d3c7" stroke-width="1.5"/>
    </g>

    <circle class="ma-iris" cx="968" cy="220" r="24" fill="{P['iris']}"/>
    <rect x="714" y="320" width="236" height="5" rx="2.5" fill="{P['bronze']}"/>

    <text class="serif" x="68" y="298" font-size="94" font-weight="700" letter-spacing="-2" fill="{P['ink']}">Eachann</text>
    <text class="sans" x="72" y="346" font-size="22" font-weight="500" letter-spacing="1.2" fill="{P['muted']}">安静、本地、顺手。</text>"""
    return frame(1200, 440, "H", "Eachann — 安静、本地、顺手。", css, body)


# ------------------------------------------------------------------ #1 block
def block() -> str:
    css = """
  .bk-drag{animation:bk-drag 7s cubic-bezier(.22,1,.36,1) infinite}
  .bk-rule{transform-origin:92px 218px;animation:bk-rule 7s cubic-bezier(.22,1,.36,1) infinite}
  .bk-caret{animation:bk-caret 1.2s steps(1,end) infinite}
  @keyframes bk-drag{0%,16%,100%{transform:translateY(0)}44%,72%{transform:translateY(48px)}}
  @keyframes bk-rule{0%,28%,82%,100%{transform:scaleX(0);opacity:0}44%,70%{transform:scaleX(1);opacity:1}}
  @keyframes bk-caret{0%,49%{opacity:1}50%,100%{opacity:0}}
"""
    body = f"""    <!-- Left Animated Architectural Editor Plate -->
    <rect x="40" y="34" width="600" height="272" rx="10" fill="{P['paper']}" stroke="{P['border']}" stroke-width="1.5"/>
    <!-- Heading & resting markdown lines -->
    <rect x="86" y="72" width="154" height="14" rx="3" fill="{P['ink']}"/>
    <rect x="86" y="102" width="388" height="7" rx="3.5" fill="#c7c0b3"/>
    <rect x="86" y="120" width="310" height="7" rx="3.5" fill="#d7d1c4"/>

    <!-- Active Modular Block Gliding -->
    <g class="bk-drag">
      <rect x="74" y="140" width="468" height="58" rx="8" fill="{P['ink']}"/>
      <g fill="{P['iris']}">
        <circle cx="94" cy="161" r="2.3"/><circle cx="102" cy="161" r="2.3"/>
        <circle cx="94" cy="169" r="2.3"/><circle cx="102" cy="169" r="2.3"/>
        <circle cx="94" cy="177" r="2.3"/><circle cx="102" cy="177" r="2.3"/>
      </g>
      <rect x="122" y="158" width="218" height="7.5" rx="3.8" fill="{P['plaster']}" opacity=".94"/>
      <rect class="bk-caret" x="348" y="153" width="2.5" height="17" rx="1" fill="#82a9f7"/>
      <rect x="122" y="175" width="144" height="5.5" rx="2.8" fill="#6b7385"/>
    </g>

    <!-- Cobalt Insertion Guide -->
    <rect class="bk-rule" x="92" y="218" width="460" height="3" rx="1.5" fill="{P['iris']}"/>
    <rect x="86" y="256" width="292" height="7" rx="3.5" fill="#cfc8ba"/>

    <!-- Vertical Divider -->
    <line x1="672" y1="42" x2="672" y2="298" stroke="{P['border']}" stroke-width="1.2"/>

    <!-- Right Editorial Copy -->
    {embedded_icon("block", 708, 48, 52, 12, "Blk")}
    <text class="serif" x="778" y="88" font-size="44" font-weight="700" letter-spacing="-0.8" fill="{P['ink']}">Block</text>
    {arrow_ne(1148, 72, P['muted'], 1.15)}

    <text class="sans" x="708" y="148" font-size="20.5" font-weight="600" fill="{P['ink']}">Pure Go + MyGo 原生块级 Markdown 笔记</text>
    <text class="sans" x="708" y="186" font-size="18" fill="{P['body']}">直读本地 .md 文件夹，零私有格式绑定。</text>
    <text class="sans" x="708" y="218" font-size="18" fill="{P['body']}">支持块拖拽、Mermaid / LaTeX 与 CLI AI。</text>

    <line x1="708" y1="252" x2="1156" y2="252" stroke="{P['border']}" stroke-width="1.2"/>
    <text class="mono" x="708" y="286" font-size="16" font-weight="500" fill="{P['irisInk']}">block.cooool.top</text>
    <text class="mono" x="1156" y="286" text-anchor="end" font-size="15.5" fill="{P['muted']}">Pure Go · MyGo</text>"""
    return frame(1200, 340, "B", "Block — Pure Go + MyGo 原生跨平台块级 Markdown 笔记", css, body)


# ------------------------------------------------------------------ #2 thinkly
def thinkly() -> str:
    css = """
  .tk-sheet{animation:tk-sheet 7s cubic-bezier(.22,1,.36,1) infinite}
  .tk-l1{transform-origin:810px 104px;animation:tk-l1 7s cubic-bezier(.22,1,.36,1) infinite}
  .tk-l2{transform-origin:810px 124px;animation:tk-l2 7s cubic-bezier(.22,1,.36,1) infinite}
  .tk-dot{transform-origin:1066px 76px;animation:tk-dot 7s ease-in-out infinite}
  @keyframes tk-sheet{0%,18%,100%{transform:translateY(0)}46%,74%{transform:translateY(-12px)}}
  @keyframes tk-l1{0%,14%{transform:scaleX(.52)}42%,82%{transform:scaleX(1)}95%,100%{transform:scaleX(.52)}}
  @keyframes tk-l2{0%,24%{transform:scaleX(.36)}54%,82%{transform:scaleX(1)}95%,100%{transform:scaleX(.36)}}
  @keyframes tk-dot{0%,100%{transform:scale(.85);opacity:.65}50%{transform:scale(1.16);opacity:1}}
"""
    body = f"""    <!-- Left Editorial Copy -->
    {embedded_icon("thinkly", 48, 40, 46, 11, "Thk")}
    <text class="serif" x="110" y="77" font-size="40" font-weight="700" letter-spacing="-0.6" fill="{P['ink']}">Thinkly</text>

    <text class="sans" x="48" y="130" font-size="20" font-weight="600" fill="{P['ink']}">本地 Markdown 桌面笔记，随手速记，向过去提问</text>
    <text class="sans" x="48" y="166" font-size="18" fill="{P['body']}">Alt+N 置顶速记进本地目录，Ctrl+Alt+K 溯源问答。</text>

    <line x1="48" y1="196" x2="624" y2="196" stroke="{P['border']}" stroke-width="1.2"/>
    <text class="mono" x="48" y="228" font-size="15.5" font-weight="500" fill="{P['irisInk']}">note.cooool.top</text>
    <text class="mono" x="624" y="228" text-anchor="end" font-size="15" fill="{P['muted']}">Electron · React · BlockNote</text>

    <!-- Vertical Divider -->
    <line x1="664" y1="36" x2="664" y2="232" stroke="{P['border']}" stroke-width="1.2"/>
    {arrow_ne(1148, 46, P['muted'], 1.1)}

    <!-- Right Animated Quick-Capture Plate -->
    <line x1="726" y1="214" x2="1116" y2="214" stroke="{P['rule']}" stroke-width="1.5"/>
    <rect x="748" y="88" width="326" height="126" rx="6" fill="{P['stone']}"/>

    <g class="tk-sheet">
      <rect x="774" y="50" width="326" height="140" rx="8" fill="{P['paper']}" stroke="{P['border']}" stroke-width="1.5"/>
      <rect x="810" y="72" width="76" height="9" rx="2.5" fill="{P['ink']}"/>
      <circle class="tk-dot" cx="1066" cy="76" r="7.5" fill="{P['iris']}"/>
      <rect class="tk-l1" x="810" y="102" width="224" height="6.5" rx="3.2" fill="#8b8477"/>
      <rect class="tk-l2" x="810" y="122" width="172" height="6.5" rx="3.2" fill="#b8b1a3"/>
      <rect x="810" y="150" width="64" height="20" rx="10" fill="{P['irisSoft']}"/>
      <text class="mono" x="842" y="164" text-anchor="middle" font-size="10.5" font-weight="500" fill="{P['irisInk']}">Alt+N</text>
    </g>"""
    return frame(1200, 268, "T", "Thinkly — 本地 Markdown 桌面笔记，随手速记，向过去提问", css, body)


# ------------------------------------------------------------------ #3a pi-mini-mode
def pi_mini_mode() -> str:
    css = """
  .pm-n1{animation:pm-fold 7.5s cubic-bezier(.22,1,.36,1) infinite}
  .pm-n2{animation:pm-fold 7.5s cubic-bezier(.22,1,.36,1) .14s infinite}
  .pm-n3{animation:pm-fold 7.5s cubic-bezier(.22,1,.36,1) .28s infinite}
  .pm-bar{transform-origin:756px 118px;animation:pm-bar 7.5s cubic-bezier(.22,1,.36,1) infinite}
  @keyframes pm-fold{0%,16%,100%{opacity:.72;transform:translateY(0)}44%,76%{opacity:.12;transform:translateY(26px)}}
  @keyframes pm-bar{0%,22%,100%{transform:scaleX(.86)}46%,76%{transform:scaleX(1)}}
"""
    body = f"""    <!-- Left Typography -->
    <text class="serif" x="46" y="56" font-size="31" font-weight="700" letter-spacing="-0.4" fill="{P['ink']}">pi-mini-mode</text>
    <rect x="516" y="31" width="166" height="30" rx="15" fill="{P['irisSoft']}"/>
    <text class="mono" x="599" y="51" text-anchor="middle" font-size="13.5" font-weight="500" fill="{P['irisInk']}">6.8K+ downloads</text>

    <text class="sans" x="46" y="96" font-size="18" fill="{P['body']}">思考与工具调用折叠为过程树，紧凑单行页脚与图片预览。</text>

    <rect x="46" y="116" width="388" height="34" rx="8" fill="{P['stone']}"/>
    <text class="mono" x="62" y="138" font-size="14.5" fill="{P['ink']}">pi install npm:@eachann1024/pi-mini-mode</text>

    <!-- Vertical Divider -->
    <line x1="712" y1="28" x2="712" y2="148" stroke="{P['border']}" stroke-width="1.2"/>
    {arrow_ne(1152, 38, P['muted'], 1.0)}

    <!-- Right Animated Compression Visual -->
    <rect class="pm-n1" x="756" y="50" width="320" height="6" rx="3" fill="#b4ada0"/>
    <rect class="pm-n2" x="756" y="66" width="256" height="6" rx="3" fill="#c3bcb0"/>
    <rect class="pm-n3" x="756" y="82" width="290" height="6" rx="3" fill="#cfc8ba"/>

    <g class="pm-bar">
      <rect x="756" y="106" width="368" height="28" rx="6" fill="{P['ink']}"/>
      <circle cx="776" cy="120" r="4.5" fill="{P['iris']}"/>
      <rect x="792" y="117" width="114" height="6" rx="3" fill="{P['plaster']}" opacity=".92"/>
      <rect x="1044" y="117" width="62" height="6" rx="3" fill="#82a9f7"/>
    </g>"""
    return frame(1200, 176, "PM", "pi-mini-mode — Pi 紧凑模式扩展", css, body)


# ------------------------------------------------------------------ #3b pi-final-model
def pi_final_model() -> str:
    css = """
  .pf-glide{animation:pf-glide 7.5s cubic-bezier(.22,1,.36,1) infinite}
  .pf-spark{transform-origin:1138px 96px;animation:pf-spark 7.5s cubic-bezier(.22,1,.36,1) infinite}
  @keyframes pf-glide{0%,16%{transform:translateX(0);opacity:0}26%{opacity:1}68%{transform:translateX(142px);opacity:1}80%,100%{transform:translateX(142px);opacity:0}}
  @keyframes pf-spark{0%,56%,100%{transform:scale(.76);opacity:.42}70%,84%{transform:scale(1.22);opacity:1}}
"""
    body = f"""    <!-- Left Typography -->
    <text class="serif" x="46" y="56" font-size="31" font-weight="700" letter-spacing="-0.4" fill="{P['ink']}">pi-final-model</text>
    <rect x="526" y="31" width="156" height="30" rx="15" fill="{P['irisSoft']}"/>
    <text class="mono" x="604" y="51" text-anchor="middle" font-size="13.5" font-weight="500" fill="{P['irisInk']}">700+ downloads</text>

    <text class="sans" x="46" y="96" font-size="18" fill="{P['body']}">工作模型跑完工具调用，由指定总结模型提炼最终答复。</text>

    <rect x="46" y="116" width="406" height="34" rx="8" fill="{P['stone']}"/>
    <text class="mono" x="62" y="138" font-size="14.5" fill="{P['ink']}">pi install npm:@eachann1024/pi-final-model</text>

    <!-- Vertical Divider -->
    <line x1="712" y1="28" x2="712" y2="148" stroke="{P['border']}" stroke-width="1.2"/>
    {arrow_ne(1152, 38, P['muted'], 1.0)}

    <!-- Right Animated Work -> Final Distillation -->
    <rect x="756" y="76" width="92" height="40" rx="7" fill="{P['paper']}" stroke="{P['border']}" stroke-width="1.5"/>
    <text class="mono" x="802" y="101" text-anchor="middle" font-size="13.5" fill="{P['muted']}">WORK</text>

    <line x1="856" y1="96" x2="1004" y2="96" stroke="{P['rule']}" stroke-width="1.8"/>
    <circle class="pf-glide" cx="858" cy="96" r="6.5" fill="{P['iris']}"/>

    <rect x="1012" y="76" width="102" height="40" rx="7" fill="{P['ink']}"/>
    <text class="mono" x="1063" y="101" text-anchor="middle" font-size="13.5" font-weight="500" fill="{P['plaster']}">FINAL</text>
    <path class="pf-spark" d="M1138 88.6l2.4 5 5 2.4-5 2.4-2.4 5-2.4-5-5-2.4 5-2.4Z" fill="{P['iris']}"/>"""
    return frame(1200, 176, "PF", "pi-final-model — Pi 最终模型提炼扩展", css, body)


# ------------------------------------------------------------------ #4 goose rows
def goose_row(uid: str, icon: str, name: str, desc: str, stat: str, delay: float) -> str:
    css = f"""
  .gs-dot{{transform-origin:1126px 53px;animation:gs-dot 8s ease-in-out {delay:.1f}s infinite}}
  @keyframes gs-dot{{0%,100%{{opacity:.28;transform:scale(.85)}}20%,35%{{opacity:1;transform:scale(1.18)}}55%{{opacity:.28;transform:scale(.85)}}}}
"""
    body = f"""    {embedded_icon(icon, 36, 31, 44, 10, uid)}
    <text class="mono" x="98" y="60" font-size="20.5" font-weight="600" fill="{P['ink']}">{name}</text>
    <line x1="358" y1="30" x2="358" y2="76" stroke="{P['border']}" stroke-width="1.2"/>
    <text class="sans" x="382" y="60" font-size="18.5" fill="{P['body']}">{desc}</text>
    <text class="mono" x="1102" y="59" text-anchor="end" font-size="15.5" fill="{P['muted']}">{stat}</text>
    <circle class="gs-dot" cx="1126" cy="53" r="3.8" fill="{P['iris']}"/>
    {arrow_ne(1156, 53, P['muted'], 0.95)}"""
    return frame(1200, 106, uid, f"{name} — {desc}", css, body)


TARGETS = {
    "hero": hero,
    "block": block,
    "thinkly": thinkly,
    "pi-mini-mode": pi_mini_mode,
    "pi-final-model": pi_final_model,
    "goose-2fa": lambda: goose_row(
        "G1", "goose-2fa", "goose-2fa",
        "本地 TOTP / HOTP 验证器，回车直贴，MCP 永不返回密钥。",
        "200+ users", 0.0,
    ),
    "goose-notes-utools": lambda: goose_row(
        "G2", "goose-notes-utools", "goose-notes-utools",
        "挂起本地 Markdown 文件夹的 uTools 块笔记与独立速记小窗。",
        "uTools", 2.0,
    ),
    "goose-mark": lambda: goose_row(
        "G3", "goose-mark", "goose-mark",
        "粘贴网址自动 AI 归组，支持拼音检索与 Ctrl+数字秒开。",
        "1.6K+ users", 4.0,
    ),
    "goose-monitor": lambda: goose_row(
        "G4", "goose-monitor", "goose-monitor",
        "归并 Helper 与端口占用，搜到回车整组退出且防 PID 复用。",
        "1.4K+ users", 6.0,
    ),
}


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    for name, fn in TARGETS.items():
        out = ASSETS / f"{name}.svg"
        out.write_text(fn(), encoding="utf-8")
        print(f"{str(out.relative_to(ROOT)):32s} {out.stat().st_size / 1024:5.1f} KB")


if __name__ == "__main__":
    main()
