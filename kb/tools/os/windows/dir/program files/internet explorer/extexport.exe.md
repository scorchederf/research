---
created: 2026-11-21
fullpath: 'C:\Program Files\Internet Explorer\Extexport.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - internet-explorer
aliases:
  - "Extexport.exe"
url: []
---

**fullpath**: C:\Program Files\Internet Explorer\Extexport.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

## simple description

> ### 2026-11-21 Claude said
> Extexport.exe is a small helper shipped with Internet Explorer that exported browser data (bookmarks/favorites and similar settings) so that other browsers, such as Firefox, could import it. It is Microsoft-signed and still present on many Windows installs even though IE is retired. Normal users almost never run it directly.
>
> **SOC NOTE**: Listed in LOLBAS: running `Extexport.exe <folder> foo bar` makes it load `mozcrt19.dll`, `mozsqlite3.dll` or `sqlite3.dll` from the given folder, enabling signed-binary DLL side-loading (T1218 System Binary Proxy Execution / T1574.002 DLL Side-Loading). Alert on any execution of Extexport.exe, especially with a user-writable folder argument, and on those DLL names being written outside their usual locations.
>
> _Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_
