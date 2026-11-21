---
created: 2026-11-21
fullpath: 'C:\Windows\System32\mshta.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - lolbin
  - hta
aliases:
  - "mshta.exe"
  - "Microsoft HTML Application Host"
  - "HTML Application Host"
url:
  - https://learn.microsoft.com/security-updates/securitybulletins/2006/ms06-013
  - https://learn.microsoft.com/security-updates/securitybulletins/2005/ms05-016
  - https://learn.microsoft.com/defender-endpoint/whats-new-in-microsoft-defender-endpoint
  - https://learn.microsoft.com/defender-endpoint/migrating-asr-rules
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/design/script-enforcement
  - https://learn.microsoft.com/azure/defender-for-cloud/alerts-windows-machines
  - https://learn.microsoft.com/windows/iot/iot-enterprise/whats-new/windows-11-iot-enterprise-26h2
---

**fullpath**:C:\Windows\System32\mshta.exe

# description

`mshta.exe` is the Microsoft HTML Application Host, a signed Windows binary in `%windir%\system32` that runs HTML Applications (.hta files). It is used by tools such as MDT LiteTouch (Wizard.hta). Microsoft security guidance recommends restricting it with App Control, exploit protection, or blocking its outbound connections.

## simple description

> ### 2026-11-21 Claude said
> mshta.exe runs .hta files, which are web pages (HTML plus VBScript/JScript) that execute as full desktop programs with the user's rights.
> It is a legitimate, Microsoft-signed part of Windows that very few modern business apps still need.
> Because it can run script from a file or URL, it is one of the most abused Windows binaries.
>
> **SOC NOTE**: Classic LOLBin (T1218.005 Mshta): used in phishing, ClickFix fake CAPTCHA campaigns and Lumma Stealer to run remote HTA/script, often spawning powershell/cmd. Hunt for mshta with http(s) URLs, `javascript:`/`vbscript:` arguments, network connections, or child processes; Defender for Cloud alerts on 'suspicious combination of HTA and PowerShell'.
>

# purpose

Hosts and executes HTML Applications. When any App Control UMCI policy is active, mshta.exe blocks all code execution. In Windows 11 IoT Enterprise 26H2, inline scripts passed directly to MSHTA.exe no longer execute due to security hardening. Microsoft Secure Score recommends blocking outbound network connections from mshta.exe, and exploit protection can stop it launching child processes such as cmd.exe, powershell.exe and regsvr32.exe.

# typical use cases

| usage | description |
| --- | --- |
| `%windir%\system32\mshta.exe /unregister` | Removes the .hta file association so double-clicked HTA files no longer open in the HTML Application Host (security bulletin workaround). |
| `%windir%\system32\mshta.exe /register` | Re-registers mshta.exe as the HTA handler, undoing the workaround. |
| `cacls %windir%\system32\mshta.exe /d everyone` | Denies the Everyone group access to mshta.exe, stopping HTA files from working. |

# options

| option | description |
| --- | --- |
| `/register` | Registers mshta.exe as the handler for HTML Applications. |
| `/unregister` | Unregisters mshta.exe; users are prompted to choose a program for .hta files. |
