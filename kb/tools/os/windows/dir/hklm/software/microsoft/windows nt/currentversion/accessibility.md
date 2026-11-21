---
created: 2026-11-21
fullpath: 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Accessibility'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Accessibility
url:
  - https://learn.microsoft.com/windows/win32/winauto/ease-of-access---assistive-technology-registration
---

**fullpath**:HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Accessibility

# description

Machine-wide registry key for the Windows Ease of Access Center. Its ATs subkey is where accessibility (assistive technology) applications register so they appear in the Ease of Access Center and can run on the secure desktop. Per-user counterparts live under HKCU\Software\Microsoft\Windows NT\CurrentVersion\Accessibility.

## simple description

> ### 2026-11-21 Claude said
> This key holds the machine-wide settings for Windows accessibility tools such as Narrator, Magnifier and On-Screen Keyboard, and for third-party screen readers that register here. The Ease of Access Center reads it to know which tools exist and how to launch them, including on the logon/lock screen. Installers write to it with admin rights.
>
> **SOC NOTE**: Because registered ATs can launch on the secure (logon) desktop as SYSTEM, a malicious ATs entry gives pre-logon code execution (T1546.008 Accessibility Features). Watch for new subkeys under ATs whose StartExe points outside Program Files/System32.
>

# purpose

Parent key for Ease of Access Center assistive technology registration; installers create subkeys under ATs with elevated privileges.

# hive

| property | value |
| --- | --- |
| hive | HKLM |
| scope | machine-wide |
| backing file | %SystemRoot%\System32\config\SOFTWARE |

# values

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# subkeys

| subkey | description |
| --- | --- |
| `ATs` | Holds one key per registered accessibility application, named "CompanyName_ProductName_v#". |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Accessibility"` | List the key's values. |
| `reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Accessibility" /s` | List the key and all subkeys, including ATs registrations. |
