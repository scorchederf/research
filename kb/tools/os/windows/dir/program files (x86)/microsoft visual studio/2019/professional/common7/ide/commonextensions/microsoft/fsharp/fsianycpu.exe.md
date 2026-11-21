---
created: 2026-11-21
fullpath: 'c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\FSharp\fsianycpu.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - visual-studio
  - fsharp
aliases:
  - fsianycpu.exe
  - FsiAnyCPU.exe
  - F# Interactive
url:
  - https://learn.microsoft.com/dotnet/fsharp/tools/fsharp-interactive/
  - https://learn.microsoft.com/dotnet/fsharp/language-reference/fsharp-interactive-options
---

**fullpath**:c:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\FSharp\fsianycpu.exe

# description

fsianycpu.exe is the .NET Framework build of F# Interactive (FSI), a REPL that runs F# code interactively or executes F# scripts (.fsx). It ships with Visual Studio or the Visual Studio Build Tools; unlike the dedicated fsi.exe it uses the machine architecture to decide whether to run as a 32-bit or 64-bit process. The .NET SDK equivalent is `dotnet fsi`.

## simple description

> ### 2026-11-21 Claude said
> fsianycpu.exe runs F# code and F# script files (.fsx) directly, without compiling a program first. It is installed with Visual Studio's F# tools. Developers use it to test code quickly.
>
> **SOC NOTE**: As a Microsoft-signed script host, fsianycpu.exe/fsi.exe can run arbitrary .fsx code, including .NET API calls, so it is listed as a LOLBin for proxy execution and AppLocker/WDAC bypass (MITRE ATT&CK T1127 Trusted Developer Utilities Proxy Execution). Investigate executions on non-developer machines or running .fsx files from temp/download folders.
>

# purpose

Run F# Interactive under the .NET Framework runtime: invoke `FsiAnyCPU.exe` from a Developer Command Prompt or put it on `PATH` instead of `dotnet fsi`. In Visual Studio, the 64-bit F# Interactive setting (Tools > Options > F# Tools) chooses between fsi.exe and fsianycpu.exe.

# typical use cases

| usage | description |
| --- | --- |
| `fsianycpu.exe` | Start an interactive F# REPL session; terminate input with `;;`. |
| `fsianycpu.exe Script.fsx` | Execute an F# script file (same syntax as `dotnet fsi [options] [script-file [arguments]]`). |
| `fsianycpu.exe --exec --quiet Script.fsx` | Run a script and exit, suppressing FSI's own output. |

# options

| option | description |
| --- | --- |
| `--` | Treat remaining arguments as arguments to the F# program or script (`fsi.CommandLineArgs`). |
| `--checked[+\|-]` | Same as the fsc.exe compiler option. |
| `--checknulls[+\|-]` | Same as the fsc.exe compiler option. |
| `--codepage:<int>` | Same as the fsc.exe compiler option. |
| `--consolecolors[+\|-]` | Outputs warning and error messages in color. |
| `--compilertool:<extensionsfolder>` | Reference an assembly or directory containing a design time tool (short form `-t`). |
| `--crossoptimize[+\|-]` | Enable or disable cross-module optimizations. |
| `--debug[+\|-]`, `--debug:[full\|pdbonly\|portable\|embedded]`, `-g` | Same as the fsc.exe compiler option. |
| `--define:<string>` | Same as the fsc.exe compiler option. |
| `--deterministic[+\|-]` | Produces a deterministic assembly. |
| `--exec` | Exit after loading the files or running the script file given on the command line. |
| `--fullpaths` | Same as the fsc.exe compiler option. |
| `--gui[+\|-]` | Enables or disables the Windows Forms event loop (default enabled). |
| `--help`, `-?` | Display command-line syntax and option descriptions. |
| `--lib:<folder-list>`, `-I:<folder-list>` | Same as the fsc.exe compiler option. |
| `--load:<filename>` | Compiles the given source at startup and loads it into the session. |
| `--mlcompatibility` | Same as the fsc.exe compiler option. |
| `--noframework` | Same as the fsc.exe compiler option. |
| `--nologo` | Same as the fsc.exe compiler option. |
| `--nowarn:<warning-list>` | Same as the fsc.exe compiler option. |
| `--optimize[+\|-]` | Same as the fsc.exe compiler option. |
| `--preferreduilang:<lang>` | Preferred output language culture name. |
| `--quiet` | Suppress F# Interactive's output to stdout. |
| `--quotations-debug` | Emit extra debugging information for quotation-derived expressions. |
| `--readline[+\|-]` | Enable or disable tab completion in interactive mode. |
| `--reference:<filename>`, `-r:<filename>` | Same as the fsc.exe compiler option. |
| `--tailcalls[+\|-]` | Enable or disable the tail IL instruction (enabled by default). |
| `--targetprofile:<string>` | Target framework profile: mscorlib (default), netcore or netstandard. |
| `--use:<filename>` | Use the given file on startup as initial input. |
| `--utf8output` | Same as the fsc.exe compiler option. |
| `--warn:<warning-level>` | Same as the fsc.exe compiler option. |
| `--warnaserror[+\|-]` | Same as the fsc.exe compiler option. |
| `--warnaserror[+\|-]:<int-list>` | Same as the fsc.exe compiler option. |
