---
created: 2026-11-21
fullpath: 'c:\Windows\Microsoft.NET\Framework\v4.0.30319\aspnet_compiler.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
  - aspnet
  - lolbin
aliases:
  - aspnet_compiler.exe
  - ASP.NET Compilation Tool
url:
  - https://learn.microsoft.com/visualstudio/msbuild/aspnetcompiler-task
  - https://learn.microsoft.com/aspnet/web-forms/overview/moving-to-aspnet-20/configuration-and-instrumentation
  - https://learn.microsoft.com/aspnet/web-forms/overview/older-versions-getting-started/deploying-web-site-projects/precompiling-your-website-cs
---

**fullpath**:c:\Windows\Microsoft.NET\Framework\v4.0.30319\aspnet_compiler.exe

# description

The ASP.NET Compilation Tool shipped with the .NET Framework, used to precompile ASP.NET applications either in place or for deployment to a target directory. MSBuild's `AspNetCompiler` task wraps it, and Visual Studio's Publish Web Site invokes it.

## simple description

> ### 2026-11-21 Claude said
> aspnet_compiler.exe compiles the pages and code of an ASP.NET website ahead of time, so the first visitor does not wait for compilation. It can compile in place or output a deployable copy of the site. It is a signed Microsoft binary that ships with every .NET Framework install.
>
> **SOC NOTE**: Listed as a LOLBin: it can be abused to compile and execute attacker-supplied code via a crafted `App_Code`/build provider in a fake web app folder (MITRE ATT&CK T1127 Trusted Developer Utilities Proxy Execution). Execution on a workstation or with paths in user-writable folders (e.g. `-p C:\Users\...\Temp`) is highly suspicious.
>

# purpose

Precompiles ASP.NET applications. In-place compilation mimics first requests; compiling for deployment (specifying a target directory) produces assemblies in `Bin` plus placeholder files, optionally updatable with `-u`.

# typical use cases

| usage | description |
| --- | --- |
| `aspnet_compiler -p "physical_path_to_app" -v / -f -u "target_location_folder"` | Precompile the site at a physical path for deployment, overwriting the target and keeping it updatable. |

# options

| option | description |
| --- | --- |
| `-m` | Full IIS metabase path of the application; cannot be combined with `-v` or `-p`. |
| `-v` | Virtual path of the application to compile. |
| `-p` | Physical path of the application to compile; if missing the IIS metabase is used. |
| `-u` | Makes the precompiled application updatable. |
| `-f` | Overwrites the target directory if it exists; existing contents are lost. |
| `-d` | Emits debug information (.PDB) during compilation. |
| `-c` | Builds clean; previously compiled components are recompiled. |
| `targetDir` | Target location for compilation for deployment; omit to compile in place. |
