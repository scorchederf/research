---
created: 2026-11-21
fullpath: 'C:\Windows\System32\CodeIntegrity'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - code-integrity
  - wdac
aliases:
  - CodeIntegrity
  - Code Integrity policy folder
url:
  - https://learn.microsoft.com/windows-insider/archive/new-in-rs5-server
  - https://learn.microsoft.com/windows-hardware/drivers/install/code-integrity-event-log-messages
  - https://learn.microsoft.com/windows-hardware/drivers/install/viewing-code-integrity-events
---

**fullpath**:C:\Windows\System32\CodeIntegrity

# description

Folder used by Code Integrity, the kernel-mode component that implements driver signature verification and Windows Defender Application Control (WDAC, also known as Code Integrity policy). Microsoft Learn shows a default CI policy being deployed by copying it to `C:\Windows\System32\CodeIntegrity\SiPolicy.p7b`; Code Integrity events are viewed in Event Viewer under Applications and Services Logs > Microsoft > Windows > CodeIntegrity.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the Code Integrity / App Control for Business (WDAC) policy files that tell Windows which drivers and programs are allowed to run. The classic single policy is `SiPolicy.p7b`; newer multi-policy systems also use a `CiPolicies\Active` subfolder with `{GUID}.cip` files. Windows reads these at boot and enforces them in the kernel. Changing them normally requires admin rights and a reboot.
>
> **SOC NOTE**: Attackers with admin rights can drop a malicious WDAC policy here to block EDR/AV drivers from loading (a known EDR-killing technique, MITRE ATT&CK T1562.001 Impair Defenses). Watch for unexpected writes of `SiPolicy.p7b` or `*.cip` files, and correlate with CodeIntegrity Operational events (e.g. 3076/3077 audit/block, 3099 policy activated).
>

# purpose

Stores Code Integrity (WDAC) policy binaries that the Code Integrity service loads at boot. For example, a default policy is deployed by copying it to `SiPolicy.p7b` in this folder and rebooting so the code integrity service loads the policy.

# common files found

| file | description |
| --- | --- |
| `SiPolicy.p7b` | Code Integrity policy binary; the default CI policy is copied here and loaded after reboot. |
