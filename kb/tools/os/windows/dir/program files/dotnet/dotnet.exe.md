---
created: 2026-11-21
fullpath: 'C:\Program Files\dotnet\dotnet.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
  - developer
aliases:
  - dotnet.exe
  - dotnet
  - .NET CLI
url:
  - https://learn.microsoft.com/dotnet/core/tools/dotnet
  - https://learn.microsoft.com/dotnet/core/tools/
---

**fullpath**:C:\Program Files\dotnet\dotnet.exe

# description

`dotnet` is the generic driver for the .NET CLI. It runs framework-dependent .NET applications and, when the SDK is installed, executes CLI commands such as `build`, `run`, `publish` and `tool install`. Installed with the .NET runtime/SDK under `C:\Program Files\dotnet`.

## simple description

> ### 2026-11-21 Claude said
> dotnet.exe is the host program for modern .NET (Core, 5+). It can run a compiled .NET app (`dotnet myapp.dll`) or, with the SDK installed, act as the developer CLI to create, build, test and publish projects. It also installs and runs .NET tools from NuGet. It is signed by Microsoft and common on developer and server machines.
>
> **SOC NOTE**: Can proxy-execute arbitrary .NET DLLs (`dotnet evil.dll`) or build/run attacker code with `dotnet build`/`run`/MSBuild tasks (MITRE T1218, T1127). Env vars like DOTNET_STARTUP_HOOKS or DOTNET_ADDITIONAL_DEPS can inject code (T1574). Investigate dotnet.exe loading DLLs from Temp/user folders or launched by non-developer users.
>

# purpose

Provides commands for working with .NET projects and runs .NET applications by finding and executing their entry point.

# typical use cases

| usage | description |
| --- | --- |
| `dotnet new console` | Creates a new .NET console application. |
| `dotnet build` | Builds a project and its dependencies. |
| `dotnet exec myapp.dll` | Runs an application. |
| `dotnet myapp.dll` | Runs an application. |
| `dotnet --roll-forward Major myapp.dll` | Runs an app allowing roll forward to a higher major runtime. |
| `dotnet --info` | Prints .NET installation and environment information. |

# options

| option | description |
| --- | --- |
| `--info` | Prints detailed information about the .NET installation and machine environment. |
| `--version` | Prints the SDK version used (may be affected by global.json); SDK only. |
| `--list-runtimes [--arch <ARCH>]` | Lists installed runtimes for the architecture; `--arch` in .NET 10+. |
| `--list-sdks [--arch <ARCH>]` | Lists installed SDKs for the architecture; `--arch` in .NET 10+. |
| `-?\|-h\|--help` | Prints available commands, or documentation for a given command. |
| `-d\|--diagnostics` | Enables diagnostic output (with a command). |
| `-v\|--verbosity <LEVEL>` | Sets verbosity: q[uiet], m[inimal], n[ormal], d[etailed], diag[nostic]; not supported by every command. |
| `command options` | Options specific to each command. |
| `--additionalprobingpath <PATH>` | Path with probing policy and assemblies to probe; repeatable. |
| `--additional-deps <PATH>` | Path to an additional .deps.json file. |
| `--roll-forward <SETTING>` | Roll-forward policy: LatestPatch, Minor (default), Major, LatestMinor, LatestMajor, Disable. |
| `--fx-version <VERSION>` | Version of the .NET runtime to use to run the application. |
| `--depsfile <PATH>` | Path to a deps.json file (exec only). |
| `--runtimeconfig <PATH>` | Path to a runtimeconfig.json file (exec only). |

