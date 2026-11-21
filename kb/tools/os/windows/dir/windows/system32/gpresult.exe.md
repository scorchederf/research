---
created: 2026-11-21
fullpath: 'C:\Windows\System32\gpresult.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - group-policy
aliases:
  - gpresult.exe
  - gpresult
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/gpresult
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/use-resultant-set-of-policy-logging
---

**fullpath**:C:\Windows\System32\gpresult.exe

# description

gpresult displays the Resultant Set of Policy (RSoP) information for a remote user and computer. It is a built-in Windows command. Starting with Windows Vista SP1, the RSoP report (Rsop.msc) does not show all Group Policy settings, so Microsoft recommends gpresult to see the full set; the PowerShell equivalent is `Get-GPResultantSetOfPolicy`.

## simple description

> ### 2026-11-21 Claude said
> gpresult.exe is a built-in Windows command-line tool that shows which Group Policy settings actually applied to a computer and to a user. It lists the GPOs that were applied or filtered out, the security groups the user belongs to, and the resulting settings. Administrators use it to troubleshoot why a policy is or is not taking effect. It can query the local machine or a remote one and export reports to HTML or XML.
>
> **SOC NOTE**: Attackers run `gpresult /r` or `/z` for domain and group-membership discovery (MITRE ATT&CK T1615 Group Policy Discovery). Look for gpresult launched from unusual parents (Office apps, script hosts, web shells) or in bursts with whoami, net, nltest. Process creation events (Security 4688, Sysmon 1) capture the command line.
>

# purpose

Displays the resulting set of policy settings that were enforced on the computer for the specified user when the user signed in. Group Policy is applied to users or computers based on membership in sites, domains, or organizational units, and overlapping settings produce a resulting set that gpresult reports.

# typical use cases

| usage | description |
| --- | --- |
| `gpresult /s srvmain /user maindom\targetuser /scope user /r` | Retrieve RSoP data for only the remote user maindom\targetuser on computer srvmain. |
| `gpresult /s srvmain /user maindom\targetuser /z > policy.txt` | Save all available Group Policy information for the remote user to policy.txt. |
| `gpresult /s srvmain /u maindom\hiropln /p p@ssW23 /r` | Display RSoP data for the signed-in user with explicit credentials on srvmain. |

# options

| option | description |
| --- | --- |
| `/s <system>` | Name or IP address of a remote computer (no backslashes). Default is the local computer. |
| `/u <username>` | Uses the credentials of the specified user to run the command. |
| `/p [<password>]` | Password for the /u account; prompts if omitted. Can't be used with /x or /h. |
| `/user [<targetdomain>\]<targetuser>` | Remote user whose RSoP data is displayed. |
| `/scope {user \| computer}` | Displays RSoP data for either the user or the computer; both if omitted. |
| `[/x \| /h] <filename>` | Saves the report in XML (/x) or HTML (/h). Can't be used with /u, /p, /r, /v, or /z. |
| `/f` | Forces gpresult to overwrite the file named in /x or /h. |
| `/r` | Displays RSoP summary data. |
| `/v` | Displays verbose policy information, including settings applied with a precedence of 1. |
| `/z` | Displays all available Group Policy information, including settings applied with a precedence of 1 and higher. |
| `/?` | Displays help at the command prompt. |
