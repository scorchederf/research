---
created: 2026-11-21
fullpath: 'C:\Windows\System32\Msdt.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - troubleshooting
  - deprecated
aliases:
  - msdt.exe
  - Microsoft Support Diagnostic Tool
  - MSDT
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/msdt
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-msdt
---

**fullpath**:C:\Windows\System32\Msdt.exe

# description

Microsoft Support Diagnostic Tool (MSDT) invokes a troubleshooting pack at the command line or in a script and can enable options without user input. It is part of Windows and is deprecated.

## simple description

> ### 2026-11-21 Claude said
> MSDT runs Windows troubleshooting packs (for example, the network or printer troubleshooter) and can collect diagnostic data for support. It can be started by ID, by path to a diagnostic package or from a cab. Microsoft has deprecated it.
>
> **SOC NOTE**: Famous for Follina (CVE-2022-30190): Office documents invoked the ms-msdt: URL protocol to run PowerShell via sdiagnhost.exe (T1218 signed binary proxy execution). Hunt for msdt.exe spawned by Office apps, `IT_BrowseForFile` parameters, and children of sdiagnhost.exe. Results land in %LOCALAPPDATA%\Diagnostics.
>

# purpose

Run troubleshooting packs interactively or unattended, and collect diagnostic data for a support provider.

# typical use cases

| usage | description |
| --- | --- |
| `msdt /id <packagename>` | Run a built-in troubleshooter by ID. |
| `msdt /path <file.diagcab>` | Run a custom pack. |
| `msdt /dt <directory>` | View troubleshooting history. |

# options

| option    | description    |
| --- | --- |
| `/id <packagename>` | Specifies which diagnostic package to run. |
| `/path <directory \| .diagpkg file \| .diagcfg file>` | Specifies the full path to a diagnostic package; cannot be combined with `/id`, `/dci` or `/cab`. |
| `/dci <passkey>` | Prepopulates the passkey field when a support provider supplied one. |
| `/dt <directory>` | Displays the troubleshooting history in the specified directory. |
| `/af <answerfile>` | Specifies an XML answer file with responses to diagnostic interactions. |
| `/modal <ownerHWND>` | Makes the troubleshooting pack modal to a window designated by the parent HWND (decimal). |
| `/moreoptions <true \| false>` | Enables or suppresses the final screen asking to explore additional options. |
| `/param <parameters>` | Specifies interaction responses at the command line, similar to an answer file. |
| `/advanced` | Expands the advanced link on the Welcome page by default. |
| `/custom` | Prompts the user to confirm each possible resolution before it is applied. |
