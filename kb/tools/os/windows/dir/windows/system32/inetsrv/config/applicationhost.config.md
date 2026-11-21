---
created: 2026-11-21
fullpath: 'C:\Windows\System32\inetsrv\config\applicationHost.config'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - applicationHost.config
  - ApplicationHost.config
url:
  - https://learn.microsoft.com/iis/get-started/planning-your-iis-architecture/introduction-to-applicationhostconfig
  - https://learn.microsoft.com/iis/manage/managing-your-configuration-settings/understanding-iis-configuration-delegation
  - https://learn.microsoft.com/iis/get-started/planning-your-iis-architecture/getting-started-with-configuration-in-iis-7-and-above
  - https://learn.microsoft.com/iis/configuration/
  - https://learn.microsoft.com/iis/manage/managing-your-configuration-settings/how-to-use-configuration-delegation-in-iis
---

**fullpath**:C:\Windows\System32\inetsrv\config\applicationHost.config

# description

ApplicationHost.config is the root file of the IIS 7+ configuration system, located in `%windir%\system32\inetsrv\config`. It replaced IIS 6.0's metabase.xml and sits alongside Administration.config and Redirection.config; its schema is defined in `inetsrv\config\schema` (IIS_schema.xml, ASPNET_schema.xml, FX_schema.xml).

## simple description

> ### 2026-11-21 Claude said
> This XML file is the master configuration for IIS web servers. It defines every site, binding, application, virtual directory and application pool, plus global settings like modules, handlers, authentication and logging. Changes are picked up immediately by worker processes. Admins edit it with IIS Manager, appcmd or PowerShell.
>
> **SOC NOTE**: Attackers modify it to install malicious native/managed IIS modules (MITRE ATT&CK T1505.004 IIS Components), add handlers or virtual directories for web shells (T1505.003), or read stored app pool credentials (encrypted, recoverable with `appcmd list apppool /text:*`). Review `<globalModules>`, `<modules>`, `<handlers>` and recent file modification times; `appcmd list config` and the IIS Configuration operational log help timeline changes.
>

# purpose

Holds definitions of all sites, applications, virtual directories and application pools plus global defaults for web server settings (similar to machine.config and root web.config for .NET). It contains the `configSections` registration for IIS and WAS sections and lock-down definitions (`overrideModeDefault`, `<location overrideMode="Allow">`) that control which sections lower-level web.config files may override. There is no in-memory configuration service: each worker process reads the file directly, so changes apply immediately. Back up the file before editing it.
