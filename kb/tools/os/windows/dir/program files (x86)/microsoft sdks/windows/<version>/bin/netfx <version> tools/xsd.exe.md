---
created: 2026-11-21
fullpath: 'C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\bin\NETFX <version> Tools\xsd.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - dotnet
  - sdk
aliases:
  - xsd.exe
  - XML Schema Definition Tool
url:
  - https://learn.microsoft.com/dotnet/standard/serialization/xml-schema-definition-tool-xsd-exe
  - https://learn.microsoft.com/visualstudio/msbuild/xsd-task
---

**fullpath**:C:\Program Files (x86)\Microsoft SDKs\Windows\<version>\bin\NETFX <version> Tools\xsd.exe

# description

The XML Schema Definition tool (Xsd.exe) generates XML schema or common language runtime classes from XDR, XML and XSD files, or from classes in a runtime assembly. It ships with the Windows SDK .NET Framework tools under `C:\Program Files (x86)\Microsoft SDKs\Windows\{version}\bin\NETFX {version} Tools\`, and is wrapped by the MSBuild XSD task.

## simple description

> ### 2026-11-21 Claude said
> xsd.exe is a .NET developer tool that converts between XML schemas and code. It can infer a schema from an XML file, generate C# or VB classes or typed DataSets from a schema, or produce a schema from types in a compiled assembly. It is installed with the Windows SDK / Visual Studio, not with Windows itself.
>
> **SOC NOTE**: Mostly benign developer tooling; seeing it on non-developer endpoints or run by unusual parents is worth a look. When pointed at a .dll/.exe it loads the assembly to reflect types, which can execute code in static constructors, so it could be abused as a signed proxy loader (T1218-style). Check command lines in 4688/Sysmon 1.
>

# purpose

Operations: XDR to XSD, XML to XSD, XSD to DataSet, XSD to Classes, and Classes to XSD. It only works with W3C XSD schemas. For .NET Framework tools to work, run SDKVars.bat to set Path, Include and Lib.

# typical use cases

| usage | description |
| --- | --- |
| `xsd myFile.xdr` | Generate an XML schema from myFile.xdr in the current directory. |
| `xsd myFile.xml /outputdir:myOutputDir` | Generate an XML schema from myFile.xml into myOutputDir. |
| `xsd /dataset /language:CS XSDSchemaFile.xsd` | Generate a C# DataSet class from the schema. |
| `xsd myAssembly.dll` | Generate XML schemas for all types in myAssembly.dll (schema0.xsd). |
| `xsd /p:GenerateSchemas.xml` | Read options from a parameters XML file. |

# options

| option | description |
| --- | --- |
| `file.extension` | Input file (.xdr, .xml, .xsd, .dll or .exe) to convert. |
| `/h[elp]` | Displays command syntax and options. |
| `/o[utputdir]:directory` | Directory for output files; default is the current directory. |
| `/?` | Displays command syntax and options. |
| `/p[arameters]:file.xml` | Read options for operation modes from the specified XML file. |
| `/c[lasses]` | Generate classes for the specified schema (.xsd only). |
| `/d[ataset]` | Generate a DataSet-derived class for the schema (.xsd only). |
| `/e[lement]:element` | Element in the schema to generate code for; can repeat. |
| `/enableDataBinding` | Implement INotifyPropertyChanged on generated types. Short form `/edb`. |
| `/enableLinqDataSet` | Make the generated DataSet queryable with LINQ to DataSet; used with /dataset. Short form `/eld`. |
| `/f[ields]` | Generate fields only instead of properties. |
| `/l[anguage]:language` | Language: CS (default), VB, JS, VJS, or a CodeDomProvider class name. |
| `/n[amespace]:namespace` | Runtime namespace for generated types; default `Schemas`. |
| `/nologo` | Suppresses the banner. |
| `/order` | Generate explicit order identifiers on all particle members. |
| `/o[ut]:directoryName` | Output directory; default is the current directory. |
| `/u[ri]:uri` | URI for the elements to generate code for. |
| `/t[ype]:typename` | Type to create a schema for (.dll/.exe input); can repeat and supports a trailing *. |

