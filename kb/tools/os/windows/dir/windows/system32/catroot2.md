---
created: 2026-11-21
fullpath: 'C:\Windows\System32\catroot2'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - code-signing
aliases:
  - catroot2
url:
  - https://learn.microsoft.com/answers/a/12334672
  - https://learn.microsoft.com/windows-hardware/drivers/install/catalog-files
---

**fullpath**:C:\Windows\System32\catroot2

# description

`C:\Windows\System32\catroot2` is a system folder used together with the CatRoot catalog store. On Microsoft Learn it appears in the standard Windows Update component reset procedure, where the Windows Update (wuauserv), Cryptographic Services (cryptSvc) and BITS services are stopped and catroot2 is renamed to Catroot2.old. Catalog files themselves are installed to the sibling CatRoot directory under the system directory.

## simple description

> ### 2026-11-21 Claude said
> catroot2 holds the Cryptographic Services catalog database (an ESE database, catdb, plus logs) that indexes the hashes in the signed .cat files stored in System32\CatRoot. Windows uses it to quickly check whether a system file or driver is signed by catalog. It is rebuilt automatically if deleted, which is why renaming it is a common fix for Windows Update errors.
>
> **SOC NOTE**: Catalog signing makes files appear "Microsoft signed" even without an embedded signature, so attackers who can add a catalog (T1553 Subvert Trust Controls, e.g. via `CryptCATAdminAddCatalog` or `signtool catdb`) can make malware look trusted. Unexpected new .cat files or catdb changes, and the reset sequence (`net stop cryptSvc` + `ren catroot2`) run outside of maintenance, are worth reviewing.
>

# purpose

Used by Cryptographic Services in support of catalog file verification; the folder is renamed as part of resetting Windows Update components. Files in the folder may be locked by core Windows functions, so renaming can fail with access denied unless the related services are stopped or the system is in safe mode.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 07:15 UTC_
