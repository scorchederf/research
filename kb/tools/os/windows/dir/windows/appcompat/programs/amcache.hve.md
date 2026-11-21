---
created: 2026-11-21
fullpath: 'C:\Windows\AppCompat\Programs\Amcache.hve'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - Amcache.hve
  - Amcache
url:
---

**fullpath**:C:\Windows\AppCompat\Programs\Amcache.hve

# description

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> Amcache.hve is a registry-format hive file that Windows uses to keep an inventory of programs, executables, drivers and devices seen on the system for application compatibility purposes. It is maintained by the compatibility/inventory components and updated as programs are installed and run. Each entry can include the file path, SHA-1 hash, size, link date, publisher and version. It is not loaded into the live registry tree, so analysts parse it offline.
>
> **SOC NOTE**: One of the most valuable execution/presence artifacts in DFIR: it can prove an attacker tool (renamed or deleted) existed on disk and supplies its SHA-1 for threat-intel lookup. Parse with tools such as AmcacheParser or RegRipper; check the InventoryApplicationFile and InventoryDriverBinary keys for malicious binaries and vulnerable drivers (BYOVD). Presence is evidence of existence, not always proof of execution. Attackers may delete or tamper with it (T1070 Indicator Removal).
>
> _Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
