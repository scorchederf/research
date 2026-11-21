---
created: 2026-11-21
fullpath: 'C:\Program Files\dotnet\sdk\<version>\FSharp\fsi.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - dotnet
  - fsharp
  - scripting
aliases:
  - fsi.exe
  - F# Interactive
  - dotnet fsi
url:
  - https://learn.microsoft.com/dotnet/fsharp/language-reference/fsharp-interactive-options
  - https://learn.microsoft.com/dotnet/fsharp/tools/fsharp-interactive/
---

**fullpath**:C:\Program Files\dotnet\sdk\<version>\FSharp\fsi.exe

# description

F# Interactive (`dotnet fsi`) is the F# REPL and script runner shipped in every .NET SDK; this path is the copy inside a specific SDK version folder. It executes `.fsx` scripts and accepts many F# compiler (fsc.exe) options. Under .NET Framework the equivalent is `FsiAnyCPU.exe` from Visual Studio.

## simple description

> ### 2026-11-21 Claude said
> fsi.exe lets you type F# code and run it immediately, or run F# script files (.fsx) without building a project. It comes with the .NET SDK, so it is found on developer machines and build servers. Normally it is started through `dotnet fsi` rather than directly.
>
> **SOC NOTE**: Signed Microsoft binary that compiles and runs arbitrary code from a script, so it can be abused for proxy execution and AppLocker/WDAC bypass (MITRE T1127 Trusted Developer Utilities Proxy Execution; listed in LOLBAS as fsi.exe/fsianycpu.exe). `.fsx` scripts can pull NuGet packages with `#r "nuget: ..."`. Alert on fsi launched outside developer contexts, from Office/browsers, or with `.fsx` files in temp/download folders, and consider blocking it via WDAC recommended block rules.
>

# purpose

Runs F# code interactively (code terminated with `;;` is compiled and executed) or runs a script: `dotnet fsi [options] [ script-file [arguments] ]`. Scripts can `#load` other scripts and read arguments through `fsi.CommandLineArgs`. Options can also be set in Visual Studio under **Tools > Options > F# Tools > F# Interactive**.

# typical use cases

| usage | description |
| --- | --- |
| `dotnet fsi` | Start an interactive F# session. |
| `dotnet fsi Script.fsx` | Run an F# script. |
| `dotnet fsi Script1.fsx hello world` | Run a script and pass arguments, read via fsi.CommandLineArgs. |
| `#version;;` | Show version information in an F# 11 session. |

# options

| option | description |
| --- | --- |
| `--` | Treat remaining arguments as arguments to the script, accessible via fsi.CommandLineArgs. |
| `--checked[+\|-]` | Same as the fsc.exe compiler option. |
| `--checknulls[+\|-]` | Same as the fsc.exe compiler option. |
| `--codepage:<int>` | Same as the fsc.exe compiler option. |
| `--consolecolors[+\|-]` | Outputs warning and error messages in color. |
| `--compilertool:<extensionsfolder>` | Reference an assembly or directory containing a design time tool (short form `-t`). |
| `--crossoptimize[+\|-]` | Enable or disable cross-module optimizations. |
| `--debug[+\|-]`, `--debug:[full\|pdbonly\|portable\|embedded]`, `-g[+\|-]`, `-g:[...]` | Same as the fsc.exe compiler option. |
| `--define:<string>` | Same as the fsc.exe compiler option. |
| `--deterministic[+\|-]` | Produces a deterministic assembly (including module version GUID and timestamp). |
| `--exec` | Exit after loading the files or running the script given on the command line. |
| `--fullpaths` | Same as the fsc.exe compiler option. |
| `--gui[+\|-]` | Enable or disable the Windows Forms event loop; enabled by default. |
| `--help`, `-?` | Display command-line syntax and option descriptions. |
| `--lib:<folder-list>`, `-I:<folder-list>` | Same as the fsc.exe compiler option. |
| `--load:<filename>` | Compile the given source at startup and load it into the session. |
| `--mlcompatibility` | Same as the fsc.exe compiler option. |
| `--noframework` | Same as the fsc.exe compiler option. |
| `--nologo` | Same as the fsc.exe compiler option. |
| `--nowarn:<warning-list>` | Same as the fsc.exe compiler option. |
| `--optimize[+\|-]` | Same as the fsc.exe compiler option. |
| `--preferreduilang:<lang>` | Preferred output language culture name (for example es-ES). |
| `--quiet` | Suppress output to stdout. |
| `--quotations-debug` | Emit extra debugging information for quotation literals and reflected definitions. |
| `--readline[+\|-]` | Enable or disable tab completion in interactive mode. |
| `--reference:<filename>`, `-r:<filename>` | Same as the fsc.exe compiler option. |
| `--tailcalls[+\|-]` | Enable or disable the tail IL instruction; enabled by default. |
| `--targetprofile:<string>` | Target framework profile: mscorlib, netcore or netstandard (default mscorlib). |
| `--use:<filename>` | Use the given file on startup as initial input. |
| `--utf8output` | Same as the fsc.exe compiler option. |
| `--warn:<warning-level>` | Same as the fsc.exe compiler option. |
| `--warnaserror[+\|-]` | Same as the fsc.exe compiler option. |
| `--warnaserror[+\|-]:<int-list>` | Same as the fsc.exe compiler option. |
