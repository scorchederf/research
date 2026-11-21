---
created: 2026-11-21
fullpath: 'C:\Windows\System32\Printing_Admin_Scripts\en-US\pubprn.vbs'
generator:
  - claude
  - microsoftlearn
tags:
  - file
  - script
  - printing
aliases:
  - pubprn.vbs
  - pubprn
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/pubprn
---

**fullpath**:C:\Windows\System32\Printing_Admin_Scripts\en-US\pubprn.vbs

# description

pubprn is a Visual Basic script in `%WINdir%\System32\printing_Admin_Scripts\<language>` that publishes a printer to Active Directory Domain Services. It is run with `cscript`, and is part of the Windows print command reference.

## simple description

> ### 2026-11-21 Claude said
> pubprn.vbs is a built-in admin script that publishes shared printers into Active Directory so users can find them. It is run through cscript with a server name or a printer UNC path and an LDAP container path. It is one of several printing admin scripts shipped with Windows.
>
> **SOC NOTE**: Microsoft-signed script that is a known LOLBin (T1216.001 PubPrn): its second argument can be abused as `script:https://...` to load and run a remote scriptlet. Hunt for cscript/wscript running pubprn.vbs with `script:` or URLs in the command line.
>

# purpose

Publishes all printers on a server, or a specific printer by UNC path, to an AD container.

Syntax: `cscript pubprn {<servername> | <UNCprinterpath>} LDAP://CN=<container>,DC=<container>`

| parameter | description |
| --- | --- |
| `<servername>` | Name of the Windows server hosting the printer; defaults to local computer. |
| `<UNCprinterpath>` | UNC path to the shared printer to publish. |
| `LDAP://CN=<Container>,DC=<Container>` | Path to the AD DS container where the printer is published. |
| `/?` | Displays help at the command prompt. |
