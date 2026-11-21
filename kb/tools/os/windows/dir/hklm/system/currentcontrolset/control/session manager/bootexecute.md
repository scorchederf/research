---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\BootExecute'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - boot
  - persistence
aliases:
  - "BootExecute"
  - "boot execute images"
url:
  - https://learn.microsoft.com/sysinternals/resources/inside-native-applications
  - https://learn.microsoft.com/windows-server/administration/windows-commands/autochk
  - https://learn.microsoft.com/windows-server/administration/windows-commands/chkntfs
  - https://learn.microsoft.com/sysinternals/downloads/autoruns
---

**fullpath**: HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\BootExecute

# description

REG_MULTI_SZ value under the Session Manager key that lists native applications (names and arguments) executed by Session Manager (smss.exe) early in boot. By default it contains `autocheck autochk *`, which runs Autochk (the boot-time chkdsk for NTFS). Sysinternals Autoruns shows its entries under "boot execute images"; Autochk behaviour is configured with `chkntfs`.

## simple description

> ### 2026-11-21 Claude said
> BootExecute tells Windows which special "native" programs to run very early during startup, before services, Explorer or any user logs on. Normally it only runs autochk, which checks disks for errors after an unclean shutdown. Because these programs run before almost anything else, with full system rights, they can touch files and disks that are locked later.
>
> **SOC NOTE**: Adding an entry here gives extremely early, SYSTEM-level persistence that runs before AV/EDR user-mode components (T1547.001 / T1547 Boot or Logon Autostart Execution). Anything other than `autocheck autochk *` (and known products such as some AV boot scanners) is suspicious. Monitor with Autoruns and registry auditing (Sysmon 13). Related Session Manager values (SetupExecute, PlatformExecute, Execute) can be abused similarly.
>

# purpose

Specifies the programs Session Manager runs between the loading of boot and system-start drivers and the enabling of paging, when no other programs are active. Session Manager looks for these executables in `%SystemRoot%\system32`. Because no files are open at that point, Autochk can open any volume in raw mode, including the boot drive. Autochk runs when chkdsk is requested on the boot volume, when chkdsk can't get exclusive use of a volume, or when a volume is flagged dirty.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `BootExecute` | REG_MULTI_SZ | Names and arguments of programs executed by Session Manager at boot; typically `autocheck autochk *`. |

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager" /v BootExecute` | Show the boot execute list. |
| `chkntfs /x d: e:` | Exclude volumes from Autochk at startup. |
| `chkntfs /t:30` | Set the Autochk initiation countdown to 30 seconds. |
