---
created: 2026-11-21
fullpath: 'C:\Windows\System32\rdpclip.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - rdp
  - clipboard
aliases:
  - rdpclip.exe
  - RDP Clipboard Monitor
url:
  - https://learn.microsoft.com/azure/virtual-desktop/redirection-configure-clipboard
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-terminalserver
  - https://learn.microsoft.com/troubleshoot/windows-server/remote/copying-2-gb-file-by-clipboard-redirection-fails
  - https://learn.microsoft.com/troubleshoot/azure/virtual-desktop/troubleshoot-device-redirections
---

**fullpath**:C:\Windows\System32\rdpclip.exe

# description

rdpclip.exe is not described by name on Microsoft Learn. Learn documents the Remote Desktop clipboard redirection feature it implements, controlled by the Do not allow Clipboard redirection policy (fDisableClip), and notes that Azure Virtual Desktop's SxS Network Stack uses a separate rdpclipcdv.exe for clipboard.

## simple description

> ### 2026-11-21 Claude said
> rdpclip.exe is the RDP Clipboard Monitor. It starts inside a Remote Desktop session on the remote computer and synchronizes copy and paste (text, images and files) between the local client and the remote session. One instance runs per RDP session under the logged-on user.
>
> **SOC NOTE**: Its presence proves an interactive RDP session (T1021.001) and helps time lateral movement; correlate with Security 4624 logon type 10 and TerminalServices logs. Attackers exfiltrate or stage tools via clipboard file copy (T1115, T1105); disable with fDisableClip. Restarting rdpclip is a common fix when clipboard breaks.
>

# purpose

Clipboard redirection shares clipboard contents between the remote computer and the client during a Remote Desktop Services session; it is allowed by default. It is disabled by the policy Computer Configuration > Administrative Templates > Windows Components > Remote Desktop Services > Remote Desktop Session Host > Device and Resource Redirection > Do not allow Clipboard redirection (registry `SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services`, value `fDisableClip`), or on the client with `HKLM\Software\Microsoft\Terminal Server Client` `DisableClipboardRedirection` = 1. Disabling drive redirection also blocks file transfer via the clipboard, and copying files larger than 2 GB through the clipboard fails silently.

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 18:48 UTC_
