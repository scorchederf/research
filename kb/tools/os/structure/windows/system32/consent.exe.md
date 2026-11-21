---
created: 2026-11-21
fullpath: 'C:\Windows\System32\consent.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - uac
aliases:
  - consent.exe
  - Consent UI
  - Consent User Interface
url:
  - https://learn.microsoft.com/windows/win32/uxguide/winenv-uac
  - https://learn.microsoft.com/windows/security/application-security/application-control/user-account-control/how-it-works
  - https://learn.microsoft.com/windows-server/security/user-account-control/how-user-account-control-works
  - https://learn.microsoft.com/security-updates/securitybulletins/2010/ms10-100
---

**fullpath**:C:\Windows\System32\consent.exe

# description

The Consent UI is part of User Account Control (UAC): with UAC enabled, protected administrators run with least privileges and self-elevate by giving explicit consent in the Consent UI, while standard users get the Credential UI. Prompts are shown on the secure desktop by default and are colour-coded by publisher (Windows, verified, unverified).

## simple description

> ### 2026-11-21 Claude said
> consent.exe draws the UAC "Do you want to allow this app to make changes?" prompt. It is launched by the Application Information service (AppInfo) when a program asks for admin rights, and it runs as SYSTEM on the secure desktop. It shows either a Yes/No consent prompt for admins or a username/password credential prompt for standard users. Users do not run it directly.
>
> **SOC NOTE**: Normal parent is svchost.exe (AppInfo); consent.exe from another path or parent is suspicious. UAC bypass techniques (T1548.002) elevate without spawning consent.exe, so an elevated child with no preceding consent.exe can be a clue. Fake UAC prompts on the normal desktop are used to phish credentials (T1056.002). EoP CVE-2010-3961 (MS10-100) abused the Consent UI.
>

# purpose

Provides the elevation prompt (consent prompt and credential prompt) for UAC so that administrative tasks such as installing software and drivers, changing system-wide settings or running admin tools require explicit approval. ShellExecute calls the Application Information service to show the prompt when CreateProcess returns ERROR_ELEVATION_REQUIRED.

# typical use cases

- Displayed automatically when an app requests elevation (Run as administrator, requireAdministrator manifest, UAC shield actions).
- Behaviour configured via the "User Account Control: Behavior of the elevation prompt..." and "Switch to the secure desktop when prompting for elevation" policies (secpol.msc / Group Policy).

# options

_Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_
