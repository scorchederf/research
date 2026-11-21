---
created: 2026-11-21
fullpath: 'C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.4-0\MpCmdRun.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - defender
  - lolbin
aliases:
  - MpCmdRun.exe
  - Microsoft Defender Antivirus command-line utility
url:
  - https://learn.microsoft.com/defender-endpoint/command-line-arguments-microsoft-defender-antivirus
  - https://learn.microsoft.com/defender-endpoint/microsoft-defender-antivirus-exclusions-configure
---

**fullpath**:C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.4-0\MpCmdRun.exe

# description

MpCmdRun.exe is the Microsoft Defender Antivirus command-line tool for running scans, managing security intelligence updates, collecting diagnostics and configuring Defender. It lives in `%ProgramFiles%\Windows Defender` and, in its latest version, in `%ProgramData%\Microsoft\Windows Defender\Platform\<antimalware platform version>` (here 4.18.2008.4-0). It must be run elevated; related tooling includes the Defender PowerShell cmdlets.

## simple description

> ### 2026-11-21 Claude said
> MpCmdRun.exe is the command-line front end for Microsoft Defender Antivirus. Admins and scripts use it to start scans, update signatures, check exclusions and collect support logs. Each Defender platform update installs a new copy under a versioned folder in ProgramData. The 4.18.2008.4-0 folder is an old platform version from August 2020.
>
> **SOC NOTE**: Known LOLBin: older builds (including 4.18.2008.x) allowed `-DownloadFile -url <url> -path <file>` for ingress tool transfer (T1105); attackers also use `-RemoveDefinitions -All` to strip signatures (T1562.001) and `-CheckExclusion` to discover exclusions. Alert on MpCmdRun with network download, definition removal or launched by non-SYSTEM/unusual parents; Defender events 5007/2030 and MPLog help reconstruct activity.
>

# purpose

Run scans, update or roll back signatures/platform, manage quarantine, trace and collect diagnostic data for Microsoft Defender Antivirus.

# typical use cases

| usage | description |
| --- | --- |
| `MpCmdRun.exe -Scan -ScanType 2` | Start a full antivirus scan. |
| `MpCmdRun.exe -CheckExclusion -Path C:\Data\Test` | Verify whether a path is excluded from scanning. |
| `MpCmdRun.exe -GetFiles` | Collect Defender support logs into MpSupportFiles.cab. |
| `MpCmdRun.exe -SignatureUpdate -MMPC` | Download updates directly from the Microsoft Malware Protection Center. |
| `MpCmdRun.exe -Restore -ListAll` | List all quarantined items. |
| `MpCmdRun.exe -ValidateMapsConnection` | Verify the device can reach the Defender cloud service. |

# options

| option | description |
| --- | --- |
| `-?` or `-h` | Displays all available commands and options. |
| `-AddDynamicSignature -Path <path>` | Loads dynamic security intelligence from the specified location. |
| `-CaptureNetworkTrace -Path <path>` | Captures Network Protection input to the path; `-Path` without value stops tracing. |
| `-CheckExclusion -Path <path>` | Verifies whether the file or path is excluded from scanning. |
| `-DeviceControl -TestPolicyXml <file> -Groups or -Rules` | Validates a Device Control groups (`-Groups`) or rules (`-Rules`) policy XML. |
| `-DisplayECSConnection` | Displays URLs used to connect to the Experimentation and Configuration Service. |
| `-GetFiles [-DlpTrace] [-SupportLogLocation <RootPath>]` | Generates MpSupportFiles.cab; optionally includes DLP traces or copies to a central location. |
| `-GetFilesDiagTrack` | Saves support logs to `%TEMP%\DiagOutputDir\MpSupportFiles.cab`. |
| `-HeapSnapshotConfig -Enable or -Disable -Pid <id> or -Name <exe>` | Enables or disables heap snapshot tracing for a process. |
| `-ListAllDynamicSignatures` | Lists SignatureSet IDs of loaded dynamic security intelligence. |
| `-ListCustomASR` | Lists custom attack surface reduction rules. |
| `-OSCA` | Verifies whether OS Copy Acceleration is enabled. |
| `-RegisterWmiSchema` | Re-registers the MpProtection MOF schema. |
| `-RemoveDefinitions [-All \| -DynamicSignatures \| -Engine]` | Restores previous signatures, removes dynamic updates, or restores the previous engine. |
| `-RemoveDynamicSignature -SignatureSetID <id>` | Removes the specified dynamic security intelligence update. |
| `-ResetPlatform` | Resets platform binaries to `%ProgramFiles%\Windows Defender`. |
| `-Restore [-ListAll \| -Name <name> [-All] \| -FilePath <path>] [-Path <path>]` | Lists or restores quarantined items; `-Output <filename>` writes item names to a file. |
| `-RevertEdr -ToVersion <Inbox\|Previous>` | Reverts EDR binaries (platform 4.18.26030.3011 or later). |
| `-RevertPlatform` | Reverts to the previously installed Defender platform. |
| `-Scan [-ScanType <0-3>]` | Scans for malware; 0 default, 1 quick, 2 full, 3 custom. |
| `-BootSectorScan` | Custom scans only: enables boot sector scanning. |
| `-Cancel` | Cancels active quick or full scans. |
| `-CpuThrottling` | Maximum CPU usage percentage (default 50). |
| `-DisableRemediation` | Custom scans only: ignore exclusions, scan archives, no actions or event log entries. |
| `-File <path>` | Custom scans only: file or folder to scan. |
| `-ReturnHR` | Return the actual HRESULT instead of 0 or 2. |
| `-Timeout <days>` | Scan timeout; default 7 for full, 1 for others, max 30. |
| `-SignatureUpdate [-UNC <path> \| -MMPC]` | Checks for new security intelligence from a UNC share or the MMPC. |
| `-Trace [-Grouping <value>] [-Level <value>]` | Traces Antimalware Service actions to `MPTrace-*.bin`. |
| `-TrustCheck -File <file>` | Checks the trust status of the file. |
| `-ValidateMapsConnection` | Verifies connectivity to the Defender cloud service (Windows 10 1703+). |
| `-WdEnable` | Re-enables Microsoft Defender Antivirus. |
