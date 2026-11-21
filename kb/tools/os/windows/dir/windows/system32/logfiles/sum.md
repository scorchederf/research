---
created: 2026-11-21
fullpath: 'C:\Windows\System32\LogFiles\Sum'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - windows-server
  - user-access-logging
aliases:
  - Sum
  - SUM
  - User Access Logging database
url:
  - https://learn.microsoft.com/windows-server/administration/user-access-logging/manage-user-access-logging
  - https://learn.microsoft.com/windows-server/administration/user-access-logging/get-started-with-user-access-logging
  - https://learn.microsoft.com/troubleshoot/windows-server/performance/esent-event-327-326
  - https://learn.microsoft.com/troubleshoot/sql/analysis-services/error-1032-application-log
---

**fullpath**:C:\Windows\System32\LogFiles\Sum

# description

The `Sum` folder holds the database and supporting files of User Access Logging (UAL), a Windows Server feature that aggregates client usage data by role and product on the local server. UAL is installed and enabled by default and stores its data with the Extensible Storage Engine (ESE); the data is read back through WMI (`root\AccessLogging`) or the UAL PowerShell cmdlets.

## simple description

> ### 2026-11-21 Claude said
> This folder is where Windows Server keeps a small database recording which users and client devices (by IP address) used services on the server, such as file shares, DHCP or Active Directory. The service that writes it is called User Access Logging and it runs by default on Windows Server 2012 and later. Records can go back up to two years. It is not present on Windows client editions.
>
> **SOC NOTE**: UAL databases (`Current.mdb`, `{GUID}.mdb`, `SystemIdentity.mdb`) are a high-value DFIR artifact for lateral movement: they show which accounts and source IPs accessed a server per day, even when Security logs have rolled over. Parse them offline (ESE format) with tools such as KStrike or SumECmd. Deletion of the folder contents or stopping the `UALSVC` service may indicate anti-forensics (T1070 Indicator Removal).
>

# purpose

Stores the UAL ESE database and logs. UAL keeps up to two years of history: the active database `current.mdb` is copied every 24 hours to a file named *GUID*.mdb for the WMI provider, and a new *GUID*.mdb is created on the first day of each year. If UAL cannot start with the existing ESE files, it deletes all files in this folder and starts fresh. Administrators may manually delete all files in the folder after stopping the User Access Logging Service; all files must be backed up together for a restore to work.

# common files found

| file | description |
| --- | --- |
| `current.mdb` | Active UAL database. |
| `<GUID>.mdb` | Daily copy of the active database used by the WMI provider; one per year is retained as an archive for up to two years. |
| `Api.log` / `Api.chk` | ESE transaction log and checkpoint files (named in SQL Server error 1032 troubleshooting). |
