---
created: 2026-11-21
fullpath: 'C:\Windows\Installer'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - windows-installer
  - msi
aliases:
  - Installer
  - Windows Installer cache
  - %windir%\Installer
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/application-management/missing-windows-installer-cache
  - https://learn.microsoft.com/troubleshoot/sql/database-engine/install/windows/restore-missing-windows-installer-cache-files
---

**fullpath**:C:\Windows\Installer

# description

The Windows Installer cache (`%windir%\Installer`), a hidden folder where Windows Installer stores stripped copies of `.msi` packages and `.msp` patches for installed products. These cached files are needed to uninstall, repair and update products, are unique per computer and must not be deleted or copied between machines.

## simple description

> ### 2026-11-21 Claude said
> When software is installed with an MSI, Windows keeps a copy of the installer database (with a random name like `19b4d2.msi`) and any patches here. Windows uses them later for repair, update and uninstall. The folder can grow large, but deleting files manually breaks future updates. It is hidden and protected.
>
> **SOC NOTE**: Attackers can drop or run malicious MSI packages (MITRE ATT&CK T1218.007 Msiexec), and cached MSIs in this folder can be abused for repair-based privilege escalation attacks (e.g. MSI repair spawning elevated processes). Unexpected new `.msi` files here show what was installed and when, which is useful for timelining.
>

# purpose

Stores cached `.msi` and `.msp` files that future product updates rely on for the required transformations. Windows automatically manages this directory; manual changes can cause errors like a missing cached MSI or patch file during updates.

# common files found

| file | description |
| --- | --- |
| `<random>.msi` | Stripped copy of the original Windows Installer database for an installed product. |
| `<random>.msp` | Cached Windows Installer patch (hotfix, cumulative update, service pack). |
