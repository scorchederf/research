---
created: 2026-11-21
fullpath: 'C:\Windows\System32\scriptrunner.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - app-v
  - scripting
aliases:
  - scriptrunner.exe
  - ScriptRunner.exe
  - ScriptRunner
url:
  - https://learn.microsoft.com/microsoft-desktop-optimization-pack/app-v/appv-dynamic-configuration
  - https://learn.microsoft.com/microsoft-desktop-optimization-pack/appv-v5/about-app-v-51-dynamic-configuration
---

**fullpath**:C:\Windows\System32\scriptrunner.exe

# description

ScriptRunner.exe is the script launcher application included in the App-V client. It lets an App-V package run multiple scripts on a single event trigger (AddPackage, PublishPackage, StartProcess and so on) defined in the dynamic deployment or user configuration file.

## simple description

> ### 2026-11-21 Claude said
> ScriptRunner.exe is a helper that ships with Microsoft App-V (application virtualization). App-V packages can run scripts at events like adding or publishing a package, and ScriptRunner lets one event run several scripts in sequence. Each script is passed after an -appvscript token with its own arguments and options. In Windows 10/11 it lives in System32 because the App-V client is built in.
>
> **SOC NOTE**: A known LOLBin (signed Microsoft binary proxy execution, MITRE ATT&CK T1218): `scriptrunner.exe -appvscript <payload>` launches arbitrary executables or scripts, including from UNC paths. Alert on ScriptRunner process creation outside App-V deployments, especially with network paths or unusual child processes (Sysmon Event 1 / Security 4688).
>

# purpose

Runs each script passed to it separately with the arguments specified, so App-V can support multiple scripts per event trigger; use only one ScriptRunner.exe entry per trigger. It runs any script whose file type is associated with an installed application. The App-V client location must be in %path% for ScriptRunner to run.

# typical use cases

| usage | description |
| --- | --- |
| `ScriptRunner.exe -appvscript script1.exe arg1 arg2 -appvscriptrunnerparameters -wait -timeout=10 -appvscript script2.vbs arg1 arg2` | Run script1.exe, wait up to 10 seconds for it, then run script2.vbs (as used in a dynamic configuration file). |
| `ScriptRunner.exe -appvscript script3.bat arg1 arg2 -appvscriptrunnerparameters -wait -timeout=30 -rollbackonerror` | Run script3.bat, stop after 30 seconds and roll back an error to the App-V client on failure. |

# options

| option | description |
| --- | --- |
| `-appvscript` | Token that represents the actual script to run, followed by the script name and its arguments. |
| `-appvscriptrunnerparameters` | Token that represents the execution options for the preceding script. |
| `-wait` | Wait for the script to complete before proceeding to the next script. |
| `-timeout=x` | Stop running the current script after x seconds; other specified scripts still run. |
| `-rollbackonerror` | Stop running all scripts that have not yet run and roll back an error to the App-V client. |
