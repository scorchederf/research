---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\Launch-VsDevShell.ps1'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - visualstudio
  - powershell
aliases:
  - Launch-VsDevShell.ps1
  - Developer PowerShell
  - Developer PowerShell for VS 2019
url:
  - https://learn.microsoft.com/visualstudio/ide/reference/command-prompt-powershell?view=visualstudio
---

**fullpath**:C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\Launch-VsDevShell.ps1

# description

`Launch-VsDevShell.ps1` is the PowerShell script that starts the Visual Studio Developer PowerShell, a PowerShell session with the same environment variables as the Developer Command Prompt (`VsDevCmd.bat`). It ships with Visual Studio (here the 2019 Community edition) in the `Common7\Tools` folder. It locates the `Microsoft.VisualStudio.DevShell.dll` module in the Visual Studio install path, loads it, and calls the `Enter-VsDevShell` cmdlet.

## simple description

> ### 2026-11-21 Claude said
> This is a PowerShell script installed with Visual Studio 2019 Community. Running it turns a normal PowerShell window into a "Developer PowerShell" where build tools like `msbuild`, `cl`, `dumpbin` and `ildasm` are on the PATH. Developers use it to compile code from the command line or in build scripts. It is a normal, Microsoft-signed file on developer machines.
>
> **SOC NOTE**: Its presence shows a developer toolchain is installed, which gives attackers living-off-the-land binaries such as `msbuild.exe` (T1127.001 Trusted Developer Utilities Proxy Execution). A Developer PowerShell started on a non-developer host, or right before `msbuild`/`csc` compiles unknown project files, is suspicious. Check the script hash and signature, because a changed script in a writable install path would run in every developer shell. PowerShell script block logging (Event ID 4104) records its execution.
>

# purpose

Sets up the developer environment in PowerShell so command-line tools (MSBuild, dotnet, clrver, ildasm, CL, NMAKE, LIB, DUMPBIN) can be used without knowing where they are installed. By default the shell is configured for the Visual Studio installation that contains the script, and it starts in the Visual Studio Project Location. Microsoft calls it the recommended way to start Developer PowerShell interactively or for build automation scripts. The PowerShell execution policy must allow it to run.

# typical use cases

| usage | description |
| --- | --- |
| `& 'C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools\Launch-VsDevShell.ps1'` | Start Developer PowerShell for Visual Studio 2019 Community from a Windows PowerShell or PowerShell 6 prompt. |
| `& 'C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\Launch-VsDevShell.ps1' -Arch arm64 -HostArch amd64` | Start Developer PowerShell for VS 2022 (17.1 or later) on a 64-bit machine, building outputs that target ARM64. |
| `& '...\Launch-VsDevShell.ps1' -SkipAutomaticLocation` | Start the shell and stay in the current directory instead of the Project Location. |

# options

| option | description |
| --- | --- |
| `-Arch <Target Architecture>` | Target architecture for build outputs (x86 default, amd64, arm, arm64). Available beginning with Visual Studio 2022 version 17.1. |
| `-HostArch <Host Architecture>` | Architecture of the build tool binaries (x86 default, amd64). Available beginning with Visual Studio 2022 version 17.1. |
| `-SkipAutomaticLocation` | Keeps the shell in the current directory instead of switching to the Visual Studio Project Location. |
