---
created: 2026-11-21
fullpath: 'C:\Windows\System32\runas.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - runas.exe
  - Runas
  - Run as
url:
  - https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771525(v=ws.11)
  - https://learn.microsoft.com/sysinternals/downloads/shellrunas
---

**fullpath**:C:\Windows\System32\runas.exe

# description

Runas is a built-in Windows command-line tool that runs programs, MMC consoles, shortcuts and Control Panel items under different credentials than the current logon. It depends on the Secondary Logon service; Sysinternals ShellRunas provides similar functionality from the Explorer context menu.

## simple description

> ### 2026-11-21 Claude said
> Runas lets you start a program as a different user without logging off, for example opening an admin console with an admin account while logged in as a normal user. It prompts for the other account's password. With `/netonly` the program runs locally as you but uses the other credentials only for network access. It needs the Secondary Logon service to be running.
>
> **SOC NOTE**: Attackers use runas (especially `/netonly` and `/savecred`) to use stolen credentials or saved credentials for lateral movement and privilege escalation (MITRE ATT&CK T1134.002, T1078). Runas generates logon events 4648 (explicit credentials) and 4624 logon type 9 (NewCredentials) for `/netonly`, or type 2 otherwise, with seclogo as the logon process. `/savecred` stores credentials in Credential Manager, which can be reused later without a password.
>

# purpose

Allows a user to run specific tools and programs with different permissions than the current logon provides, so administrators can use a restricted account for routine work and a privileged account only when needed. Group Policy is not processed for the user whose credentials are supplied. If runas fails, the Secondary Logon service may not be running or the account may be invalid.

# typical use cases

| usage | description |
| --- | --- |
| `runas /user:<localmachinename>\administrator cmd` | Start a command prompt as the local administrator. |
| `runas /user:contoso\domainadmin "mmc %windir%\system32\compmgmt.msc"` | Start Computer Management with a domain admin account. |
| `runas /user:jayj@domain.contoso.com "notepad my_file.txt"` | Start Notepad with a file as another domain user. |
| `runas /netonly /user:<Domain>\<User_Name> "<Command>"` | Run a tool that administers a server in another forest, using the credentials for remote access only. |

# options

| option | description |
| --- | --- |
| `/profile` | Loads the user's profile (default). Cannot be used with `/netonly`. |
| `/no profile` | Does not load the user's profile; faster, but some applications may malfunction. |
| `/env` | Uses the current network environment instead of the user's local environment. |
| `/netonly` | The specified user information is for remote access only. Cannot be used with `/profile`. |
| `/savecred` | Uses credentials previously saved by this user. Cannot be used with `/smartcard`; ignored on Home/Starter editions. |
| `/smartcard` | Credentials are supplied from a smartcard. Cannot be used with `/savecred`. |
| `/showtrustlevels` | Displays the trust levels that can be used as arguments to `/trustlevel`. |
| `/trustlevel` | Specifies the level of authorization at which the application runs. |
| `/user:<UserAccountName> "<ProgramName> <PathToProgramFile>"` | Account (`User@Domain` or `Domain\User`) to run the program as, and the program to run. |
| `/?` | Displays help at the command prompt. |
