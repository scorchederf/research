---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Roaming\Microsoft\Outlook\VbaProject.OTM'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - VbaProject.OTM
  - Project1
url:
  - https://learn.microsoft.com/troubleshoot/outlook/deployment/manage-distribute-outlook-vba-project
  - https://learn.microsoft.com/office/vba/outlook/concepts/getting-started/using-visual-basic-for-applications-in-outlook
  - https://learn.microsoft.com/troubleshoot/outlook/deployment/macros-in-this-project-disabled-outlook
---

**fullpath**:C:\Users\<username>\AppData\Roaming\Microsoft\Outlook\VbaProject.OTM

# description

VbaProject.OTM is the per-user file in which Microsoft Outlook stores its single VBA project (Project1). Outlook supports only one VBA project at a time; the file is a product storage file not meant for distribution, and Microsoft recommends COM/VSTO or Office add-ins for distributing solutions.

## simple description

> ### 2026-11-21 Claude said
> This file holds all the VBA macros a user has written in Outlook's Visual Basic Editor. Outlook loads it at startup from the user's roaming profile, so macros follow the user. Code in ThisOutlookSession can react to events such as new mail arriving. Most users never have one.
>
> **SOC NOTE**: Known persistence technique (T1137 Office Application Startup, used by APT32 and in Ruler-style attacks): malicious code in ThisOutlookSession runs on Outlook start or on incoming mail, enabling email-triggered C2. Investigate creation/modification of this file, related LoadMacroProviderOnBoot/macro security registry changes, and examine its VBA with olevba.
>

# purpose

Stores the user's Outlook VBA project. To start a new project or switch projects, exit Outlook, rename VbaProject.otm, optionally rename another file to VbaProject.otm, and restart. Projects can be moved between computers by copying the file, though Microsoft does not support deploying solutions that way. Manually saving via **File > Save VbaProject.OTM** is needed to keep a digital signature assigned to macros.
