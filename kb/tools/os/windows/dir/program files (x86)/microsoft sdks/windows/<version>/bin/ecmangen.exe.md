---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\Bin\ECMangen.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - windows-sdk
  - etw
aliases:
  - ECMangen.exe
  - ECManGen
url:
  - https://learn.microsoft.com/windows/win32/wes/writing-an-instrumentation-manifest
  - https://learn.microsoft.com/windows/win32/wes/message-compiler--mc-exe-
---

**fullpath**:C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\Bin\ECMangen.exe

# description

`ECManGen.exe` is a GUI tool included in the `\Bin` folder of the Windows SDK that guides you through creating an event instrumentation manifest from scratch without writing XML tags. After authoring, the manifest is compiled with the Message Compiler (`mc.exe`).

## simple description

> ### 2026-11-21 Claude said
> ECManGen is a developer tool for building the XML manifest that describes an application's Windows event log provider, channels and events. It provides a graphical editor instead of hand-editing XML. It ships with older Windows SDKs. It has no security function itself.
>
> **SOC NOTE**: Rarely seen on end-user systems; its presence indicates a developer workstation with the Windows SDK. Low abuse potential; unexpected execution on servers would merely indicate developer tooling installed.
>

# purpose

Authoring instrumentation (event) manifests for Windows Event Log providers.

# typical use cases

| usage | description |
| --- | --- |
| `ECManGen.exe` | Launches the GUI to create an instrumentation manifest. |

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
