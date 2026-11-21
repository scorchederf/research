---
created: 2026-11-21
fullpath: 'C:\Windows\System32\bcdedit.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - bcdedit.exe
  - BCDEdit
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/bcdedit
---

**fullpath**:C:\Windows\System32\bcdedit.exe

# description

BCDEdit is a command-line tool for managing Boot Configuration Data (BCD) stores, which replace Boot.ini. It is included in %WINDIR%\System32 since Windows Vista, serves the same purpose as Bootcfg.exe with more parameters and better scripting, and requires administrative privileges to modify BCD; the BCD WMI API is suggested for complex operations.

## simple description

> ### 2026-11-21 Claude said
> Bcdedit edits the Boot Configuration Data, the database that tells Windows how to boot: which OS entries exist, the default entry, timeouts, debug and recovery settings. Admins use it to add dual-boot entries, enable kernel debugging, or turn on test signing. It requires an elevated prompt. Changes take effect at the next boot.
>
> **SOC NOTE**: Ransomware runs `bcdedit /set {default} recoveryenabled No` and `bootstatuspolicy ignoreallfailures` to block recovery (MITRE ATT&CK T1490). Attackers also enable `testsigning`/`nointegritychecks` or debug mode to load unsigned drivers or rootkits (T1553.006, T1542). Bcdedit command lines in process logs and BCD changes are high-value alerts; `bcdedit /enum` output helps confirm tampering.
>

# purpose

Create, export, import and modify BCD stores and entries, control the boot manager, Emergency Management Services and boot/kernel debugging.

# typical use cases

- View entries: `bcdedit /enum` (or `bcdedit /v` for full identifiers)
- Back up the store: `bcdedit /export <file>`
- Enable kernel debugger: `bcdedit /debug on`

# options

| option    | description    |
| --- | --- |
| `/?` | Displays a list of commands; `bcdedit /? <command>` gives detailed help. |
| `/createstore` | Creates a new empty (non-system) BCD store. |
| `/export` | Exports the system store to a file (system store only). |
| `/import` | Restores the system store from an `/export` backup, deleting existing entries first. |
| `/store` | Specifies the store to use; default is the system store. |
| `/copy` | Makes a copy of a boot entry in the same system store. |
| `/create` | Creates a new entry in the store. |
| `/delete` | Deletes an element from a specified entry. |
| `/deletevalue` | Deletes a specified element from a boot entry. |
| `/set` | Sets an entry option value. |
| `/enum` | Lists entries in a store (default action). |
| `/v` | Verbose mode; displays all identifiers in full. |
| `/bootsequence` | One-time display order for the next boot. |
| `/default` | Default entry selected when the timeout expires. |
| `/displayorder` | Display order used by the boot manager. |
| `/timeout` | Seconds to wait before selecting the default entry. |
| `/toolsdisplayorder` | Display order for the **Tools** menu. |
| `/bootems` | Enables or disables EMS for the specified entry. |
| `/ems` | Enables or disables EMS for an OS boot entry. |
| `/emssettings` | Sets the global EMS settings. |
| `/bootdebug` | Enables or disables the boot debugger for a boot entry. |
| `/dbgsettings` | Specifies or displays global debugger settings. |
| `/debug` | Enables or disables the kernel debugger for a boot entry. |
