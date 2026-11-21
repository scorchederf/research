---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework\v4.0.30319\vbc.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
  - compiler
aliases:
  - vbc.exe
  - Visual Basic command-line compiler
url:
  - https://learn.microsoft.com/dotnet/visual-basic/reference/command-line-compiler/compiler-options-listed-alphabetically
  - https://learn.microsoft.com/dotnet/visual-basic/reference/command-line-compiler/sample-compilation-command-lines
  - https://learn.microsoft.com/dotnet/visual-basic/reference/command-line-compiler/specify-response-file
  - https://learn.microsoft.com/visualstudio/msbuild/vbc-task
---

**fullpath**:C:\Windows\Microsoft.NET\Framework\v4.0.30319\vbc.exe

# description

vbc.exe is the Visual Basic command-line compiler, an alternative to compiling from the Visual Studio IDE that produces executables (.exe), dynamic-link libraries (.dll) or code modules (.netmodule). This copy ships with .NET Framework 4.x; the MSBuild Vbc task wraps vbc.exe, and the default response file Vbc.rsp sits in the same directory.

## simple description

> ### 2026-11-21 Claude said
> vbc.exe compiles Visual Basic .NET source code into programs or libraries. It is installed with the .NET Framework on every modern Windows machine, so it is present even without Visual Studio. Developers rarely call it directly; MSBuild usually does.
>
> **SOC NOTE**: Attackers abuse framework compilers like vbc.exe and csc.exe to compile payloads on the target (MITRE ATT&CK T1027.004 Compile After Delivery, T1127 Trusted Developer Utilities). Alert on vbc.exe launched by Office, script hosts, browsers or w3wp.exe, on compiling files from Temp/AppData, and on new .exe/.dll output in user-writable paths shortly after compilation.
>

# purpose

Compile Visual Basic source files into .exe, .dll or .netmodule outputs from the command line.

# typical use cases

| usage | description |
| --- | --- |
| `vbc -reference:Microsoft.VisualBasic.dll File.vb` | Compile File.vb and create File.exe. |
| `vbc -target:library File.vb` | Compile File.vb and create File.dll. |
| `vbc -out:My.exe File.vb` | Compile File.vb and create My.exe. |
| `vbc -target:library -ref:.\debug\bin\ref\file.dll File.vb` | Create both a library and a reference assembly named File.dll. |
| `vbc -define:DEBUG=1 -optimize -out:File2.exe *.vb` | Compile all .vb files with optimizations and DEBUG defined, producing File2.exe. |
| `vbc -target:library -out:File2.dll -nowarn -nologo -debug *.vb` | Produce a debug File2.dll without logo or warnings. |
| `vbc @file1.rsp` | Compile using options from a response file. |

# options

| option | description |
| --- | --- |
| `@` | Specifies a response file. |
| `-?` | Displays compiler options, same as `-help`; no compilation occurs. |
| `-additionalfile` | Names additional files used by analyzers that don't directly affect code generation. |
| `-addmodule` | Makes all type information from the specified file(s) available to the project. |
| `-analyzer` | Runs the analyzers from this assembly (short form `-a`). |
| `-baseaddress` | Specifies the base address of a DLL. |
| `-bugreport` | Creates a file with information for reporting a bug. |
| `-checksumalgorithm:<alg>` | Algorithm for the source file checksum stored in the PDB: SHA1 (default) or SHA256. |
| `-codepage` | Code page for all source files. |
| `-debug` | Produces debugging information. |
| `-define` | Defines symbols for conditional compilation. |
| `-delaysign` | Whether the assembly is fully or partially signed. |
| `-deterministic` | Outputs an assembly whose binary content is identical across compilations with identical inputs. |
| `-doc` | Processes documentation comments to an XML file. |
| `-errorreport` | How internal compiler errors are reported. |
| `-filealign` | Where to align sections of the output file. |
| `-help` | Displays compiler options, same as `-?`. |
| `-highentropyva` | Whether the executable supports high entropy ASLR. |
| `-imports` | Imports a namespace from a specified assembly. |
| `-keycontainer` | Key container name for strong-naming. |
| `-keyfile` | File containing a key or key pair for strong-naming. |
| `-langversion` | Language version: 9, 9.0, 10, 10.0, 11, 11.0. |
| `-libpath` | Location of assemblies referenced by `-reference`. |
| `-linkresource` | Creates a link to a managed resource. |
| `-main` | Class containing the `Sub Main` startup procedure. |
| `-moduleassemblyname` | Assembly a module will be part of. |
| `-modulename:<string>` | Name of the source module. |
| `-netcf` | Targets the .NET Compact Framework. |
| `-noconfig` | Do not compile with Vbc.rsp. |
| `-nologo` | Suppresses compiler banner. |
| `-nostdlib` | Doesn't reference the standard libraries. |
| `-nowarn` | Suppresses warnings. |
| `-nowin32manifest` | Doesn't embed an application manifest. |
| `-optimize` | Enables/disables optimization. |
| `-optioncompare` | Binary or text string comparisons. |
| `-optionexplicit` | Enforces explicit variable declaration. |
| `-optioninfer` | Enables local type inference. |
| `-optionstrict` | Enforces strict language semantics. |
| `-out` | Specifies the output file. |
| `-parallel[+\|-]` | Whether to use concurrent build. |
| `-pathmap` | Maps physical paths to source path names output by the compiler. |
| `-platform` | Target processor platform. |
| `-preferreduilang` | Preferred output language name. |
| `-quiet` | Doesn't display code for syntax errors and warnings. |
| `-recurse` | Searches subdirectories for source files. |
| `-reference` | Imports metadata from an assembly. |
| `-refonly` | Outputs only a reference assembly. |
| `-refout` | Output path of a reference assembly. |
| `-removeintchecks` | Disables integer overflow checking. |
| `-resource` | Embeds a managed resource. |
| `-rootnamespace` | Namespace for all type declarations. |
| `-ruleset:<file>` | Ruleset file that disables specific diagnostics. |
| `-sdkpath` | Location of Mscorlib.dll and Microsoft.VisualBasic.dll. |
| `-subsystemversion` | Minimum subsystem version for the executable. |
| `-target` | Format of the output file. |
| `-utf8output` | Displays compiler output in UTF-8. |
| `-vbruntime` | Compile without, or with a specific, Visual Basic Runtime reference. |
| `-verbose` | Outputs extra information during compilation. |
| `-warnaserror` | Promotes warnings to errors. |
| `-win32icon` | Inserts an .ico file into the output. |
| `-win32manifest` | User-defined Win32 manifest to embed. |
| `-win32resource` | Inserts a Win32 resource into the output. |
