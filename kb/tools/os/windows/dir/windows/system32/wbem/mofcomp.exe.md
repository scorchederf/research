---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wbem\mofcomp.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - wmi
  - lolbin
aliases:
  - "mofcomp.exe"
  - "mofcomp"
  - "MOF Compiler"
url:
  - https://learn.microsoft.com/windows/win32/wmisdk/mofcomp
  - https://learn.microsoft.com/windows/win32/wmisdk/running-the-mof-compiler-on-a-file
  - https://learn.microsoft.com/windows/win32/wmisdk/wmi-command-line-tools
---

**fullpath**:C:\Windows\System32\wbem\mofcomp.exe

# description

mofcomp, the MOF Compiler, parses Managed Object Format (MOF) files and adds the classes and instances they define to the WMI repository. It is one of the WMI command-line tools in `%Windir%\System32\wbem`, alongside winmgmt, wmiadap, smi2smir and wmic; compilation can also be done programmatically with IMofCompiler.

## simple description

> ### 2026-11-21 Claude said
> mofcomp.exe compiles .mof text files into the WMI repository, which is how WMI providers register their classes. Admins use it to repair WMI by recompiling system MOF files. Classes go into root\default unless another namespace is given with -N or #pragma namespace.
>
> **SOC NOTE**: Attackers compile malicious MOF files to create permanent WMI event subscriptions (__EventFilter, CommandLineEventConsumer, __FilterToConsumerBinding) for persistence (T1546.003); `-autorecover` makes them survive repository rebuilds. Watch for mofcomp.exe executions on non-admin-authored files, WMI-Activity Operational event 5861, and new entries in the autorecover list.
>

# purpose

Compiles MOF files into the WMI repository, optionally checking syntax only, creating binary MOF, splitting localized amendments, or registering the file for autorecovery. Returns 0 on success, 1 if it cannot connect to WMI, 2 for invalid switches and 3 for a MOF syntax error.

# typical use cases

| usage | description |
| --- | --- |
| `mofcomp MOFfile.mof` | Compile a MOF file into the root\default namespace. |
| `mofcomp -check MOFfile.mof` | Perform a syntax check only, without connecting to WMI. |
| `mofcomp -N:root\cimv2 MOFfile.mof` | Load the MOF file into the root\cimv2 namespace. |
| `mofcomp -autorecover MOFfile.mof` | Compile the file and add it to the list compiled during repository recovery. |

# options

| option | description |
| --- | --- |
| `-autorecover` | Adds the MOF file to the list of files compiled during repository recovery (stored under `HKLM\SOFTWARE\Microsoft\WBEM\CIMOM`). |
| `-check` | Performs a syntax check only; no other switch can be used and WMI is not modified. |
| `-N:<namespacepath>` | Loads the MOF file into the specified namespace instead of root\default. |
| `-class:createonly` | Makes no changes to existing classes; fails if a class already exists. |
| `-class:forceupdate` | Forces class updates when conflicting child classes exist; fails if child classes have instances. |
| `-class:safeupdate` | Allows class updates with child classes as long as no conflicts are caused. |
| `-class:updateonly` | Does not create new classes; fails if a class does not exist. |
| `-instance:updateonly` | Does not create new instances; fails if an instance does not exist. |
| `-instance:createonly` | Makes no changes to existing instances; fails if an instance already exists. |
| `-B:<filename>` | Creates a binary MOF file without modifying the WMI repository. |
| `-WMI` | Performs a WMI syntax check for binary MOF used by WDM drivers; requires -B. |
| `-P:<Password>` | Password for the user logging on. |
| `-U:<UserName>` | Name of the user logging on. |
| `-A:<Authority>` | Authority (domain name) used when logging on to WMI. |
| `-MOF:<path>` | Name of the language-neutral output used with -AMENDMENT. |
| `-MFL:<path>` | Name of the language-specific output used with -AMENDMENT. |
| `-AMENDMENT:<Locale>` | Splits the MOF into language-neutral and language-specific (MFL) versions for locale MS_xxx. |
| `-ER <ResourceName>` | Extracts binary MOF from a named resource. |
| `-L:<ResourceLocale>` | Extracts localized MOF descriptions from the binary MOF when used with -ER. |
| `<MOFfile>` | Name of the file to parse. |
