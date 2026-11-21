---
created: 2026-11-21
fullpath: 'C:\Windows\System32\termsrv.dll'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - rdp
aliases:
  - termsrv.dll
  - Termsrv
url:
  - https://learn.microsoft.com/windows/win32/api/_termserv/
  - https://learn.microsoft.com/windows/win32/termserv/about-terminal-services
---

**fullpath**:C:\Windows\System32\termsrv.dll

# description

Termsrv is the Remote Desktop Services (formerly Terminal Services) server component that works with RDP protocol stacks; for example it uses IWRdsWddmIddProps::OnDriverLoad / OnDriverUnload to hand the protocol stack the WDDM ID driver handle. Remote Desktop Services lets multiple users run sessions on an RD Session Host server.

## simple description

> ### 2026-11-21 Claude said
> termsrv.dll is the main library of the Remote Desktop Services service (TermService), loaded into an svchost.exe process. It manages RDP sessions, listeners and concurrent-session limits on the host. Without it running, nobody can connect to the machine over Remote Desktop.
>
> **SOC NOTE**: Attackers patch termsrv.dll (or use RDP Wrapper) to allow multiple concurrent RDP sessions on client Windows, or change `HKLM\SYSTEM\CurrentControlSet\Services\TermService\Parameters\ServiceDll` for persistence/hijack (T1021.001, T1112). Check hash/signature against known good, the ServiceDll value, and RDP logs (4624 type 10, LocalSessionManager 21/24/25, RemoteConnectionManager 1149).
>

# purpose

Provides the server-side Remote Desktop Services functionality used to host remote sessions and coordinate with RDP protocol providers.
