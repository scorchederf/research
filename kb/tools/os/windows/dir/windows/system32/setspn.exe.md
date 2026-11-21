---
created: 2026-11-21
fullpath: 'C:\Windows\System32\setspn.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - active-directory
aliases:
  - setspn.exe
  - Setspn
url:
  - https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731241(v=ws.11)
---

**fullpath**:C:\Windows\System32\setspn.exe

# description

`setspn` reads, modifies and deletes the Service Principal Names (SPN) directory property of an Active Directory service account. It is available when the AD DS server role (or RSAT tools) is installed and runs from an elevated command prompt.

## simple description

> ### 2026-11-21 Claude said
> setspn manages Service Principal Names, the identifiers Kerberos uses to find which account runs a service (for example `MSSQLSvc/sql01.contoso.com`). Admins use it to list, add, remove or find duplicate SPNs. Any domain user can list SPNs; changing them needs delegated rights.
>
> **SOC NOTE**: `setspn -T <domain> -Q */*` is classic Kerberoasting reconnaissance to find user accounts with SPNs (T1558.003, T1087.002). Adding an SPN to an account you control enables targeted Kerberoasting. Watch process creation with `-Q`/`-T`, Directory Service Changes event 5136 on `servicePrincipalName`, and spikes of 4769 TGS requests with RC4 encryption.
>

# purpose

Views current SPNs, resets an account's default SPNs, adds or deletes supplemental SPNs, and searches for duplicates. SPN format is `serviceclass/host:port/servicename`. Modifying SPNs requires Domain Admins, Enterprise Admins or the delegated **Validated write to service principal name** permission.

# typical use cases

| usage | description |
| --- | --- |
| `setspn -l daserver1` | List SPNs registered for computer daserver1. |
| `setspn -r daserver1` | Reset default HOST SPNs for daserver1. |
| `setspn -s http/daserver1.reskit.contoso.com daserver1` | Add an SPN after checking for duplicates. |
| `setspn -d http/daserver1.reskit.contoso.com daserver1` | Remove an SPN. |
| `setspn -U -S http/daserver dauser` | Register an SPN on user account dauser. |
| `setspn -T * -T contoso -X` | Report duplicate SPNs in this domain and contoso. |
| `setspn -T contoso -F -Q */daserver` | Find all SPNs of the form */daserver in the forest. |

# options

| option | description |
| --- | --- |
| `<Computer>` | Active Directory account object to configure, normally the computer's NetBIOS name. |
| `-l` | Lists registered SPNs for the account. |
| `-r` | Resets the default SPN registrations for the host names. |
| `-d <SPN>` | Deletes the specified SPN. |
| `-s <SPN>` | Adds the SPN after verifying no duplicates exist. |
| `-A` | Adds SPNs without the duplicate check; use `-S` instead. |
| `-?` | Displays help (default). |
| `-C` | Specifies that accountname is a computer account. |
| `-U` | Specifies that accountname is a user account. |
| `-X` | Searches for duplicate SPNs. |
| `-Q` | Queries for SPNs matching a pattern on each target. |
| `-F` | Performs queries at the forest rather than domain level. |
| `-T` | Performs the query on the specified domain or forest; `""` or `*` means current. Can be repeated. |
