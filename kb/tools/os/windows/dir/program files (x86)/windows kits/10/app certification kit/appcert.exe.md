---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Windows Kits\10\App Certification Kit\appcert.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - windows-sdk
  - app-certification
aliases:
  - appcert.exe
  - Windows App Certification Kit
url:
  - https://learn.microsoft.com/windows/uwp/debug-test-perf/windows-app-certification-kit
  - https://learn.microsoft.com/windows/uwp/debug-test-perf/windows-app-certification-kit-tests
---

**fullpath**:C:\Program Files (x86)\Windows Kits\10\App Certification Kit\appcert.exe

# description

Command-line front end of the Windows App Certification Kit (WACK), included in the Windows SDK, used to validate Windows apps locally before Windows certification or Microsoft Store submission. The default install path is `C:\Program Files (x86)\Windows Kits\10\App Certification Kit\`.

## simple description

> ### 2026-11-21 Claude said
> appcert.exe runs the Windows App Certification Kit tests against an installed app or an app package and writes a report. Developers use it to check apps for crashes, security features and Store policy compliance before publishing. It must run elevated in an active user session. It is a developer tool and is rarely present on regular end-user machines.
>
> **SOC NOTE**: Uncommon outside developer/build systems; execution on a normal workstation is unusual. It installs and launches the tested app packages, so it could be used to sideload and run an arbitrary package. Its kit tests also flag private signing keys (`.pfx`, `.snk`) included in packages.
>

# purpose

Tests a Windows app (installed or packaged) and produces a certification report. Run `appcert.exe reset` before each test.

# typical use cases

| usage | description |
| --- | --- |
| `appcert.exe reset` | Reset the kit state before a test run. |
| `appcert.exe test -packagefullname [package full name] -reportoutputpath [report file name]` | Test an app that is already installed and write the report. |
| `appcert.exe test -appxpackagepath [package path] -reportoutputpath [report file name]` | Test an app package that is not installed; the kit opens the package and applies the right workflow. |
| `appcert.exe /?` | Show command-line help. |

# options

| option | description |
| --- | --- |
| `reset` | Resets the kit before testing. |
| `test` | Runs the certification tests. |
| `-packagefullname` | Full name of an installed package to test. |
| `-appxpackagepath` | Path to an app package that is not installed. |
| `-reportoutputpath` | File name of the test report. |
| `/?` | Displays more information about the command line. |
