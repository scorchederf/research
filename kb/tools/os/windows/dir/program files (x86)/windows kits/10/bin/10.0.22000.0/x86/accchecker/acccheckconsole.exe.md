---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x86\AccChecker\AccCheckConsole.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - sdk
  - accessibility
  - exe
aliases:
  - "AccCheckConsole.exe"
  - "AccChecker Console"
  - "UI Accessibility Checker"
url:
  - https://learn.microsoft.com/windows/win32/winauto/the-accchecker-console
  - https://learn.microsoft.com/windows/win32/winauto/ui-accessibility-checker
---

**fullpath**:C:\Program Files (x86)\Windows Kits\10\bin\10.0.22000.0\x86\AccChecker\AccCheckConsole.exe

# description

AccChecker Console is the command-line version of UI Accessibility Checker (AccChecker), which verifies MSAA/UI Automation accessibility implementation of application UI. It is installed with the Windows SDK in \bin\<version>\<platform>\AccChecker and requires .NET Framework 2.0 or later. AccChecker is a legacy tool; Microsoft recommends Accessibility Insights instead.

## simple description

> ### 2026-11-21 Claude said
> AccCheckConsole.exe is a Windows SDK developer tool that tests whether an application's windows are accessible (screen-reader names, keyboard tabbing, events). It targets a window by handle, title or process name and returns an exit code reflecting errors and warnings.
>
> **SOC NOTE**: Low abuse risk. It can load custom verification routine DLLs passed on the command line, which could be used to proxy-load arbitrary .NET code (T1218-style); unexpected execution on non-developer machines merits review.
>

# purpose

Verifies the accessibility implementation of an application's UI from the command line, supplying an exit code: 0 no errors/warnings, 1 usage requested, 2 errors only, 3 errors and warnings, 4 warnings only, 5 invalid command line.

# typical use cases

| usage | description |
| --- | --- |
| `AccCheckConsole -window "Untitled - Notepad"` | Run all verifications on the window with the given title. |
| `AccCheckConsole -hwnd 0x00382f00 -enable CheckTabbing -enable CheckName -suppress suppress.xml` | Run a subset of verifications against an HWND using a suppression file. |
| `AccCheckConsole -window "Untitled - Notepad" VerificationRoutine1.dll` | Run all verifications from a new verification DLL. |

# options

| option | description |
| --- | --- |
| `-hwnd <hwnd>` | Validates the window with the specified handle (hex or decimal). |
| `-window <title>` | Validates the window with the specified title. |
| `-process <name>` | Validates the main window of the process with the specified name. |
| `-list` | Lists all available verification routines. |
| `-enable <name>` | Runs the specified verification routine; can be repeated. |
| `-disable <name>` | Runs all but the specified verification routine; can be repeated. |
| `-log (info \| warn \| err)` | Lowest event rating that will be logged. |
| `-logfile <file>` | Writes output to the specified log file; can be repeated. |
| `-suppress <file>` | Uses the specified XML file to suppress errors. |
| `-quiet` | Does not write logging output to stdout. |
| `-help` | Displays quick help. |
