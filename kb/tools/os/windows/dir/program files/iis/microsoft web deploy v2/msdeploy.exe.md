---
created: 2026-11-21
fullpath: 'C:\Program Files\IIS\Microsoft Web Deploy V2\msdeploy.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - iis
  - web-deploy
aliases:
  - msdeploy.exe
  - MSDeploy
  - Web Deploy
  - Web Deployment Tool
url:
  - https://learn.microsoft.com/iis/publish/using-web-deploy/introduction-to-web-deploy
  - https://learn.microsoft.com/aspnet/web-forms/overview/deployment/web-deployment-in-the-enterprise/deploying-web-packages
  - https://learn.microsoft.com/iis/publish/using-web-deploy/web-deploy-automatic-backups
  - https://learn.microsoft.com/aspnet/web-forms/overview/deployment/advanced-enterprise-web-deployment/taking-web-applications-offline-with-web-deploy
---

**fullpath**:C:\Program Files\IIS\Microsoft Web Deploy V2\msdeploy.exe

# description

`msdeploy.exe` is the command-line executable of Microsoft Web Deploy (Web Deployment Tool), typically at `%PROGRAMFILES%\IIS\Microsoft Web Deploy {version}\msdeploy.exe`. It drives the Web Deploy framework, which syncs data between a source and destination through providers (contentPath, iisApp, appHostConfig, dbFullSql, package, auto, and more). It is also exposed via a public API, PowerShell cmdlets, and Visual Studio-generated `.deploy.cmd` scripts.

## simple description

> ### 2026-11-21 Claude said
> msdeploy.exe is the command-line tool for Microsoft Web Deploy, used to publish, back up and synchronize IIS websites, configuration and databases between servers. It works with a verb (such as sync, dump, delete), a source and a destination. It can talk to remote servers through the Web Deploy Remote Agent Service or the Web Management Service handler. V2 is an older release; current installs are usually V3.
>
> **SOC NOTE**: msdeploy is a documented LOLBin: providers like `runCommand` can execute arbitrary commands, and `sync` can copy files or dump IIS config/credentials (MITRE T1218 System Binary Proxy Execution, T1105, T1552). Remote agent (MsDepSvc, port 80 /MSDEPLOYAGENTSERVICE) and WMSvc (8172) are lateral movement surfaces. Alert on msdeploy launched by unexpected parents or with `-verb:sync -source:runCommand`.
>

# purpose

Performs Web Deploy operations - most modelled as a sync between source and destination - such as deploying web packages, syncing sites across a web farm, managing automatic backups, and deploying/deleting App_offline files.

# typical use cases

| usage | description |
| --- | --- |
| `msdeploy.exe -verb:sync -source:iisapp=<siteName> -dest:auto,computername=<remoteComputerName>` | Syncs a site to a remote server via the Web Deployment Agent. |
| `msdeploy.exe -verb:sync -source:package='[path to web package]' -dest:auto='[server name or service URL]'` | Deploys a web package to an IIS website. |
| `msdeploy.exe -verb:dump -source:backupManager=<siteName>` | Lists automatic backups for a site. |
| `msdeploy.exe -verb:sync -source:backupManager -dest:backupManager=<siteName>,useLatest=true` | Restores the latest backup for a site. |
| `msdeploy.exe -verb:delete -dest:contentPath="[IIS application path]/App_offline.htm",computerName="[Destination web server]"` | Deletes a file on the destination site. |

# options

| option | description |
| --- | --- |
| `-source:<providerName>=<location>` | Indicates where data comes from, using a Web Deploy provider. |
| `-dest:<providerName>=<location>` | Indicates where data goes to; settings like `computerName`, `authtype`, `includeAcls` can be added. |
| `-verb:<operation>` | The operation to perform, e.g. `sync`, `dump`, `delete`. |
| `-whatif` | Trial run that reports what would happen without deploying. |
| `-skip:<rule>` | Skips matching objects, e.g. `-skip:xpath=dirPath[@path='App_Data']`. |

