---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft Office\Office14\Visio.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Visio.exe
  - Microsoft Visio 2010
url:
  - https://learn.microsoft.com/office/vba/api/visio.application.commandline
---

**fullpath**:C:\Program Files (x86)\Microsoft Office\Office14\Visio.exe

# description

Visio.exe is the main executable of Microsoft Visio; the `Office14` folder corresponds to Office 2010 (32-bit install on 64-bit Windows). Learn documents Visio's startup command-line switches in the Visio VBA `Application.CommandLine` property reference.

## simple description

> ### 2026-11-21 Claude said
> This is the program file for Microsoft Visio 2010, the Office diagramming application used for flowcharts, network diagrams and floor plans. It opens Visio drawings (.vsd), stencils and templates. Office14 means Office 2010, which is out of support since 2020. Visio supports VBA macros like other Office apps.
>
> **SOC NOTE**: As an Office app, Visio can run VBA macros and host embedded OLE objects, so malicious `.vsd`/`.vsdm` files can be used for initial access (MITRE ATT&CK T1566.001, T1204.002). Child processes such as `cmd.exe`, `powershell.exe` or `wscript.exe` spawned by Visio.exe are suspicious. An Office 2010 install is unsupported and unpatched, increasing exploit risk.
>

# purpose

Starts Microsoft Visio. When started by double-clicking a drawing, template or stencil, the file name is on the command line; `/Automation` appears when started via `CreateObject`, and `/Embedding` when a Visio embedded object is opened in an OLE container.

# typical use cases

| usage | description |
| --- | --- |
| `Visio.exe drawing.vsd` | Open a Visio file. |
| `Visio.exe /nologo /nonew` | Start without the startup screen and without the New tab. |
| `Visio.exe /p drawing.vsd` | Show the Print dialog to quickly print a file. |

# options

| option | description |
| --- | --- |
| `/nonew` | The **New** tab is not shown on startup. |
| `/nologo` | The startup screen is not shown on startup. |
| `/p filename` | The **Print** dialog box is shown so that you can quickly print a file. |
| `filename` | Opens a Visio file; it must be in the Drawings file path or given as an absolute path. |
| `/1, /2, /3,.../9` | Opens one of the last-opened files. |
| `/noreg` | Prevents Visio from registering itself. |
| `/u` | Unregisters Visio. |
| `/r` | Registers Visio. |
| `/s` | Silently registers Visio. |
| `/pt filename, [printername, drivername, portname]` | Directs the file to print on a particular printer. |
| `::ODMA` | Visio uses ODMA to open a file. |
| `/Automation` | Appears when Visio is started with a `CreateObject` call. |
| `/Embedding` | Appears when a Visio embedded object is opened in an OLE container application. |
