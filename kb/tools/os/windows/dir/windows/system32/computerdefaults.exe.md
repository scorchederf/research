---
created: 2026-11-21
fullpath: 'C:\Windows\System32\ComputerDefaults.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - windows
aliases:
  - "ComputerDefaults.exe"
  - "Set Program Access and Computer Defaults"
  - "SPAD"
url:
  - https://learn.microsoft.com/windows/win32/shell/cpl-setprogramaccess
  - https://learn.microsoft.com/windows/win32/shell/vista-managing-defaults
---

**fullpath**:C:\Windows\System32\ComputerDefaults.exe

# description

ComputerDefaults.exe opens the Set Program Access and Computer Defaults (SPAD) page, located under the Default Programs Control Panel item in Windows Vista and later. Learn documents the SPAD feature but does not name the executable. The page can be hidden by the `NoDefaultPrograms` policy.

## simple description

> ### 2026-11-21 Claude said
> ComputerDefaults.exe shows the Windows page for choosing default programs (browser, email, media player, messaging, Java VM) and whether their shortcuts are shown. It is a small Microsoft-signed UI program in System32. It auto-elevates, meaning it runs with high integrity without a UAC prompt for admin users.
>
> **SOC NOTE**: Classic UAC bypass: ComputerDefaults.exe is auto-elevated and reads the per-user `HKCU\Software\Classes\ms-settings\Shell\Open\command` handler, so an attacker who writes a command there gets it executed elevated (MITRE ATT&CK T1548.002 Bypass User Account Control). Hunt for writes to that key (DelegateExecute value) and child processes of ComputerDefaults.exe.
>

# purpose

SPAD lets administrators manage defaults and the display of program icons, shortcuts and menu entries for registered programs in five client types (browser, email, instant messaging, media player, virtual machine for Java). It offers Microsoft Windows, Non-Microsoft, Custom and optional Computer Manufacturer configurations. As of Windows 8 SPAD configures per-user defaults; before Windows 8 it set per-computer defaults. `LastUserInitiatedDefaultChange` under `HKLM\SOFTWARE\Clients\<ClientTypeName>` records the last user change.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
