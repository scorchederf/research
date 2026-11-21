---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wusa.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - windows-update
aliases:
  - wusa.exe
  - Windows Update Standalone Installer
  - WUSA
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/installing-updates-features-roles/command-line-switches-deploy-update-packages
  - https://learn.microsoft.com/troubleshoot/windows-server/installing-updates-features-roles/windows-update-standalone-installer-returns-error
---

**fullpath**:C:\Windows\System32\wusa.exe

# description

Wusa.exe is the Windows Update Standalone Installer, used to manually install or uninstall update packages (.msu) from the command line on Windows client and server. It uses the Windows Update Agent API, and the .msu extension is associated with it. Related tools include dism.exe for installing extracted .cab packages.

## simple description

> ### 2026-11-21 Claude said
> wusa.exe installs and removes Windows update packages (.msu files), for example when an admin manually applies a KB. It can run silently and can also uninstall a specific KB by number. It ships with Windows.
>
> **SOC NOTE**: Attackers may run `wusa /uninstall /kb:<n> /quiet /norestart` to remove security patches and reopen vulnerabilities (MITRE ATT&CK T1562.001 Impair Defenses). Historically `wusa /extract` was abused to write files into protected folders for UAC bypass/DLL hijacking (T1548.002). Check Application event log source Microsoft-Windows-WUSA and Setup event log for install/uninstall records.
>

# purpose

Manually install or uninstall Windows update packages from the command line. Installing an update on a remote machine through WUSA or the WUA APIs (for example over WinRM) isn't supported and returns 0x5 access denied; the workaround is to extract the .msu with `/extract` and install the .cab with dism.exe.

# typical use cases

| usage | description |
| --- | --- |
| `wusa.exe d:\934307\Windows6.0-KB934307-x86.msu /quiet` | Install an update package without user interaction. |
| `wusa <update> [/quiet] [/norestart \| /warnrestart:<seconds> \| /promptrestart \| /forcerestart] [/log:<file name>]` | General install syntax. |
| `wusa /uninstall /kb:<KB number> [/norestart] [/log:<file name>]` | Uninstall an update by KB number. |
| `winrs.exe -r:<computername> wusa.exe <update> /extract:<destination>` | Extract an .msu remotely so it can be installed with dism.exe. |

# options

| option | description |
| --- | --- |
| `/extract` | Extracts the update package contents to a destination folder. |
| `/help`, `/h`, `/?` | Displays a dialog box showing usage and all switches. |
| `/log:<file name>` | Turns on logging to the given file. |
| `/quiet` | Quiet mode without user interaction; restarts automatically if required. |
| `/norestart` | With `/quiet`: does not restart after install/uninstall even if required. |
| `/promptrestart` | With `/quiet`: prompts the user to restart if required. |
| `/forcerestart:<seconds>` | With `/quiet`: forcefully closes applications and restarts, even if not required. |
| `/warnrestart` | With `/quiet`: warns the user before restarting if required. |
| `/uninstall <update>` or `/uninstall /kb:<KB number>` | Removes the specified update by file name or KB number. |
