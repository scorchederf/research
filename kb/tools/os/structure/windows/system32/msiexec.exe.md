---
created: 2026-11-21
fullpath: 'C:\Windows\System32\msiexec.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - installer
aliases:
  - msiexec.exe
  - msiexec
  - Windows Installer
  - Microsoft Standard Installer
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/msiexec
  - https://learn.microsoft.com/windows/win32/msi/standard-installer-command-line-options
  - https://learn.microsoft.com/windows/win32/msi/command-line-options
---

**fullpath**:C:\Windows\System32\msiexec.exe

# description

msiexec.exe is the Windows Installer executable that interprets packages and installs products, providing the means to install, modify, and perform operations on Windows Installer from the command line. It ships with Windows as part of Windows Installer. It sets an error level on return that corresponds to system error codes; command-line options are case-insensitive.

## simple description

> ### 2026-11-21 Claude said
> msiexec.exe is the built-in Windows program that installs, repairs, patches and uninstalls software packaged as .msi or .msp files. Whenever you double-click an MSI, msiexec does the work in the background, often with a SYSTEM-level service instance. Administrators use it with switches like /i and /qn for silent deployments. It can also register or unregister DLLs.
>
> **SOC NOTE**: msiexec is a classic LOLBin (MITRE ATT&CK T1218.007): attackers install remote MSIs (`msiexec /q /i http://...`) or load DLLs with `/y`/`/z`. Watch for msiexec making network connections, spawning cmd/powershell, running from unusual parents (Office, browsers), and MsiInstaller events 1033/1034/11707/11724 in the Application log. Malicious MSIs also abuse AlwaysInstallElevated (T1548.002).
>

# purpose

Provides the means to install, modify, and perform operations on Windows Installer from the command line: install, advertise, uninstall, repair, patch, configure UI level, restart behavior, logging, and set public properties.

# typical use cases

- Normal install: `msiexec.exe /i "C:\example.msi"`.
- Silent install with no UI: `msiexec.exe /i "C:\example.msi" /qn`.
- Install without rebooting: `msiexec.exe /i "C:\example.msi" /norestart`.
- Verbose logging: `msiexec.exe /i "C:\example.msi" /L*V "C:\package.log"`.
- Apply a patch: `msiexec.exe /p "C:\MyPatch.msp"`.
- Force full repair: `msiexec.exe /fa {ProductCode}`.
- Uninstall: `msiexec /x msisample.msi`.

# options

| option    | description    |
| --- | --- |
| `/i` | Specifies normal installation. |
| `/a` | Specifies administrative installation. |
| `/ju` | Advertise the product to the current user. |
| `/jm` | Advertise the product to all users. |
| `/j/g` | Specifies the language identifier used by the advertised package. |
| `/j/t` | Applies transform to the advertised package. |
| `/x` | Uninstalls the package. |
| `<path_to_package>` | Location and name of the installation package file. |
| `/quiet` | Quiet mode; no user interaction required. |
| `/passive` | Unattended mode; installation only shows a progress bar. |
| `/qn` | No UI during the installation process. |
| `/qn+` | No UI except a final dialog box at the end. |
| `/qb` | Basic UI during the installation process. |
| `/qb+` | Basic UI including a final dialog box at the end. |
| `/qr` | Reduced UI experience during installation. |
| `/qf` | Full UI experience during installation. |
| `/norestart` | Stops the device from restarting after installation completes. |
| `/promptrestart` | Prompts the user if a reboot is required. |
| `/forcerestart` | Restarts the device after installation completes. |
| `/li` | Logging; includes status messages. |
| `/lw` | Logging; includes non-fatal warnings. |
| `/le` | Logging; includes all error messages. |
| `/la` | Logging; includes when an action started. |
| `/lr` | Logging; includes action-specific records. |
| `/lu` | Logging; includes user request information. |
| `/lc` | Logging; includes initial UI parameters. |
| `/lm` | Logging; includes out-of-memory or fatal exit information. |
| `/lo` | Logging; includes out-of-disk-space messages. |
| `/lp` | Logging; includes terminal properties. |
| `/lv` | Logging; includes verbose output. |
| `/lx` | Logging; includes extra debugging information. |
| `/l+` | Logging; appends to an existing log file. |
| `/l!` | Logging; flushes each line to the log file. |
| `/l*` | Logs all information except verbose (/lv) or extra debugging (/lx). |
| `<path_to_logfile>` | Location and name of the output log file. |
| `/p` | Installs a patch. Silent installs must also set REINSTALLMODE=ecmus and REINSTALL=ALL. |
| `/update` | Install patches option; separate multiple updates with a semicolon. |
| `/package` | Installs or configures a product. |
| `/fp` | Repairs if a file is missing. |
| `/fo` | Repairs if a file is missing or an older version is installed. |
| `/fe` | Repairs if a file is missing or an equal or older version is installed. |
| `/fd` | Repairs if a file is missing or a different version is installed. |
| `/fc` | Repairs if a file is missing or checksum doesn't match. |
| `/fa` | Forces all files to be reinstalled. |
| `/fu` | Repairs all required user-specific registry entries. |
| `/fm` | Repairs all required computer-specific registry entries. |
| `/fs` | Repairs all existing shortcuts. |
| `/fv` | Runs from source and re-caches the local package. |
| `/y` | Calls DllRegisterServer to self-register the specified module (from Msiexec.exe Command-Line Options). |
| `/z` | Calls DllUnRegisterServer to unregister the specified module (from Msiexec.exe Command-Line Options). |
| `/c` | Advertises a new instance of the product; used with /t (from Msiexec.exe Command-Line Options). |
| `/n` | Specifies a particular instance of the product by product code (from Msiexec.exe Command-Line Options). |
| `/?` or `/h` | Displays copyright information for Windows Installer (from Msiexec.exe Command-Line Options). |
| `/help` | Displays correct usage of msiexec including all switches (Standard Installer option). |
