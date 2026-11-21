---
created: 2026-11-21
fullpath: 'c:\windows\system32\wbem\wbemtest.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - wmi
  - exe
aliases:
  - "wbemtest.exe"
  - "WBEMTEST"
  - "Windows Management Instrumentation Tester"
url:
  - https://learn.microsoft.com/intune/configmgr/develop/core/understand/introduction-to-wbemtest
  - https://learn.microsoft.com/dotnet/framework/wcf/diagnostics/wmi/
---

**fullpath**:c:\windows\system32\wbem\wbemtest.exe

# description

WBEMTEST (Windows Management Instrumentation Tester) is a GUI tool installed by Windows for working with WMI namespaces, classes and instances. It is available on most systems without download; WMI is Microsoft's implementation of Web Based Enterprise Management. Related: WMI CIM Studio, PowerShell CIM cmdlets.

## simple description

> ### 2026-11-21 Claude said
> wbemtest.exe is a built-in graphical tool for exploring and testing WMI. You connect to a namespace like root\cimv2, then enumerate classes, view instances, run WQL queries, execute methods or create/delete objects.
>
> **SOC NOTE**: Can be used interactively for WMI recon or to create/delete event subscriptions (__EventFilter, consumers) for persistence (T1546.003) or to execute methods like Win32_Process.Create (T1047). Unusual on servers outside admin troubleshooting; review WMI-Activity/Operational events (5857-5861) when it runs.
>

# purpose

Connect to a WMI namespace and browse classes, view instances and MOF, and run WMI queries. It doesn't browse namespaces, so you must know the namespace (e.g. ROOT\CIMV2, ROOT\CCM on ConfigMgr clients, ROOT\SMS\site_<code> on site servers). Can connect to remote namespaces with Packet privacy authentication.

# typical use cases

| usage | description |
| --- | --- |
| `wbemtest.exe` | Launch the WMI Tester GUI; then Connect to root\cimv2, Enum Classes (Recursive), open Win32_Service > Instances > Show MOF. |
| `wbemtest.exe` | Connect to root\ServiceModel with Authentication level Packet privacy to access WCF WMI instances on a remote machine. |

# options

_Not documented on Microsoft Learn at 2026/11/21 13:48 UTC_
