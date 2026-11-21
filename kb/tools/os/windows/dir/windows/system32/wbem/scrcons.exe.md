---
created: 2026-11-21
fullpath: 'C:\Windows\System32\wbem\scrcons.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - wmi
aliases:
  - "scrcons.exe"
  - "WMI Standard Event Consumer - scripting"
  - "ActiveScriptEventConsumer"
url:
  - https://learn.microsoft.com/windows/win32/wmisdk/activescripteventconsumer
  - https://learn.microsoft.com/windows/win32/wmisdk/running-a-script-based-on-an-event
  - https://learn.microsoft.com/windows/win32/wmisdk/standard-consumer-classes
---

**fullpath**: C:\Windows\System32\wbem\scrcons.exe

# description

WMI binary that implements the **ActiveScriptEventConsumer** standard event consumer, which runs a predefined script in an arbitrary scripting language when an event is delivered to it. The class lives in the `root\subscription` namespace and is defined in `Scrcons.mof`. Related standard consumers include CommandLineEventConsumer, LogFileEventConsumer, NTEventLogEventConsumer and SMTPEventConsumer.

## simple description

> ### 2026-11-21 Claude said
> scrcons.exe is the WMI "script consumer" host. When someone creates a permanent WMI event subscription that uses ActiveScriptEventConsumer (VBScript/JScript code tied to an event filter), WMI starts scrcons.exe to run that script as SYSTEM whenever the event fires. Legitimate use is rare in most environments.
>
> **SOC NOTE**: Classic fileless persistence: WMI event subscription (T1546.003). Any scrcons.exe process, especially spawning cmd/powershell or making network connections, is highly suspicious. Check root\subscription for __EventFilter, ActiveScriptEventConsumer and __FilterToConsumerBinding instances; WMI-Activity/Operational event 5861 and Sysmon events 19/20/21 record subscription creation. The OBJECTS.DATA repository holds the evidence forensically.
>

# purpose

Runs the scripts of ActiveScriptEventConsumer instances. Scripts run in the LocalSystem security context with no screen output and without Windows Script Host (WScript methods are unavailable); they have no network access or user logon data such as environment variables and network shares. Only a local or domain administrator can configure the consumer, but once configured any user can trigger the event. Either `ScriptText` or `ScriptFileName` must be set (not both). Overall behaviour is tuned with the `Timeout` and `MaximumScripts` properties of the single ScriptingStandardConsumerSetting instance, and per-consumer `KillTimeout` (0 = never terminate).

# typical use cases

| usage | description |
| --- | --- |
| `Mofcomp -n:root\<namespace> scrcons.mof` | Register the ActiveScriptEventConsumer class in another namespace. |

# options

_Not documented on Microsoft Learn at 2026/11/21 08:47 UTC_
