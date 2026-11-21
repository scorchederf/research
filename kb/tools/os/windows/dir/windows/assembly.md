---
created: 2026-11-21
fullpath: 'C:\Windows\assembly'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - dotnet
aliases:
  - assembly
  - Global Assembly Cache
  - GAC
url:
  - https://learn.microsoft.com/dotnet/framework/app-domains/gac
  - https://learn.microsoft.com/dotnet/framework/app-domains/working-with-assemblies-and-the-gac
  - https://learn.microsoft.com/dotnet/framework/app-domains/how-to-view-the-contents-of-the-gac
---

**fullpath**:C:\Windows\assembly

# description

`%windir%\assembly` is the default location of the .NET Framework Global Assembly Cache (GAC) for versions earlier than .NET Framework 4; from .NET Framework 4 the default is `%windir%\Microsoft.NET\assembly`. The GAC is a machine-wide code cache that stores assemblies designated to be shared by several applications. Assemblies are installed with Windows Installer or, in development, with the Global Assembly Cache tool (Gacutil.exe).

## simple description

> ### 2026-11-21 Claude said
> C:\Windows\assembly is the older .NET Global Assembly Cache, a shared library folder where strong-named .NET DLLs live so many programs can use the same version. Inside are folders like GAC_MSIL, GAC_32 and GAC_64, and NativeImages folders created by ngen. Explorer used to show it as a special view; the real structure is visible from the command line.
>
> **SOC NOTE**: Because the CLR checks the GAC before the application directory, a malicious or tampered assembly placed here can be loaded by trusted .NET apps (persistence / hijacking, MITRE ATT&CK T1574). Writing requires admin rights, so new unsigned or unexpected assemblies or recent writes outside of updates are suspicious. Attackers also drop tooling into NativeImages folders to blend in.

# purpose

Stores shared, strong-named assemblies for side-by-side versioning and as an additional search location: the common language runtime checks the GAC for a matching assembly before probing or using codebase information. Because it is under the systemroot directory it inherits that directory's ACL, and only administrators should delete files from it. Integrity checks are performed on all files of an assembly when it is added.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
