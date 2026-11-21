---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\IntelliTrace\IntelliTrace.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - visual-studio
  - debugging
aliases:
  - IntelliTrace.exe
  - IntelliTrace
url:
  - https://learn.microsoft.com/visualstudio/debugger/using-the-intellitrace-stand-alone-collector?view=visualstudio
---

**fullpath**:C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\IntelliTrace\IntelliTrace.exe

# description

IntelliTrace.exe lives in the Visual Studio IntelliTrace folder (`Common7\IDE\CommonExtensions\Microsoft\IntelliTrace`), the same folder Microsoft Learn names as the source of IntelliTraceCollection.cab for the IntelliTrace stand-alone collector (IntelliTraceSC.exe). Learn does not document IntelliTrace.exe itself. IntelliTrace data (.iTrace files) can only be opened in Visual Studio Enterprise.

## simple description

> ### 2026-11-21 Claude said
> IntelliTrace.exe is the Visual Studio IntelliTrace recorder process that captures historical debugging data (events, exceptions, and optionally method calls) from .NET applications into .iTrace files. Visual Studio launches it in the background when IntelliTrace is enabled during a debugging session. IntelliTrace recording is an Enterprise feature, though the binary ships with other editions.
>
> **SOC NOTE**: As a Microsoft-signed tool that can launch and attach to processes and record method parameters and return values, it can collect sensitive data (Learn warns .iTrace files may contain connection strings and user data) and could be abused as a LOLBin for process launch or data collection (T1005, T1218). Look for IntelliTrace.exe run outside a Visual Studio parent (devenv.exe) or writing .iTrace files to unusual locations.
>
> _Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
