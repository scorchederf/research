---
created: 2026-11-21
fullpath: 'C:\Windows\System32\inetsrv\appcmd.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - iis
aliases:
  - appcmd.exe
  - AppCmd
url:
  - https://learn.microsoft.com/iis/get-started/getting-started-with-iis/getting-started-with-appcmdexe
  - https://learn.microsoft.com/iis/publish/using-webdav/how-to-configure-webdav-settings-using-appcmd
  - https://learn.microsoft.com/iis/web-hosting/web-server-for-shared-hosting/create-a-backup-with-appcmd
---

**fullpath**:C:\Windows\System32\inetsrv\appcmd.exe

# description

AppCmd.exe is the single command-line tool for managing IIS 7 and above, located in `%systemroot%\system32\inetsrv\` (not on the PATH by default). It exposes server management objects (sites, apps, virtual directories, application pools, configuration, worker processes, requests, modules, backups, trace logs) and replaces the older adsutil.vbs script.

## simple description

> ### 2026-11-21 Claude said
> AppCmd is the built-in command-line administration tool for IIS web servers. Admins use it to create, list, change, start and stop websites and application pools, and to read or edit IIS configuration. It can also back up and restore the IIS configuration. It only exists on systems where the IIS role is installed.
>
> **SOC NOTE**: Attackers abuse appcmd to install malicious IIS native modules / backdoors (`appcmd install module`, T1505.004 IIS Components), to disable logging (`set config /section:httpLogging /dontLog:true`, T1562.002), and to dump application pool identity passwords in cleartext (`appcmd list apppool /text:*`, T1552). Watch process creation (4688 / Sysmon 1) for these command lines and changes to applicationHost.config.
>

# purpose

Manage IIS from the command line or scripts without the GUI: create/configure sites, apps, virtual directories and application pools; start/stop sites and recycle app pools; list running worker processes and executing requests; search, edit, export and import IIS and ASP.NET configuration.

# typical use cases

- `appcmd list site` / `appcmd list apppool` - inventory sites and pools.
- `appcmd add site /name:... /bindings:... /physicalPath:...` - create a site.
- `appcmd set config <URL> /section:<name> /property:value` - edit configuration.
- `appcmd add backup "Name"` / `appcmd restore backup "Name"` - back up and restore configuration.
- `appcmd list vdir /text:physicalPath` - feed output into other shell tools.

# options

| option | description |
| --- | --- |
| `LIST` | Display objects on the machine; an optional ID or property parameters filter the result. |
| `ADD` | Create a new object with the specified properties. |
| `DELETE` | Delete the object specified by the ID. |
| `SET` | Set parameters on the object specified by the ID. |
| `SITE` | Object: administration of virtual sites. |
| `APP` | Object: administration of applications. |
| `VDIR` | Object: administration of virtual directories. |
| `APPPOOL` | Object: administration of application pools. |
| `CONFIG` | Object: administration of general configuration sections. |
| `WP` | Object: administration of worker processes. |
| `REQUEST` | Object: administration of HTTP requests. |
| `MODULE` | Object: administration of server modules. |
| `BACKUP` | Object: administration of server configuration backups. |
| `TRACE` | Object: working with failed request trace logs. |
| `/?` | Help; usable as `APPCMD /?`, `APPCMD <OBJECT> /?` or `APPCMD <COMMAND> <OBJECT> /?`. |
| `/config:*` | Display effective configuration including inherited and default values. |
| `/config` | Display returned objects as raw configuration XML. |
| `/section:<name>` | Configuration section to list or edit (`/section:?` lists sections). |
| `/text:<property>` | Output only the named property, one item per line. |
| `/xml` | Output well-formed XML result sets that can be piped into another AppCmd command. |
