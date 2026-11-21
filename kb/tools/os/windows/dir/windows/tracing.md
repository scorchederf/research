---
created: 2026-11-21
fullpath: 'C:\Windows\tracing'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - tracing
  - rras
aliases:
  - tracing
  - %systemroot%\tracing
url:
  - https://learn.microsoft.com/windows/win32/eaphost/enabling-tracing
  - https://learn.microsoft.com/windows-server/administration/windows-commands/netsh-ras
---

**fullpath**:C:\Windows\tracing

# description

`%systemroot%\tracing` is the folder where Routing and Remote Access Service (RRAS) trace logs are written when RAS tracing is enabled with `netsh ras`. It relates to netsh ras diagnostics and EAPHost tracing.

## simple description

> ### 2026-11-21 Claude said
> C:\Windows\tracing is a Windows folder that holds plain-text trace logs from networking components, mainly Remote Access / RRAS and VPN pieces (rasman, rasppp, raseap, etc.). It is usually empty or small unless tracing was turned on for troubleshooting. Admins enable it with netsh ras commands and read the .LOG files afterward.
>
> **SOC NOTE**: Trace logs here can reveal VPN/dial-up connection attempts, usernames, authentication methods and remote endpoints, which helps reconstruct remote-access activity. The folder is writable by some services and has historically been used as a staging location by malware; unexpected executables or scripts in it are suspicious (T1074 Data Staged, T1036 Masquerading).
>

# purpose

Stores RAS traces. Enable RRAS tracing from an elevated prompt with `netsh ras set tr * en`, view traces in `%systemroot%\tracing`, and disable with `netsh ras set tr * dis`. `netsh ras diagnostics set rastracing` enables extended tracing per RRAS component (rasman, rasppp, rasauth, rasip, rasl2tp, raspptp, rassstp, rasgre, raseap, rasqec, rasmobility, rascustom) or all with `state=*`.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_
