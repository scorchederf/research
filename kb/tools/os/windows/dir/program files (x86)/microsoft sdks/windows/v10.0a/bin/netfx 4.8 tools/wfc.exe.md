---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.8 Tools\wfc.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - dotnet
  - sdk
  - lolbin
aliases:
  - wfc.exe
  - Workflow Command-line Compiler Tool
  - Windows Workflow Compiler
url:
  - https://learn.microsoft.com/dotnet/framework/windows-workflow-foundation/wfc-exe-workflow-compiler-tool
  - https://learn.microsoft.com/dotnet/api/system.workflow.componentmodel.compiler.workflowcompiler?view=netframework-4.8.1
---

**fullpath**:C:\Program Files (x86)\Microsoft SDKs\Windows\v10.0A\bin\NETFX 4.8 Tools\wfc.exe

# description

wfc.exe is the Windows Workflow Foundation command-line compiler for old (obsolete) `.xoml` workflow markup files. It ships with the Windows SDK .NET Framework tools and wraps the deprecated `System.Workflow.ComponentModel.Compiler.WorkflowCompiler` class.

## simple description

> ### 2026-11-21 Claude said
> wfc.exe compiles old-style Windows Workflow files (.xoml plus C# or VB code) into a .NET assembly. It is a developer tool from the Windows SDK and is rarely used today because those workflow types are deprecated. It is not part of a normal Windows install, only of SDK / Visual Studio installs.
>
> **SOC NOTE**: A related binary, `Microsoft.Workflow.Compiler.exe`, is a known LOLBin (MITRE T1127 Trusted Developer Utilities Proxy Execution) that compiles and runs attacker C#/XOML code. wfc.exe uses the same compiler classes, so execution with `/t:exe` or with code-beside files outside build contexts is suspicious. Look for wfc.exe launched by Office, scripts or from user temp folders, and for newly created assemblies afterwards.
>

# purpose

Compiles workflow markup: validates activities, generates a partial class from the markup, generates runtime helper code, and passes the partial classes to the C# or Visual Basic compiler to produce a .NET assembly. A list of authorized types is defined in `wfc.exe.config`; with `/checktypes` a workflow that references types not in the list is rejected.

# typical use cases

| usage | description |
| --- | --- |
| `wfc.exe <Xoml file list> /target:assembly [<vb/cs file list>]` | Build a workflow assembly from xoml and code-beside files. |
| `wfc.exe workflow.xoml /t:exe /out:app.exe` | Build a Windows Workflow application. |
| `wfc.exe workflow.xoml /checktypes+` | Compile and enforce the authorized type list from wfc.exe.config. |

# options

| option | description |
| --- | --- |
| `/out:<file>` | Output file name. |
| `/target:assembly` | Build a Windows Workflow assembly (default). Short form `/t:assembly`. |
| `/target:exe` | Build a Windows Workflow application. Short form `/t:exe`. |
| `/delaysign[+\|-]` | Delay-sign the assembly using only the public portion of the strong name key. |
| `/keyfile:<file>` | Specifies a strong name key file. |
| `/keycontainer:<string>` | Specifies a strong name key container. |
| `<Xoml file list>` | Xoml source file name(s). |
| `<vb/cs file list>` | Code-beside file name(s). |
| `/reference:<file list>` | Reference metadata from the specified assembly file(s). Short form `/r:`. |
| `/library:<path list>` | Directories in which to look up references. Short form `/lib:`. |
| `/resource:<resinfo>` | Embed the specified resource (`<file>[,<name>[,public\|private]]`). Short form `/res:`. |
| `/debug[+\|-]` | Emit full debugging information. Default `+`. |
| `/nocode[+\|-]` | Disallow code-beside model. Default `-`. Short form `/nc:`. |
| `/checktypes[+\|-]` | Check for permitted types in wfc.exe.config. Default `-`. Short form `/ct:`. |
| `/language:[cs\|vb]` | Language for the generated class. Default CS. Short form `/l:`. |
| `/rootnamespace:<string>` | Root namespace for all type declarations; VB only. Short form `/rns:`. |
| `/help` | Display usage. Short form `/?`. |
| `/nologo` | Suppress copyright message. Short form `/n`. |
| `/nowarn` | Ignore compiler warnings. Short form `/w`. |
