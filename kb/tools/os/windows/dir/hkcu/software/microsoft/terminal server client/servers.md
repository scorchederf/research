---
created: 2026-11-21
fullpath: 'HKCU\Software\Microsoft\Terminal Server Client\Servers'
generator:
  - claude
  - microsoftlearn
tags:
  - registry
  - rdp
  - lateral-movement
aliases:
  - Terminal Server Client\Servers
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/remote/remove-entries-from-remote-desktop-connection-computer
---

**fullpath**:HKCU\Software\Microsoft\Terminal Server Client\Servers

# description

Per-user key used by the Remote Desktop Connection client (mstsc.exe). Learn documents only the sibling `Terminal Server Client\Default` key, which holds the MRU list shown in the Remote Desktop Connection **Computer** box; the `Servers` subkey itself is not described.

## simple description

> ### 2026-11-21 Claude said
> Each time a user connects with Remote Desktop Connection, Windows creates a subkey here named after the remote computer (host name or IP). Inside it, the `UsernameHint` value records the user name that was used, and `CertHash` may store the accepted server certificate. Together with the `Default` key's MRU list it is the user's RDP connection history.
>
> **SOC NOTE**: Key lateral-movement evidence (MITRE T1021.001 Remote Desktop Protocol): outbound RDP targets and account names from this host, per user (Ntuser.dat). Attackers often delete these entries and `Default.rdp` to cover tracks (T1070). Correlate with TerminalServices-RDPClient/Operational events 1024/1102 on the source and 4624 type 10 / 1149 on the destination.
>

# purpose

The Remote Desktop Connection client tracks previously used computers. Learn documents that every new connection is written as MRU0 under `Terminal Server Client\Default` (an FQDN or IP), older entries shift down, and entries can be removed by deleting the values in Registry Editor.

# hive

| property | value |
| --- | --- |
| hive | HKCU |
| scope | per-user |
| backing file | `Ntuser.dat` |

# values

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# subkeys

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# query

| usage | description |
| --- | --- |
| `reg query "HKCU\Software\Microsoft\Terminal Server Client\Servers"` | List the key's values. |
| `reg query "HKCU\Software\Microsoft\Terminal Server Client\Servers" /s` | List each saved server subkey and its values. |
| `reg query "HKCU\Software\Microsoft\Terminal Server Client\Default"` | List the MRU*number* entries of the Computer box. |
