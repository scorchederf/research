---
created: 2026-11-21
fullpath: 'C:\Windows\write.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
aliases:
  - write.exe
  - WordPad
url:
  - https://learn.microsoft.com/windows/whats-new/deprecated-features-resources
  - https://learn.microsoft.com/windows/configuration/shell-launcher/
---

**fullpath**:C:\Windows\write.exe

# description

`write.exe` is a WordPad launcher: it creates a 32-bit `wordpad.exe` process and exits. WordPad was removed from all editions of Windows starting with Windows 11 version 24H2 and Windows Server 2025, and `write.exe`, `wordpad.exe` and `wordpadfilter.dll` were removed with it. Microsoft recommends Word for .doc/.rtf files and Notepad for plain text.

## simple description

> ### 2026-11-21 Claude said
> `write.exe` is a small stub kept for compatibility with the old Windows "Write" program. When you run it, it simply starts WordPad and closes itself. On Windows 11 24H2 and later it no longer exists.
>
> **SOC NOTE**: Low risk itself, but WordPad has had document-parsing RCE bugs (MS09-010, MS11-033), so malicious .rtf/.doc files opened with it matter. Since the binary is gone on newer builds, a `write.exe` on Windows 11 24H2+ or in an unusual folder deserves a hash check. Its launch-and-exit behaviour is sometimes used in proof-of-concept code as a harmless "calc-like" payload.
>

# purpose

Starts WordPad. Because it exits right after launching `wordpad.exe`, it can't be used as a Shell Launcher custom shell; Shell Launcher would act on the exit code of `write.exe`.

# typical use cases

| usage | description |
| --- | --- |
| `write.exe` | Launch WordPad (on Windows versions that still include it). |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
