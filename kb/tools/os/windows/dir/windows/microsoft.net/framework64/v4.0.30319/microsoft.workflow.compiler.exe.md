---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.Net\Framework64\v4.0.30319\Microsoft.Workflow.Compiler.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
  - workflow
  - lolbin
  - appcontrol-bypass
aliases:
  - 'Microsoft.Workflow.Compiler.exe'
  - 'Windows Workflow Foundation 3 compiler'
url:
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/design/applications-that-can-bypass-appcontrol
  - https://learn.microsoft.com/dotnet/framework/windows-workflow-foundation/deprecated-types
---

**fullpath**:C:\Windows\Microsoft.Net\Framework64\v4.0.30319\Microsoft.Workflow.Compiler.exe

# description

`Microsoft.Workflow.Compiler.exe` is a .NET Framework 4 tool belonging to the deprecated Windows Workflow Foundation 3 (WF 3, `System.Workflow.*`) stack, alongside `wfc.exe` and `Microsoft.Workflow.DebugController.dll`. It is listed by Microsoft among applications that can bypass App Control.

## simple description

> ### 2026-11-21 Claude said
> This is a leftover compiler for the old Windows Workflow Foundation 3 technology that ships with .NET Framework 4. It takes a settings XML file and source files and compiles/loads workflow code. Almost no modern software uses it, but it is still present on most Windows systems and is signed by Microsoft.
>
> **SOC NOTE**: Known LOLBin: `Microsoft.Workflow.Compiler.exe <options.xml> <results.xml>` can compile and execute attacker-supplied C#/VB code, bypassing application allow-listing (T1127 Trusted Developer Utilities Proxy Execution). Microsoft recommends blocking it in App Control policies. Any execution on a non-developer endpoint, especially with XML files in temp/user folders, should be investigated; look for csc.exe/cvtres.exe children.
>

# purpose

Microsoft recommends blocking Microsoft.Workflow.Compiler.exe unless explicitly required, because an attacker could use it to circumvent application allow policies including App Control. It is part of the WF 3 assemblies and tools marked obsolete starting with .NET Framework 4.5; existing WF 3 applications continue to run and are supported under the Microsoft Support Lifecycle Policy.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
