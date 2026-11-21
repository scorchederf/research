---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wbem\AutoRecover'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - wmi
  - mof
aliases:
  - "AutoRecover"
url: []
---

**fullpath**:C:\Windows\System32\wbem\AutoRecover

# description

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

## simple description

> ### 2026-11-21 Claude said
> This folder is used by WMI to keep copies of MOF (Managed Object Format) files that were compiled with the autorecover option. If the WMI repository becomes corrupt, WMI rebuilds it and recompiles the autorecover MOFs so classes and providers come back. Files here are typically named with a hash and the .mof extension.
>
> **SOC NOTE**: Attackers can achieve WMI persistence (T1546.003) by compiling MOFs with #pragma autorecover; copies of those MOFs may land here and in HKLM\SOFTWARE\Microsoft\Wbem\CIMOM 'Autorecover MOFs', so a rebuilt repository re-creates their event subscriptions. Review recently created MOFs here for __EventFilter / CommandLineEventConsumer definitions.
>
> _Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_

# common files found

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
