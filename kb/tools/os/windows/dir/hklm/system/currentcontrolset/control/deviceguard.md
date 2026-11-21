---
created: 2026-11-21
fullpath: 'HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - registry
  - vbs
aliases:
  - DeviceGuard
  - Device Guard
  - Virtualization-based security
url:
  - https://learn.microsoft.com/windows/security/hardware-security/enable-virtualization-based-protection-of-code-integrity
  - https://learn.microsoft.com/windows/security/identity-protection/credential-guard/configure
  - https://learn.microsoft.com/windows-hardware/design/device-experiences/oem-vbs
  - https://learn.microsoft.com/windows-hardware/customize/desktop/unattend/microsoft-windows-deviceguard-unattend-enablevirtualizationbasedsecurity
---

**fullpath**:HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard

# description

This key holds the local configuration for virtualization-based security (VBS) and memory integrity (hypervisor-protected code integrity, HVCI). Device Guard is no longer used as a product name except to locate memory integrity and VBS settings in Group Policy or the registry. The same settings can be set through Group Policy (`SOFTWARE\Policies\Microsoft\Windows\DeviceGuard`), the DeviceGuard Policy CSP, or the Microsoft-Windows-DeviceGuard-Unattend component.

## simple description

> ### 2026-11-21 Claude said
> This registry key turns on and configures Virtualization-Based Security, a Windows feature that uses the hypervisor to create an isolated memory area the normal kernel cannot touch. Features such as Credential Guard and memory integrity (HVCI) run inside that protected area. The values here say whether VBS is on, which hardware protections are required, and whether the setting is locked with UEFI. Changes take effect after a reboot.
>
> **SOC NOTE**: Attackers with admin rights may set `EnableVirtualizationBasedSecurity` or HVCI `Enabled` to 0 to disable Credential Guard/HVCI before credential dumping or loading vulnerable drivers (MITRE ATT&CK T1562.001 Impair Defenses, prerequisite for T1003.001 and BYOVD T1068). Monitor Sysmon Event ID 13 on this key, compare with `Win32_DeviceGuard` WMI state, and note that a UEFI lock (`Locked`=1) prevents simple registry disablement.
>

# purpose

Virtualization-based security uses hardware virtualization and the Windows hypervisor to create an isolated environment that becomes the root of trust of the OS. Windows hosts security solutions there, such as memory integrity, which runs kernel-mode code integrity inside VBS, and Credential Guard. Setting values in this key enables VBS, selects required platform security features, and controls UEFI lock and mandatory mode. Restart the device to apply changes.

# hive

| property | value |
| --- | --- |
| hive | HKLM (HKEY_LOCAL_MACHINE) |
| scope | machine-wide |

# values

| value name | type | description |
| --- | --- | --- |
| `EnableVirtualizationBasedSecurity` | REG_DWORD | 1 enables VBS; 0 (default) disables it. If 0 or absent, other values aren't read and existing BCD settings are used. |
| `RequirePlatformSecurityFeatures` | REG_DWORD | 1 requires Secure Boot; 3 requires Secure Boot and DMA protection (IOMMU). |
| `Locked` | REG_DWORD | 0 enables VBS without UEFI lock; 1 enables VBS with UEFI lock. |
| `Mandatory` | REG_DWORD | 1 enables VBS in mandatory mode; the OS loader won't boot if the hypervisor, Secure Kernel or a dependent module fails to load. |

# subkeys

| subkey | description |
| --- | --- |
| `Scenarios\HypervisorEnforcedCodeIntegrity` | Memory integrity settings: `Enabled` (1 turns it on), `Locked` (UEFI lock) and `WasEnabledBy` (controls whether the UI is grayed out as managed by administrator). |

# query

| usage | description |
| --- | --- |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard"` | List the key's values. |
| `reg query "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard" /s` | List the key, its values and the Scenarios subkeys. |
| `reg add "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard" /v "EnableVirtualizationBasedSecurity" /t REG_DWORD /d 1 /f` | Enable VBS only (no memory integrity). |
| `reg add "HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity" /v "Enabled" /t REG_DWORD /d 1 /f` | Enable memory integrity. |
| `(Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard).SecurityServicesRunning` | Check which VBS security services (such as Credential Guard) are running. |
