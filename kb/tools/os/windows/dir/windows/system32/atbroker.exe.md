---
created: 2026-11-21
fullpath: 'C:\Windows\System32\Atbroker.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - accessibility
  - lolbin
aliases:
  - "Atbroker.exe"
  - "AtBroker"
  - "Assistive Technology Broker"
url: []
---

**fullpath**:C:\Windows\System32\Atbroker.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

## simple description

> ### 2026-11-21 Claude said
> AtBroker.exe is the Windows Assistive Technology broker that starts accessibility tools (Narrator, Magnifier, On-Screen Keyboard and registered third-party AT apps) and moves them between the normal desktop and the secure/logon desktop. It is launched by Windows when the user starts an accessibility feature from the Ease of Access settings or the logon screen. Registered assistive technologies are described under `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Accessibility\ATs`.
>
> **SOC NOTE**: AtBroker is a known LOLBin: `atbroker.exe /start <name>` launches any program registered as an AT under the `Accessibility\ATs` key, giving proxy execution and persistence, including at the logon screen as SYSTEM-adjacent context (T1218, T1546.008 Accessibility Features). Watch for new `ATs` subkeys and the `Configuration` value in `HKCU\...\Accessibility`, and for AtBroker spawning unusual children.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_
