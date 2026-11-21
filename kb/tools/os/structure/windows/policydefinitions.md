---
created: 2026-11-21
fullpath: 'C:\Windows\PolicyDefinitions'
generator:
  - claude
  - microsoftlearn
tags:
  - directory
  - group-policy
aliases:
  - PolicyDefinitions
  - %SystemRoot%\PolicyDefinitions
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/group-policy/create-and-manage-central-store
  - https://learn.microsoft.com/troubleshoot/windows-server/group-policy/group-policy-settings-show-as-extra-registry-settings
  - https://learn.microsoft.com/windows/client-management/understanding-admx-backed-policies
---

**fullpath**:C:\Windows\PolicyDefinitions

# description

Local store of Group Policy Administrative Template files (.admx) and language-specific .adml files shipped with Windows. It is the source for building the domain Central Store in SYSVOL and is used by Group Policy editors when no Central Store exists or when `EnableLocalStoreOverride` is set.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the template files that define the settings you see under Administrative Templates in the Group Policy editor. .admx files describe the settings and registry keys; .adml files in language subfolders (like en-US) hold the display text. Admins copy this folder to the domain SYSVOL to make a Central Store.
>
> **SOC NOTE**: Template files only describe settings and do not apply policy, but tampering can mislead admins or break editing. Third-party ADMX files dropped here show installed software. Policy actually applied lives in Registry.pol/registry, not here.
>

# purpose

Provides the inbox ADMX/ADML definitions; inbox ADMX files are also processed into MDM Policy CSP policies. Replacing files here with ADMX download packages is not supported.

# common files found

- `*.admx` - language-neutral policy definition files
- `<culture>\*.adml` (e.g. `en-US\`) - language-specific resource files
