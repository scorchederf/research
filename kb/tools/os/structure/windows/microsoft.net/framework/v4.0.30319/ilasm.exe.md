---
created: 2026-11-21
fullpath: 'C:\Windows\Microsoft.NET\Framework\v4.0.30319\ilasm.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - ilasm.exe
  - IL Assembler
url:
  - https://learn.microsoft.com/dotnet/framework/tools/ilasm-exe-il-assembler
---

**fullpath**:C:\Windows\Microsoft.NET\Framework\v4.0.30319\ilasm.exe

# description

The IL Assembler (Ilasm.exe) generates a portable executable (PE) file from intermediate language (IL) assembly source. It is part of the .NET Framework tools, installed with Visual Studio, and is the companion of Ildasm.exe (IL Disassembler), which produces IL text from a PE file.

## simple description

> ### 2026-11-21 Claude said
> Ilasm is the .NET Framework's assembler: it turns human-readable .NET intermediate language (.il text) into a runnable .exe or .dll. Developers and tool vendors use it with ildasm to round-trip and hand-edit compiled .NET programs. The 32-bit copy lives in the Framework folder and ships with every .NET Framework 4.x install. It does not need Visual Studio to run from this path.
>
> **SOC NOTE**: Ilasm is a known LOLBin: attackers drop a .il text file and compile it on the target into an exe/dll, evading controls that block downloaded binaries (MITRE ATT&CK T1127 Trusted Developer Utilities Proxy Execution, T1027.004 Compile After Delivery). Any ilasm.exe execution on non-developer machines, especially with .il files in temp or user folders, should be investigated; the new PE it writes is a key artifact.
>

# purpose

Assemble IL source into PE files (.exe/.dll) without intermediate object files or linking, letting compiler and tool developers focus on IL and metadata generation; used with Ildasm.exe to hand-edit and re-assemble managed code.

# typical use cases

- Assemble an exe: `ilasm myTestFile`
- Assemble a dll: `ilasm myTestFile /dll`
- Assemble with a new name: `ilasm myTestFile /dll /output:myNewTestFile.dll`

# options

| option    | description    |
| --- | --- |
| `filename` | Name of the .il source file; multiple files can produce a single PE file. |
| `/32bitpreferred` | Creates a 32-bit-preferred image (PE32). |
| `/alignment:integer` | Sets FileAlignment in the NT Optional header; overrides `.alignment`. |
| `/appcontainer` | Produces a .dll or .exe that runs in the Windows app container. |
| `/arm` | Targets ARM; default bitness is `/32bitpreferred`. |
| `/base:integer` | Sets ImageBase in the NT Optional header; overrides `.imagebase`. |
| `/clock` | Measures and reports compilation times in milliseconds. |
| `/debug[:IMPL\|OPT]` | Includes debug information and creates a PDB; IMPL/OPT control JIT optimization and sequence points. |
| `/dll` | Produces a .dll file as output. |
| `/enc:file` | Creates Edit-and-Continue deltas (academic use only). |
| `/exe` | Produces an executable file (default). |
| `/flags:integer` | Sets ImageFlags in the CLR header; overrides `.corflags`. |
| `/fold` | Folds identical method bodies into one. |
| `/highentropyva` | Produces an executable that supports high-entropy ASLR. |
| `/include:includePath` | Sets a path to search for `#include` files. |
| `/itanium` | Targets Intel Itanium; default bitness `/pe64`. |
| `/key:keyFile` | Strong-name signs using the private key in keyFile. |
| `/key:@keySource` | Strong-name signs using the private key produced at keySource. |
| `/listing` | Produces a listing file on standard output (not supported in .NET Framework 2.0 or later). |
| `/mdv:versionString` | Sets the metadata version string. |
| `/msv:major.minor` | Sets the metadata stream version. |
| `/noautoinherit` | Disables default inheritance from Object when no base class is specified. |
| `/nocorstub` | Suppresses generation of the CORExeMain stub. |
| `/nologo` | Suppresses the startup banner. |
| `/output:file.ext` | Specifies the output file name and extension (does not imply `/dll`). |
| `/optimize` | Optimizes long instructions to short (e.g. `br` to `br.s`). |
| `/pe64` | Creates a 64-bit image (PE32+). |
| `/pdb` | Creates a PDB without enabling debug information tracking. |
| `/quiet` | Quiet mode; does not report assembly progress. |
| `/resource:file.res` | Includes one .res resource file in the output. |
| `/ssver:int.int` | Sets the subsystem version number in the NT optional header. |
| `/stack:stackSize` | Sets SizeOfStackReserve in the NT Optional header. |
| `/stripreloc` | Specifies that no base relocations are needed. |
| `/subsystem:integer` | Sets subsystem in the NT Optional header; overrides `.subsystem`. |
| `/x64` | Targets 64-bit AMD; default bitness `/pe64`. |
| `/?` | Displays command syntax and options. |
