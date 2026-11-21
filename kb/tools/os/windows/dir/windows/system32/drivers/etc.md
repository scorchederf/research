---
created: 2026-11-21
fullpath: 'C:\Windows\System32\drivers\etc'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - networking
  - dns
aliases:
  - etc
  - drivers\etc
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/cannot-modify-hosts-lmhosts-files
  - https://learn.microsoft.com/troubleshoot/windows-client/networking/troubleshoot-dns-client-resolution-issues
  - https://learn.microsoft.com/windows/powertoys/hosts-file-editor
---

**fullpath**:C:\Windows\System32\drivers\etc

# description

The `%SystemRoot%\System32\drivers\etc` folder holds the Windows TCP/IP name-resolution configuration files, most notably the `hosts` file (no extension) and the `Lmhosts` file. Editing these files requires administrative rights; the PowerToys Hosts File Editor also stores its `hosts` backups here by default.

## simple description

> ### 2026-11-21 Claude said
> This folder contains small text files that Windows networking reads, inspired by the Unix `/etc` directory. The best known is `hosts`, which maps host names to IP addresses before DNS is asked. Others include `lmhosts.sam`, `networks`, `protocol` and `services`. Only administrators can change them.
>
> **SOC NOTE**: Attackers modify `hosts` to redirect or block domains (e.g., blocking AV/EDR update servers or redirecting banking sites) — MITRE ATT&CK T1565.001 / T1562.001. Monitor file write events on `hosts` (Sysmon 11, FIM), compare against the default commented-only content, and check last-modified timestamps during investigations.

# purpose

Holds the local name-resolution files. The DNS client resolves names by checking its cache, then the Hosts file, then the DNS server; if a name has an entry in `hosts`, the DNS server isn't queried. Windows may deny access to `hosts`/`Lmhosts` unless the editor (e.g., Notepad) is run as administrator.

# common files found

| file | description |
| --- | --- |
| `hosts` | Maps host names to IP addresses, overriding DNS for the local computer. |
| `Lmhosts` | LAN Manager hosts file for NetBIOS name resolution. |
| `hosts_PowerToysBackup_YYYYMMDDHHMMSS` | Backups created by the PowerToys Hosts File Editor. |
