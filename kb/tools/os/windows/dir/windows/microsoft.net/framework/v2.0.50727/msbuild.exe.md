---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework\v2.0.50727\Msbuild.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
  - build
  - lolbin
  - appcontrol-bypass
aliases:
  - 'Msbuild.exe'
  - 'MSBuild'
  - 'Microsoft Build Engine'
url:
  - https://learn.microsoft.com/visualstudio/msbuild/msbuild-command-line-reference?view=visualstudio
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/design/applications-that-can-bypass-appcontrol
---

**fullpath**:C:\Windows\Microsoft.NET\Framework\v2.0.50727\Msbuild.exe

# description

`MSBuild.exe` is the Microsoft Build Engine, which builds project and solution files; this copy is the one installed with .NET Framework 2.0 (v2.0.50727). The .NET CLI commands (`dotnet build`, `dotnet msbuild`, ...) pass the same switches to MSBuild. Note: the options below come from the current MSBuild reference; older framework builds support a subset.

## simple description

> ### 2026-11-21 Claude said
> MSBuild reads an XML project file (.csproj, .proj, etc.) and runs the build steps (targets and tasks) defined in it. Because a project file can contain inline C# code tasks, MSBuild can compile and run arbitrary code without a separate compiler. It ships with every .NET Framework install, so it exists on almost every Windows machine, signed by Microsoft.
>
> **SOC NOTE**: Classic trusted-developer-utility proxy execution (T1127.001): attackers run `msbuild.exe payload.xml/.csproj` with inline tasks to execute shellcode or C# while bypassing application allow-listing. Microsoft lists msbuild.exe and Microsoft.Build.dll on its App Control block list. Alert on MSBuild launched by Office, script hosts, wmiprvse or from user-writable folders, on project files outside source trees, and on MSBuild making network connections or spawning children.
>

# purpose

Builds the targets in the project file you specify; with no project file, MSBuild searches the working directory for a file whose extension ends in *proj*, and it also accepts Visual Studio solution files. Every switch is available as `-switch` and `/switch` and switches aren't case-sensitive. Microsoft's App Control guidance lists msbuild.exe among applications an attacker could use to bypass application allow policies and recommends blocking it except on development systems that need it.

# typical use cases

| usage | description |
| --- | --- |
| `MSBuild.exe MyProject.proj -t:rebuild` | Build the `rebuild` target of *MyProject.proj*. |
| `msbuild myproject.proj -maxcpucount:3` | Build using three MSBuild processes. |
| `msbuild myfile.proj -flp:FileLogger,Microsoft.Build;logfile=MyLog.log;append=true` | Append the build log to *MyLog.log*. |

# options

| option | description |
| --- | --- |
| `-detailedSummary[:{True or False}]` / `-ds` | Show detailed information at the end of the log about configurations built and how they were scheduled to nodes. |
| `-getItem:{itemName,...}` | Write out item values after evaluation without building (or after the build with `-targets`/`-getTargetResult`). |
| `-getProperty:{propertyName,...}` | Write out property values after evaluation without building (or after the build). |
| `-getTargetResult:{targetName,...}` | Write out the output values of the specified targets. |
| `-graphBuild[:{True or False}]` / `-graph` | Construct and build a project graph, building references first. Requires MSBuild 16 or later. |
| `-help` / `/?` / `-h` | Display usage information. |
| `-ignoreProjectExtensions:{extensions}` / `-ignore` | Ignore the specified extensions when determining which project file to build. |
| `-inputResultsCaches[:{cacheFile;...}]` / `-irc` | Input cache files MSBuild reads build results from; sets `-isolateProjects` to True. |
| `-interactive[:{True or False}]` | Allow actions in the build to interact with the user; not for automated scenarios. |
| `-isolateProjects[:{True, MessageUponIsolationViolation, False}]` / `-isolate` | Build each project in isolation. |
| `-lowPriority[:{True or False}]` / `-low` | Run MSBuild at low process priority. |
| `-maxCpuCount[:{number}]` / `-m` | Maximum number of concurrent build processes; default 1, or all processors if no value is given. |
| `-multiThreaded[:{True or False}]` / `-mt` | Enable multithreaded task execution within one MSBuild process. Requires MSBuild 18.4 or later. |
| `-noAutoResponse` / `-noautorsp` | Don't automatically include *MSBuild.rsp* or *Directory.Build.rsp* files. |
| `-nodeReuse:{value}` / `-nr` | Enable (True, default) or disable reuse of MSBuild nodes after the build. |
| `-nologo` | Don't display the startup banner or copyright message. |
| `-preprocess[:{filepath}]` / `-pp` | Create a single aggregated project file by inlining all imports; the project isn't built. |
| `-outputResultsCache[:{cacheFile}]` / `-orc` | Output cache file for build result caches; sets `-isolateProjects` to True. |
| `profileEvaluation:{file}` | Profile MSBuild evaluation and write the result to the file (Markdown if `.md`, else tab-separated). |
| `-property:{name}={value}` / `-p` | Set or override project-level properties. |
| `-restore` / `-r` | Run the `Restore` target before building the actual targets. |
| `-restoreProperty:{name}={value}` / `-rp` | Set or override project properties only during restore. |
| `-target:{targets}` / `-t` | Build the specified targets instead of the `DefaultTargets`. |
| `-targets[:{file}]` / `-ts` | Write the list of available targets to a file or the console without building. |
| `-toolsVersion:{version}` / `-tv` | Specify a custom toolset. |
| `-validate:[{schema}]` / `-val` | Validate the project file (against the default or given schema) and build if valid. |
| `-verbosity:{level}` / `-v` | Build log detail: `q[uiet]`, `m[inimal]`, `n[ormal]` (default), `d[etailed]`, `diag[nostic]`. |
| `-version` / `-ver` | Display version information only; the project isn't built. |
| `@{file}` | Insert command-line switches from a response file. |
| `-warnAsError[:{code;...}]` / `-err` | Treat the listed (or all) warnings as errors. |
| `-warnNotAsError[:{code;...}]` / `-noerr` | Warning codes not to promote to errors when `-warnAsError` promotes all. MSBuild 17.0 and later. |
| `-warnAsMessage[:{code;...}]` / `-noWarn` | Treat the listed warnings as low-importance messages. |
| `-binaryLogger[:[LogFile=]{output.binlog}[;ProjectImports=None,Embed,ZipFile]]` / `-bl` | Serialize all build events to a compressed binary log (default *msbuild.binlog*). |
| `-consoleLoggerParameters:{parameters}` / `-clp` | Pass parameters (PerformanceSummary, Summary, ErrorsOnly, ShowTimestamp, Verbosity, ...) to the console logger. |
| `-distributedFileLogger` / `-dfl` | Log each MSBuild node's output to its own file (*MSBuild{NodeId}.log*). |
| `-distributedLogger:{central logger},{forwarding logger}` / `-dl` | Attach a different logger instance to each node. |
| `-fileLogger[{number}]` / `-fl` | Log build output to *msbuild.log* (or *msbuild<n>.log*) in the current directory. |
| `-fileLoggerParameters[{number}]:{parameters}` / `-flp` | Extra parameters for the file logger: LogFile, Append, Encoding plus console logger parameters. |
| `-logger:logger` / `-l` | Specify a logger as `[LoggerClass,]LoggerAssembly[;LoggerParameters]`. |
| `-noConsoleLogger` / `-noconlog` | Disable the default console logger. |
| `-terminalLogger[:auto,on,off]` / `-tl` | Enable or disable the terminal logger. MSBuild 17.8 and later. |
