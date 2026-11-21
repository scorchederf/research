---
created: 2026-11-21
fullpath: 'C:\Windows\System32\runonce.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - persistence
aliases:
  - "runonce.exe"
  - "Run Once Wrapper"
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/remote/application-not-start-in-remoteapp-session
  - https://learn.microsoft.com/windows/win32/setupapi/run-and-runonce-registry-keys
  - https://learn.microsoft.com/windows-hardware/test/wpt/cpu-analysis
---

**fullpath**:C:\Windows\System32\runonce.exe

# description

`runonce.exe` is the Windows component that processes RunOnce-type startup entries at logon. Learn documents starting it with `/AlternateShellStartup` in a RemoteApp logon script so applications relying on Explorer.exe startup processing can run.

## simple description

> ### 2026-11-21 Claude said
> runonce.exe runs the one-time programs registered in the RunOnce registry keys when a user logs on.
> After an entry runs, Windows deletes it so it does not run again.
> It is a normal Windows process seen briefly at logon, often after software installs or updates.
>
> **SOC NOTE**: RunOnce/RunOnceEx keys are a persistence location (T1547.001 Registry Run Keys); runonce.exe launching unusual children at logon points to them. RunOnceEx can also load DLLs (T1574/T1218 abuse). Correlate with registry writes to ...\CurrentVersion\RunOnce*.
>

# purpose

Processes the RunOnce lists at logon (`HKLM`/`HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce`). In boot performance analysis, threads can be seen waiting for the RunOnce.exe process to exit.

# typical use cases

| usage | description |
| --- | --- |
| `runonce.exe /AlternateShellStartup` | Added as a logon script in a TS RemoteApp session so startup applications that rely on Explorer.exe run. |

# options

| option | description |
| --- | --- |
| `/AlternateShellStartup` | Runs startup processing when an alternate shell (RemoteApp) is used instead of Explorer. |
