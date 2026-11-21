---
created: 2026-11-21
fullpath: 'C:\Windows\System32\WerFaultSecure.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - wer
aliases:
  - "WerFaultSecure.exe"
url: []
---

**fullpath**: C:\Windows\System32\WerFaultSecure.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_

## simple description

> ### 2026-11-21 Claude said
> WerFaultSecure.exe is the Windows Error Reporting helper used when a protected process (such as a Protected Process Light or a secure/isolated process) crashes. Because normal WerFault.exe cannot read memory of protected processes, Windows launches this signed, protected variant to collect crash information. It typically produces encrypted crash dumps rather than plain minidumps. You will normally see it briefly spawned by the system right after a crash of a protected process.
>
> **SOC NOTE**: WerFaultSecure.exe runs as a protected process and can read memory of other protected processes such as LSASS; public research (2025) showed it can be abused to dump LSASS or suspend EDR processes (T1003.001 OS Credential Dumping: LSASS Memory, T1562.001 Impair Defenses). Alert on WerFaultSecure.exe launched by unusual parents, with command-line arguments referencing lsass or EDR PIDs, or running from paths other than System32. Crash reports land under C:\ProgramData\Microsoft\Windows\WER.
>
> _Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:14 UTC_
