---
created: 2026-11-21
fullpath: 'C:\Windows\regedit.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - registry
aliases:
  - regedit.exe
  - Regedit
  - Registry Editor
  - Regedt32.exe
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/windows-registry-advanced-users
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/registry-changes-in-x64-based-windows
  - https://learn.microsoft.com/sysinternals/downloads/regjump
---

**fullpath**:C:\Windows\regedit.exe

# description

Registry Editor (Regedit.exe, also Regedt32.exe) is the built-in Windows graphical tool administrators use to view and modify the registry. Related tools include the Console Registry Tool `reg.exe`, Group Policy (Gpedit.msc), .reg files, WMI and the Sysinternals RegJump applet that opens Regedit at a given path.

## simple description

> ### 2026-11-21 Claude said
> regedit.exe is the Registry Editor, the GUI program used to browse and change the Windows registry, the database that stores system and application settings. It can also import and export .reg files, load offline hives and connect to a remote computer's registry. On 64-bit Windows a 32-bit copy lives in SysWOW64. Normal users rarely run it; admins and support staff do.
>
> **SOC NOTE**: Attackers use `regedit /s file.reg` to silently import persistence (Run keys, services, IFEO) or disable defenses (T1112 Modify Registry, T1547.001). Regedit export can also dump SAM/SECURITY-related keys when run as SYSTEM. Look for regedit.exe launched by scripts, Office or unusual parents, with /s or /e arguments, and for the last viewed key in HKCU\Software\Microsoft\Windows\CurrentVersion\Applets\Regedit (LastKey) as evidence of what a user browsed. Can be blocked with the DisableRegistryTools policy.
>

# purpose

Registry Editor lets administrators locate a subtree, key, subkey or value; add a subkey or value; change a value; delete a subkey or value; and rename a subkey or value. The navigation area shows a folder for each predefined key on the local computer; when connected to a remote computer's registry only HKEY_USERS and HKEY_LOCAL_MACHINE appear. Both 32-bit and 64-bit versions are included with x64 Windows; the 32-bit version is %WinDir%\SysWOW64\regedit.exe. Incorrect edits can cause serious problems that may require reinstalling Windows.

# typical use cases

| usage | description |
| --- | --- |
| `regedit` | Start the 64-bit Registry Editor (from Start > Run on an x64 system). |
| `%WinDir%\SysWOW64\regedit.exe -m` | Start the 32-bit Registry Editor; the m switch allows multiple instances. |
| `regjump HKLM\Software\Microsoft\Windows` | Use Sysinternals RegJump to open Regedit directly at a key. |

# options

| option | description |
| --- | --- |
| `-m` | Lets you run multiple instances of Registry Editor. |
