---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TestWindow\vstest.console.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - visual-studio
  - testing
aliases:
  - vstest.console.exe
  - VSTest.Console.exe
url:
  - https://learn.microsoft.com/visualstudio/test/vstest-console-options
---

**fullpath**:C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TestWindow\vstest.console.exe

# description

VSTest.Console.exe is the Visual Studio command-line tool to run tests, located under the edition's Common7\IDE\CommonExtensions folder and available from the Developer Command Prompt. It is required to run automated tests on ARM-based machines, and the MSTest adapter can also run in legacy mstest.exe mode; `dotnet vstest`/`dotnet test` are related tools.

## simple description

> ### 2026-11-21 Claude said
> vstest.console.exe is the test runner that ships with Visual Studio. Given one or more test DLLs it discovers and runs unit tests (MSTest, xUnit, NUnit through adapters) and reports results, for example to a .trx file. Build servers and developers use it to run tests outside the IDE. This copy belongs to Visual Studio 2022 Community.
>
> **SOC NOTE**: Microsoft-signed binary that loads and executes arbitrary code from any "test" DLL and can load custom adapters via /TestAdapterPath, so it can be abused as a proxy execution LOLBin (MITRE ATT&CK T1218/T1127 Trusted Developer Utilities). Suspicious on non-developer machines, when run against DLLs in Temp/Downloads/user profiles, or when spawned by Office/script hosts; it spawns testhost.exe child processes.
>

# purpose

Runs tests from specified test files with options for filtering (/Tests, /TestCaseFilter), parallel or isolated execution, platform and framework selection, loggers (trx, console), data collectors, blame mode crash/hang diagnostics and diagnostic logs. It returns exit code 0 on success and 1 on failure.

# typical use cases

| usage | description |
| --- | --- |
| `vstest.console.exe myTestProject.dll` | Runs tests in the test library. |
| `vstest.console.exe myTestFile.dll myOtherTestFile.dll` | Runs tests from multiple files. |
| `vstest.console.exe myTestFile.dll /Settings:Local.RunSettings /InIsolation /TestCaseFilter:"Priority=1" /Logger:trx` | Runs Priority=1 tests in an isolated process with a runsettings file and logs to a .trx file. |
| `vstest.console.exe myTestFile.dll /blame` | Runs in blame mode, generating sequence.xml if the test host crashes. |
| `vstest.console.exe myTestFile.dll /logger:"console;verbosity=detailed"` | Uses the console logger with detailed verbosity. |
| `vstest.console.exe /Logger:trx /Platform:x64 /framework:frameworkuap10 UnitTestsUWP\bin\x64\Release\UnitTestsUWP.build.appxrecipe` | Runs UWP tests from an appxrecipe file. |

# options

| option | description |
| --- | --- |
| `[test file names]` | Run tests from the specified files, separated by spaces. |
| `/Settings:[file name]` | Run tests with additional settings such as data collectors (.runsettings). |
| `/Tests:[test name]` | Run tests whose full names contain the values (comma-separated); can't be combined with /TestCaseFilter. |
| `/Parallel` | Execute tests in parallel, using up to all available cores by default. |
| `/InIsolation` | Run tests in an isolated process. |
| `/TestAdapterPath:[path]` | Use custom test adapters from the specified path. |
| `/Platform:[platform type]` | Force the platform architecture (x86, x64, ARM, ARM64, S390x, Ppc64le, RiscV64, LoongArch64). |
| `/Framework:[framework version]` | Target .NET version for execution (e.g. net8.0, Framework40, FrameworkUap10). |
| `/TestCaseFilter:[expression]` | Run tests matching the expression; can't be combined with /Tests. |
| `/Environment:[NAME]=[VALUE]` | Set an environment variable for the test host; implies /InIsolation. Short form /e. |
| `/?` | Display usage information. |
| `/Logger:[uri/friendlyname]` | Specify a logger for test results (e.g. trx with LogFileName or LogFilePrefix); repeatable. |
| `/ListTests:[file name]` | List discovered tests from the test container. Short form /lt. |
| `/Blame` | Run in blame mode to isolate tests crashing the test host; can collect crash or hang dumps. |
| `/Diag:[file name]` | Write diagnostic trace logs to the file, with optional tracelevel. |
| `/ResultsDirectory:[path]` | Directory for test results, created if missing. |
| `/ParentProcessId:[parentProcessId]` | Process ID of the parent process that launched this process. |
| `/Port:[port]` | Port for socket connection and receiving event messages. |
| `/Collect:[dataCollector friendlyName]` | Enable a data collector for the test run. |
| `@[file]` | Read additional options from a response file. |
