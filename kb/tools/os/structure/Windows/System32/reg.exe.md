---
created: 2026-11-21
fullpath: 'C:\Windows\System32\reg.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - reg.exe
  - reg
  - Console Registry Tool for Windows
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/reg
  - https://learn.microsoft.com/windows-server/administration/windows-commands/reg-add
  - https://learn.microsoft.com/windows-server/administration/windows-commands/reg-query
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/windows-registry-advanced-users
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/windows-10-s-planning?view=windows-11
---

**fullpath**:C:\Windows\System32\reg.exe

# description

reg.exe (the Console Registry Tool for Windows) performs operations on registry subkeys and values from the command line. Some operations work on local or remote computers (remote root keys are limited to HKLM and HKU); others are local only. Microsoft cautions against editing the registry directly unless there's no alternative.

## simple description

> ### 2026-11-21 Claude said
> Reg.exe is Windows' built-in command-line tool for working with the registry, the database where Windows and applications store their settings. It can read (query), add, change, delete, export and import registry keys and values. It can also save whole sections of the registry to a file and load them back, and it can work against remote computers (HKLM and HKU only).
>
> **SOC NOTE**: `reg save` and `reg export` copy registry data to files, `reg add` and `reg delete` change settings, and `reg query /s /f` searches the registry, so all of these are worth reviewing in process command lines. Microsoft lists reg.exe among the components blocked in Windows S mode.
>

# purpose

- Query keys and values, including recursive searches (`reg query /s /f`).
- Add, change or delete keys and values.
- Export/import .reg files, and save/restore/load/unload hive files.
- Valid local root keys: HKLM, HKCU, HKCR, HKU, HKCC.

# typical use cases

- Add a key on a remote computer: `reg add \\ABC\HKLM\Software\MyCo`
- Add a binary value: `reg add HKLM\Software\MyCo /v Data /t REG_BINARY /d fe340ead`
- Find keys matching a string: `reg query HKLM\SOFTWARE\Microsoft /s /f asp.net /k`
- Show the default value: `reg query HKLM\SOFTWARE /ve`
- Help: `reg /?`

# options

| option    | description    |
| --- | --- |
| `reg add` | Adds a new subkey or entry to the registry. |
| `reg compare` | Compares specified registry subkeys or entries. |
| `reg copy` | Copies a registry entry to a specified location on the local or remote computer. |
| `reg delete` | Deletes a subkey or entries from the registry. |
| `reg export` | Copies the specified subkeys, entries, and values of the local computer into a file for transfer to other servers. |
| `reg import` | Copies the contents of a file that contains exported registry subkeys, entries, and values into the registry of the local computer. |
| `reg load` | Writes saved subkeys and entries into a different subkey in the registry. |
| `reg query` | Returns a list of the next tier of subkeys and entries under a specified subkey. |
| `reg restore` | Writes saved subkeys and entries back to the registry. |
| `reg save` | Saves a copy of specified subkeys, entries, and values of the registry in a specified file. |
| `reg unload` | Removes a section of the registry that was loaded using reg load. |

### reg add parameters

| option    | description    |
| --- | --- |
| `<keyname>` | Full path of the subkey or entry; include `\\<computername>\` for a remote computer. Quote names with spaces. |
| `/v <Valuename>` | Name of the registry entry to add. |
| `/ve` | The added entry has a null value. |
| `/t <Type>` | Entry type: REG_SZ, REG_MULTI_SZ, REG_DWORD_BIG_ENDIAN, REG_DWORD, REG_BINARY, REG_DWORD_LITTLE_ENDIAN, REG_LINK, REG_FULL_RESOURCE_DESCRIPTOR, REG_EXPAND_SZ. |
| `/s <Separator>` | Separator for multiple REG_MULTI_SZ data instances (default \0). |
| `/d <Data>` | Data for the new entry. |
| `/f` | Adds the entry without prompting for confirmation. |
| `/reg:32` | Access the key using the 32-bit registry view. |
| `/reg:64` | Access the key using the 64-bit registry view. |
| `/?` | Displays help at the command prompt. |

### reg query parameters

| option    | description    |
| --- | --- |
| `<keyname>` | Full path of the subkey; include `\\<computername>\` for a remote computer. |
| `/v <valuename>` | Value name to query; if omitted, all values are returned. |
| `/ve` | Queries for value names that are empty. |
| `/s` | Queries all subkeys and value names recursively. |
| `/se <separator>` | Value separator to search for in REG_MULTI_SZ (default \0). |
| `/f <data>` | Data or pattern to search for (default `*`). |
| `/k` | Searches key names only; must be used with /f. |
| `/d` | Searches data only. |
| `/c` | Case-sensitive query. |
| `/e` | Returns only exact matches. |
