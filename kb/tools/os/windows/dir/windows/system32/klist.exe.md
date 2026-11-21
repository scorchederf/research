---
created: 2026-11-21
fullpath: 'C:\Windows\System32\klist.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - kerberos
aliases:
  - klist.exe
  - klist
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/klist
---

**fullpath**:C:\Windows\System32\klist.exe

# description

klist is a Windows command that displays a list of currently cached Kerberos tickets. It ships with Windows and Windows Server as part of the Windows Commands set. It's related to ksetup, which configures Kerberos realms and KDCs.

## simple description

> ### 2026-11-21 Claude said
> klist.exe is a built-in Windows command-line tool for viewing and managing Kerberos tickets cached in a logon session. Kerberos tickets are what Windows uses to prove your identity to domain resources without resending your password. Administrators use klist to check which tickets exist, purge them, or request a ticket for a specific service. It's a normal admin and troubleshooting tool found on every modern Windows system.
>
> **SOC NOTE**: Attackers run `klist` for discovery after compromise and during pass-the-ticket / Kerberoasting / golden or silver ticket operations (MITRE ATT&CK T1558, T1550.003, T1087) to check injected tickets or purge them (`klist purge`). Look for process creation (Sysmon 1 / Security 4688) of klist by unusual parents, `-li 0x3e7` (SYSTEM session) use, and correlate with Kerberos events 4768/4769 on domain controllers.
>

# purpose

Displays a list of currently cached Kerberos tickets. You must be at least a Domain Admin, or equivalent, to run all the parameters of this command. With no parameters, klist retrieves all tickets for the currently logged on user.

# typical use cases

| usage | description |
| --- | --- |
| `klist`, `klist -li 0x3e7` | Query the ticket cache to find missing tickets, target server/account errors, or unsupported encryption types (Event ID 27). |
| `klist tgt` | View the TGT details. |
| `klist purge`, `klist purge -li 0x3e7` | Purge the ticket cache. |
| `klist sessions` | Locate logon sessions and logon IDs. |
| `klist kcd_cache` | Diagnose Kerberos constrained delegation failures. |
| `klist get host/%computername%` | Request a ticket for a specific SPN. |
| `klist add_bind`, `klist query_bind`, `klist purge_bind` | Target, query, or flush preferred domain controllers. |

# options

| option    | description    |
| --- | --- |
| `-lh` | High part of the user's LUID, in hexadecimal. Defaults to the current user's LUID if neither -lh nor -li is present. |
| `-li` | Low part of the user's LUID, in hexadecimal. Defaults to the current user's LUID if neither -lh nor -li is present. |
| `tickets` | Lists cached TGTs and service tickets of the specified logon session. Default option. |
| `tgt` | Displays the initial Kerberos TGT. |
| `purge` | Deletes all tickets of the specified logon session. |
| `sessions` | Displays a list of logon sessions on this computer. |
| `kcd_cache` | Displays the Kerberos constrained delegation cache information. |
| `get` | Requests a ticket to the target computer specified by the SPN. |
| `add_bind` | Specifies a preferred domain controller for Kerberos authentication. |
| `query_bind` | Displays cached preferred domain controllers for each domain Kerberos has contacted. |
| `purge_bind` | Removes the cached preferred domain controllers for the specified domains. |
| `kdcoptions` | Displays the KDC options specified in RFC 4120. |
| `/?` | Displays Help for this command. |
