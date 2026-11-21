---
created: 2026-11-21
fullpath: 'C:\Windows\System32\GroupPolicy'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - GroupPolicy
  - Local Group Policy store
url:
  - https://learn.microsoft.com/answers/a/1989780
  - https://learn.microsoft.com/answers/a/2015154
---

**fullpath**:C:\Windows\System32\GroupPolicy

# description

Folder holding the local Group Policy object. Administrative Template settings configured with gpedit.msc are written to Registry.pol files under its Machine and User subfolders, and the Group Policy engine merges them into the registry. Domain GPOs use the equivalent layout under SYSVOL\Policies\{GUID}.

## simple description

> ### 2026-11-21 Claude said
> This hidden folder is where Windows keeps the local Group Policy settings for the computer. Machine settings live under Machine and user settings under User, mainly in Registry.pol files, plus scripts and a gpt.ini version file. gpedit.msc reads and writes these files. Changing the registry directly does not update them.
>
> **SOC NOTE**: Local GPO is a persistence and defense-evasion vector: attackers drop startup/logon scripts under Machine\Scripts or User\Scripts (T1037), or edit Registry.pol to disable Defender or firewall (T1562, T1484.001). Parse Registry.pol and check scripts.ini and gpt.ini timestamps.
>

# purpose

Stores the local Group Policy object. Registry.pol holds Administrative Template settings; Microsoft Q&A answers note that deleting it is typically recreated by `gpupdate /force`, but failed updates should be troubleshot with the error message or `gpresult /h`.

# common files found

| file | description |
| --- | --- |
| `Machine\Registry.pol` | Administrative Template computer configuration settings. |
| `User\Registry.pol` | Administrative Template user configuration settings. |
