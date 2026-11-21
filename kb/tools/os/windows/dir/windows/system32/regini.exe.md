---
created: 2026-11-21
fullpath: 'C:\Windows\System32\regini.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - registry
aliases:
  - regini.exe
  - regini
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/regini
  - https://learn.microsoft.com/troubleshoot/windows-client/application-management/change-registry-values-permissions
---

**fullpath**:C:\Windows\System32\regini.exe

# description

regini modifies the registry from the command line or a script, applying changes preset in one or more text files. It can create, modify or delete registry keys and modify the permissions on registry keys. It is documented in the Windows Commands reference and originated in the Windows NT/2000/2003 Resource Kits; related tools include `reg` and REGDMP.

## simple description

> ### 2026-11-21 Claude said
> regini.exe is a built-in Windows tool that reads a text script and applies the registry changes it describes. Besides setting values, it can replace the permissions (ACLs) on registry keys. It uses kernel-style paths such as `\Registry\Machine\Software` instead of `HKLM\Software`. Administrators use it in older deployment scripts.
>
> **SOC NOTE**: regini is a living-off-the-land binary for registry modification (MITRE ATT&CK T1112) and can write values from a script file, including from alternate data streams, which avoids `reg.exe` command-line detections. Because it can rewrite key ACLs it can also be used to lock defenders out of persistence keys. Look for process creation of regini.exe with a text file argument and review the referenced file.

# purpose

Applies registry data from ANSI or Unicode text files. In those files the semicolon is an end-of-line comment character, backslash continues a line, and hard tabs indicate tree structure. Lines use the format `\Registry\Hiveroot\Subkeys registry value=data [permissions]`. HKEY_LOCAL_MACHINE maps to `\registry\machine`, HKEY_USERS to `\registry\user`, HKEY_CURRENT_USER to `\registry\user\user_sid`, and HKEY_CLASSES_ROOT to `\registry\machine\software\classes`. When regini changes permissions, the current permissions are replaced, not edited.

# typical use cases

| usage | description |
| --- | --- |
| `regini script.txt` | Apply the registry changes in script.txt to the local registry. |
| `regini -m \\remoteworkstation auoptions.txt` | Apply the registry changes in auoptions.txt to a remote computer. |
| `\registry\machine\system\currentcontrolset\services\lanmanserver\parameters DiskSpaceThreshold = REG_DWORD 0x00000000` | Script-file line that sets the DiskSpaceThreshold value. |
| `\Registry\Machine\Software [1 5 10]` | Script-file line that sets HKLM\Software permissions to Administrators Full Control, Creator/Owner Full Control, Everyone Read. |

# options

| option | description |
| --- | --- |
| `-m <\\computername>` | Specifies the remote computer whose registry is to be modified, in the format \\ComputerName. |
| `-h <hivefile hiveroot>` | Specifies the local registry hive to modify, as the hive file name and the root of the hive. |
| `-i <n>` | Level of indentation used to show the tree structure of keys in output; default is 4. |
| `-o <outputwidth>` | Width of the command output in characters; defaults to the window width, or 240 when output goes to a file. |
| `-b` | Makes output backward compatible with previous versions of regini.exe. |
| `textfiles` | One or more ANSI or Unicode text files containing registry data. |
