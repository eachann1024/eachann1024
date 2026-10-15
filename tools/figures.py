"""《小王子》风格的可复用角色与景物。每个函数返回一段 SVG，原点在脚下。"""


def prince(scale=1.0, flip=False, delay=0.0):
    f = " scale(-1 1)" if flip else ""
    return f"""<g transform="scale({scale}){f}">
  <ellipse cx="1" cy="1.5" rx="22" ry="3.6" fill="#A87B4E" opacity=".26"/>
  <g class="cape" style="animation-delay:{delay}s">
    <path d="M-4-63C-26-55-40-30-38-6c-10 2-14-2-13-8C-49-32-30-58-9-66Z" fill="#D65F67"/>
    <path d="M-4-63C-26-55-38-30-36-8c-9-3-11-14-9-22C-42-44-24-60-7-65Z" fill="#E4747A"/>
  </g>
  <g stroke="#2E5F8C" stroke-width="5.2" stroke-linecap="round"><path d="M-5.5-22v13"/><path d="M5.5-22v13"/></g>
  <g fill="#8A5A32">
    <path d="M-9.6-9.6h8.2c.9 0 1.4.6 1.4 1.5v4c0 1.1-.7 1.8-1.8 1.8h-8.6c-1.1 0-1.8-.6-1.8-1.6 0-1.3.9-1.9 2-2.4l.6-3.3Z"/>
    <path d="M1.4-9.6h8.2l.6 3.3c1.1.5 2 1.1 2 2.4 0 1-.7 1.6-1.8 1.6H1.8C.7-2.3 0-3 0-4.1v-4c0-.9.5-1.5 1.4-1.5Z"/>
  </g>
  <path d="M-13.5-23c0-15 1.5-27 4-34 2.5-6 16.5-6 19 0 2.5 7 4 19 4 34Z" fill="#3E6F9E"/>
  <path d="M-13.5-23c0-15 1.5-27 4-34 1.2-2.9 4.8-4.4 8.4-4.5-1.6 10-3 25-2.9 38.5Z" fill="#4A7FB0" opacity=".55"/>
  <path d="M-13.6-23h27.2" stroke="#2E5F8C" stroke-width="2.4"/>
  <path d="M-13-31.5h26" stroke="#E0A33F" stroke-width="3"/>
  <rect x="-2.4" y="-33.4" width="4.8" height="3.8" rx="1" fill="#F2C45C" stroke="#C98B33" stroke-width=".5"/>
  <g fill="#F2C45C"><circle cx="0" cy="-45" r="1.5"/><circle cx="0" cy="-39" r="1.5"/><circle cx="0" cy="-52" r="1.5"/></g>
  <path d="M-7.6-57.5 0-52.5l7.6-5c-2-3.2-13.2-3.2-15.2 0Z" fill="#5A93C4"/>
  <path d="M-12.6-52c-5 4-8 10-8.4 16.4" stroke="#3E6F9E" stroke-width="5" fill="none" stroke-linecap="round"/>
  <path d="M12.6-52c5.4 3.6 8.6 9.4 9.4 15.6" stroke="#3E6F9E" stroke-width="5" fill="none" stroke-linecap="round"/>
  <circle cx="-21.4" cy="-34.4" r="3" fill="#F7DCAE"/>
  <circle cx="22.3" cy="-35.2" r="3" fill="#F7DCAE"/>
  <g class="scarf" style="animation-delay:{delay}s">
    <path d="M12-64c10 2 20 9 26 19-11-6-22-7-28-5Z" fill="#D65F67"/>
    <path d="M12-64c9 1 18 7 24 15-10-5-20-6-26-4Z" fill="#E4747A"/>
  </g>
  <path d="M-9.4-64.5c6 4.2 12.8 4.2 18.8 0l1.4 4.6c-6.6 4.6-15 4.6-21.6 0Z" fill="#E4747A"/>
  <path d="M-9.4-64.5c6 4.2 12.8 4.2 18.8 0l.5 1.7c-6.4 4-14 4-19.8 0Z" fill="#F08A8F"/>
  <circle cx="0" cy="-77" r="12.6" fill="#F7DCAE"/>
  <path d="M-12.6-77a12.6 12.6 0 0 0 25.2 0Z" fill="#EFCF9B" opacity=".4"/>
  <circle cx="-12.4" cy="-76" r="2.4" fill="#F2D2A0"/><circle cx="12.4" cy="-76" r="2.4" fill="#F2D2A0"/>
  <g fill="#F2C45C">
    <path d="M-12.7-78.6c-.6-9.6 5.4-16 12.7-16s13.3 6.4 12.7 16c-1.6-4.2-4-6.4-6.6-6.6-2.2-.2-3.4 1.4-6.1 1.4-2.7 0-3.9-1.6-6.1-1.4-2.6.2-5 2.4-6.6 6.6Z"/>
    <circle cx="-8.4" cy="-85.6" r="4.4"/><circle cx="0" cy="-89.4" r="5"/><circle cx="8.4" cy="-85.6" r="4.4"/>
    <circle cx="-12" cy="-80.6" r="3.4"/><circle cx="12" cy="-80.6" r="3.4"/>
  </g>
  <g class="tuft" style="animation-delay:{delay}s"><path d="M2-92c2.6-5 7-7.4 11.4-6.6-3.6 1.6-5.4 4-6 7.4-2 .6-3.8.2-5.4-.8Z" fill="#F2C45C"/></g>
  <g fill="#FBE0A4" opacity=".7"><circle cx="-3.6" cy="-88.6" r="2"/><circle cx="5.4" cy="-86.6" r="1.6"/></g>
  <g class="blink" style="animation-delay:{delay}s" fill="#3F4D5A">
    <ellipse cx="-4" cy="-77.4" rx="1.3" ry="1.6"/><ellipse cx="4" cy="-77.4" rx="1.3" ry="1.6"/>
  </g>
  <g stroke="#C9A063" stroke-width=".9" stroke-linecap="round" opacity=".75" fill="none"><path d="M-6-81.2q2-1.2 4 0"/><path d="M2-81.2q2-1.2 4 0"/></g>
  <g fill="#E9A0A0" opacity=".5"><ellipse cx="-7.4" cy="-73.6" rx="2.4" ry="1.5"/><ellipse cx="7.4" cy="-73.6" rx="2.4" ry="1.5"/></g>
  <path d="M-2.6-72.4q2.6 2.6 5.2 0" stroke="#C47A6A" stroke-width="1.1" fill="none" stroke-linecap="round"/>
</g>"""


def fox(scale=1.0, delay=0.0):
    return f"""<g transform="scale({scale})">
  <ellipse cx="-1" cy="1.2" rx="20" ry="3.2" fill="#A87B4E" opacity=".24"/>
  <g class="tail" style="animation-delay:{delay}s">
    <path d="M7-6c11-1 18-7 21-16 6 9 5 21-3 28-7 6-16 7-23 3-3-2-4-5-3-8 2 2 5 2 8-7Z" fill="#E08A4C"/>
    <path d="M28-22c4.4 5 5.6 12 3.4 18-1.4-5.6-4.6-9.8-9-11.8 2.4-1.6 4.2-3.8 5.6-6.2Z" fill="#FFF6E8"/>
    <path d="M9-5c9-1.4 15.6-6.6 19-14.6" stroke="#D1813F" stroke-width=".9" fill="none" opacity=".45"/>
  </g>
  <path d="M-11.6 0c-2.6-13.4 1.4-23 8.8-25.6 7.6-2.6 14.2 4.4 15.2 14.2.4 4.2 0 8.2-1 11.4Z" fill="#E89A5C"/>
  <path d="M-11.6 0c-2.6-13.4 1.4-23 8.8-25.6 2.6-.9 5 0 7 1.6-5.4 2.8-9 11-8.4 24Z" fill="#F0A96C" opacity=".55"/>
  <path d="M2.4-2c4.8-2.8 7.6-7.8 8-13.8 1.4 5.6.4 11.2-2.2 15.8Z" fill="#D1813F" opacity=".26"/>
  <g stroke="#E89A5C" stroke-width="4.2" stroke-linecap="round"><path d="M-7.6-10.5v8"/><path d="M-1.4-10.5v8"/></g>
  <g fill="#FFF6E8"><ellipse cx="-7.6" cy="-1.4" rx="2.9" ry="1.9"/><ellipse cx="-1.4" cy="-1.4" rx="2.9" ry="1.9"/></g>
  <g stroke="#E3B98C" stroke-width=".5" opacity=".7"><path d="M-7.6-2.6v1.5M-1.4-2.6v1.5"/></g>
  <path d="M-9.6-3.4c-2.2-9.8.4-16.8 5-19 3.2 3.6 3.8 11.4 2.4 19Z" fill="#FFF6E8"/>
  <g transform="translate(-4.5 -30)">
    <g class="ear" style="transform-origin:28% 96%;animation-delay:{delay}s">
      <path d="M-8.6-5.6-12-18.6l10 8Z" fill="#E08A4C"/>
      <path d="M-8.2-7.4-10.4-15l6.2 4.8Z" fill="#F2B8A8"/>
    </g>
    <g class="ear" style="transform-origin:72% 96%;animation-delay:{delay + 1.6}s">
      <path d="M6.8-6.4 11-19 2-11.2Z" fill="#E08A4C"/>
      <path d="M6.6-8 9.6-15.6 3.6-10.8Z" fill="#F2B8A8"/>
    </g>
    <path d="M9 0c0 4.4-2.4 8-6 9.4-1.9 2.6-4.6 4-7.8 4-1.9 0-3.6-.5-5.1-1.4-2.3.3-4.6.1-6.4-.6-1.7-.6-2.7-1.6-2.7-2.7 0-1 .8-1.9 2.2-2.6-.7-.6-1.1-1.3-1.1-2 0-1.5 1.8-2.7 4.6-3.3 1.6-.4 3.5-.6 5.4-.6-.5-1.1-.8-2.4-.8-3.7 0-5 3.9-9 8.7-9S9-5 9 0Z" fill="#E89A5C"/>
    <path d="M-8.6-2.2C-9.2-7-5.8-11-1.6-11.8-4-8.6-5.2-5.2-5.4-1.8Z" fill="#F0A96C"/>
    <path d="M-6.4 4.6c-2.4-.3-5-.2-7 .3-2.8.6-4.6 1.8-4.6 3.3 0 1.1 1 2.1 2.7 2.7 2.4.9 5.6 1.1 8.4.7 1.5-2.2 1.8-4.8.5-7Z" fill="#FFF6E8"/>
    <path d="M-5 10.4c-1 2.2-3.2 3.4-6 3.4 2.2-.2 4.2-1.2 5.4-2.6Z" fill="#FFF6E8"/>
    <ellipse cx="-16.4" cy="7.6" rx="2" ry="1.6" fill="#4A3A30" transform="rotate(-10 -16.4 7.6)"/>
    <circle cx="-17" cy="6.9" r=".5" fill="#FFFFFF" opacity=".5"/>
    <path d="M-15.2 9c-.5 1.3-1.6 2-2.8 1.9" stroke="#C98B33" stroke-width=".7" fill="none" opacity=".6" stroke-linecap="round"/>
    <path d="M3.4-1.2c3-.2 5.2-1.8 6.2-4.2.4 4.2-2.2 7.4-6.2 7.8Z" fill="#F7C190" opacity=".6"/>
    <g class="blink" style="animation-delay:{delay + 2.2}s">
      <ellipse cx="-4.6" cy="-2.6" rx="1.55" ry="1.95" fill="#3F3028"/>
      <ellipse cx="3.4" cy="-3" rx="1.55" ry="1.95" fill="#3F3028"/>
      <circle cx="-4.1" cy="-3.3" r=".55" fill="#FFFFFF" opacity=".85"/>
      <circle cx="3.9" cy="-3.7" r=".55" fill="#FFFFFF" opacity=".85"/>
    </g>
    <g stroke="#D1813F" stroke-width=".75" stroke-linecap="round" opacity=".5" fill="none">
      <path d="M-6.8-6.2q2.2-1.3 4.4-.3"/><path d="M1.4-6.6q2.2-1.1 4.4 0"/>
    </g>
    <g stroke="#A07A5C" stroke-width=".5" opacity=".4" stroke-linecap="round" fill="none">
      <path d="M-14 5.4q-4-2.2-6.4-3.8"/><path d="M-14.4 8.2q-4.4-.4-7-.8"/><path d="M-13.4 10.2q-3.6 1.6-5.6 3.4"/>
    </g>
  </g>
</g>"""


def sheep(scale=1.0, delay=0.0):
    return f"""<g transform="scale({scale})">
  <ellipse cx="0" cy="1" rx="18" ry="3.2" fill="#A87B4E" opacity=".22"/>
  <g stroke="#8C7F8E" stroke-width="2.6" stroke-linecap="round"><path d="M-7-8v7"/><path d="M-2.4-8v7"/><path d="M4-8v7"/><path d="M8.4-8v7"/></g>
  <g fill="#FFF6E8">
    <circle cx="-8" cy="-14" r="6.6"/><circle cx="0" cy="-17" r="7.6"/><circle cx="8" cy="-14.4" r="6.8"/>
    <circle cx="-4" cy="-9.6" r="5.6"/><circle cx="4.4" cy="-9.4" r="5.4"/>
  </g>
  <g fill="#EDE0CB" opacity=".8"><circle cx="-6" cy="-10.6" r="2.6"/><circle cx="2.4" cy="-13" r="2.2"/><circle cx="7.6" cy="-16" r="1.8"/></g>
  <g class="nod" style="animation-delay:{delay}s;transform-origin:70% 58%">
    <path d="M11.6-18.6c-4.2-1-7-3.4-7.4-6.4 3.4.4 6.4 2.2 8.4 4.8Z" fill="#9A8C9C"/>
    <path d="M24.4-17.6c3-2.8 6.6-3.6 9.4-2-3.2 1.2-5.8 3.2-7.4 5.8Z" fill="#9A8C9C"/>
    <path d="M11.2-19.6c1.4-3.6 4.6-5.6 8-5.6 3.8 0 7 2.4 8.2 6.4 1 3.4.2 7-2.2 9.4-2 2-4.6 3-7.2 2.8-2.8-.2-5.2-1.6-6.8-4-1.6-2.4-1.8-5.6 0-9Z" fill="#8C7F8E"/>
    <path d="M12.8-9.6c1.8 1.8 4.2 2.8 6.6 2.6-1 1.6-3 2.2-5 1.6-1-.4-1.6-1.2-1.6-2.4Z" fill="#7A6E7C"/>
    <g class="blink" style="animation-delay:{delay + 1.1}s">
      <ellipse cx="14.6" cy="-17.4" rx="1.2" ry="1.5" fill="#2F2A33"/>
      <ellipse cx="20.6" cy="-16.8" rx="1.2" ry="1.5" fill="#2F2A33"/>
      <circle cx="14.2" cy="-18" r=".42" fill="#FFFFFF" opacity=".85"/>
      <circle cx="20.2" cy="-17.4" r=".42" fill="#FFFFFF" opacity=".85"/>
    </g>
    <g fill="#5E5460"><circle cx="24.2" cy="-13.4" r=".7"/><circle cx="26" cy="-11.6" r=".7"/></g>
    <path d="M22.6-9q2 1.2 3.6-.4" stroke="#6F6474" stroke-width=".8" fill="none" stroke-linecap="round"/>
  </g>
</g>"""


def rose(scale=1.0, delay=0.0):
    """玻璃罩里的玫瑰，原点在底座中心。"""
    return f"""<g transform="scale({scale})">
  <ellipse cx="0" cy="1" rx="22" ry="3.6" fill="#A87B4E" opacity=".2"/>
  <path d="M-18 0h36v-3.4a2 2 0 0 0-2-2h-32a2 2 0 0 0-2 2Z" fill="#C98B33"/>
  <path d="M-16-5.4h32V-8h-32Z" fill="#E0A33F"/>
  <path d="M0-8v-22" stroke="#5C8A55" stroke-width="2.2" stroke-linecap="round" fill="none"/>
  <path d="M0-17c-7.4-1-10.6-7.4-10.6-7.4 7.4-1 11.6 3.2 11.6 3.2" fill="#5C8A55" opacity=".9"/>
  <path d="M0-24c6.4-1 9.6-6.4 9.6-6.4 1 6.4-4.2 9.6-8.6 8.6" fill="#6FA063" opacity=".85"/>
  <g class="bloom" style="animation-delay:{delay}s;transform-origin:50% 76%">
    <circle cx="0" cy="-34" r="7.4" fill="#D65F67"/>
    <path d="M-7.4-34a7.4 7.4 0 0 1 14.8 0Z" fill="#E4747A"/>
    <path d="M-7.4-34c1.4-4.4 5-6.6 7.4-6.6s6 2.2 7.4 6.6c-2.4-2.4-5-3.4-7.4-3.4s-5 1-7.4 3.4Z" fill="#F08A8F"/>
    <circle cx="0" cy="-34" r="3" fill="#F08A8F"/>
    <circle cx="0" cy="-34.6" r="1.3" fill="#FBE3DF"/>
  </g>
  <path d="M-17-5.4C-17-26-9.6-43 0-43s17 17 17 37.6" fill="#CFE4F2" fill-opacity=".22" stroke="#9FC4DD" stroke-width="1.2"/>
  <path d="M-10.6-14c-.6-12 2.6-20.4 7-23.6" stroke="#FFFFFF" stroke-width="1.8" fill="none" opacity=".7" stroke-linecap="round"/>
  <circle cx="0" cy="-44.6" r="2" fill="#9FC4DD"/>
</g>"""
