---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wbem\Repository'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - wmi
aliases:
  - Repository
  - WMI repository
  - CIM repository
url:
  - https://learn.microsoft.com/windows/win32/wmisdk/winmgmt
  - https://learn.microsoft.com/windows/win32/wmisdk/wmi-infrastructure
  - https://learn.microsoft.com/troubleshoot/windows-server/system-management-components/scenario-guide-troubleshoot-wmi-connectivity-access-issues
  - https://learn.microsoft.com/troubleshoot/azure/virtual-machines/windows/windows-azure-guest-agent
  - https://learn.microsoft.com/windows/win32/api/wbemcli/nn-wbemcli-iwbembackuprestore
---

**fullpath**:C:\Windows\System32\wbem\Repository

# description

The Repository folder holds the WMI repository (also called the CIM repository), the storage area for WMI static data used by the WMI service (Winmgmt) running in SVCHOST as LocalSystem. It is managed with `winmgmt` switches and the IWbemBackupRestore interface.

## simple description

> ### 2026-11-21 Claude said
> This folder is WMI's database. It stores class definitions, namespaces and other static data that Windows Management Instrumentation needs, in files such as OBJECTS.DATA, INDEX.BTR and MAPPING*.MAP. WMI is used by admin tools, scripts, SCCM and many applications. If it gets corrupted, WMI queries fail.
>
> **SOC NOTE**: WMI event subscription persistence (T1546.003: __EventFilter, CommandLineEventConsumer, __FilterToConsumerBinding) is stored in OBJECTS.DATA, so this folder is a key forensic artifact even after the attacker's script is gone; parse with tools like PyWMIPersistenceFinder or flare-wmi. Also check Microsoft-Windows-WMI-Activity/Operational events 5857-5861. Attackers may also compile MOF files with #pragma autorecover to survive repository rebuilds.
>

# purpose

Stores the static WMI data (such as class definitions compiled from MOF files); dynamic data is supplied by providers. The repository is not a single file but a collection of files in the Repository folder that work together as a database. `winmgmt /verifyrepository [path]` checks consistency (returning ERROR_INTERNAL_DB_CORRUPTION, 1358, if inconsistent), `winmgmt /salvagerepository` rebuilds and merges readable content, `winmgmt /resetrepository` resets it to the initial OS state (restoring MOFs with #pragma autorecover), and `winmgmt /backup` / `/restore` back it up to a single compressed file. Microsoft advises not to delete the repository as a first action; it can be backed up with `xcopy c:\windows\system32\wbem\repository c:\windows\system32\wbem\repository.bak /e /i`.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_
