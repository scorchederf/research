---
created: 2026-11-21
fullpath: 'C:\inetpub\wwwroot'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - iis
aliases:
  - "wwwroot"
  - "Inetpub\Wwwroot"
url:
  - https://learn.microsoft.com/iis/get-started/getting-started-with-iis/create-a-web-site
  - https://learn.microsoft.com/iis/install/installing-iis-7/compatibility-and-feature-requirements-for-windows-vista
  - https://learn.microsoft.com/troubleshoot/developer/webapps/iis/www-administration-management/default-permissions-user-rights
  - https://learn.microsoft.com/iis/get-started/getting-started-with-iis/getting-started-with-the-iis-manager-in-iis-7-and-iis-8
---

**fullpath**:C:\inetpub\wwwroot

# description

C:\inetpub\wwwroot is the default content directory of the IIS Default Web Site, created when Internet Information Services is installed. IIS setup always installs \inetpub in %SystemDrive%; the site mapping is stored in ApplicationHost.config.

## simple description

> ### 2026-11-21 Claude said
> This is the default web root for Microsoft IIS. Files placed here are served by the Default Web Site, for example http://localhost/. It is created when the IIS role or feature is installed.
>
> **SOC NOTE**: Prime location for web shells (MITRE ATT&CK T1505.003): look for new .aspx/.asp/.ashx files, recently modified web.config, and w3wp.exe spawning cmd.exe or powershell.exe. Correlate with IIS logs in C:\inetpub\logs\LogFiles.
>

# purpose

Holds the content of the Default Web Site. You can publish content here or create a site in another location. By default the folder inherits from \inetpub: CREATOR OWNER and SYSTEM/Administrators/TrustedInstaller have full control, Users have Read & execute, List folder contents and Read, and IIS_IUSRS has Read & execute.

# common files found

| file | description |
| --- | --- |
| `web.config` | Site-level configuration written by IIS Manager for unlocked sections such as defaultDocument. |
| `aspnet_client` | Subfolder listed in the default IIS permissions reference. |
