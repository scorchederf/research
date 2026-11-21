---
created: 2026-11-21
fullpath: 'c:\Program Files (x86)\Microsoft Visual Studio\2017\Community\MSBuild\15.0\Bin\Roslyn\csi.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - visual-studio
  - lolbin
aliases:
  - "csi.exe"
  - "C# Interactive"
  - "C# REPL"
url:
  - https://learn.microsoft.com/visualstudio/releases/2015/vs2015-update1-vs
---

**fullpath**: c:\Program Files (x86)\Microsoft Visual Studio\2017\Community\MSBuild\15.0\Bin\Roslyn\csi.exe

# description

csi.exe is the command-line C# Interactive (REPL) and C# script runner from the Roslyn compiler, shipped with Visual Studio (first in Visual Studio 2015 Update 1). It runs C# script files (.csx) or evaluates C# snippets interactively from the Developer Command Prompt. The related in-IDE experience is the C# Interactive Window.

## simple description

> ### 2026-11-21 Claude said
> csi.exe lets developers run C# code as a script without building a project. You can give it a .csx file or start it with no arguments to type C# code line by line. It is installed with Visual Studio and lives in the Roslyn compiler folder. It is normally only used by developers.
>
> **SOC NOTE**: csi.exe is a Microsoft-signed LOLBin that can execute arbitrary C# code from a .csx file or stdin, enabling application-control bypass (T1127 Trusted Developer Utilities Proxy Execution) and is on the WDAC recommended block list. Alert on csi.exe launched by non-developers, from Office/browsers, or with scripts in temp/user-writable folders.
>

# purpose

Runs a C# script file (.csx) from the Developer Command Prompt, or enters a command-line REPL mode to interactively evaluate snippets of C# code when run with no arguments.

# typical use cases

| usage | description |
| --- | --- |
| `csi myScript.csx` | Run a C# script file. |
| `csi` | Enter interactive REPL mode to evaluate C# snippets. |

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
