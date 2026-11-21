---
created: 2026-11-21
fullpath: 'c:\windows\system32\cipher.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - efs
  - encryption
  - lolbin
aliases:
  - "cipher.exe"
  - "cipher"
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/cipher
---

**fullpath**:c:\windows\system32\cipher.exe

# description

cipher displays or alters the encryption of directories and files on NTFS volumes; without parameters it displays the encryption state of the current directory and its files. It is a built-in Windows command for the Encrypting File System (EFS).

## simple description

> ### 2026-11-21 Claude said
> cipher.exe is the built-in command-line tool for Windows EFS file encryption. It can encrypt or decrypt files and folders, back up EFS keys, create recovery agent certificates, and wipe free disk space with `/w`. It is present on all modern Windows versions.
>
> **SOC NOTE**: `cipher /w:C:\` overwrites deleted data in free space and is used by ransomware and wipers to prevent file recovery after encryption (T1485 Data Destruction, T1070.004). EFS itself has also been abused for ransomware-style encryption (T1486). Alert on cipher.exe with `/w` or mass `/e` outside of IT activity.
>

# purpose

Manages EFS encryption on NTFS: encrypting/decrypting files and folders, managing EFS certificates and recovery agents, rekeying files, and removing data from unused disk space.

# typical use cases

| usage | description |
| --- | --- |
| `cipher` | Display the encryption status of files and subdirectories in the current directory (E = encrypted, U = unencrypted). |
| `cipher /e private` | Encrypt the Private directory so files added later are encrypted too. |
| `cipher /w:C:\` | Remove data from available unused disk space on the volume. |

# options

| option | description |
| --- | --- |
| `/b` | Aborts if an error is encountered; by default cipher continues. |
| `/c` | Displays information on the encrypted file. |
| `/d` | Decrypts the specified files or directories. |
| `/e` | Encrypts the specified files or directories and marks directories so new files are encrypted. |
| `/h` | Displays files with hidden or system attributes, which are not encrypted or decrypted by default. |
| `/k` | Creates a new EFS certificate and key; all other parameters are ignored. |
| `/r:<filename> [/smartcard]` | Generates an EFS recovery agent key and certificate to .pfx and .cer files, or to a smart card with /smartcard. |
| `/s:<directory>` | Performs the operation on all subdirectories of the directory. |
| `/u [/n]` | Finds all encrypted files on local drives; with /n no updates are made, otherwise keys are compared and updated. |
| `/w:<directory>` | Removes data from available unused disk space on the entire volume; all other parameters are ignored. |
| `/x[:efsfile] [<FileName>]` | Backs up the EFS certificate and keys to the file; with :efsfile backs up the certificates used to encrypt that file. |
| `/y` | Displays the current EFS certificate thumbnail. |
| `/adduser [/certhash:<hash> \| /certfile:<filename>]` | _Not documented on Microsoft Learn at 2026/11/21 13:51 UTC_ |
| `/rekey` | Updates the encrypted files to use the currently configured EFS key. |
| `/removeuser /certhash:<hash>` | Removes a user from the files; the hash must be the SHA1 hash of the certificate to remove. |
| `/?` | Displays help at the command prompt. |
