---
created: 2026-11-21
fullpath: 'C:\Windows\System32\drivers\etc\hosts'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - hosts
  - Hosts file
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/networking/troubleshoot-dns-client-resolution-issues
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/cannot-modify-hosts-lmhosts-files
  - https://learn.microsoft.com/windows/win32/snmp/host-names-and-ip-addresses
  - https://learn.microsoft.com/windows/powertoys/hosts-file-editor
  - https://learn.microsoft.com/windows/win32/winprog64/file-system-redirector
---

**fullpath**:C:\Windows\System32\drivers\etc\hosts

# description

The hosts file is a text file (no extension) at `%SystemRoot%\System32\drivers\etc\hosts` that maps host names to IP addresses and overrides name resolution for the local computer. It can be edited with Notepad run as administrator or the PowerToys Hosts File Editor; the same folder holds the Lmhosts file.

## simple description

> ### 2026-11-21 Claude said
> The hosts file is a simple list of "IP address  hostname" lines that Windows checks before asking DNS. Admins and developers use it to test sites or block domains (e.g. pointing them to 127.0.0.1). Lines starting with # are comments. Editing requires administrator rights.
>
> **SOC NOTE**: Malware edits hosts to block security-vendor/update domains or redirect banking and login sites to attacker IPs (MITRE ATT&CK T1565.001 / T1562.001). Any non-comment entries, recent modification times, or writes by non-admin tools should be reviewed; Defender flags some hijacks as SettingsModifier:Win32/HostsFileHijack. Sysmon 11 / file integrity monitoring on this path is cheap and useful.
>

# purpose

Overrides name resolution locally. The DNS client resolves names by checking the cache, then the Hosts file, then querying the DNS server, so a hosts entry prevents any DNS query for that name. The file is loaded at startup and consulted when a host name requires resolution. Access to `%windir%\system32\drivers\etc` is exempt from WOW64 file system redirection. If Windows denies access when saving, run Notepad as administrator.
