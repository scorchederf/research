| fullpath | perplexitysays |
|---|---|
|C:\$Extend\$UsnJrnl|NTFS USN Journal: records file creation, deletion, renaming and moves with timestamps across the volume. Gold for proving an attacker staged tools, deleted files or renamed payloads even after the files are gone.|
|C:\$LogFile|NTFS transaction journal holding very recent metadata changes. Short lived, but useful in deep forensics to reconstruct what happened to files minutes before acquisition.|
|C:\$MFT|Master File Table: one record per file and folder on the volume with timestamps. Comparing $STANDARD_INFORMATION and $FILE_NAME timestamps is the classic way to spot timestomping. Usually one of the first artifacts pulled in triage.|
|C:\$Recycle.Bin\<SID>|Per user Recycle Bin. The $I files map deleted files back to their original path, size and deletion time, so great for proving what a user (or attacker) deleted.|
|C:\_SMSTaskSequence|SCCM task sequence working folder during OS imaging. Frequently left behind with world-readable scripts and variables that can contain domain join or service account credentials, so treat any leftover content as sensitive.|
|C:\hiberfil.sys|Hibernation file containing a compressed snapshot of RAM from last hibernate. Can be carved for passwords, encryption keys and memory resident malware.|
|C:\inetpub\logs\LogFiles\W3SVC<n>|IIS access logs. First stop when hunting webshells: look for POSTs to odd .aspx/.asp files, single source IPs, scanning patterns, and requests around suspicious file write times.|
|C:\inetpub\wwwroot|Default IIS web root. Newly dropped .aspx, .asp or .ashx files here often mean a webshell. Correlate file creation times with entries in the W3SVC logs.|
|C:\pagefile.sys|The swap file; contains fragments of memory paged to disk. Can yield credentials, URLs, file contents and other artifacts and is worth acquiring on important cases.|
|C:\Program Files (x86)\Microsoft Endpoint Manager\AdminConsole\AdminUILog|SCCM admin console logs. Show what an administrator did in the console, so if an admin machine is compromised these reveal attacker actions performed through the console.|
|C:\Program Files (x86)\Microsoft Intune Management Extension|Install folder for the Intune Management Extension, which runs scripts pushed from Intune as SYSTEM. Attackers who abuse Intune will have activity here, and the folder correlates with the IME logs in ProgramData.|
|C:\Program Files (x86)\Microsoft Intune Management Extension\AgentExecutor.exe|Component of the Intune Management Extension that executes PowerShell scripts as SYSTEM. Unexpected child processes or command lines from this binary are a high value detection point for Intune abuse and lateral movement.|
|C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\Excel.exe|Excel executable. Excel spawning powershell.exe, cmd.exe, wscript or certutil is the classic malicious macro pattern; also watch for network connections from Excel.|
|C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\MSAccess.exe|Microsoft Access. Same macro and child process abuse as Excel, and because few users legitimately open Access, any execution often deserves a look.|
|C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\MSOHTMED.exe|Office HTML editor, rarely seen in normal use. Unexpected execution, especially with child processes, is suspicious.|
|C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\MSPUB.exe|Microsoft Publisher. Macro abuse is possible here too; check for child processes such as scripts or PowerShell.|
|C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\Outlook.exe|Outlook client. Abuse patterns include malicious rules, the VbaProject.OTM macro backdoor and COM abuse. Outlook spawning script interpreters is suspicious.|
|C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\Powerpnt.exe|PowerPoint. Macro enabled presentations can spawn child processes just like Word and Excel, so alert on script or shell children.|
|C:\Program Files (x86)\Microsoft Office 16\ClientX86\Root\Office16\ProtocolHandler.exe|Office URI protocol handler. Abused in phishing chains (for example search-ms and WebDAV style links), so check its parent process and any URL arguments.|
|C:\Program Files (x86)\Microsoft Office\Office14\Visio.exe|Visio 2010. Macro abuse vector, and the presence of Office 2010 itself is notable because it is long out of support.|
|C:\Program Files (x86)\Microsoft Office\Office14\WinProj.exe|Microsoft Project 2010. Another macro capable Office app; look for child processes if it runs.|
|C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\Bin\ECMangen.exe|Windows SDK event collector manifest generator. Rarely run on end user machines, so execution is worth a second look.|
|C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\bin\NETFX <version> Tools\xsd.exe|XML schema definition tool from the .NET SDK. Listed as a LOLBin style binary that can be abused for code execution or compilation; rarely run by end users.|
|C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.8 Tools\wfc.exe|Windows Workflow Compiler from the .NET SDK. Can compile and run workflow markup containing C#, so it is a known LOLBin on developer machines.|
|C:\Program files (x86)\Microsoft SQL Server\100\Tools\Binn\sqlps.exe|SQL Server PowerShell host (SQL 2008). Gives an attacker a PowerShell like runner that can bypass some PowerShell logging and restrictions, so execution is suspicious off admin workflows.|
|C:\Program files (x86)\Microsoft SQL Server\130\Tools\Binn\sqlps.exe|SQL Server PowerShell host (SQL 2016). Same story: a mini PowerShell environment attackers can abuse while dodging normal PowerShell monitoring.|
|c:\Program Files (x86)\Microsoft Visual Studio\2017\Community\MSBuild\15.0\Bin\Roslyn\csi.exe|C# Interactive from Visual Studio. Executes inline C# scripts and is a known LOLBin on hosts with a dev toolset installed.|
|C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os64\OpenConsole.exe|Console host shipped with Visual Studio ServiceHub. Unexpected locations, parents or renamed copies are suspicious since attackers like signed console binaries to blend in.|
|C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\Extensions\Microsoft\Web Tools\ProjectSystem\VSIISExeLauncher.exe|Visual Studio helper that launches IIS Express for debugging web projects. Expected on dev machines only; odd elsewhere.|
|C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\Launch-VsDevShell.ps1|Script that sets up the Visual Studio developer shell. Running it outside development workflows is unusual.|
|c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\FSharp\fsianycpu.exe|F# Interactive from Visual Studio. Executes F# scripts; almost never used legitimately outside developers, so treat as a LOLBin on servers and workstations.|
|c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\Extensions\Microsoft\LiveShare\Agent\vsls-agent.exe|Visual Studio Live Share agent, which allows remote collaborative sessions into a dev environment. Check that use is authorised because it is effectively a remote access channel.|
|C:\Program Files (x86)\Microsoft Visual Studio\Installer\Feedback\dump64.exe|Visual Studio feedback tool that can create dumps. Rarely run interactively; watch for abuse as a process dump utility.|
|C:\Program Files (x86)\Microsoft\Copilot\Application\mscopilot.exe|Microsoft Copilot app. New binary, so baseline what normal looks like; unexpected network destinations or parentage deserve review.|
|C:\Program Files (x86)\Microsoft\Copilot\Application\mscopilot_proxy.exe|Proxy component of the Copilot app. Same guidance: verify it is talking to expected Microsoft endpoints and is launched from the normal app path.|
|C:\Program Files (x86)\Microsoft\DefaultPack\DefaultPack.exe|Microsoft DefaultPack component. Rarely seen; treat unexpected execution or network activity cautiously.|
|C:\Program Files (x86)\Microsoft\Edge\Application\114.0.1823.43\msedgewebview2.exe|WebView2 runtime browser. Malware abuses it to render phishing pages or C2 traffic inside a signed Microsoft process, so watch for odd parent processes and unusual network destinations.|
|C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe|Shim/proxy executable for Edge. Known proxy execution LOLBin; rarely invoked directly by users.|
|C:\Program Files (x86)\Windows Kits\10\App Certification Kit\appcert.exe|Windows App Certification Kit tool. Can be abused to load or execute binaries, another SDK LOLBin that rarely runs on production hosts.|
|C:\Program Files (x86)\Windows Kits\10\bin\10.0.16299.0\x86\mftrace.exe|Media Foundation trace tool from the SDK. Documented LOLBin that can spawn processes.|
|C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x86\AccChecker\AccCheckConsole.exe|Accessibility checker console tool from the SDK. Appears on LOLBin lists for executing code; rare on non dev machines.|
|c:\Program Files (x86)\Windows Kits\10\bin\<version>\arm64\UIAVerify\VisualUiaVerifyNative.exe|UI Automation verification tool from the SDK. LOLBin capable of loading DLLs and interacting with other processes; uncommon in normal use.|
|C:\Program Files (x86)\Windows Kits\10\bin\<version>\x64\vshadow.exe|VSS sample tool from the SDK that creates volume shadow copies. Attackers use shadow copies to grab locked files like ntds.dit and the SAM hive, so execution on servers or DCs is high signal.|
|C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\adplus.exe|Debugger crash dump tool from the Windows SDK debuggers. Can dump process memory including lsass, which means credential theft.|
|C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe|Command line debugger. Can attach to and dump any process including lsass; check who ran it and why.|
|C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\dbgsrv.exe|Debugging server that accepts remote debug connections. Rare in production and a suspicious remote access channel.|
|C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\ntsd.exe|NT symbolic debugger, the oldest MS command line debugger. Like cdb it can dump process memory; watch for use against lsass.|
|C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\remote.exe|Remote debugging helper. Any use on servers should be justified.|
|C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe|GUI debugger. Same risk: capable of dumping lsass memory for credential theft.|
|C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\logger.exe|Debugger logging extension. Rarely used; minor risk but unusual on non dev boxes.|
|C:\Program Files\Azure Advanced Threat Protection Sensor\<version>|Install folder for the Microsoft Defender for Identity sensor (Azure ATP). Tampering with files or the service here blinds identity focused detections for the domain, so monitor closely on DCs.|
|C:\Program Files\dotnet\dotnet.exe|.NET runtime host that can run arbitrary .NET assemblies. Watch for unusual DLL loads, odd working directories or network connections from dotnet.exe.|
|C:\Program Files\dotnet\sdk\<version>\FSharp\fsi.exe|F# Interactive shipped with the .NET SDK. Script execution LOLBin; unexpected on production hosts.|
|C:\Program Files\dotnet\shared\Microsoft.NETCore.App\<version>\createdump.exe|.NET dump utility that creates memory dumps of processes. Like other dumpers, usable against lsass for credential theft.|
|C:\Program Files\IIS\Microsoft Web Deploy V2\msdeploy.exe|Web Deploy tool for IIS. Can push packages and execute commands against remote IIS servers, a documented LOLBin for lateral movement and execution.|
|C:\Program Files\Internet Explorer\Extexport.exe|Internet Explorer export utility. LOLBin: passing an arbitrary path makes it load and run a DLL.|
|C:\Program Files\Internet Explorer\iediagcmd.exe|IE diagnostics command. Rarely used; appears on LOLBin lists, so unexpected execution is suspicious.|
|C:\Program Files\Microsoft Azure AD Sync|Install folder of Entra Connect (Azure AD Connect) sync. High value host: the sync service account and password hash sync are prime targets for credential theft and tenant wide compromise.|
|C:\Program Files\Microsoft Configuration Manager\Logs|SCCM site server logs. Useful both for attacker recon of your deployment and for tracing malicious packages or scripts pushed through ConfigMgr.|
|C:\Program Files\Microsoft Monitoring Agent\Agent|Microsoft Monitoring Agent (SCOM/Azure Monitor agent) folder. Tampering here blinds centralised monitoring and alerting.|
|C:\Program Files\Microsoft MPI\Bin\mpiexec.exe|Microsoft MPI launcher that can start processes locally and on remote nodes. LOLBin used for proxy execution.|
|C:\Program Files\Microsoft Network Monitor 3\nmcap.exe|Network Monitor capture tool. An attacker running this is sniffing traffic on the host; unexpected use on servers is high signal.|
|C:\Program Files\Microsoft Office\root\client\appvlp.exe|Office application virtualization proxy. Known LOLBin for proxy execution of other binaries.|
|C:\Program Files\Microsoft Office\root\Office16\winword.exe|Microsoft Word. The number one macro abuse target: alert on Word spawning cmd, PowerShell, wscript, mshta or certutil, and on template injection via Normal.dotm.|
|C:\Program Files\Microsoft Office\root\vfs\ProgramFilesCommonX64\Microsoft Shared\Office16\msoxmled.exe|Office XML editor, rarely used interactively. Listed as a LOLBin; unusual execution deserves review.|
|C:\Program Files\Microsoft PIX\pixtool.exe|DirectX/graphics debugging tool. Uncommon outside game and driver development; treat unexpected use cautiously.|
|C:\Program Files\Microsoft Silverlight\5.1.50918.0\coregen.exe|Silverlight .NET native image generator. Legacy component; any execution today is unusual.|
|C:\Program Files\Microsoft SQL Server\90\Shared\SQLDumper.exe|Tool that dumps SQL Server process memory. It can target arbitrary PIDs including lsass, making it a living off the land credential dumping tool.|
|C:\Program Files\Microsoft SQL Server\<version>\DTS\Binn\dtutil.exe|SSIS package utility. Can copy and execute SSIS packages, a documented LOLBin on SQL hosts.|
|C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\bcp.exe|Bulk copy tool for SQL Server. Attackers use it to rapidly exfiltrate table data, so watch for large exports.|
|C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\IntelliTrace\IntelliTrace.exe|Visual Studio IntelliTrace component. Rare outside development; unexpected execution or file drops are worth a look.|
|C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TestWindow\RemoteAgent\TestWindowRemoteAgent.exe|Remote test host agent for Visual Studio. Provides remote execution style functionality, so verify it belongs in your environment.|
|C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TestWindow\vstest.console.exe|Visual Studio test runner that executes compiled test assemblies. Known LOLBin for running arbitrary code inside signed binaries.|
|C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\Extensions\TestPlatform\Extensions\DumpMinitool.exe|Mini dump tool shipped with Visual Studio test platform. Can dump process memory including lsass; same credential theft risk as procdump.|
|C:\Program Files\Microsoft Visual Studio\2022\Community\Team Tools\DiagnosticsHub\Collector\VSDiagnostics.exe|Visual Studio diagnostics collector. Capable of collecting traces and dumps; rare in production.|
|C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\IDE\Extensions\Microsoft\NodeJsTools\NodeJsTools\Microsoft.NodejsTools.PressAnyKey.exe|Node.js Tools launcher shim in Visual Studio. LOLBin usable to run commands; uncommon outside dev boxes.|
|C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\IDE\VSLaunchBrowser.exe|Visual Studio helper that launches a browser for debugging. Minor risk; odd parentage is the giveaway.|
|C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\Tools\devinit\devinit.exe|Visual Studio dev machine initialisation tool that can run commands from a definition file. LOLBin style execution vector.|
|c:\Program Files\Microsoft\Edge\Application\msedge.exe|The Edge browser itself. Watch for C2 traffic blended into Edge, unexpected proxy settings, or extensions being added.|
|C:\Program Files\Update Services\LogFiles\SoftwareDistribution.log|WSUS update log. Useful for establishing the patch timeline of the host during an investigation.|
|C:\Program Files\Windows Defender|Microsoft Defender install folder. Defender binaries and config live here; any unauthorised writes or tampering is serious.|
|C:\Program Files\Windows Defender Advanced Threat Protection|Microsoft Defender for Endpoint sensor folder. Tampering with files or services here kills your EDR visibility; treat changes as high severity.|
|C:\Program Files\Windows Defender\ConfigSecurityPolicy.exe|Defender component that applies security policy. Rarely run manually; check the context if it executes.|
|C:\Program Files\Windows Defender\Offline\OfflineScannerShell.exe|Defender offline scan shell. Only legitimately runs during offline scans, so unexpected execution is notable.|
|C:\Program Files\Windows Kits\10\Microsoft User Experience Virtualization\Management\AppLauncher.exe|UE-V application launcher from the Windows Kits. LOLBin capable of launching other programs.|
|C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgr.exe|Windows Performance Toolkit boot trace tool. Rarely used on servers; appears on LOLBin lists for sideloading.|
|C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgrsleep.exe|Companion to xbootmgr for sleep tracing. Same rarity guidance.|
|C:\Program Files\Windows Mail\wab.exe|Windows Address Book. LOLBin that can be abused to load an attacker supplied DLL; rarely used for its real purpose.|
|C:\Program Files\Windows Photo Viewer\PhotoViewer.dll|Photo Viewer DLL. Can be invoked via rundll32 for proxy execution; check command lines referencing it.|
|C:\Program Files\WindowsApps\Microsoft.DesktopAppInstaller_1.11.2521.0_x64__8wekyb3d8bbwe\AppInstaller.exe|App Installer (ms-appinstaller). The ms-appinstaller URI scheme was abused for malware delivery to the point Microsoft restricted it, so investigate any use.|
|C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_<version_packageid>\wt.exe|Windows Terminal. Mainly note its child processes and settings.json, which can be abused for command persistence.|
|C:\Program Files\WindowsPowerShell\Modules|Machine wide PowerShell modules folder. Attackers can drop a malicious module here so it loads for any user; review contents for additions.|
|c:\Program Files\WindowsPowerShell\Modules\Pester\<VERSION>\bin\Pester.bat|Pester testing framework launcher. LOLBin that can execute code inside Pester tests on machines where it is installed.|
|C:\ProgramData\Microsoft\Crypto|Machine key store for DPAPI and CNG. Theft of the master keys here enables offline decryption of secrets protected on this machine.|
|C:\ProgramData\Microsoft\Group Policy\History|Local record of which Group Policies applied and when. Useful for spotting GPO tampering or unexpected policy changes.|
|C:\ProgramData\Microsoft\IntuneManagementExtension\Logs|Intune Management Extension logs. Show exactly which scripts were pushed and when, so they are key for investigating Intune based attacks.|
|C:\ProgramData\Microsoft\Network\Downloader\qmgr.db|BITS jobs database. Recovers the history of Background Intelligent Transfer jobs including attacker downloads, staging and persistence, even after jobs are deleted.|
|C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.edb|Windows Search index database. A quick win in triage: search indexed file names, paths and even some content for what existed on the host.|
|C:\ProgramData\Microsoft\Vault|Machine scoped saved credential vaults. A credential theft target.|
|C:\ProgramData\Microsoft\Windows Defender|Defender operational data in ProgramData. Watching for tampering here helps catch defence evasion.|
|C:\ProgramData\Microsoft\Windows Defender Advanced Threat Protection|Defender for Endpoint sensor data. Useful both for tamper evidence and MDE local state.|
|C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.4-0\MpCmdRun.exe|Defender command line tool. Legit for scans, but abused with -DownloadFile to pull malware from URLs, so alert on that command line.|
|C:\ProgramData\Microsoft\Windows Defender\Platform\<version>|Defender platform binaries for a specific engine version. Files here change with updates; unexpected new files are suspicious.|
|C:\ProgramData\Microsoft\Windows Defender\Quarantine|Defender quarantine. Lets you recover original malware samples for deeper analysis.|
|C:\ProgramData\Microsoft\Windows Defender\Scans\History\Service\DetectionHistory|History of what Defender detected and when. Great for building the infection timeline.|
|C:\ProgramData\Microsoft\Windows Defender\Scans\mpenginedb.db|Defender engine database with detection metadata. An alternative forensic source of detection history.|
|C:\ProgramData\Microsoft\Windows Defender\Support|Defender support and diagnostic output such as MpCmdRun captures. Check for unexpected dumps or log collection.|
|C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp|All users Startup folder. Anything here launches at every user logon, making it classic persistence; review contents regularly.|
|C:\ProgramData\Microsoft\Windows\WER\ReportArchive|Archived Windows Error Reporting crash reports. Can contain memory snippets from crashed (including exploited) processes.|
|C:\ProgramData\Microsoft\Windows\WER\ReportQueue|Queued Windows Error Reporting crash reports not yet uploaded. Same forensic value as the archive.|
|C:\ProgramData\ssh|OpenSSH server configuration and host keys when sshd is installed. Check for unauthorised sshd_config changes and planted keys.|
|C:\SMS_CCM\Logs|Legacy SMS/SCCM client logs. Useful on servers managed by ConfigMgr for tracing pushed software and scripts.|
|C:\System Volume Information|Home of volume shadow copies and restore points. Ransomware operators delete it; and it can recover previous versions of files and hives during IR.|
|C:\there\is\no\default\installation\path\WFMFormat.exe|Placeholder style vendor path from a LOLBin list: a binary attackers can drop anywhere because it has no fixed install location. Treat unknown executables in odd directories as suspicious by default.|
|C:\Users|Root of all user profiles. New or unexpected profile folders can indicate new local accounts or attacker activity.|
|C:\Users\<username>\.dotnet\tools\dotnet-counters.exe|.NET diagnostic tool for live counter monitoring of processes. Rarely used by end users; minor LOLBin value.|
|C:\Users\<username>\.dotnet\tools\dotnet-trace.exe|.NET tracing tool that can attach to processes and collect detailed traces. Unusual outside development work.|
|C:\Users\<username>\.ssh|User SSH folder holding private keys, config and authorized_keys. A new authorized_keys entry is a classic backdoor, and stolen private keys enable lateral movement.|
|C:\Users\<username>\AppData\Local|Per user local application data. Very common malware staging and execution location; baseline what is normal here.|
|C:\Users\<username>\AppData\Local\ConnectedDevicesPlatform\<id>\ActivitiesCache.db|Windows Timeline activity database. Records applications run and documents opened, tied to the user, making it excellent for user activity reconstruction.|
|C:\Users\<username>\AppData\Local\Microsoft\Edge\User Data\Default|Edge profile data including history, cookies and saved passwords (Login Data). Prime target for infostealers and a rich source of user activity evidence.|
|C:\Users\<username>\AppData\Local\Microsoft\OneDrive|OneDrive sync client data. Review for exfiltration staging and to see what synced where.|
|C:\Users\<username>\AppData\Local\Microsoft\OneDrive\OneDriveStandaloneUpdater.exe|OneDrive updater, legitimately signed and internet facing. Verify signature and parent process since masquerading under update names is common.|
|C:\Users\<username>\AppData\Local\Microsoft\Outlook|Offline Outlook data (OST files). Enables offline review of the user's mailbox contents during an investigation.|
|C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Squirrel.exe|Squirrel based Teams updater component. The Squirrel framework has been abused for execution, so watch its command lines.|
|C:\Users\<username>\AppData\Local\Microsoft\Teams\current\Teams.exe|Classic Teams client (Electron). Check for abuse as a C2 channel and review its local storage on compromised hosts.|
|C:\Users\<username>\AppData\Local\Microsoft\Teams\update.exe|Teams Squirrel Update.exe. Known LOLBin: can be made to execute arbitrary binaries via its update mechanisms.|
|C:\Users\<username>\AppData\Local\Microsoft\Terminal Server Client\Cache|RDP client bitmap cache tiles. Can be reconstructed to partially see what the user saw in RDP sessions, handy in insider and hands on keyboard cases.|
|C:\Users\<username>\AppData\Local\Microsoft\Vault|User credential vault files. Another credential theft target.|
|C:\Users\<username>\AppData\Local\Microsoft\Windows\Explorer|Shell data including thumbcache and iconcache databases. Proves certain files or network shares existed and were browsed.|
|C:\Users\<username>\AppData\Local\Microsoft\Windows\UsrClass.dat|User class registry hive. Contains shellbags: per user folder browsing history that survives deletion of the folders.|
|C:\Users\<username>\AppData\Local\Microsoft\Windows\WebCache\WebCacheV01.dat|Legacy IE/Edge cache database. Historical browsing and download evidence even after browser cleanup.|
|C:\Users\<username>\AppData\Local\Microsoft\WindowsApps|Per user Windows Store apps folder. Attackers sometimes stage payloads here because it is user writable and looks Microsoft related.|
|C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\wsb.exe|Windows Sandbox executable. Legitimate, but malware has abused sandbox binaries; unexpected use on servers is worth review.|
|C:\Users\<username>\AppData\Local\Packages\<PackageFamilyName>\LocalState|UWP app local state folders. Some apps store credentials and config here; check attacker persistence in app settings or scripts.|
|C:\Users\<username>\AppData\Local\Packages\MSTeams_8wekyb3d8bbwe|New Teams (MSIX) app data folder. Baseline it for your fleet so anomalies stand out.|
|C:\Users\<username>\AppData\Local\Temp|User temp folder. Classic malware drop and run location; alert on executables launching from Temp.|
|C:\Users\<username>\AppData\Local\Temp\.net\devtunnel\devtunnel.exe|Microsoft dev tunnels client. A legitimate Microsoft signed tool that creates outbound tunnels, which makes it attractive as a covert C2 or remote access channel.|
|C:\Users\<username>\AppData\Local\Temp\<process>.DMP|Process crash dumps written to temp. Can contain credentials and tokens; also check whether an attacker wrote an lsass dump here.|
|C:\Users\<username>\AppData\Roaming|Roaming profile data synced across machines. Malware often stores config or stages files here.|
|C:\Users\<username>\AppData\Roaming\Microsoft\Credentials|DPAPI protected saved credentials (Windows Credential Manager files). A standard theft target for infostealers.|
|C:\Users\<username>\AppData\Roaming\Microsoft\Crypto|User DPAPI master keys. Combined with the user's password hash they decrypt all of that user's protected secrets.|
|C:\Users\<username>\AppData\Roaming\Microsoft\Excel\XLSTART|Excel startup folder: any workbook here opens automatically with Excel. Dropping a macro file here is quiet Office persistence.|
|C:\Users\<username>\AppData\Roaming\Microsoft\Outlook\VbaProject.OTM|Outlook VBA macro project file. Rarely present legitimately; its existence after a phish should be treated as macro persistence until proven otherwise.|
|C:\Users\<username>\AppData\Roaming\Microsoft\Protect\<SID>|Per user DPAPI master key containers keyed by SID. Direct tie in to decrypting Credentials and Vault artifacts.|
|C:\Users\<username>\AppData\Roaming\Microsoft\SystemCertificates\My\Certificates|User personal certificate store files. Review for rogue certificates installed for interception or code signing.|
|C:\Users\<username>\AppData\Roaming\Microsoft\Templates\Normal.dotm|Word global template loaded at every Word start. Replacing or infecting it is classic macro persistence; check timestamps and macros.|
|C:\Users\<username>\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt|Plain text PowerShell command history per user. Attackers regularly forget it exists, so it often contains their exact commands.|
|C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent|Per user Recent Items shortcuts. Quick view of recently opened files and folders.|
|C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations|Automatic jumplist destinations: per application records of files opened. Strong user activity evidence.|
|C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations|Custom jumplist entries. Complements AutomaticDestinations for application usage history.|
|C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup|Per user Startup folder. Anything dropped here runs at that user's logon, so it is classic user level persistence.|
|C:\Users\<username>\Documents\Default.rdp|Saved RDP connection settings including last server and username. Handy for mapping user and attacker RDP activity.|
|C:\Users\<username>\Documents\WindowsPowerShell|User PowerShell folder holding profile scripts and modules. A profile.ps1 here runs every time PowerShell starts, a common persistence spot.|
|C:\Users\<username>\Downloads\<filename>:Zone.Identifier|Mark of the Web alternate data stream on downloaded files. Records the origin zone and often the source URL, making it key evidence for phishing downloads.|
|C:\Users\<username>\NTUSER.DAT|User registry hive containing Run keys, MRUs, UserAssist and shell settings. A core triage artifact for per user activity and persistence.|
|C:\Users\Default|Template profile copied to every new user. Modifications propagate to all future profiles, a sneaky persistence trick.|
|C:\Users\Public|World writable shared profile area. Very common malware staging location (Public Documents, Public Downloads); executables here deserve scrutiny.|
|C:\Users\user\AppData\Local\Microsoft\WindowsApps\winget.exe|Windows Package Manager CLI. Attackers use winget to install tooling quietly, so review install history and unexpected invocations.|
|C:\Windows|Windows operating system root folder.|
|C:\Windows\ADFS|AD FS component folder on federation servers. High value target: tampering here is the road to Golden SAML style token forgery, so monitor closely.|
|C:\Windows\AppCompat\pca|Program Compatibility Assistant data. Records program executions (PcaAppLaunchDic and PcaGeneralDb files) and is a useful execution artifact even when Prefetch is off.|
|C:\Windows\AppCompat\Programs|Compatibility data folder that on modern builds holds Amcache and related files about executed programs and drivers.|
|C:\Windows\AppCompat\Programs\Amcache.hve|Amcache hive: evidence of executed programs and loaded drivers including SHA1 hashes and first run times. Especially useful for deleted executables.|
|C:\Windows\assembly|Global Assembly Cache for .NET. Attackers can register malicious assemblies here for persistence on developer and server hosts.|
|C:\Windows\CCM|SCCM client installation folder.|
|C:\Windows\CCM\Logs|SCCM client logs such as execmgr.log and AppEnforce.log. These record packages and scripts run on the client, great for catching malicious deployments pushed through ConfigMgr.|
|C:\Windows\ccmcache|Cache of downloaded SCCM packages. May contain scripts or even credentials, so review contents on suspicious clients.|
|C:\Windows\ccmsetup\Logs|SCCM client installation logs. Useful for timeline work around client install or repair events.|
|C:\Windows\debug|Windows debug log folder including the netlogon log when enabled.|
|C:\Windows\debug\netlogon.log|Netlogon debug log, mainly enabled on DCs. Records authentication and secure channel activity useful in lateral movement investigations.|
|C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1|Built in Windows troubleshooting pack script. Signed diagnostic scripts like this are known LOLBins used for proxy code execution, so unexpected runs on servers are suspicious.|
|C:\Windows\diagnostics\system\Audio\CL_LoadAssembly.ps1|Built in diagnostic script for audio troubleshooting. Same LOLBin guidance: legit content, abused as a signed execution proxy.|
|C:\Windows\diagnostics\system\Networking\UtilityFunctions.ps1|Built in networking diagnostic script that has appeared on LOLBin lists. Watch for execution outside troubleshooting scenarios.|
|C:\Windows\diagnostics\system\WindowsUpdate\CL_Mutexverifiers.ps1|Built in Windows Update diagnostic script. Another signed script worth baselining.|
|C:\Windows\explorer.exe|Windows shell. Explorer spawning script interpreters or shells is suspicious, and it is a frequent injection target because it is always running as the user.|
|C:\Windows\hh.exe|HTML Help viewer that opens .chm files. LOLBin: weaponised CHM files execute embedded scripts, a long running phishing technique.|
|C:\Windows\IMECache|Input Method Editor cache. Unexpected files here are suspicious given its obscure, low visibility nature.|
|C:\Windows\inf\setupapi.dev.log|Device and driver installation log. Records USB device and driver installs with timestamps, useful for rogue peripheral and evidence timeline work.|
|C:\Windows\Installer|Cache of MSI installer packages. Helps establish software install history and recover original installers.|
|C:\Windows\Logs|General Windows log folder containing many setup and servicing logs.|
|C:\Windows\Logs\CBS\CBS.log|Component Based Servicing log. Records patching and feature changes; useful for install timelines.|
|C:\Windows\Logs\DISM\dism.log|DISM servicing log. Use it to detect image tampering or drivers and packages being added.|
|C:\Windows\MEMORY.DMP|Full system crash dump. Complete memory for forensic analysis including credentials and injected code, so handle it as sensitive.|
|C:\Windows\Microsoft.NET\Framework64\v2.0.50727\RegSvcs.exe|.NET services registration tool. LOLBin that executes arbitrary .NET assemblies while looking like framework plumbing.|
|C:\Windows\Microsoft.NET\Framework64\v3.5\DataSvcUtil.exe|WCF Data Services utility. LOLBin for code execution; rarely used legitimately today.|
|C:\Windows\Microsoft.NET\Framework64\v4.0.30319|.NET Framework v4 runtime root (64 bit).|
|C:\Windows\Microsoft.Net\Framework64\v4.0.30319\Microsoft.Workflow.Compiler.exe|Workflow compiler. LOLBin that compiles and runs XOML/C# workflow files picked to bypass allow lists.|
|C:\Windows\Microsoft.NET\Framework\v2.0.50727\Applaunch.exe|ClickOnce related launcher. LOLBin usable for proxy execution.|
|C:\Windows\Microsoft.NET\Framework\v2.0.50727\Dfsvc.exe|ClickOnce deployment service. LOLBin that fetches and executes ClickOnce apps, including from URLs.|
|C:\Windows\Microsoft.NET\Framework\v2.0.50727\ieexec.exe|Legacy .NET CAS launcher. LOLBin that can execute remote .NET applications.|
|C:\Windows\Microsoft.NET\Framework\v2.0.50727\InstallUtil.exe|Top tier LOLBin: installs or executes .NET assemblies and is a favourite AppLocker bypass. Any interactive use on servers is suspicious.|
|C:\Windows\Microsoft.NET\Framework\v2.0.50727\Msbuild.exe|Top tier LOLBin: builds project files and can run inline C# tasks, executing attacker code with a signed Microsoft binary on hosts with dev tools or build servers.|
|C:\Windows\Microsoft.NET\Framework\v2.0.50727\ngen.exe|.NET native image generator. Normally only runs during installs, so interactive use is unusual.|
|C:\Windows\Microsoft.NET\Framework\v2.0.50727\regasm.exe|.NET assembly registration tool. LOLBin that loads assemblies and can bypass application allow lists.|
|C:\Windows\Microsoft.NET\Framework\v4.0.30319|.NET Framework v4 runtime root (32 bit).|
|C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe|.NET add-in pipeline utility. LOLBin for proxy execution.|
|c:\Windows\Microsoft.NET\Framework\v4.0.30319\aspnet_compiler.exe|ASP.NET precompilation tool. Watch it on IIS servers: it can be used to compile webshells.|
|C:\Windows\Microsoft.NET\Framework\v4.0.30319\Csc.exe|In-box C# compiler. Attackers use it to compile payloads directly on the victim host.|
|C:\Windows\Microsoft.NET\Framework\v4.0.30319\ilasm.exe|.NET IL assembler. Lets attackers build executables from IL source on host.|
|C:\Windows\Microsoft.NET\Framework\v4.0.30319\Jsc.exe|JScript .NET compiler. LOLBin that compiles JScript into executables.|
|C:\Windows\Microsoft.NET\Framework\v4.0.30319\vbc.exe|VB.NET compiler. Same on host compilation abuse pattern as csc.exe.|
|C:\Windows\NTDS|Active Directory database folder on domain controllers. Guard it heavily.|
|C:\Windows\NTDS\ntds.dit|The AD database itself containing every domain account's password hashes. The crown jewels: any copy, export or shadow copy access on a DC is a critical event.|
|C:\Windows\Panther|Windows setup and upgrade logs. Check for unattend.xml leftovers which can contain plaintext local admin or domain join credentials.|
|C:\Windows\PolicyDefinitions|Local copies of ADMX policy definition templates.|
|C:\Windows\Prefetch|Prefetch folder with execution evidence: binary name, run count and last run times. A first stop artifact for proving a program ran, assuming Prefetch is enabled.|
|C:\Windows\PSEXESVC.exe|PsExec service binary. Its presence plus a service install event (7045) is the classic PsExec lateral movement pattern; also catches PsExec clones reusing the same name.|
|C:\Windows\regedit.exe|Registry Editor GUI. Silent reg import via command line is a persistence and config tamper vector, so watch command line usage, not just the GUI.|
|C:\Windows\ServiceProfiles\LocalService\AppData\Local\Microsoft\Ngc|Windows Hello for Business PIN and biometric container data. Relevant to credential and account compromise investigations.|
|C:\Windows\SoftwareDistribution|Windows Update download cache and logs. Baseline for patch state and update failures.|
|C:\Windows\Sysmon64.exe|Sysmon default install path. Correct location for the real Sysmon; conversely, a binary masquerading as Sysmon anywhere else is suspect, and watch for service or config tampering since it kills visibility.|
|C:\Windows\System32|Core Windows binary folder. Masquerading is common: check for files with system like names that are unsigned or newly created.|
|c:\windows\system32\advpack.dll|Advanced INF install DLL. LOLBin used through rundll32 to run INF based payloads.|
|C:\Windows\System32\amsi.dll|Antimalware Scan Interface. In memory patching or tampering with amsi.dll is a classic malware and red team evasion technique, so watch AMSI health.|
|C:\Windows\System32\AppLocker|AppLocker policy and assembly data. Verify policy integrity and check for unexpected changes.|
|C:\Windows\System32\arp.exe|ARP cache viewer. Basic host network recon tool used in attacker discovery phases.|
|C:\WINDOWS\System32\At.exe|Legacy task scheduler, deprecated but still present on some builds. Because legitimate use is near zero, any execution is suspicious.|
|C:\Windows\System32\Atbroker.exe|Accessibility/AT broker. LOLBin that can launch arbitrary executables and has featured in UAC bypass style abuse.|
|C:\Windows\System32\attrib.exe|Attribute tool. Malware and ransomware use attrib +h +s to hide files and folders, so watch for that pattern on user directories.|
|C:\Windows\System32\auditpol.exe|Audit policy tool. Mass disabling of audit categories is defence evasion with high signal.|
|C:\Windows\System32\bash.exe|WSL bash launcher. LOLBin that runs Linux commands and binaries from Windows; unexpected on workstations and servers.|
|C:\Windows\System32\bcdedit.exe|Boot configuration editor. Ransomware operators disable recovery options with it (for example recoveryenabled no), so alert on changes.|
|C:\Windows\System32\bitsadmin.exe|Classic LOLBin: downloads files, manages BITS jobs and can create persistence through BITS notify commands. Usually safe to alert on outside admin tooling.|
|C:\Windows\System32\catroot2|Driver catalog database used for code integrity and driver signing. Tampering affects signature validation.|
|C:\Windows\System32\CertLog|AD CS transaction log folder on certificate authority servers. High value host evidence for certificate abuse.|
|c:\windows\system32\certoc.exe|Certificate enrollment component. Rarely run directly; unexpected execution is worth review.|
|C:\Windows\System32\certreq.exe|Certificate request tool. Attackers abuse AD CS to mint certificates, so watch usage off CA admin workflows.|
|C:\Windows\System32\certsrv.exe|Certificate authority service process on AD CS servers. This host tier is critical; any anomalies around the CA service are high severity.|
|C:\Windows\System32\CertSrv\CertEnroll|Folder where the CA publishes CRLs and enrolment data. Baseline contents on your CA.|
|C:\Windows\System32\certutil.exe|Swiss army LOLBin: decodes base64 files, downloads from URLs, and manages certificates and AD CS. Certutil touching the network is almost always worth an investigation.|
|c:\windows\system32\change.exe|Remote Desktop Session Host change tool (change logon/port/user). Disabling logons before destructive actions is an attacker pattern on terminal servers.|
|c:\windows\system32\cipher.exe|Secure deletion tool: cipher /w wipes free space. That is anti forensic behaviour often seen with ransomware staging.|
|C:\Windows\System32\cmd.exe|Command shell. Spawns during most attack chains; the parent process (Office, wscript, mshta, web server) is usually the key signal.|
|C:\Windows\System32\cmdkey.exe|Saved credential manager CLI. Attackers create stored credentials with it to ease lateral movement.|
|C:\Windows\System32\cmdl32.exe|Legacy LAN connection manager. LOLBin documented for file download; near zero legitimate modern use.|
|C:\Windows\System32\cmstp.exe|Connection Manager profile installer. LOLBin that executes SCT/INF payloads and has UAC bypass uses.|
|C:\Windows\System32\CodeIntegrity|Code Integrity event log folder. Blocked unsigned driver loads (BYOVD attempts) show up here.|
|C:\Windows\System32\colorcpl.exe|Color management control panel. Rarely launched; verify context if it runs with odd arguments.|
|C:\Windows\System32\ComputerDefaults.exe|Known LOLBin for UAC bypass via ms-settings registry hijacking (fodhelper family). Execution on servers is unusual.|
|c:\windows\system32\comsvcs.dll|COM+ services DLL with a MiniDump export. The famous technique rundll32 comsvcs.dll MiniDump dumps a process such as lsass for credentials without extra tooling.|
|C:\Windows\System32\config|Folder holding the live registry hives (SAM, SYSTEM, SECURITY, SOFTWARE).|
|C:\Windows\System32\config\RegBack|Backup copies of registry hives. Empty on modern builds but historically a source of the SAM for offline credential attacks.|
|C:\Windows\System32\config\SAM|Local account database with password hashes. Any access or copy of this hive is credential theft tier evidence.|
|C:\Windows\System32\config\SECURITY|SECURITY hive holding LSA secrets and cached domain logons. Another prime credential theft target.|
|C:\Windows\System32\config\SOFTWARE|SOFTWARE hive: installed software, run keys, policies and third party config. Core triage hive.|
|C:\Windows\System32\config\SYSTEM|SYSTEM hive: services, control sets, device and driver config. Core triage hive.|
|C:\Windows\System32\config\systemprofile|Profile folder for the SYSTEM account. Services drop data here; check for attacker staged files hiding under system contexts.|
|c:\windows\system32\conhost.exe|Console window host spawned by shells. Conhost with an unusual parent (for example Word or a service) is a classic C2 beacon indicator (Cobalt Strike pattern).|
|C:\Windows\System32\consent.exe|UAC consent prompt process. Unexpected spawning chains around it deserve review.|
|C:\Windows\System32\control.exe|Control Panel launcher. LOLBin that loads .cpl payloads, which are just DLLs, for proxy execution.|
|C:\Windows\System32\cscript.exe|Windows Script Host console engine. Executes VBS and JS malware droppers; alert on unexpected parents and network activity.|
|C:\Windows\System32\csvde.exe|AD CSV export/import tool. On DCs it enables bulk directory recon and extraction; legitimate use is narrowly scoped to admins.|
|C:\Windows\System32\curl.exe|curl is now built into Windows. Attackers use it for downloads and data exfiltration; watch usage on servers especially.|
|C:\Windows\System32\CustomShellHost.exe|Shell infrastructure host used on kiosk style configurations. Rare on normal builds, so execution stands out.|
|C:\Windows\System32\dcdiag.exe|Domain controller diagnostics. Recon of AD health from a non admin host is an attacker discovery pattern.|
|C:\Windows\System32\desk.cpl|Display settings control panel. Minor risk; masquerading and sideloads are the concern.|
|c:\windows\system32\desktopimgdownldr.exe|Lock screen image download component. LOLBin: attacker configured URL plus this binary downloads arbitrary files.|
|C:\Windows\System32\DeviceCredentialDeployment.exe|Device credential deployment tool. Rarely used; appears on LOLBin lists.|
|c:\windows\system32\devtoolslauncher.exe|Developer tools launcher. LOLBin for proxy execution on machines with dev tooling.|
|C:\Windows\System32\dhcp|DHCP server data and logs on DHCP servers. Rogue DHCP grants and leases are relevant to on path attacks.|
|c:\windows\system32\diantz.exe|Legacy alias of makecab. LOLBin usable to package and compress files for exfiltration staging.|
|C:\Windows\System32\diskpart.exe|Disk management CLI. Pre ransomware disk actions and discovery can surface here.|
|C:\Windows\System32\diskshadow.exe|Shadow copy aware disk tool. LOLBin that runs embedded script commands and is abused to copy locked files like ntds.dit via shadow copies.|
|C:\Windows\System32\dllhost.exe|COM surrogate host for out of process COM servers. dllhost with network activity, high CPU, or odd parents is classic injection and masquerading.|
|C:\Windows\System32\dns|DNS server data folder including zone files, on DNS servers.|
|C:\Windows\System32\Dnscmd.exe|DNS server administration CLI. A malicious ServerLevelPluginDll registered through dnscmd gives persistence as SYSTEM on DNS servers, which are often DCs.|
|C:\Windows\System32\drivers|Kernel driver location. The BYOVD pattern (bring your own vulnerable driver) drops drivers here or nearby; new .sys files deserve review.|
|C:\Windows\System32\drivers\etc|TCP/IP network configuration folder.|
|C:\Windows\System32\drivers\etc\hosts|Hosts file. Check for hijacked entries such as AV update domains blocked or internal names redirected; also note whether it has been emptied suspiciously.|
|C:\Windows\System32\dsacls.exe|AD ACL viewing and editing tool. Attackers use it to enumerate or grant dangerous rights such as DCSync; alert on usage outside AD admin teams.|
|C:\Windows\System32\dsdbutil.exe|AD DS database utility that can create snapshots and install media. A vector for copying the AD database on DCs.|
|C:\Windows\System32\dsquery.exe|AD query tool used for directory recon (users, groups, computers). Uncommon on non admin machines.|
|C:\Windows\System32\dsregcmd.exe|Shows device Entra ID / domain join state. Mostly benign; attackers use the output for environment recon.|
|C:\Windows\System32\dxcap.exe|Visual Studio graphics capture tool. Rare; baseline before trusting.|
|C:\Windows\System32\esentutl.exe|Extensible Storage Engine utility. LOLBin that can copy locked files (including via VSS) such as hives and ntds.dit, and dump ESE databases.|
|c:\windows\system32\eudcedit.exe|Private character editor. Obscure binary on LOLBin lists; unexpected execution is notable.|
|C:\Windows\System32\eventvwr.exe|Event Viewer. Launch patterns mscfile hijacks have enabled UAC bypasses, so check parent and arguments when spawned unexpectedly.|
|C:\Windows\System32\Expand.exe|Cabinet file extractor. LOLBin for copying/decompressing payloads into place.|
|C:\Windows\System32\extrac32.exe|Another cabinet extractor with a very small footprint. Used to unpack payloads from cab files.|
|C:\Windows\System32\findstr.exe|Text search tool. Attackers grep whole drives for password, secret and similar strings; watch for broad recursive searches.|
|c:\windows\system32\finger.exe|Finger client. LOLBin: transfers and executes data over the finger protocol; almost no legitimate modern use.|
|C:\Windows\System32\fltMC.exe|Minifilter driver manager. Attackers list (and attempt to unload) AV and EDR filter drivers with it.|
|C:\Windows\System32\fodhelper.exe|Features on Demand helper. Famous LOLBin UAC bypass via ms-settings registry hijack; execution by standard users on servers is worth alerting.|
|C:\Windows\System32\forfiles.exe|File batch command tool. LOLBin that executes commands per matched file; also seen in ransomware clean up loops.|
|C:\Windows\System32\fsutil.exe|File system utility. Ransomware and wipers use fsutil usn deletejournal to destroy the USN journal for anti forensics; alert on that command.|
|C:\Windows\System32\ftp.exe|FTP client scriptable with -s. Simple download and exfiltration path; unusual to see used today.|
|C:\Windows\System32\gpresult.exe|Group Policy results tool. Benign; occasionally part of attacker environment recon.|
|C:\Windows\System32\gpscript.exe|Runs GPO logon and logoff scripts. Execution off logon events is suspicious.|
|C:\Windows\System32\gpupdate.exe|Group Policy refresh tool. An attacker forcing refresh can be trying to apply tampered GPOs.|
|C:\Windows\System32\GroupPolicy|Local Group Policy store on machine. Review for local policy tampering when GPOs do not match expectations.|
|C:\Windows\System32\GroupPolicyUsers|Per user sections of the local Group Policy store.|
|C:\Windows\System32\icacls.exe|ACL editor. Watch for mass permission grants (Everyone:F), ransomware ACL resets and staged access changes on shares.|
|c:\windows\system32\ie4uinit.exe|IE per user initialisation tool. LOLBin that executes INF based commands.|
|c:\windows\system32\ieadvpack.dll|IE advanced package DLL. LOLBin used via rundll32 to run INF commands.|
|c:\windows\system32\ieframe.dll|IE rendering engine DLL. Can be invoked through rundll32 (OpenURL) to open URLs or proxies; part of the legacy IE LOLBin family.|
|C:\Windows\System32\IME\SHARED\IMEWDBLD.exe|IME dictionary builder. LOLBin documented for executing commands or URLs.|
|C:\Windows\System32\inetsrv\appcmd.exe|IIS administration CLI. Attackers enumerate sites, add modules or bindings and deploy webshells through it on web servers.|
|C:\Windows\System32\inetsrv\config\applicationHost.config|IIS global configuration file. Backdoor IIS modules and handler mappings land here, so it is a key file to review after IIS compromise.|
|C:\Windows\System32\Infdefaultinstall.exe|INF default install handler. LOLBin that executes commands embedded in malicious INF files.|
|C:\Windows\System32\ipconfig.exe|Network configuration recon. ipconfig /all and /displaydns are standard post compromise discovery commands.|
|c:\windows\system32\iscsicpl.exe|iSCSI initiator control panel. Uncommon on most workstations; treat out of place execution cautiously.|
|C:\Windows\System32\klist.exe|Kerberos ticket tool. klist purge before ticket based attacks and klist sessions for ticket enumeration are credential attack signals.|
|c:\windows\system32\ldifde.exe|AD export/import via LDIF files. Bulk directory recon and extraction tool on DCs; admin only use expected.|
|C:\Windows\System32\LogFiles|Parent folder for many service logs including IIS and HTTPERR when logging to the default system location.|
|C:\Windows\System32\LogFiles\Firewall\pfirewall.log|Windows Firewall packet log when logging is enabled. Connection evidence for allowed and dropped traffic.|
|C:\Windows\System32\LogFiles\HTTPERR|HTTP.sys kernel error logs. Large floods of bad requests show scanning and exploitation attempts against IIS services.|
|C:\Windows\System32\LogFiles\IN<yymm>.log|RAS/remote access log files. Mostly legacy; presence of activity may indicate dial up or VPN style connections.|
|C:\Windows\System32\LogFiles\Sum|SCCM and MDM software update summariser logs. Patch compliance evidence.|
|C:\Windows\System32\LogFiles\WMI|Text logs for WMI activity. Useful alongside the WMI-Activity event log.|
|C:\Windows\System32\logman.exe|Performance counter and ETW trace manager. Attackers can use it to stop trace sessions and blind ETW based sensors.|
|C:\Windows\System32\lsass.exe|Local Security Authority: holds credentials and tickets in memory. Any abnormal process opening a handle with read access is the core credential dumping detection (Sysmon event 10 on lsass).|
|C:\Windows\System32\magnify.exe|Magnifier accessibility tool. Part of the accessibility binary swap family used to get shells at the logon screen.|
|C:\Windows\System32\makecab.exe|Cabinet archive tool. Used to compress stolen data before exfiltration.|
|C:\Windows\System32\manage-bde.wsf|BitLocker management script. Attackers check encryption state with it; occasionally used in destructive scenarios.|
|C:\Windows\System32\mavinject.exe|MUI resource injection tool. Clean LOLBin for injecting DLLs into running processes.|
|C:\Windows\System32\mdmdiagnosticstool.exe|MDM diagnostics collector. Can gather and package device info; verify use is admin driven.|
|C:\Windows\System32\mmc.exe|Microsoft Management Console. LOLBin: malicious .msc files run embedded code, and it features in UAC bypass patterns.|
|C:\Windows\System32\msconfig.exe|System configuration GUI. Benign, but review unexpected boot or startup changes made shortly before an incident.|
|C:\Windows\System32\Msdt.exe|Microsoft Support Diagnostics Tool. LOLBin that runs diagcab payloads and was central to the Follina ms-msdt vulnerability chain.|
|C:\Windows\System32\mshta.exe|Top tier LOLBin: executes HTA applications including inline JScript/VBScript and remote HTAs from URLs. High confidence alert when it runs from email, Office or script parents.|
|c:\windows\system32\mshtml.dll|Legacy IE HTML engine DLL. Exploited historically; rundll32 based invocation is a proxy execution trick.|
|C:\Windows\System32\msiexec.exe|Windows Installer service tool. msiexec /i pointing at http URLs or odd UNC paths installs remote packages; suspicious msiexec children also matter.|
|C:\Windows\System32\mstsc.exe|RDP client. Review launches from servers and admin workstations, plus .rdp file usage, for lateral movement.|
|C:\Windows\System32\narrator.exe|Narrator accessibility tool. Another binary swap target for logon screen persistence.|
|C:\Windows\System32\nbtstat.exe|NetBIOS status tool. Legacy network recon of remote hosts and name tables.|
|C:\Windows\System32\net.exe|Swiss army network/admin tool: net user, net localgroup administrators, net view, net share, net stop. Account creation, group changes and service stopping are all high signal detections.|
|C:\WINDOWS\System32\Netsh.exe|Network shell. Watch for firewall rule changes, portproxy rules for pivoting, and 'netsh wlan show profile key=clear' Wi-Fi password extraction.|
|C:\Windows\System32\netstat.exe|Connection listing tool. Noisy, but correlates with attacker discovery phases.|
|C:\Windows\System32\nltest.exe|Domain and DC discovery tool (dclist, dsgetdc, trusts). Recon signal on non admin hosts.|
|C:\Windows\System32\nslookup.exe|DNS query tool. Recon use; also commonly seen when testing DNS tunnelling channels.|
|C:\Windows\System32\ntdsutil.exe|Active Directory maintenance tool. 'ntdsutil activate instance ntds ifm create' exports the AD database; on a DC this is a critical credential theft indicator.|
|c:\windows\system32\odbcad32.exe|ODBC data source administrator. Review for attacker added data sources; rarely used day to day.|
|C:\Windows\System32\odbcconf.exe|ODBC registration tool. LOLBin that can load and register arbitrary DLLs.|
|C:\Windows\System32\OpenSSH|Built in OpenSSH server folder when the feature is installed. Baseline sshd_config and host keys.|
|C:\Windows\System32\OpenSSH\scp.exe|Secure copy client. Quick exfiltration path to remote hosts; watch usage on servers.|
|C:\Windows\System32\OpenSSH\sftp.exe|SFTP client. Same exfiltration considerations as scp.|
|c:\windows\system32\OpenSSH\ssh.exe|SSH client. Local and reverse tunnels (ssh -L/-R) provide covert C2 and pivoting channels; alert on tunnels from unlikely hosts.|
|C:\Windows\System32\osk.exe|On-screen keyboard. Accessibility binary swap target for logon screen shells.|
|C:\Windows\System32\pcalua.exe|Program Compatibility Assistant tool. LOLBin: pcalua -a executes arbitrary programs as a signed proxy.|
|C:\Windows\System32\pcwrun.exe|Performance counter tool. LOLBin that can be driven to run commands.|
|c:\windows\system32\pcwutl.dll|Performance counter helper DLL. Rare, but check for rundll32 based invocation.|
|c:\windows\system32\pktmon.exe|Built in packet capture tool on Windows 10+. Attackers can sniff traffic with no third party tools installed, so unexpected use is worth alerting.|
|C:\Windows\system32\pnputil.exe|Driver package installer. Attackers install malicious or vulnerable (BYOVD) drivers with it.|
|C:\Windows\System32\Presentationhost.exe|WPF browser application host. LOLBin that runs remote XBAP payloads.|
|C:\Windows\System32\print.exe|Command line print tool. Minor exfil/rare use considerations; mostly benign.|
|C:\Windows\System32\Printing_Admin_Scripts\en-US\pubprn.vbs|Printer publishing admin script. Known LOLBin: feeds a remote scriptlet (SCT) to the script engine for execution.|
|c:\windows\system32\provlaunch.exe|Provisioning package launcher. Rare; unexpected launches deserve review.|
|c:\windows\system32\psr.exe|Problem Steps Recorder. Records screens and keystrokes context; theoretically usable for surveillance but mainly benign.|
|c:\windows\system32\query.exe|Session/query display tools (quser, qprocess etc.). Attackers enumerate sessions to find admin RDP logons to hijack.|
|C:\Windows\System32\quser.exe|Lists logged on users and RDP sessions. Admin session discovery is a common attacker step before tscon style hijacks.|
|C:\Windows\System32\rasautou.exe|RAS auto dialer. LOLBin for proxy execution; near zero modern legitimate use.|
|C:\Windows\System32\rdpclip.exe|RDP clipboard redirection process. Unexpected activity can align with clipboard based data theft during RDP sessions.|
|c:\windows\system32\rdrleakdiag.exe|RDR leak diagnosis tool. Rare diagnostic; verify context.|
|C:\Windows\System32\reg.exe|Registry CLI. reg save HKLM\SAM and reg add to Run keys are classic credential theft and persistence commands; very detection friendly.|
|C:\Windows\System32\regini.exe|Script based registry editor. Can modify keys including security ACLs on keys via scripts.|
|C:\Windows\System32\Register-cimprovider.exe|Registers WMI/CIM providers. LOLBin that loads arbitrary provider DLLs into WMI.|
|C:\Windows\System32\regsvr32.exe|Top tier LOLBin: registers DLLs and executes scriptlets. The Squiblydoo pattern (regsvr32 /s /n /u /i:http scrobj.dll) runs code from a URL with a signed binary.|
|C:\Windows\System32\repadmin.exe|AD replication admin tool. /showrepl is benign recon, but combined with replication rights it underpins DCSync style attacks.|
|C:\Windows\System32\replace.exe|File replace tool. LOLBin usable to copy files to locations with side effects.|
|c:\windows\system32\reset.exe|Resets terminal server sessions. Attackers kick admins/users off sessions during intrusions.|
|C:\Windows\System32\robocopy.exe|Robust copy tool. Popular for staging and exfiltrating large data sets; watch /mir and bulk copies to unfamiliar destinations.|
|C:\Windows\System32\route.exe|Routing table editor. Changes support pivoting and traffic redirection.|
|C:\Windows\System32\rpcping.exe|RPC ping tool. Recon of RPC endpoints; minor but rarely used day to day.|
|C:\Windows\System32\runas.exe|Run program as another user. runas /netonly is used with plain credentials for remote access without local logon.|
|C:\Windows\System32\rundll32.exe|Mega LOLBin: executes DLL exports with patterns like setupapi InstallHinfSection, comsvcs MiniDump (lsass dump), shell32 Control_RunDLL and even javascript: URLs. Rich, high value detection surface.|
|c:\windows\system32\runexehelper.exe|Office click to run helper. LOLBin for proxy execution.|
|C:\Windows\System32\runonce.exe|RunOnce handler. LOLBin that can execute attacker supplied commands during fake setup flows.|
|C:\Windows\System32\sc.exe|Service control CLI. sc create/start/stop/config drives lateral movement and security tool tampering; correlates with System log 7045 events.|
|c:\windows\system32\schtasks.exe|Scheduled tasks CLI. Persistent and lateral movement classic: schtasks /create /s remotehost. Compare creations against change tickets.|
|C:\Windows\System32\scriptrunner.exe|App-V script runner. LOLBin that executes arbitrary commands and scripts through signed plumbing.|
|c:\windows\system32\scrobj.dll|Scriptlet object DLL. The payload half of the regsvr32 Squiblydoo technique; references to it in command lines are suspicious.|
|C:\Windows\System32\sdclt.exe|Backup and restore GUI tool. Known UAC bypass LOLBin (Folder hijack class).|
|C:\Windows\System32\secedit.exe|Security configuration tool. secedit /configure imports weakened security policy; watch for unexpected import and export use.|
|C:\Windows\System32\services.exe|Service Control Manager process. Children of services.exe represent service execution; a crash here forces reboot, so tampering is significant.|
|C:\Windows\System32\sethc.exe|Sticky keys. Replacing or hijacking it gives a SYSTEM shell from the logon screen, the textbook accessibility backdoor.|
|c:\windows\system32\setres.exe|Display resolution setter. Rarely used; verify context.|
|C:\Windows\System32\setspn.exe|SPN management tool. setspn -Q */* enumeration is the classic Kerberoasting recon step.|
|C:\Windows\System32\SettingSyncHost.exe|Settings sync host. LOLBin used as a signed proxy to launch other binaries.|
|c:\windows\system32\setupapi.dll|Driver install API DLL. LOLBin: rundll32 setupapi,InstallHinfSection runs INF commands.|
|C:\Windows\System32\setupugc.exe|Setup upgrade component. Rarely interactive; check context.|
|c:\windows\system32\shdocvw.dll|Shell document object DLL. rundll32 shdocvw,OpenURL is a proxy execution pattern.|
|c:\windows\system32\shell32.dll|Core shell DLL. Many rundll32 invocation patterns exist (Control_RunDLL etc.), a standard proxy execution family.|
|c:\windows\system32\shimgvw.dll|Legacy picture viewer DLL. Rare rundll32 target; minor risk.|
|C:\Windows\System32\sigverif.exe|Signature verification GUI. Benign; rarely used.|
|C:\Windows\System32\spool\drivers\color|Print driver colour profile folder. Historically writable and tied into print spooler abuse paths; unexpected files here deserve review.|
|C:\Windows\System32\spool\drivers\x64\3|Installed printer drivers. Rogue drivers landing here equal print spooler persistence or exploitation (PrintNightmare family).|
|C:\Windows\System32\spool\PRINTERS|Spooled print jobs (SPL/SHD files). Lets you see what was printed; also part of the spooler attack surface.|
|C:\Windows\System32\spool\tools\PrintBrm.exe|Printer migration tool. Can import printer settings including remote/attacker influenced configs; rarely used day to day.|
|C:\Windows\System32\spoolsv.exe|Print Spooler service. Exploitation target (PrintNightmare); child processes of spoolsv.exe are a prime detection.|
|C:\Windows\System32\sru\SRUDB.dat|System Resource Usage Monitor database. Records per app foreground time plus per app network bytes in/out per hour: excellent evidence of what ran and communicated.|
|c:\windows\system32\stordiag.exe|Storage diagnostic tool. Rare; verify context.|
|C:\Windows\System32\svchost.exe|Service host process. Heavy injection and C2 masquerade target: svchost without -k arguments or with an unexpected parent is a classic malware indicator.|
|C:\Windows\System32\SyncAppvPublishingServer.exe|App-V publishing sync tool. LOLBin that executes supplied commands.|
|C:\Windows\System32\SyncAppvPublishingServer.vbs|Script version of the App-V sync tool. Same LOLBin proxy execution angle via a signed VBS.|
|C:\Windows\System32\Sysprep|Sysprep folder on imaged machines. Unattend answer files sometimes left here can contain credentials.|
|c:\windows\system32\syssetup.dll|System setup DLL. Rare rundll32 target; minor.|
|C:\Windows\System32\systeminfo.exe|System info recon: OS version, patches, domain. A staple of attacker discovery scripts right after initial access.|
|C:\Windows\System32\takeown.exe|Ownership seizure tool. takeown on system or security tool files precedes tampering and destruction; also seen before mass encryption.|
|C:\Windows\System32\tar.exe|Built in bsdtar. Used to archive staged data (tar of document folders) before exfiltration.|
|C:\Windows\System32\taskkill.exe|Process killer. Bulk taskkill of SQL, backup and security tooling is a hallmark pre encryption ransomware step.|
|C:\Windows\System32\tasklist.exe|Process listing. Standard attacker recon to identify security tools and targets.|
|C:\Windows\System32\Tasks|Scheduled task files on disk. Rogue or renamed task XML files here can hide tasks that schtasks queries miss.|
|C:\Windows\System32\telnet.exe|Telnet client, not installed by default. Its presence or use is worth explaining; can be an exfil/test channel.|
|C:\Windows\System32\termsrv.dll|Remote Desktop service DLL. Patching or replacing it (concurrent session hacks) or hooking it for credential capture are known attacks; check integrity.|
|C:\Windows\System32\tftp.exe|Trivial FTP client. Simple download/exfil tool; rare legit use.|
|C:\Windows\System32\tracerpt.exe|ETL trace report tool. Rarely used; verify context.|
|C:\Windows\System32\tscon.exe|Session connect tool for Remote Desktop. Lets an attacker hijack another user's console/RDP session without their password; high signal on session hosts.|
|C:\Windows\System32\ttdinject.exe|Time travel debugging injector. Signed Microsoft injection capable tooling outside dev use is suspicious.|
|C:\Windows\System32\tttracer.exe|Time travel tracer. Same injection/tracing considerations as ttdinject.|
|C:\Windows\System32\unregmp2.exe|Windows Media Player setup tool. Obscure LOLBin family member; unexpected execution stands out.|
|c:\windows\system32\url.dll|URL monikers DLL. rundll32 url.dll,FileProtocolHandler or OpenURL patterns are proxy execution.|
|C:\Windows\System32\userinit.exe|Runs once per logon then should exit. Its target is defined by the Winlogon Userinit value, a classic persistence location; children that persist are suspicious.|
|C:\Windows\System32\utilman.exe|Utility Manager accessibility tool at the logon screen. Binary swap defensive check: an attacker with SYSTEM shell at logon is the misuse scenario.|
|C:\Windows\System32\vaultcmd.exe|Credential vault management CLI. Attackers enumerate stored vault credentials with it.|
|C:\Windows\System32\verclsid.exe|Class ID verification tool. LOLBin for proxy execution.|
|c:\windows\system32\vsjitdebugger.exe|Visual Studio just in time debugger. LOLBin that can launch processes; unexpected outside dev boxes.|
|C:\Windows\System32\vssadmin.exe|Shadow copy admin. 'vssadmin delete shadows /all /quiet' is the ransomware hallmark; alert loudly on any use on servers and modern endpoints.|
|C:\Windows\System32\wbadmin.exe|Backup admin tool. Deleting the backup catalog or system state backups is anti forensic; combined with vssadmin deletion it signals pre ransomware prep.|
|C:\Windows\System32\wbem|WMI infrastructure folder.|
|C:\Windows\System32\wbem\AutoRecover|MOF files registered for autorecovery into the WMI repository. Attackers drop MOF here historically for WMI persistence.|
|C:\Windows\System32\wbem\Logs|WMI text logs. Supporting detail for WMI based investigations.|
|C:\Windows\System32\wbem\mofcomp.exe|MOF compiler. Used to install malicious WMI providers and subscriptions; execution off admin workflows is suspicious.|
|C:\Windows\System32\wbem\Repository|WMI repository holding providers and permanent event subscriptions. Inspect it when hunting WMI persistence.|
|c:\windows\system32\wbem\wbemtest.exe|Interactive WMI test GUI. Rarely used legitimately day to day; interactive use by non admins is odd.|
|C:\Windows\System32\wbem\wmic.exe|Top LOLBin: remote command execution (process call create), XSL stylesheet code exec, and system recon. Deprecated and removable now, so simply detect and remove.|
|C:\Windows\System32\wbem\WmiPrvSE.exe|WMI provider host. Processes spawned under it mean WMI executed them (remote or subscription); beacon processes hiding under WmiPrvSE are a known pattern.|
|C:\Windows\System32\WerFaultSecure.exe|Secure crash reporting process. Rarely seen; verify parentage.|
|C:\Windows\System32\wevtutil.exe|Event log utility. 'wevtutil cl Security' clears logs; event 1102 confirms. Also used to export logs for collection. Clearing is a high signal anti forensics action.|
|C:\Windows\System32\whoami.exe|Identity and privilege display. whoami /priv and /groups spam is a post compromise recon staple, often in the same chain as systeminfo and net commands.|
|C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe|Windows PowerShell. The most abused built in tool: look for -enc/-e encoded commands, -w hidden, download cradles (IEX, DownloadString) and AMSI bypass strings.|
|C:\Windows\System32\WindowsPowerShell\v1.0\powershell_ise.exe|PowerShell ISE. Rarely used by admins on servers; script execution through it bypasses some transcript paths, so note usage.|
|C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1|All users PowerShell profile. Runs at every PowerShell start for every user; a quiet persistence spot worth reviewing.|
|C:\Windows\System32\winevt\Logs|Folder containing every Windows event log. Look for gaps, size anomalies and cleared logs.|
|C:\Windows\System32\winevt\Logs\Active Directory Web Services.evtx|AD Web Services authentication log on DCs. Useful for non interactive AD access by PowerShell AD module style tooling.|
|C:\Windows\System32\winevt\Logs\Application.evtx|Application event log. Application crashes here can reveal exploitation attempts; also hosts many third party app events.|
|C:\Windows\System32\winevt\Logs\DFS Replication.evtx|DFS Replication log on DCs. SYSVOL replication issues here can tie into GPO tampering timelines.|
|C:\Windows\System32\winevt\Logs\Directory Service.evtx|Directory Service log on DCs. Records replication, lingering objects and directory changes.|
|C:\Windows\System32\winevt\Logs\DNS Server.evtx|DNS Server log on DNS servers. Zone changes and transfers of interest in infrastructure attacks.|
|C:\Windows\System32\winevt\Logs\ForwardedEvents.evtx|Log receiving forwarded events via Windows Event Forwarding. On collectors this is your centralised evidence base.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-AAD%4Operational.evtx|Entra ID (AAD) operational log. Join, SSO and PRT related events; tampering here ties into cloud identity attacks.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-AppLocker%4EXE and DLL.evtx|AppLocker EXE/DLL log. Audit and block events (e.g. 8003/8004) show what policy stopped or would stop, including LOLBin attempts.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-AppLocker%4MSI and Script.evtx|AppLocker script/MSI log. Same idea for scripts, installers and packaged apps.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-Bits-Client%4Operational.evtx|BITS client operational log (events 3, 59, 60...). Traces BITS download and persistence jobs even when bitsadmin history is cleared.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-CAPI2%4Operational.evtx|Crypto API operational log. Certificate chain building and retrieval events; useful for detecting rogue certs and interception roots.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-CodeIntegrity%4Operational.evtx|Code Integrity log. Blocked unsigned or policy violating drivers appear here: the BYOVD early warning feed.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider%4Admin.evtx|MDM/Intune administrative events. Enrollment and management actions; rogue enrollments of devices or reconfigurations show up here.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-DHCP-Server%4Operational.evtx|DHCP server operational log. Lease grants and server events; rogue DHCP activity is relevant to on path attacks.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-DNS-Client%4Operational.evtx|DNS client log (event 3020 among others). Records domains the host resolved, supporting C2 domain confirmation.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-DNSServer%4Analytical.etl|High volume DNS server analytical channel (ETL). Enable during investigations on DNS servers/DCs to capture full query detail.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-DNSServer%4Audit.evtx|DNS server audit log. Zone and record changes; attacker modifications to internal DNS show up here.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-DriverFrameworks-UserMode%4Operational.evtx|User mode driver framework log. Driver and device activity including USB related user mode drivers.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-GroupPolicy%4Operational.evtx|Group Policy operational log. Shows what GPOs applied, from where, and errors, great for GPO tamper timelines.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-Kernel-PnP%4Configuration.evtx|Kernel PnP configuration log. Device installation evidence.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-LAPS%4Operational.evtx|LAPS operational log. Local admin password rotation and retrieval events; unexpected accesses stand out.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-NTLM%4Operational.evtx|NTLM operational log on servers. NTLMv1 usage and restrictions events assist pass the hash and NTLM relay hunting.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-OpenSSH%4Operational.evtx|OpenSSH server operational log. SSH authentication events including key based logins and brute force patterns.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-PowerShell%4Operational.evtx|The premium PowerShell log: 4103 module logging and 4104 script block logging capture what scripts actually ran. Any attempt to disable or tamper with it is itself a red flag.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-PrintService%4Admin.evtx|PrintService admin log. Driver and spooler errors; exploitation attempts (PrintNightmare family) leave traces here.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-PrintService%4Operational.evtx|PrintService operational log. Print jobs (event 307) and driver installs (event 316 etc.); unexpected driver installs are suspicious.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-RemoteDesktopServices-RdpCoreTS%4Operational.evtx|RDP core log. Captures RDP connection metadata including remote client names and crypto negotiation.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-Security-Mitigations%4KernelMode.evtx|Kernel mode security mitigation blocks. Evidence of exploit attempts stopped by mitigations.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-SENSE%4Operational.evtx|MDE (SENSE) operational log. Sensor health, tamper protection and onboarding events; gaps here coincide with defence evasion.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-SmbClient%4Security.evtx|SMB client security log. Insecure guest logons, NTLM fallback and signing failures highlight downgrade and relay conditions.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-SMBServer%4Security.evtx|SMB server security log. Share authentication failures and insecure access attempts: share brute force and relay evidence.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-Sysmon%4Operational.evtx|Sysmon log. If deployed, the workhorse telemetry feed: process creation with hashes and command lines (1), network connections (3), DNS (22), file creation (11). Its absence or tampering is an alert on its own.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-TaskScheduler%4Operational.evtx|Task Scheduler operational log (events 106, 200, 201). Catches task creation and execution even after the attacker deletes the task.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-Gateway%4Operational.evtx|RD Gateway log. External RDP authentications through the gateway; key for internet facing RDP investigations.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx|Local session manager log: events 21/23/24/25 record RDP and local session connect/disconnect with source hosts. Core lateral movement evidence.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-RDPClient%4Operational.evtx|Outbound RDP client log. Event 1102 records which servers this host RDPed to, tracking attacker movement FROM this machine.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-TerminalServices-RemoteConnectionManager%4Operational.evtx|Remote Connection Manager log. Event 1149 ties users to RDP source network info: fast answers to 'who RDPed in'.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-User Profile Service%4Operational.evtx|User Profile Service log. New profile creation maps to first logon of a user on that host; useful for spotting new local accounts.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-VHDMP%4Operational.evtx|VHD mount events. Tracks virtual disk attachment including suspect VHD use.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-Windows Defender%4Operational.evtx|Defender operational log: detections (1116), actions (1117) and config changes (5001/5007) such as exclusion additions. Exclusion changes before an incident are classic defence evasion.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-Windows Firewall With Advanced Security%4Firewall.evtx|Windows Firewall advanced security log. Rule additions (2004 family) and policy changes; attacker added allow rules leave evidence here.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-WindowsUpdateClient%4Operational.evtx|Windows Update client log. Patch events and failures establish the update timeline; long patching pauses can be deliberate.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-Winlogon%4Operational.evtx|Winlogon operational log. Session and notification package activity around logon.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-WinRM%4Operational.evtx|WinRM operational log (events 91, 168 among others). Records remote PowerShell and WinRM sessions: prime lateral movement evidence.|
|C:\Windows\System32\winevt\Logs\Microsoft-Windows-WMI-Activity%4Operational.evtx|WMI activity log. Event 5861 records permanent event subscription registrations, the WMI persistence detection.|
|C:\Windows\System32\winevt\Logs\Operations Manager.evtx|SCOM Operations Manager agent log on monitored servers.|
|C:\Windows\System32\winevt\Logs\PowerShellCore%4Operational.evtx|PowerShell 7 operational log. Mirrors the 4104 style value for the newer PowerShell runtime.|
|C:\Windows\System32\winevt\Logs\Security.evtx|The core Security log: 4624/4625 logons, 4688 process creation, 4698 scheduled tasks, 4732 group changes, 4769/4771 Kerberos, 1102 log cleared. Centre of most investigations.|
|C:\Windows\System32\winevt\Logs\Setup.evtx|Setup log. OS servicing and installation events.|
|C:\Windows\System32\winevt\Logs\System.evtx|System log. Includes 7045 new service installs (persistence and lateral movement), 7000 service failures and boot/shutdown markers 6005 6009.|
|C:\Windows\System32\winevt\Logs\Windows PowerShell.evtx|Legacy Windows PowerShell log (400/403/600). With logging policy it captures engine and command execution history.|
|C:\Windows\System32\winfile.exe|Legacy File Manager. LOLBin that can launch programs; near zero legitimate use today.|
|C:\Windows\System32\winlogon.exe|Logon session manager. Persistence via its registry values is common, and a lookalike winlogon.exe in the wrong folder is a classic trojan tell.|
|C:\Windows\System32\winrm.vbs|Legacy WinRM configuration script. Rarely used now; scripted usage is notable.|
|C:\Windows\System32\winrs.exe|WinRM command shell client. Executes commands on remote hosts; lateral movement tooling.|
|c:\windows\system32\wlrmdr.exe|Windows logon reminder component. Obscure; execution outside expected scenarios is worth a check.|
|C:\Windows\System32\WorkFolders.exe|Work Folders sync client. Rarely deployed; unexpected syncing could be an exfil channel.|
|C:\Windows\System32\wscript.exe|Windows Script Host GUI engine. Runs VBS/JS droppers just like cscript; unexpected parents and network traffic are the tells.|
|C:\Windows\System32\wsl.exe|Windows Subsystem for Linux launcher. LOLBin that runs Linux ELF payloads and commands, sidestepping some Windows focused controls.|
|C:\Windows\System32\wsmprovhost.exe|Host process for remote PowerShell sessions over WinRM. Its presence means someone is remoted in via PowerShell.|
|C:\Windows\System32\wsreset.exe|Store cache reset tool. Known UAC bypass LOLBin via registry hijack (delegate execute pattern).|
|C:\Windows\System32\wuauclt.exe|Windows Update client launcher. Command line use is rare now; masquerading under this name outside System32 is the bigger risk.|
|C:\Windows\System32\xwizard.exe|Setup wizard framework tool. LOLBin that loads attacker supplied DLLs or runs XML driven commands.|
|c:\windows\system32\zipfldr.dll|Zip folder explorer DLL. rundll32 invocation patterns exist for proxy execution.|
|C:\Windows\SYSVOL\domain|SYSVOL domain share replicated to all DCs: GPOs and logon scripts for the domain. Tampering equals domain wide execution.|
|C:\Windows\SYSVOL\domain\Policies\PolicyDefinitions|Central store of ADMX templates in SYSVOL.|
|C:\Windows\SYSVOL\domain\Policies\{<GPO-GUID>}|Per GPO folder in SYSVOL. Compare timestamps and version numbers against AD to catch sneaky GPO edits.|
|C:\Windows\SYSVOL\domain\Policies\{<GPO-GUID>}\Machine\Microsoft\Windows NT\SecEdit\GptTmpl.inf|Security settings template within a GPO (password policy, audit policy etc.). Changes here ripple across the domain.|
|C:\Windows\SYSVOL\domain\Policies\{<GPO-GUID>}\Machine\Preferences\Groups\Groups.xml|Group Policy Preferences local users file. Historically held AES protected (cpassword) credentials that are trivially decryptable; still worth checking today.|
|C:\Windows\SYSVOL\domain\scripts|SYSVOL scripts share holding domain logon scripts. Editing or adding scripts here executes at every affected user logon: high value persistence.|
|C:\Windows\SysWOW64|32 bit system binary folder on 64 bit Windows. Awareness matters: 32 bit versions of tools bypass some path based rules and confuse analysts.|
|C:\Windows\Tasks|Legacy task folder (.job files). Rogue tasks can hide here with low visibility.|
|C:\Windows\Temp|World writable system temp folder. Common staging area where any user can drop files; watch for executables and staged archives.|
|C:\Windows\WinSxS|Component store holding OS components. Very large; unauthorised modifications can backdoor system components.|
|C:\Windows\WinSxS\amd64_microsoft-windows-u..ed-telemetry-client_31bf3856ad364e35_10.0.16299.15_none_c2df1bba78111118\Runscripthelper.exe|Component store copy of a telemetry related helper. The vulnerability research around this exact file made it noteworthy; baseline and verify signature.|
|C:\Windows\write.exe|WordPad launcher shim. Minor LOLBin surface; unexpected invocation is odd.|
|HKCU\Control Panel\Desktop|Per user desktop settings including SCRNSAVE.EXE, the screensaver value. Setting it to an attacker binary gives persistence with a GUI launch trigger.|
|HKCU\Environment|User environment variables. The UserInitMprLogonScript value here defines a logon script: a lesser known persistence spot.|
|HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\BagMRU|Shellbags for the user: folder browsing history stored in the registry. Survives deletion and proves what folders and shares a user opened.|
|HKCU\Software\Microsoft\Office\<version>\<App>\Security\Trusted Documents\TrustRecords|Office Trust Records: documents the user chose to trust (enable content). Records that malicious docs were opened and trusted, useful in phishing investigations.|
|HKCU\Software\Microsoft\Terminal Server Client\Servers|Per server RDP client history including stored usernames per server. Maps where the user RDPed and as whom.|
|HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSavePidlMRU|Open/save dialog MRU by file extension. Evidence of documents accessed and saved through common dialogs.|
|HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs|Registry record of recently opened documents and folders.|
|HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU|Commands typed in the Start Run box. Often captures attacker or admin commands that never touched a console history.|
|HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths|Paths typed into the Explorer address bar, including UNC shares. Shows direct network browsing.|
|HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{<GUID>}\Count|Per user GUI program execution records (ROT13 encoded names) with run counts and timestamps. Solid execution evidence especially on servers.|
|HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings|User proxy configuration. Attacker set ProxyServer or AutoConfigURL (PAC) values enable traffic interception; review changes.|
|HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run|Per user autostart registry key. Anything listed runs at that user's logon: the most common persistence location; review value names and paths.|
|HKLM\SOFTWARE\Classes\CLSID\{<CLSID>}\InprocServer32|COM server DLL registration. Hijacking or proxying CLSIDs loaded by logon processes (like explorer) is a stealthy persistence technique.|
|HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components|Active Setup entries run a StubPath command at each user's logon. Abuse gives machine installed, per user execution persistence.|
|HKLM\SOFTWARE\Microsoft\CCM\Logging\@Global|SCCM client logging configuration. Tampering reduces client log fidelity.|
|HKLM\SOFTWARE\Microsoft\Enrollments|MDM enrollment records. Rogue enrollments or tampered management entries are visible here.|
|HKLM\SOFTWARE\Microsoft\IntuneManagementExtension|Intune Management Extension configuration. Correlates with its ProgramData logs during Intune based attack investigations.|
|HKLM\SOFTWARE\Microsoft\NetSh|netsh helper DLL registrations. A malicious helper registered here loads with netsh: obscure but effective persistence.|
|HKLM\SOFTWARE\Microsoft\Office test\Special\Perf|Little known Office test key that can point Office to load a DLL at startup. Office persistence vector.|
|HKLM\SOFTWARE\Microsoft\SystemCertificates\ROOT\Certificates|Machine trusted root CA store. An extra root here enables TLS interception; compare against known good lists.|
|HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status|MDE (Defender for Endpoint) onboarding state. Offboarding or tamper attempts reduce EDR coverage.|
|HKLM\SOFTWARE\Microsoft\Windows Defender\Exclusions|Defender exclusion list. Attackers add path/process exclusions before dropping tooling: one of the highest signal defence evasion artifacts.|
|HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\InstalledSDB|Installed custom compatibility shims. Malicious SDB shims (e.g. RedirectEXE) provide sneaky persistence.|
|HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options|Image File Execution Options: per binary settings including the Debugger value. Setting Debugger on sethc.exe/utilman.exe etc. is classic persistence; also check VerifierDll.|
|HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles|Known network profiles with names, first and last connection timestamps. Supports physical movement and rogue network analysis.|
|HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks\{<TaskGUID>}|Binary task definitions per GUID. Stealth tasks may exist here even when missing from schtasks output.|
|HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree|Mapping of task names and paths to their GUIDs. Complements the Tasks entries for full task visibility.|
|HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit|SilentProcessExit: defines a MonitorProcess launched when a target process exits. Abused for persistence and to dump lsass when it exits.|
|HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows|Old school AppInit_DLLs injection vector lives in this key (legacy OS versions). Any populated AppInit_DLLs value is suspicious.|
|HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon|Winlogon values including Shell and Userinit. Changing Shell from explorer.exe or appending to Userinit are textbook persistence moves.|
|HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\ShellServiceObjectDelayLoad|Shell service objects loaded at user logon. Adding entries here gives logon triggered persistence.|
|HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System|System policy values including EnableLUA and LocalAccountTokenFilterPolicy. Attackers disable UAC or set LocalAccountTokenFilterPolicy=1 to enable remote local admin logons.|
|HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\Audit|Advanced audit policy as written to the registry. Tampering with categories weakens your detection surface.|
|HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run|Machine wide autostart key: every listed value runs at every user logon. Review names and binary paths regularly.|
|HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection|MDE policy key. Tampering here weakens or disables the sensor.|
|HKLM\SOFTWARE\Policies\Microsoft\Windows Defender|Defender policy key. Policy delivered exclusions can hide here as well as under the main Defender key; review both.|
|HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell|PowerShell logging policy (script block, module, transcription). Disabling these blinds the 4104 evidence trail.|
|HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard|Device Guard / WDAC code integrity policy configuration. Disabling application control here is defence evasion.|
|HKLM\SYSTEM\CurrentControlSet\Control\Lsa|LSA configuration. Watch for added Authentication/Security Packages (custom SSPs like mimilib capture plaintext creds) and RunAsPPL state.|
|HKLM\SYSTEM\CurrentControlSet\Control\Lsa\FipsAlgorithmPolicy|FIPS mode flag. Changes can break application crypto and are worth explaining.|
|HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters|Kerberos policy parameters on DCs. Unexpected changes weaken domain authentication security.|
|HKLM\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order|Network provider order list. Custom provider DLLs registered here load at every logon: persistence.|
|HKLM\SYSTEM\CurrentControlSet\Control\Print\Environments\Windows x64\Print Processors|Print processor DLLs loaded by the spooler. An attacker DLL here runs as SYSTEM in spoolsv: well documented persistence.|
|HKLM\SYSTEM\CurrentControlSet\Control\Print\Monitors|Print monitor DLL registrations. Adding a monitor is classic SYSTEM level persistence via the spooler.|
|HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot|Services allowed in Safe Mode. Malware sometimes flips a system into safe boot or tampers here to dodge security tools.|
|HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest|WDigest setting. UseLogonCredential=1 re enables plaintext password caching in memory, which is exactly what Mimikatz wants: very high signal.|
|HKLM\SYSTEM\CurrentControlSet\Control\Session Manager|Session Manager values including BootExecute and PendingFileRenameOperations. Both are abused for boot time persistence and for deleting locked security files.|
|HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache|ShimCache: records binaries that ran (or were touched) with timestamps, surviving deletion of the file. Core execution evidence on servers.|
|HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment|System wide environment variables. PATH manipulation here enables DLL search order hijacking across the machine.|
|HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server|Terminal Server settings. fDenyTSConnections flipped to 0 means someone enabled RDP; port changes and security downgrades also appear here.|
|HKLM\SYSTEM\CurrentControlSet\Control\TimeZoneInformation|Machine time zone. Needed to normalise artifact timestamps during analysis.|
|HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR|USB storage device history: device serials, friendly names and first/last connection times (with related logs). Primary evidence for USB based data theft.|
|HKLM\SYSTEM\CurrentControlSet\Services|All Windows service definitions. New services equal persistence: inspect odd ImagePaths, random names and non standard binaries.|
|HKLM\SYSTEM\CurrentControlSet\Services\bam\State\UserSettings\<SID>|Background Activity Moderator data: per user last execution timestamps of programs (Windows 10 1709+). Fast execution evidence even for GUI apps.|
|HKLM\SYSTEM\CurrentControlSet\Services\CertSvc\Configuration\<CAName>|Certificate authority configuration on AD CS servers. Dangerous flags (for example EDITF_ATTRIBUTESUBJECTALTNAME2) enable certificate based persistence and privilege escalation; audit them.|
|HKLM\SYSTEM\CurrentControlSet\Services\DNS\Parameters|DNS server service config. The ServerLevelPluginDll value loads a custom DLL into the DNS service at startup: stealthy SYSTEM persistence on DNS servers, often DCs.|
|HKLM\SYSTEM\CurrentControlSet\Services\EventLog|Event Log service configuration per log channel. Retention and size tampering or disabled services reduce your evidence.|
|HKLM\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters|Netlogon settings on DCs. Secure channel and site settings; weakening changes are notable.|
|HKLM\SYSTEM\CurrentControlSet\Services\NTDS\Parameters|AD DS service parameters. Changes here on DCs deserve review.|
|HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy|Registry copy of firewall policy rules and profile settings. Attacker added allow rules show up here as well as in the firewall event log.|
|HKLM\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders|Windows Time providers. A custom time provider DLL registered here loads into the w32time service: obscure persistence.|
|HKLM\SYSTEM\MountedDevices|Drive letter and volume mount history including USB volumes and encrypted container mounts. Shows what storage was attached.|
|<ESP>\EFI\Microsoft\Boot|UEFI boot files on the EFI system partition. Bootkits target this area; unexpected modifications are significant.|
|<no default path>\Bginfo.exe|Sysinternals BGInfo. Dual use: benign wallpaper watermark, but its custom fields execute VBS, making it a signed script runner LOLBin.|
|<no default path>\dnx.exe|Legacy .NET execution environment host. Runs .NET code; LOLBin on machines where present.|
|<no default path>\msxsl.exe|MSXSL command line XSLT processor. Runs XSLT with embedded JScript for code execution that bypasses many allow lists: clean LOLBin.|
|<no default path>\Procdump.exe|Sysinternals ProcDump. Attackers use it to dump lsass memory for offline credential extraction; any use on servers or DCs needs justification.|
|<no default path>\rcsi.exe|Roslyn C# interactive from Visual Studio. Executes C# scripts: dev host LOLBin.|
|<no default path>\te.exe|Test Authoring and Execution Framework runner. Executes test binaries through signed Microsoft tooling: LOLBin.|
|<no default path>\Tracker.exe|MSBuild file tracking tool. LOLBin that can be made to spawn arbitrary processes via its tracking interface.|
|\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy<N>|Direct device path to a volume shadow copy. Tools open this to read locked files (SAM, ntds.dit) from snapshots; unexpected access is high signal.|
