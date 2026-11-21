---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft SQL Server\<version>\DTS\Binn\dtutil.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - sql-server
  - ssis
aliases:
  - dtutil.exe
  - dtutil
  - dtutil Utility
url:
  - https://learn.microsoft.com/sql/integration-services/dtutil-utility
---

**fullpath**:C:\Program Files\Microsoft SQL Server\<version>\DTS\Binn\dtutil.exe

# description

`dtutil` is the SQL Server Integration Services (SSIS) command prompt utility that manages SSIS packages. It ships with SQL Server Integration Services (and applies to the SSIS Integration Runtime in Azure Data Factory); many of its operations can also be done in SQL Server Management Studio.

## simple description

> ### 2026-11-21 Claude said
> dtutil.exe is a command-line tool installed with SQL Server Integration Services. Database admins use it to copy, move, delete, sign, encrypt or check for SSIS packages (.dtsx files) stored in the msdb database, the SSIS Package Store or the file system. The <version> folder is the SQL Server version number (for example 150 or 160). It is normally run by DBAs or deployment scripts on SQL servers.
>
> **SOC NOTE**: SSIS packages can run arbitrary commands and scripts when executed by SQL Agent, so an attacker with SQL access could use dtutil to plant or replace packages in msdb (persistence, T1505 Server Software Component / T1543-like abuse). Command lines can contain SQL credentials in clear text (/SourcePassword, /DestPassword) - check process creation logs (4688 / Sysmon 1). Unexpected dtutil runs outside deployment windows or by non-DBA accounts are worth investigating.
>

# purpose

Manages SSIS packages: it can copy, move, delete, or verify the existence of a package stored in a SQL Server msdb database, the SSIS Package Store, or the file system (selected with /SQL, /DTS and /FILE). It also creates/deletes/renames folders, signs, encrypts and regenerates package IDs. Options start with `/` or `-`, can be typed in any order, and the tool does not support command files or redirection.

# typical use cases

| usage | description |
| --- | --- |
| `dtutil /SQL srcPackage /COPY DTS;destFolder\destPackage` | Copy a package from msdb (Windows Authentication) to the SSIS Package Store. |
| `dtutil /FILE c:\myPackages\mypackage.dtsx /COPY FILE;c:\myTestPackages\mynewpackage.dtsx` | Copy a package on the file system under a new name. |
| `dtutil /FILE c:\sourcepkg.dtsx /DestServer <servername> /COPY SQL;destpkgname` | Copy a file-system package to msdb on a remote SQL Server. |
| `dtutil /I /FILE copiedpkg.dtsx` | Create a new package ID (GUID) after copying. |
| `dtutil /SQL delPackage /DELETE` | Delete a package stored in msdb. |
| `dtutil /FILE c:\srcPackage.dtsx /EXISTS` | Check whether a package exists on the file system. |
| `dtutil /DTS srcPackage.dtsx /MOVE SQL;destPackage` | Move a package from the Package Store into msdb. |
| `dtutil /H` | Display extended help for all options. |

# options

| option | description |
| --- | --- |
| `/?` | Displays the command prompt options. |
| `/C[opy] location;destinationPathandPackageName` | Copies an SSIS package (source given with /FI, /SQ or /DT); prompts before overwriting unless /Q is used. |
| `/Dec[rypt] password` | Sets the decryption password used to load a password-encrypted package. |
| `/Del[ete]` | Deletes the package specified by the SQL, DTS or FILE option. |
| `/DestP[assword] password` | Password for SQL Server Authentication to the destination instance; requires the user option. |
| `/DestS[erver] server_instance` | Destination server (and instance) for actions that save to SQL Server. |
| `/DestU[ser] username` | User name for SQL Server Authentication to the destination instance. |
| `/Dump process ID` | Causes the specified process (dtexec or dtsDebugHost) to pause and create debug dump files. |
| `/DT[S] filespec` | Specifies that the package is in the SSIS Package Store (path relative to its root). |
| `/En[crypt] {SQL \| FILE}; Path;ProtectionLevel[;password]` | Encrypts the loaded package with a protection level (0-5) and optional password and saves it to Path. |
| `/Ex[ists]` | Determines whether the package specified by SQL, DTS or FILE exists. |
| `/FC[reate] {SQL \| DTS};ParentFolderPath;NewFolderName` | Creates a new folder. |
| `/FDe[lete] {SQL \| DTS}[;ParentFolderPath;FolderName]` | Deletes a folder from SQL Server or SSIS. |
| `/FDi[rectory] {SQL \| DTS};FolderPath[;S]` | Lists folders and packages in a folder; S includes subfolders. |
| `/FE[xists] {SQL \| DTS};FolderPath` | Verifies that a folder exists. |
| `/Fi[le] filespec` | Specifies that the package is in the file system (UNC or local path). |
| `/FR[ename] {SQL \| DTS}[;ParentFolderPath;OldFolderName;NewFolderName]` | Renames a folder. |
| `/H[elp] option` | Displays extensive help, optionally for one option. |
| `/I[DRegenerate]` | Creates a new GUID for the package and updates its package ID. |
| `/M[ove] {SQL \| File \| DTS};pathandname` | Moves an SSIS package; prompts before overwriting unless /Q is used. |
| `/Q[uiet]` | Suppresses confirmation prompts for COPY, MOVE or SIGN. |
| `/R[emark] text` | Adds a comment to the command line. |
| `/Si[gn] {SQL \| File \| DTS};path;hash` | Signs a package with the certificate identified by a hexadecimal hash. |
| `/SourceP[assword] password` | Password for SQL Server Authentication to retrieve a package; requires /SourceUser. |
| `/SourceS[erver] server_instance` | Server used with the SQL option to retrieve a package. |
| `/SourceU[ser] username` | User name for SQL Server Authentication to retrieve a package. |
| `/SQ[L] package_path` | Specifies that the package is stored in the msdb database. |
