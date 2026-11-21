---
created: 2026-11-21
fullpath: 'C:\Windows\SYSVOL\domain\Policies\PolicyDefinitions'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - grouppolicy
  - activedirectory
aliases:
  - PolicyDefinitions
  - Central Store
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/group-policy/create-and-manage-central-store
  - https://learn.microsoft.com/fslogix/how-to-use-group-policy-templates
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/group-policy-settings-show-as-extra-registry-settings
---

**fullpath**:C:\Windows\SYSVOL\domain\Policies\PolicyDefinitions

# description

This folder on a domain controller is the Group Policy Central Store for Administrative Templates (.admx and .adml files). It is reached over the network as `\\<domain>\SYSVOL\<domain>\Policies\PolicyDefinitions` and replicates to all domain controllers in the domain. Group Policy tools (GPMC, Group Policy Management Editor) use it instead of the local `C:\Windows\PolicyDefinitions` folder.

## simple description

> ### 2026-11-21 Claude said
> This folder on a domain controller holds the template files that describe every Group Policy setting admins can configure. The `.admx` files define the settings and the language folders (like `en-US`) hold `.adml` files with the display text. It only changes what admins see in the policy editor, not what is applied to computers. It is copied to every domain controller through SYSVOL replication.
>
> **SOC NOTE**: Templates are not executed, so this folder is low risk on its own, but SYSVOL write access is a domain-admin-level privilege; unexpected changes here can show an attacker exploring or altering the GPO environment (T1484.001). Watch for new non-ADMX files (scripts, executables) in SYSVOL, which every domain member can read.
>

# purpose

Gives all Group Policy administrators in the domain the same, up-to-date set of Administrative Templates. Learn recommends building a new folder (for example `PolicyDefinitions-24H2`) from a current Windows client's `C:\Windows\PolicyDefinitions`, merging application ADMX files, then renaming it to production so the old version can be restored. Setting `EnableLocalStoreOverride` = 1 under `HKLM\SOFTWARE\Policies\Microsoft\Windows\Group Policy` makes the editor use the local store instead.

# common files found

| file | description |
| --- | --- |
| `*.admx` | Language-neutral Administrative Template files (for example `fslogix.admx`, `Microsoft-Windows-Geolocation-WLPAdm.admx`). |
| `<culture>\*.adml` | Language-specific resource files in folders such as `en-US` or `ko-KR`. |
