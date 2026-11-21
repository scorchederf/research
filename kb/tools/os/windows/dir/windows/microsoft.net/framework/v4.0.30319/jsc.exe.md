---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework\v4.0.30319\Jsc.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - dotnet
  - compiler
  - lolbin
aliases:
  - Jsc.exe
  - jsc.exe
  - JScript command-line compiler
url:
  - https://learn.microsoft.com/dotnet/api/microsoft.jscript.cmdlineoptionparser?view=netframework-4.8.1
  - https://learn.microsoft.com/dotnet/api/microsoft.jscript.cmdlineexception?view=netframework-4.8.1
---

**fullpath**:C:\Windows\Microsoft.NET\Framework\v4.0.30319\Jsc.exe

# description

`jsc.exe` is the command-line compiler for JScript (.NET), shipped with the .NET Framework. Its option parsing and errors are implemented in the `Microsoft.JScript` namespace (`Microsoft.JScript.dll`) by `CmdLineOptionParser` and `CmdLineException`, which are infrastructure APIs not intended for direct use.

## simple description

> ### 2026-11-21 Claude said
> Jsc.exe is a legacy compiler included with the .NET Framework that turns JScript.NET source files (.js) into .NET executables or DLLs. It is present on most Windows machines even though very few developers use it today. It works like csc.exe or vbc.exe, but for JScript.
>
> **SOC NOTE**: Jsc.exe is a known LOLBin: attackers can drop a .js source file and compile it on the host to produce a payload, bypassing application allowlisting and avoiding dropping a precompiled binary (MITRE ATT&CK T1127, T1027.004 Compile After Delivery). Any execution outside of development contexts, especially spawned by Office, script hosts or from temp folders, and newly created .exe/.dll files written by jsc.exe, are suspicious.
>

# purpose

Compiles JScript source code from the command line into .NET assemblies. Microsoft Learn documents only the supporting API classes: `CmdLineOptionParser` determines whether options specified to jsc.exe are correctly formed and reads their arguments, and `CmdLineException` represents errors that occur when running jsc.exe.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
