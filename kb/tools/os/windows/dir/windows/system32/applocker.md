---
created: 2026-11-21
fullpath: 'C:\Windows\System32\AppLocker'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - AppLocker
url:
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/applocker/applocker-processes-and-interactions
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/operations/appcontrol-debugging-and-troubleshooting
---

**fullpath**:C:\Windows\System32\AppLocker

# description

Folder used by AppLocker. AppLocker policies are enforced through the Application Identity service (appid.sys), which reads and caches the effective AppLocker policy for DLLs and executable files; a policy converter task notifies appid.sys whenever a new policy is applied. Related tools are the Local Security Policy snap-in, Group Policy and the AppLocker PowerShell cmdlets.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the compiled AppLocker policy files that Windows actually enforces, one per rule collection (for example Exe, Dll, Msi, Script, Appx) plus managed installer policy. When Group Policy or MDM delivers AppLocker rules, they are converted and written here for the Application Identity driver to read. Editing them directly is not supported. Admins normally inspect policy with Get-AppLockerPolicy instead.
>
> **SOC NOTE**: File writes here outside policy refresh may indicate tampering to weaken application control (T1562.001). Timestamps show when policy last changed. MANAGEDINSTALLER.APPLOCKER means a managed installer is configured, which attackers may abuse to get files trusted. Stopping the AppIDSvc service is a common bypass.
>

# purpose

Stores the effective AppLocker policy that the Application Identity service evaluates. Microsoft's App Control troubleshooting guidance refers to an AppLocker file called MANAGEDINSTALLER.APPLOCKER that must exist when a managed installer is configured.

# common files found

| file | description |
| --- | --- |
| `MANAGEDINSTALLER.APPLOCKER` | Managed installer AppLocker configuration; if missing, redeploy and enable the managed installer AppLocker configuration. |
