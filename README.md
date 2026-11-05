![Eachann](assets/hero.svg)

<table>
<tr>
<td width="50%" valign="top">

[![Thinkly](assets/notes.svg)](https://github.com/eachann1024/thinkly)

### <img src="https://raw.githubusercontent.com/eachann1024/thinkly/main/public/logo.png" width="28" height="28" align="absmiddle" alt=""> [Thinkly](https://github.com/eachann1024/thinkly)

**Local Markdown. Quick capture. Ask your notes.**

在别的软件里按 Alt+N，置顶速记小窗先把念头写进自己的 Markdown 文件夹；记不清原话时按 Ctrl+Alt+K，向这些笔记提问并看到出处。

官网：[note.cooool.top](https://note.cooool.top/)

`TypeScript · React · Electron · BlockNote`

</td>
<td width="50%" valign="top">

[![Goose Herdr](assets/herdr.svg)](https://github.com/eachann1024/goose-herdr-gpui)

### <img src="https://raw.githubusercontent.com/eachann1024/goose-herdr-gpui/main/resources/icons/app/herdrm-icon-1024.png" width="28" height="28" align="absmiddle" alt=""> [goose-herdr-gpui](https://github.com/eachann1024/goose-herdr-gpui)

**Sessions. SSH. Split terminals.**

Goose Herdr 的 macOS 原生客户端，用 Rust + GPUI 管理 Herdr 会话、SSH 连接与终端分栏。
终端基于 Zed 终端核心与批量网格渲染，沿用原有 Herdr 协议、偏好和 Keychain，退出界面不会关闭共享 daemon。

`Rust · GPUI · gpui-component · zed-terminal`

</td>
</tr>
</table>

![Pi — Mini Mode · Final Model](assets/pi.svg)

<table>
<tr>
<td width="50%" valign="top">

### [pi-mini-mode](https://github.com/eachann1024/pi-mini-mode)

**Less noise. More focus.**

![downloads](https://img.shields.io/badge/downloads-6.8K%2B-blue)

输入框上方可预览图片，支持斜杠命令直接插入技能；输出默认将思考与工具调用折叠为过程树，支持展开子代理详情。
紧凑页脚单行展示模型、Token、缓存命中率、费用与上下文占用，内置 cc-light / cc-dark 主题。

`TypeScript · Pi TUI · grok-mermaid`

```sh
pi install npm:@each1024/pi-mini-mode
```

</td>
<td width="50%" valign="top">

### [pi-final-model](https://github.com/eachann1024/pi-final-model)

**Work runs. Final finishes.**

![downloads](https://img.shields.io/badge/downloads-700%2B-blue)

由主会话模型正常调用工具执行任务，再自动交由指定的总结模型提炼最终答复，保留原思考强度与上下文。
提炼失败时回退为原输出，成功后在答复首尾显示提示标记。

`TypeScript · Pi Extension API · Pi TUI`

```sh
pi install npm:@each1024/pi-final-model
```

</td>
</tr>
</table>

## Tools, within reach.

<table>
<tr>
<td width="50%" valign="top">

### <img src="https://raw.githubusercontent.com/eachann1024/goose-2fa/main/public/logo.png" width="28" height="28" align="absmiddle" alt=""> [goose-2fa](https://github.com/eachann1024/goose-2fa)

**Local codes, close at hand.**

![users](https://img.shields.io/badge/users-200%2B-blue)

uTools 插件，主框输入 `2fa github` 回车，验证码直接贴到上一个窗口；TOTP 与 HOTP 同屏管理。
支持粘贴 Google Authenticator 迁移码和 otpauth 链接，备份保留分组与备注；MCP 只读脱敏元数据，永不返回种子和动态码。

`TypeScript · React · uTools · MCP`

</td>
<td width="50%" valign="top">

### <img src="https://raw.githubusercontent.com/eachann1024/raycast-2fa/main/assets/icon.png" width="28" height="28" align="absmiddle" alt=""> [raycast-2fa](https://github.com/eachann1024/raycast-2fa)

**Codes at command speed.**

Raycast 上的本地 TOTP / HOTP 管理器：粘贴 Base32 密钥，或用 Swift Vision 识别截图和图片里的二维码添加账户，回车复制或粘贴验证码。
可导出为二维码或 otpauth 链接迁移到手机，支持 JSON 备份，并可与 uTools 版共用同一份数据文件。

`TypeScript · Raycast API · Swift Vision`

</td>
</tr>
<tr>
<td valign="top">

### <img src="https://raw.githubusercontent.com/eachann1024/goose-monitor/main/utools/logo.png" width="28" height="28" align="absmiddle" alt=""> [goose-monitor](https://github.com/eachann1024/goose-monitor)

**Know what is running.**

![users](https://img.shields.io/badge/users-1.4K%2B-blue)

把 Electron、Chrome 的 Helper 归并到所属应用，搜到回车即整组结束；输入端口号就能找到占用者。
可按界面应用、CPU、内存、网络等分类查看实时网速，结束前用快照复核，避免误杀复用 PID 的进程；附带 MCP 服务。

`TypeScript · Vite · uTools · MCP`

</td>
<td valign="top">

### <img src="https://raw.githubusercontent.com/eachann1024/raycast-monitor/main/assets/icon.png" width="28" height="28" align="absmiddle" alt=""> [raycast-monitor](https://github.com/eachann1024/raycast-monitor)

**Find. Inspect. Quit.**

按应用名、PID 或端口查找进程，Helper 与子进程归并到所属应用，回车直接结束整个应用，顽固进程可强制退出。
结束前复核进程身份，按从子到父的顺序发送信号防止重启；网速只在网络分类采样，另带 CPU 菜单栏。

`TypeScript · React · Raycast API / Utils`

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### <img src="https://raw.githubusercontent.com/eachann1024/goose-mark/main/public/logo.png" width="28" height="28" align="absmiddle" alt=""> [goose-mark](https://github.com/eachann1024/goose-mark)

**Keep the web within reach.**

![users](https://img.shields.io/badge/users-1.6K%2B-blue)

主框粘贴网址即可入库，AI 自动润色标题、简介并归组；URL 中写 `{query}` 的书签可当搜索引擎，Tab 填参打开。
支持拼音搜索、`Ctrl+数字` 秒开前 10 个书签，图标本地缓存，并在本机探测死链。

`TypeScript · React · Vite · uTools · AI SDK`

</td>
</tr>
</table>
