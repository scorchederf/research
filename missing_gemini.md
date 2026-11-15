# Valuable Missing Filepaths & Registry Keys for SOC Analysts

Your existing list (`filepaths_2.md`) is remarkably comprehensive, covering core NTFS artifacts, LOLBins, Event Logs, and persistence locations. Below is a curated list of **high-value forensic artifacts, LOLBins, and registry locations that are currently missing** from your list, along with why they are critical for SOC investigations and threat hunting.

---

## 1. Execution & Program Evidence

| Filepath / Registry Key | SOC & Forensic Value |
| :--- | :--- |
| `HKLM\SYSTEM\CurrentControlSet\Services\dam\State\UserSettings\<SID>` | **Desktop Activity Moderator (DAM):** Complements the `bam` key (which is in your list). Tracks background/desktop application execution times and full paths, especially useful on systems where BAM data has rolled over or for Modern/UWP apps. |
| `C:\Users\<username>\AppData\Local\Microsoft\Windows\Notifications\wpndatabase.db` | **Windows Push Notifications Database:** Contains historical toast notifications (emails, chat messages, system alerts, browser notifications). Crucial for identifying phishing lures, initial access vectors, or suspicious alerts shown to the user even after the source app is closed. |
| `C:\Windows\System32\AppHostSvc` / `C:\Windows\System32\sru` (Specific sub-artifacts like `C:\Windows\AppCompat\Programs\RecentFileCache.bcf`) | **RecentFileCache.bcf:** Found on older Windows/Server OS versions (Windows 7 / Server 2008 R2) prior to `Amcache.hve`. Tracks recently executed binaries and is a primary artifact for proving execution on legacy servers. |
| `C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent\*.lnk` | **Individual LNK (Shortcut) Files:** While you have `AutomaticDestinations` and `CustomDestinations`, the standalone `.lnk` files in the `Recent` folder contain crucial metadata: target file MACB timestamps, volume serial numbers, NetBIOS names of remote file shares (proving lateral movement/data staging), and local paths. |

---

## 2. Persistence & Hijacking Locations

| Filepath / Registry Key | SOC & Forensic Value |
| :--- | :--- |
| `HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce` & `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce` | **RunOnce Persistence:** Your list includes `Run`, but attackers frequently use `RunOnce` (or `*RunOnce` with an asterisk to execute even in Safe Mode) to establish persistence that cleans itself up after execution or triggers on the next reboot. |
| `HKCU\Software\Classes\CLSID\{<CLSID>}\InprocServer32` | **User-Level COM Hijacking:** Your list includes the `HKLM` version, which requires admin rights. Attackers heavily favor the `HKCU` hive to hijack legitimate COM objects without needing elevated privileges, bypassing UAC and achieving stealthy persistence. |
| `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs` | **Accessibility Feature Persistence:** Used alongside `sethc.exe` or `utilman.exe` (which you have), attackers register custom Assistive Technology (AT) binaries here so Windows automatically launches their payload at the logon screen when accessibility shortcuts are pressed. |
| `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\BootExecute` | **BootExecute / Native Persistence:** Controls native executables (like `autochk.exe`) that run before the Windows subsystem and EDR/AV agents fully initialize. Abuse here indicates sophisticated, pre-OS boot persistence. |
| `C:\Users\<username>\AppData\Local\Microsoft\OneDrive\StandaloneUpdater` / `C:\Users\<username>\AppData\Local\Programs` | **User-Writable App Execution / DLL Side-Loading:** Common staging ground for DLL side-loading attacks (e.g., dropping a legitimate signed binary alongside a malicious `version.dll` or `dbghelp.dll`) because standard users have full write permissions here. |

---

## 3. Credential Access & Defense Evasion

| Filepath / Registry Key | SOC & Forensic Value |
| :--- | :--- |
| `HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL` | **SChannel / TLS Configuration:** Attackers or poorly configured tools may modify SChannel settings to downgrade TLS protocols or enable weak ciphers to facilitate Man-in-the-Middle (MitM) interception of credentials and traffic. |
| `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LocalAccountTokenFilterPolicy` | **UAC Remote Restrictions:** When set to `1`, this disables UAC remote restrictions, allowing local administrator accounts (other than the built-in RID 500 Admin) to perform Pass-the-Hash (PtH) and remote administration over SMB/RPC. A huge red flag for lateral movement preparation. |
| `C:\Windows\System32\rundll32.exe` (specifically monitoring `comsvcs.dll, MiniDump`) / `C:\Windows\Temp\*.dmp` | **LSASS Memory Dumping:** While `comsvcs.dll` is in your list, tracking the standard output paths where attackers dump `lsass.exe` (such as `C:\Windows\Temp\debug.out` or `lsass.dmp`) is essential for detecting credential harvesting. |
| `C:\ProgramData\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt` | **SYSTEM / Service Account PowerShell History:** You included the `<username>` path, which covers interactive users. However, if an attacker elevates to `NT AUTHORITY\SYSTEM` (via PsExec or a service) and runs interactive PowerShell, the command history is saved in the service profile path (`C:\Windows\System32\config\systemprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`). |

---

## 4. LOLBins & Living-off-the-Land Binaries (Missing from List)

| Filepath | SOC & Forensic Value |
| :--- | :--- |
| `C:\Windows\System32\winget.exe` | **Windows Package Manager:** You have the `WindowsApps` user path for `winget.exe`, but on newer Windows 10/11 builds, it can also be invoked or aliased via System32/AppExecutionAliases. Attackers use it to download and install unapproved software or RMM (Remote Monitoring and Management) tools silently. |
| `C:\Windows\System32\msedge.exe` / `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` | **Headless Browser Abuse:** You have the 64-bit `Program Files` path, which is standard now, though 32-bit `Program Files (x86)` is still heavily deployed on enterprise endpoints. Attackers use Edge with `--headless --dump-dom` to download payloads or bypass proxy/firewall rules that only allow browser user-agents. |
| `C:\Windows\System32\schtasks.exe` vs `C:\Windows\SysWOW64\schtasks.exe` | **32-bit WOW64 Redirection Binaries:** You listed `C:\Windows\SysWOW64` as a directory, which is great. Specifically monitoring `C:\Windows\SysWOW64\cmd.exe`, `powershell.exe`, and `rundll32.exe` is vital because attackers often spawn 32-bit processes from 64-bit malware (or vice versa) to evade EDR user-mode hooks that only monitor the 64-bit `System32` binaries. |
| `C:\Windows\System32\certutil.exe` Cache: `C:\Users\<username>\AppData\LocalLow\Microsoft\CryptnetUrlCache\Content` & `MetaData` | **CryptnetUrlCache:** Whenever `certutil.exe -urlcache` (or any Windows API using WinINet/Crypt32) downloads a malicious payload or C2 certificate, Windows caches the downloaded file in `Content` and the source URL/timestamp in `MetaData`. Even if the attacker deletes the payload, forensic proof of the exact URL and file remains here! |
| `C:\Windows\System32\wbem\MOF` | **WMI MOF Staging Folder:** You have `wbem\Logs` and `wbem\Repository`. The `MOF` directory is where Managed Object Format files are placed; if an attacker drops a malicious `.mof` file here (or compiles it via `mofcomp.exe`), it can trigger WMI event consumer persistence. |

---

## 5. Browser, Cloud & Data Exfiltration Artifacts

| Filepath | SOC & Forensic Value |
| :--- | :--- |
| `C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default\History` (and `Login Data`, `Cookies`, `Web Data`) | **Google Chrome Forensic Artifacts:** Your list includes Edge (`User Data\Default`), which is Chromium-based, but Chrome remains the #1 third-party browser in enterprises. These SQLite databases hold download histories (showing initial payload URLs), visited sites, and saved credentials targeted by infostealers. |
| `C:\Users\<username>\AppData\Local\Microsoft\Edge\User Data\Default\Network\Cookies` & `Login Data` | **Browser Credential & Session Theft Targets:** Infostealer malware (like RedLine, Lumma, Vidar) specifically targets these exact files to steal active session cookies (bypassing MFA) and saved passwords. File access telemetry on these paths is a top-tier detection rule for infostealers. |
| `C:\Users\<username>\AppData\Local\Microsoft\OneDrive\logs\Personal` & `Business1` | **OneDrive Sync Logs:** Attackers increasingly use OneDrive (or Rclone) to exfiltrate stolen corporate data. OneDrive logs record the names of files synced to external accounts and the account IDs associated with the sync. |
| `C:\ProgramData\AnyDesk` / `C:\Users\<username>\AppData\Roaming\AnyDesk` (and `ScreenConnect`, `TeamViewer`, `RustDesk`) | **RMM (Remote Monitoring & Management) Tool Artifacts:** Ransomware affiliates heavily abuse legitimate RMM tools for persistent C2. Monitoring default installation and config paths in `ProgramData` and `AppData` catches unauthorized RMM deployments quickly. |