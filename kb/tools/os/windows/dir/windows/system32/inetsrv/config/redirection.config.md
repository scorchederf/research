---
created: 2026-11-21
fullpath: 'C:\Windows\System32\inetsrv\config\redirection.config'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - redirection.config
  - configurationRedirection
url:
  - https://learn.microsoft.com/iis/configuration/configurationredirection
  - https://learn.microsoft.com/iis/manage/managing-your-configuration-settings/shared-configuration_264
  - https://learn.microsoft.com/iis/get-started/introduction-to-iis/web-site-deployment-made-easy
---

**fullpath**:C:\Windows\System32\inetsrv\config\redirection.config

# description

redirection.config is an IIS 7.0+ configuration file in %windir%\system32\inetsrv\config that contains settings used to redirect a web server to configuration files and schemas located on another computer. It holds the `<configurationRedirection>` element that implements IIS Shared Configuration, alongside applicationHost.config and administration.config.

## simple description

> ### 2026-11-21 Claude said
> This small XML file tells IIS whether to read its main configuration from the local disk or from a shared network location. When Shared Configuration is turned on, it stores the UNC path plus a user name and (encrypted) password for that share. It lets a web farm share one applicationHost.config. On a standalone server it is usually present but disabled.
>
> **SOC NOTE**: If enabled unexpectedly, an attacker could point IIS at attacker-controlled configuration and load malicious modules or handlers (T1505.004). It can contain credentials for the config share (encrypted, but recoverable by an admin on the host - T1552.001). Check enabled/path values and file modification time during IIS compromise investigations.
>

# purpose

Stores the `<configurationRedirection>` settings so IIS reads applicationHost.config, administration.config and encryption keys from a central location (for example a UNC share). IIS Manager's Shared Configuration feature updates it, and it can also be read or written programmatically through the AHADMIN COM API.

| attribute | description |
| --- | --- |
| `enabled` | Whether configuration redirection is enabled; default `false`. |
| `enableUncPolling` | Use UNC polling instead of change notifications (IIS 7.5+); default `false`. |
| `password` | Password to authenticate the user name to the configuration location; set via AppCmd or IIS Manager so it is encrypted. |
| `path` | Network path or local folder from which to read configuration files and encryption keys. |
| `pollingPeriod` | Interval between UNC checks when polling is enabled (IIS 7.5+); default `00:03:00`. |
| `userName` | User name used to access the configuration location. |
