---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework64\v2.0.50727\RegSvcs.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
aliases:
  - "RegSvcs.exe"
  - ".NET Services Installation Tool"
url:
  - https://learn.microsoft.com/dotnet/framework/tools/regsvcs-exe-net-services-installation-tool
---

**fullpath**:C:\Windows\Microsoft.NET\Framework64\v2.0.50727\RegSvcs.exe

# description

Regsvcs.exe, the .NET Services Installation tool, loads and registers an assembly, generates, registers and installs a type library into a specified COM+ application, and configures services added programmatically to a class. It ships with the .NET Framework; related tools include Regasm.exe and Installutil.exe.

## simple description

> ### 2026-11-21 Claude said
> RegSvcs.exe is a .NET Framework tool that registers a .NET assembly as a COM+ (Enterprise Services) application. It loads the assembly, creates a type library and installs it into COM+. Administrative rights are required, and the assembly must be strong-name signed.
>
> **SOC NOTE**: A well-known signed-binary proxy execution LOLBin (MITRE ATT&CK T1218.009 Regsvcs/Regasm): attackers run `regsvcs.exe evil.dll` so code in the assembly's registration functions executes under a Microsoft-signed process, bypassing application control. Alert on RegSvcs.exe launched from user-writable paths, by Office/scripting parents, or making network connections.
>

# purpose

Registers .NET assemblies with COM+ by loading the assembly, producing and installing a type library into a COM+ application, and configuring declared services.

# typical use cases

| usage | description |
| --- | --- |
| `regsvcs /appname:myTargetApp myTest.dll` | Adds all public classes in myTest.dll to the existing COM+ application myTargetApp and produces myTest.tlb. |
| `regsvcs /appname:myTargetApp /tlb:newTest.tlb myTest.dll` | Adds the classes to myTargetApp and produces the newTest.tlb type library. |

# options

| option | description |
| --- | --- |
| `assemblyFile.dll` | The source assembly file; must be signed with a strong name. |
| `/appdir:path` | Specifies the root directory of the application. |
| `/appname:applicationName` | Specifies the name of the COM+ application to find or create. |
| `/c` | Creates the target application. |
| `/componly` | Configures components only; ignores methods and interfaces. |
| `/exapp` | Expects an existing application. |
| `/extlb` | Uses an existing type library. |
| `/fc` | Finds or creates the target application. |
| `/help` | Displays command syntax and options. |
| `/noreconfig` | Does not reconfigure an existing target application. |
| `/nologo` | Suppresses the Microsoft startup banner. |
| `/parname:name` | Specifies the name or id of the COM+ application to find or create. |
| `/reconfig` | Reconfigures an existing target application (default). |
| `/tlb:typelibraryfile` | Specifies the type library file to install. |
| `/u` | Uninstalls the target application. |
| `/quiet` | Quiet mode; suppresses logo and success message. |
| `/?` | Displays command syntax and options. |
