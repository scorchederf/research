---
created: 2026-11-21
fullpath: 'C:\Windows\System32\config\TxR'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - registry
aliases:
  - TxR
  - Transactional Registry
url:
  - https://learn.microsoft.com/windows/win32/ktm/kernel-transaction-manager-portal
  - https://learn.microsoft.com/windows/win32/ktm/about-ktm
  - https://learn.microsoft.com/windows-hardware/drivers/kernel/using-log-streams-with-ktm
---

**fullpath**:C:\Windows\System32\config\TxR

# description

TxR is the Transactional Registry, which allows transacted registry operations and is implemented on the Kernel Transaction Manager (KTM), available starting with Windows Vista. KTM relies on the Common Log File System (CLFS) and creates a CLFS log stream for each transaction manager object to record transaction state for commit, rollback and recovery. Learn does not document the `config\TxR` folder itself.

## simple description

> ### 2026-11-21 Claude said
> This hidden folder sits next to the registry hive files and stores the transaction logs for the Transactional Registry (TxR). These are Common Log File System files (.blf and .regtrans-ms) that let registry changes be committed or rolled back as a unit. Windows manages them automatically.
>
> **SOC NOTE**: The TxR .regtrans-ms/.blf files can contain fragments of recent registry transactions and are occasionally used for registry forensics and recovery. Attackers have abused transacted registry APIs (e.g. RegCreateKeyTransacted) to make stealthier changes; the files are also commonly in use and locked, so copy them via VSS or raw disk access.
>

# purpose

Backs the Transactional Registry: KTM uses the transaction manager object's log stream to record internal state for associated resource managers, transactions and enlistments, so interrupted transactional operations can be committed or rolled back, and `ZwRecoverTransactionManager` reads the log to recover to a known good point after a crash.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
