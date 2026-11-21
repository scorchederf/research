---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework\v4.0.30319\Csc.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
  - compiler
  - lolbin
aliases:
  - "csc.exe"
  - "C# compiler"
  - "Visual C# compiler"
url:
  - https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/
  - https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/language
  - https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/output
  - https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/inputs
  - https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/errors-warnings
  - https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/code-generation
  - https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/security
  - https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/resources
  - https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/miscellaneous
  - https://learn.microsoft.com/dotnet/csharp/language-reference/compiler-options/advanced
---

**fullpath**: C:\Windows\Microsoft.NET\Framework\v4.0.30319\Csc.exe

# description

`csc.exe` is the C# compiler shipped with the .NET Framework, located in `Microsoft.NET\Framework\<Version>` under the Windows directory (here v4.0.30319). .NET Framework projects build with csc.exe, while modern .NET uses `dotnet build`/MSBuild properties; the MSBuild `Csc` task wraps it. Multiple copies exist when several .NET Framework versions are installed.

## simple description

> ### 2026-11-21 Claude said
> Csc.exe is the command-line C# compiler that comes built into every Windows machine with .NET Framework 4.x. It turns C# source files (.cs) into executables or DLLs. Developers rarely call it directly today, but build tools and some applications (for example ASP.NET or PowerShell Add-Type) invoke it in the background. Seeing it run is normal on developer and web servers but unusual on ordinary workstations.
>
> **SOC NOTE**: Attackers use csc.exe to compile payloads on the target to evade signature detection (T1027.004 Obfuscated Files or Information: Compile After Delivery, T1127 Trusted Developer Utilities Proxy Execution). Look for csc.exe spawned by Office, scripting hosts, PowerShell or w3wp.exe, compiling files from %TEMP%/user folders, and the cvtres.exe child it creates. Newly written .exe/.dll files in temp folders right after csc.exe runs are strong indicators; PowerShell Add-Type also triggers csc.exe and leaves .cs/.cmdline files in %TEMP%.
>

# purpose

Compiles C# source code into assemblies (.exe, .dll, .netmodule). Every option is available as `-option` or `/option`; arguments follow a colon (for example `-doc:DocFile.xml`). The `csc.rsp` response file in the same directory is included automatically unless `-noconfig` is used.

# typical use cases

| usage | description |
| --- | --- |
| `csc.exe -target:exe -out:MyExe.exe source1.cs source2.cs` | Compile source files into a console executable. |
| `csc.exe -target:library -out:MyLib.dll file.cs` | Build a class library DLL. |
| `csc.exe -doc:DocFile.xml file.cs` | Generate XML documentation from `///` comments. |
| `csc.exe @CustomOpts.RSP` | Read options and source files from a response file. |
| `csc.exe -nologo -optimize -out:app.exe app.cs` | Optimized build without the banner. |

# options

| option    | description    |
| --- | --- |
| `-checked` | Generate overflow checks; default context becomes checked. |
| `-unsafe` | Allow code that uses the `unsafe` keyword. |
| `-define` | Define conditional compilation symbols for all source files. |
| `-langversion` | Specify the accepted C# language version (for example `default`, `latest`, `7.3`, `ISO-1`). |
| `-nullable` | Set the nullable context: `enable`, `disable`, `warnings` or `annotations`. |
| `-doc:` | Generate an XML documentation file from `///` comments. |
| `-out:` | Specify the output assembly file. |
| `-platform:` | Specify the target platform CPU. |
| `-refout:` | Generate a reference assembly. |
| `-target:` | Specify the type of output assembly (exe, winexe, library, module). |
| `-reference / -references` | Reference metadata from the specified assembly file(s). |
| `-addmodule` | Add a module (created with `-target:module`) to this assembly. |
| `-link` | Embed metadata from the specified interop assembly files. |
| `-warn` | Set the warning level. |
| `-warnaserror` | Treat all warnings as errors. |
| `-warnaserror+` | Treat one or more specified warnings as errors. |
| `-warnaserror-` | Treat one or more specified warnings not as errors. |
| `-nowarn` | Disable a list of warnings. |
| `-ruleset` | Specify a ruleset file that disables specific diagnostics. |
| `-errorlog` | Log all compiler and analyzer diagnostics to a file. |
| `-reportanalyzer` | Report extra analyzer information such as execution time. |
| `-debug` | Emit (or do not emit) debugging information. |
| `-optimize` | Enable optimizations. |
| `-deterministic` | Produce byte-for-byte identical output from identical inputs. |
| `-refonly` | Produce a reference assembly instead of a full assembly as the primary output. |
| `-publicsign` | Publicly sign the assembly (applies the public key without signing); requires -keyfile or -keycontainer. |
| `-delaysign` | Delay-sign the assembly using only the public portion of the strong name key. |
| `-keyfile` | Specify a strong name key file used to sign the assembly. |
| `-keycontainer` | Specify a strong name key container. |
| `-highentropyva` | Enable high-entropy ASLR. |
| `-win32res` | Insert a Win32 resource file (.res) into the output. |
| `-win32icon` | Insert an .ico file into the output. |
| `-win32manifest` | Specify a Win32 manifest file (.xml). |
| `-nowin32manifest` | Do not include the default Win32 manifest. |
| `-resource` | Embed the specified resource (short form `/res`). |
| `-linkresource` | Link the specified resource to this assembly. |
| `@file.rsp` | Read the specified response file for more options and source files. |
| `-nologo` | Suppress the compiler copyright banner. |
| `-noconfig` | Do not auto-include the `csc.rsp` file. |
| `-main` | Specify the type that contains the entry point. |
| `-pdb` | Specify the debug information file name. |
| `-pathmap` | Map source path names output by the compiler. |
| `-appconfig` | Specify an application configuration file with assembly binding settings. |
| `-lib` | Specify additional directories to search for references. |
| `-fullpath` | Generate fully qualified paths. |
| `-preferreduilang` | Specify the preferred output language name. |
| `-baseaddress` | Specify the base address for the library to be built. |
| `-checksumalgorithm` | Specify the algorithm for the source file checksum stored in the PDB (SHA1 or SHA256). |
| `-codepage` | Specify the code page used when opening source files. |
| `-utf8output` | Output compiler messages in UTF-8. |
| `-filealign` | Specify the alignment used for output file sections. |
| `-errorendlocation` | Output line and column of the end location of each error. |
| `-nostdlib` | Do not reference the standard library (mscorlib.dll). |
| `-subsystemversion` | Specify the subsystem version of the assembly. |
| `-moduleassemblyname` | Name of the assembly this module will be part of. |
| `-reportivts` | Produce additional information on InternalsVisibleToAttribute. |
