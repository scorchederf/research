---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\IDE\VSLaunchBrowser.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - visualstudio
  - lolbin
aliases:
  - VSLaunchBrowser.exe
url:
---

**fullpath**:C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\IDE\VSLaunchBrowser.exe

# description

VSLaunchBrowser.exe is a helper in the Visual Studio IDE folder. _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> VSLaunchBrowser.exe is a small Visual Studio helper that opens a web browser for the IDE, for example when you start debugging a web project. It lives in the Common7\IDE folder of each Visual Studio edition and version. Developers never call it directly. It only exists on machines with Visual Studio installed.
>
> **SOC NOTE**: LOLBAS lists it as a download/execute proxy (T1105, T1218): `VSLaunchBrowser.exe .exe https://<url>` opens a URL with the default handler, and it can launch local files. Execution outside a Visual Studio parent (devenv.exe) or with external URLs on a non-developer host is suspicious.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
