---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - exchange
aliases:
  - "HttpProxy"
  - "FrontEnd\\HttpProxy"
url:
  - https://learn.microsoft.com/troubleshoot/exchange/setup/owa-your-request-cannot-be-completed
  - https://learn.microsoft.com/troubleshoot/exchange/client-connectivity/event-1309-code-3005-cannot-access-owa-ecp
  - https://learn.microsoft.com/exchange/management/health/troubleshooting-owa-proxy-health-set
---

**fullpath**:C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy

# description

The Exchange Server 2013/2016/2019 front-end (Client Access) HTTP proxy folder. It contains the front-end web applications that proxy client protocols (OWA, ECP, EWS, OAB, RPC, PowerShell, etc.) to back-end mailbox servers, and a `SharedWebConfig.config` generated during setup.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the Exchange front-end web apps that receive client connections (Outlook on the web, ActiveSync, EWS, Autodiscover) and forward them to the mailbox back end.
> IIS serves these virtual directories on the Exchange server.
> It is different from the HttpProxy log folder under the Exchange Logging directory.
>
> **SOC NOTE**: Key folder for Exchange compromise investigations (ProxyLogon/ProxyShell, T1505.003 Web Shell): look for unexpected .aspx files in the owa/auth or ecp subfolders and modified web.config files. Correlate with HttpProxy logs in %ExchangeInstallPath%Logging\HttpProxy.
>

# purpose

Hosts the front-end proxy web applications. If `SharedWebConfig.config` is missing here, OWA/ECP fail (Event ID 1309); it is regenerated with `DependentAssemblyGenerator.exe ... -exchangePath "%ExchangeInstallPath%\FrontEnd\HttpProxy" -configFile "%ExchangeInstallPath%\FrontEnd\HttpProxy\SharedWebConfig.config"`. Protocol proxy logs are separate, in `%ExchangeInstallPath%Logging\HttpProxy\<protocol>`.

# common files found

| file | description |
| --- | --- |
| `SharedWebConfig.config` | Shared configuration generated during the post-installation phase of Setup; required for OWA and ECP. |
