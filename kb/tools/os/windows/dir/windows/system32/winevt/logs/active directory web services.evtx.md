---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\Active Directory Web Services.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - eventlog
  - active-directory
  - adws
aliases:
  - Active Directory Web Services.evtx
  - ADWS event log
  - ADWS Instance Events
url:
  - https://learn.microsoft.com/windows-server/identity/ad-ds/manage/virtual-dc/virtualized-domain-controller-troubleshooting
  - https://learn.microsoft.com/troubleshoot/windows-server/active-directory/specify-server-port-active-directory-powershell-cmdlet
  - https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-health-alert-catalog
---

**fullpath**:C:\Windows\System32\winevt\Logs\Active Directory Web Services.evtx

# description

Event log file for the Active Directory Web Services (ADWS) service on domain controllers and AD LDS servers. ADWS (TCP 9389) is the service that most Active Directory PowerShell module cmdlets connect to; it connects to the local directory instance on their behalf. Its events (source ADWS Instance Events) are visible in Event Viewer.

## simple description

> ### 2026-11-21 Claude said
> This is the event log written by Active Directory Web Services, the service on a domain controller that the Active Directory PowerShell module and AD Administrative Center talk to on port 9389. It records the service starting, loading its configuration, servicing the directory instance (NTDS or an AD LDS instance) and certificate problems. It only exists on servers running AD DS or AD LDS.
>
> **SOC NOTE**: Shows ADWS availability, which matters because AD PowerShell enumeration (Get-ADUser, Get-ADComputer) and tools like SharpHound/ADExplorer alternatives (e.g. SOAPHound) use ADWS on 9389 for reconnaissance (T1087.002, T1482). The log itself rarely records individual queries, so correlate with network logs of 9389 connections and Security 4624 logons. A stopped ADWS service (alerted by Entra Connect Health) breaks AD PowerShell management.
>

# purpose

Records ADWS service events. Documented events (source ADWS Instance Events): 1000 ADWS is starting; 1008 ADWS has reduced its security privileges; 1100 the <appsettings> section of the configuration file loaded without errors; 1200 ADWS is now servicing the specified directory instance (e.g. NTDS, LDAP 389, SSL 636); 1202 the computer hosts the directory instance but ADWS couldn't service it and will retry; 1400 ADWS couldn't find a server certificate with the specified name, required for SSL/TLS. If ADWS is stopped or disabled, clients such as Active Directory PowerShell can't manage directory instances on that server (`net start adws` restarts it).
