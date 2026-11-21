---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework\v2.0.50727\regasm.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
  - com
  - lolbin
aliases:
  - 'regasm.exe'
  - 'Regasm.exe'
  - 'Assembly Registration Tool'
url:
  - https://learn.microsoft.com/dotnet/framework/tools/regasm-exe-assembly-registration-tool
  - https://learn.microsoft.com/dotnet/standard/native-interop/registering-assemblies-with-com
---

**fullpath**:C:\Windows\Microsoft.NET\Framework\v2.0.50727\regasm.exe

# description

`Regasm.exe` (Assembly Registration Tool) reads the metadata in a .NET Framework assembly and adds the registry entries that let COM clients create .NET classes transparently. This copy belongs to .NET Framework 2.0; related tools are Tlbexp.exe, Tlbimp.exe and Regsvcs.exe.

## simple description

> ### 2026-11-21 Claude said
> RegAsm registers a .NET DLL so old-style COM programs can use it, writing CLSID, ProgID and type library keys into HKEY_CLASSES_ROOT. It can also unregister them or write a .reg file instead. It is a signed Microsoft binary present on most Windows machines.
>
> **SOC NOTE**: Abused for signed binary proxy execution (T1218.009 Regsvcs/Regasm): `regasm.exe /U evil.dll` runs code in the assembly's `[ComUnregisterFunction]` (and register functions) without needing admin rights for /U, bypassing allow-listing. Watch for regasm launched from scripts/Office or against DLLs in user-writable paths, and for new HKCR\CLSID entries with `InprocServer32 = mscoree.dll` plus `CodeBase` pointing at odd locations (COM hijack persistence).
>

# purpose

Registers the creatable classes of an assembly for COM. It creates version-dependent registry keys (CLSID, Interface, TypeLib, ProgID under HKEY_CLASSES_ROOT), sets `InprocServer32` to Mscoree.dll and adds `Class` and `Assembly` values the runtime uses to resolve the assembly. Classes are registered once, when the assembly is installed.

# typical use cases

| usage | description |
| --- | --- |
| `regasm myTest.dll` | Register all public classes contained in *myTest.dll*. |
| `regasm myTest.dll /regfile:myTest.reg` | Generate *myTest.reg* with the needed registry entries without updating the registry. |
| `regasm myTest.dll /tlb:myTest.tlb` | Register the public classes and generate and register the type library *myTest.tlb*. |

# options

| option | description |
| --- | --- |
| `assemblyFile` | The assembly to be registered with COM. |
| `/codebase` | Create a Codebase entry giving the file path of an assembly not installed in the GAC; use with strong-named assemblies. |
| `/registered` | Only refer to type libraries that have already been registered. |
| `/asmpath:directory` | Directory containing assembly references; must be used with `/regfile`. |
| `/nologo` | Suppress the Microsoft startup banner. |
| `/regfile[:regFile]` | Generate a .reg file with the needed registry entries instead of changing the registry; not with `/u` or `/tlb`. |
| `/silent` or `/s` | Suppress success messages. |
| `/tlb[:typeLibFile]` | Generate a type library from the assembly with definitions of its accessible types. |
| `/unregister` or `/u` | Unregister the creatable classes found in *assemblyFile*. |
| `/verbose` | Verbose mode; with `/tlb`, list referenced assemblies needing a type library. |
| `/?` or `/help` | Display command syntax and options. |
