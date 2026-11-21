---
created: 2026-11-21
fullpath: 'C:\Windows\System32\AppHostSvc'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - AppHostSvc
  - ApplicationHost Helper Service
  - Application Host Helper Service
url:
  - https://learn.microsoft.com/iis/install/installing-iis-7/applicationhost-helper-service
  - https://learn.microsoft.com/iis/configuration/system.applicationhost/confighistory
---

**fullpath**:C:\Windows\System32\AppHostSvc

# description

AppHostSvc corresponds to the IIS ApplicationHost Helper Service, installed whenever IIS 7.0 or later is installed. It hosts IIS functionality needed even when IIS isn't running: configuration history and application pool account mapping. Microsoft Learn does not document a System32\AppHostSvc folder itself.

## simple description

> ### 2026-11-21 Claude said
> AppHostSvc relates to the IIS Application Host Helper Service, which periodically backs up applicationHost.config into history folders and maps application pool identities to SIDs. A folder of this name under System32 is associated with that service on servers with IIS installed. It is not a user-facing location. Most IIS configuration lives in System32\inetsrv\config.
>
> **SOC NOTE**: Mainly context on IIS servers. Configuration history (by default %systemdrive%\inetpub\history) produced by this service lets responders diff applicationHost.config over time to spot malicious modules, handlers or virtual directories added for IIS backdoors (T1505.004). If the service is stopped, history stops, which may hide changes.
>

# purpose

The ApplicationHost Helper Service provides configuration history (saving applicationHost.config to history subdirectories, by default under `%systemdrive%\inetpub\history`) and application pool account mapping. It is runtime-independent, starts automatically and does not depend on WAS or the WWW service.

# common files found

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
