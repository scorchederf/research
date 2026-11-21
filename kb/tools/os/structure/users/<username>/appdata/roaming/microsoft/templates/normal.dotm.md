---
created: 2026-11-21
fullpath: 'C:\Users\<username>\AppData\Roaming\Microsoft\Templates\Normal.dotm'
generator:
  - claude
  - microsoftlearn
tags:
  - office
  - file
  - word
aliases:
  - Normal.dotm
  - Normal template
  - global template
url:
  - https://learn.microsoft.com/answers/a/12408553
  - https://learn.microsoft.com/office/dev/add-ins/word/word-add-ins-troubleshooting
  - https://learn.microsoft.com/office/vba/word/concepts/miscellaneous/modifying-a-word-command
---

**fullpath**:C:\Users\<username>\AppData\Roaming\Microsoft\Templates\Normal.dotm

# description

Normal.dotm is Microsoft Word's global template, stored per user in `%appdata%\Microsoft\Templates`. Every new blank document is based on it, and it holds default fonts, margins, styles and global macros. The user templates location can be customized under File > Options > Advanced > File Locations.

## simple description

> ### 2026-11-21 Claude said
> Normal.dotm is the macro-enabled template Word loads every time it starts and uses for every new blank document. When users click "Set as Default" for fonts or styles, Word saves the change here. It can also hold VBA macros that are available in every document. If it is deleted or renamed, Word simply recreates a clean one.
>
> **SOC NOTE**: Because its macros load on every Word launch, Normal.dotm is a known persistence location (MITRE ATT&CK T1137.001 Office Application Startup: Office Template Macros), e.g. an AutoExec/AutoOpen macro injected by malware. Watch for writes to Normal.dotm by processes other than winword.exe, unusual size growth, or presence of a vbaProject.bin inside it; extract and inspect with olevba. Its modification time can help timeline user/attacker activity.
>

# purpose

The global template used as the base for new blank documents. Changes such as Set As Default update Normal.dotm; macros saved to "Normal.dot (Global Template)" (e.g. a FileSave override) apply to all documents using the Normal template. If it becomes corrupted, renaming it (e.g. Normal.old) with Word closed causes Word to create a fresh default copy.
