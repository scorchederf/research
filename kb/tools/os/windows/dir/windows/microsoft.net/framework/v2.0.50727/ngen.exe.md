---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework\v2.0.50727\ngen.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
aliases:
  - ngen.exe
  - Native Image Generator
url:
  - https://learn.microsoft.com/dotnet/framework/tools/ngen-exe-native-image-generator
---

**fullpath**:C:\Windows\Microsoft.NET\Framework\v2.0.50727\ngen.exe

# description

Ngen.exe (Native Image Generator) creates native images (precompiled processor-specific machine code) for .NET Framework assemblies and installs them in the native image cache so the runtime does not need to JIT-compile them. It ships with the .NET Framework (this copy is the 2.0.50727 runtime) and is installed with Visual Studio. The native image service (".NET Runtime Optimization Service") performs deferred compilation; Mpgo.exe can optimize images further.

## simple description

> ### 2026-11-21 Claude said
> Ngen.exe is the .NET Framework tool that pre-compiles managed programs into native code to make them start faster. It is normally run by installers and by the .NET optimization service (mscorsvw.exe) in the background. It needs administrator rights. Seeing it on a machine is completely normal.
>
> **SOC NOTE**: Ngen is a signed Microsoft binary that loads and compiles arbitrary assemblies; it is rarely abused directly but heavy ngen/mscorsvw activity after .NET updates can mask other process noise. Unexpected `ngen install` of an unusual assembly path (e.g. user temp) is worth reviewing. Native images land under `C:\Windows\assembly\NativeImages_*`, which can be a forensic artifact showing which assemblies were compiled.
>

# purpose

Generate, install, display, update and uninstall native images, and control the native image service queue.

# typical use cases

| usage | description |
| --- | --- |
| `ngen install ClientApp.exe` | Generate native images for ClientApp.exe and its referenced DLLs and install them in the cache. |
| `ngen install MyComponent /queue` | Queue installation for the native image service instead of compiling immediately. |
| `ngen display` | List all root assemblies and native images in the cache. |
| `ngen update /queue` | Queue regeneration of all invalidated native images. |
| `ngen uninstall ClientApp` | Uninstall all scenarios for the root ClientApp.exe. |
| `ngen queue pause` | Pause the native image service before an installation. |
| `ngen executeQueuedItems` | Process all queued compilation jobs synchronously. |

# options

| option | description |
| --- | --- |
| `install [assemblyName \| assemblyPath] [scenarios] [config] [/queue[:{1\|2\|3}]]` | Generate native images for an assembly and its dependencies and install them in the cache; `/queue` defers to the service (default priority 3). |
| `uninstall [assemblyName \| assemblyPath] [scenarios] [config]` | Delete the native images of an assembly and its dependencies. `uninstall *` is not supported from .NET Framework 4. |
| `update [/queue]` | Update native images that have become invalid. |
| `display [assemblyName \| assemblyPath]` | Display the state of native images; with no argument, the whole cache. |
| `executeQueuedItems [1\|2\|3]` / `eqi` | Execute queued compilation jobs of the given priority or higher. |
| `queue {pause \| continue \| status}` | Pause, resume or query the native image service. |
| `assemblyName` | Full display name of the assembly; partial names allowed for display and uninstall. |
| `assemblyPath` | Explicit full or relative path of the assembly. |
| `1` | Priority: generate and install immediately. |
| `2` | Priority: install without waiting for idle time, after priority 1 actions. |
| `3` | Priority: install when the service detects the computer is idle. |
| `/Debug` | Generate images usable under a debugger. |
| `/Profile` | Generate images usable under a profiler. |
| `/NoDependencies` | Generate the minimum number of native images for the scenario. |
| `/ExeConfig:exePath` | Use the configuration of the specified executable to resolve dependencies. |
| `/AppBase:directoryPath` | Use the directory as application base when locating dependencies. |
| `/nologo` | Suppress the startup banner. |
| `/silent` | Suppress success messages. |
| `/verbose` | Display detailed debugging information. |
| `/help`, `/?` | Display command syntax and options. |
