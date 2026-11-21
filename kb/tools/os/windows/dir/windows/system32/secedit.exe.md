---
created: 2026-11-21
fullpath: 'C:\Windows\System32\secedit.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - security-policy
  - configuration
aliases:
  - 'secedit.exe'
  - 'secedit'
  - 'Security Configuration and Analysis'
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/secedit
  - https://learn.microsoft.com/windows-server/administration/windows-commands/secedit-analyze
  - https://learn.microsoft.com/windows-server/administration/windows-commands/secedit-configure
  - https://learn.microsoft.com/windows-server/administration/windows-commands/secedit-export
  - https://learn.microsoft.com/windows-server/administration/windows-commands/secedit-import
  - https://learn.microsoft.com/windows-server/administration/windows-commands/secedit-generaterollback
---

**fullpath**:C:\Windows\System32\secedit.exe

# description

`secedit.exe` configures and analyzes system security by comparing the current configuration against security templates stored in a database (.sdb). It is the command-line counterpart of the Security Configuration and Analysis and Security Templates MMC snap-ins.

## simple description

> ### 2026-11-21 Claude said
> Secedit can export, import, apply and compare local security policy: password and lockout policy, audit policy, user rights, restricted groups, registry/file permissions and service security. Admins use it to back up or apply hardening templates. Its exports are plain .inf text files.
>
> **SOC NOTE**: Attackers use `secedit /export /cfg` for discovery of password/lockout and user-rights policy (T1201, T1082), and `secedit /configure` to weaken settings, e.g. grant SeDebugPrivilege or disable auditing (T1484 / T1562.002). Review process creation with /configure or /import, and check %windir%\security\logs\scesrv.log for applied changes.
>

# purpose

Configures and analyzes system security by comparing your current security configuration against specified security templates. Analysis results are stored in a separate area of the database viewable in the Security Configuration and Analysis snap-in. Files created include `scesrv.log` in `%windir%\security\logs` (overwritten by analyze, configure, export or import), .sdb databases, .log files and .inf templates.

# typical use cases

| usage | description |
| --- | --- |
| `secedit /analyze /db C:\Security\FY11\SecDbContoso.sdb /log C:\Security\FY11\SecAnalysisContosoFY11.log` | Analyze security parameters against the database and log the output. |
| `secedit /configure /db C:\Security\FY11\SecDbContoso.sdb /cfg SecContoso.inf /overwrite /log C:\Security\FY11\SecAnalysisContosoFY11.xml /quiet` | Apply the settings from *SecContoso.inf* without prompting. |
| `secedit /export /db C:\Security\FY11\SecDbContoso.sdb /mergedpolicy /cfg SecContoso.inf /log C:\Security\FY11\SecAnalysisContosoFY11.log /quiet` | Export the database and domain policies to an .inf file. |
| `secedit /import /db C:\Security\FY12\SecDbContoso.sdb /cfg SecContoso.inf /areas securitypolicy /log C:\Security\FY11\SecAnalysisContosoFY12.log /quiet` | Import only the security policies portion of a template into another database. |
| `secedit /generaterollback /db C:\Security\FY11\SecDbContoso.sdb /cfg sectmplcontoso.inf /rbk sectmplcontosoRBK.inf /log C:\Security\FY11\SecAnalysisContosoFY11.log` | Create a rollback template for a configuration template. |

# options

| option | description |
| --- | --- |
| `/analyze` | Analyze current system settings against baseline settings stored in a database. |
| `/configure` | Configure the system with security settings stored in a database. |
| `/export` | Export security settings stored in a database. |
| `/generaterollback` | Generate a rollback template with respect to a configuration template. |
| `/import` | Import a security template into a database for applying or analysis. |
| `/validate` | Validate the syntax of a security template. |
| `/db` | Path and file name of the database containing the stored configuration (required for analyze/configure). |
| `/cfg` | Path and file name of the security template to import into the database. |
| `/overwrite` | Overwrite the stored template instead of appending; only with `/cfg`. |
| `/areas` | Security areas to apply/export: securitypolicy, group_mgmt, user_rights, regkeys, filestore, services. |
| `/mergedpolicy` | Merge and export domain and local policy security settings (export). |
| `/log` | Path and file name of the log file. |
| `/quiet` | Suppress screen (and log) output. |
