---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - ATs
  - Assistive Technologies
url:
  - https://learn.microsoft.com/windows/win32/winauto/ease-of-access---assistive-technology-registration
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs

# description

Registry key where accessibility applications register with the Ease of Access Center. Each application creates a subkey named "CompanyName_ProductName_v#" with values describing how to start it and how it behaves on the secure desktop. Users enable startup via HKCU\...\Accessibility\Configuration.

## simple description

> ### 2026-11-21 Claude said
> Each subkey here is one assistive technology (built-in tools like Narrator, osk and Magnifier, or third-party screen readers). The values tell Windows the program's name, which EXE to start and whether it may run on the lock/logon screen. Installers need admin rights to add entries. The Ease of Access Center lists everything registered here.
>
> **SOC NOTE**: Persistence/privilege-escalation spot (T1546.008): a fake AT whose StartExe points to malware and is enabled in Configuration can run on the secure desktop as SYSTEM before logon. Audit subkeys and StartExe/ATExe paths; changes should coincide with software installs.
>

# purpose

Registers accessibility applications with the Ease of Access Center so they appear there and can run on the secure desktop. Installers must run elevated to add values.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | %SystemRoot%\System32\config\SOFTWARE |

# values

| value name | type | description |
| --- | --- | --- |
| `ApplicationName` | REG_SZ | Localized application name from a resource file; shown in the Ease of Access Center (mandatory). |
| `ATExe` | REG_SZ | Executable name Windows uses to determine whether the AT is running (mandatory). |
| `CopySettingsToLockedDesktop` | REG_DWORD | 1 copies the AT's settings from HKCU\...\ATConfig to the locked desktop. |
| `Description` | REG_SZ | Localized description (<512 chars); also used to tell users about secure desktop behaviour (mandatory). |
| `Profile` | REG_SZ | XML listing accommodations so the AT is categorized correctly (mandatory). |
| `PassiveAutoStartBehavior` | REG_DWORD | 0 = legacy auto-start; 1 = start once per session only if "start after sign-in" is checked. |
| `SecureDesktopAccommodation` | REG_SZ | Alternate AT to run on the secure desktop: another key name, osk, magnifierpane, Narrator, or none. |
| `SimpleProfile` | REG_SZ | One- or two-word classification, e.g. ScreenReader or Magnification (mandatory). |
| `StartExe` | REG_SZ | Full path of the executable used to launch the AT (mandatory). |
| `StartParams` | REG_SZ | Command-line parameters passed at launch. |
| `TerminateOnDesktopSwitch` | REG_DWORD | Absent or non-zero runs the AT in a job restarted on each desktop switch; 0 disables that. |

# subkeys

| subkey | description |
| --- | --- |
| `<CompanyName_ProductName_v#>` | One key per registered AT, e.g. `Contoso_Screen Reader_v2.0`. |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs"` | List the key's values. |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs" /s /v StartExe` | Show the launch path of every registered AT. |
