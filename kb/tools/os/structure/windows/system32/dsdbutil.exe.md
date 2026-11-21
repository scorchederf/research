---
created: 2026-11-21
fullpath: 'C:\Windows\System32\dsdbutil.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - active-directory
aliases:
  - dsdbutil.exe
  - dsdbutil
url:
  - https://learn.microsoft.com/exchange/modify-ad-lds-configuration-exchange-2013-help
---

**fullpath**:C:\Windows\System32\dsdbutil.exe

# description

dsdbutil is an AD LDS management tool intended for use only by experienced administrators. Exchange Server's ConfigureAdam.ps1 script invokes dsdbutil to change AD LDS settings (LDAP/SSL ports, log and database paths) on Edge Transport servers.

## simple description

> ### 2026-11-21 Claude said
> dsdbutil is a command-line database maintenance tool for Active Directory Lightweight Directory Services (AD LDS), the AD LDS counterpart of ntdsutil. It can change instance ports, move database and log files, check integrity and create snapshots / installation media. It is installed with the AD LDS role or its tools and is menu-driven like ntdsutil.
>
> **SOC NOTE**: Like ntdsutil, it can create IFM/snapshot copies of a directory database that attackers may use for offline credential theft (T1003.003). Use on hosts without AD LDS or outside maintenance windows is suspicious; correlate with Directory Service/ESENT events and new .dit files.
>

# purpose

Manage AD LDS instance configuration and database files, such as ports and file locations (used by Exchange Edge Transport via ConfigureAdam.ps1).

# typical use cases

- Change AD LDS LDAP/SSL ports or move data/log paths (Exchange Edge Transport, via ConfigureAdam.ps1).

# options

_Not documented on Microsoft Learn at 2026/11/21 05:51 UTC_
