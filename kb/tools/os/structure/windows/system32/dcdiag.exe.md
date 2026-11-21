---
created: 2026-11-21
fullpath: 'C:\Windows\System32\dcdiag.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - active-directory
aliases:
  - dcdiag.exe
  - Dcdiag
url:
  - https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731968(v=ws.11)
---

**fullpath**:C:\Windows\System32\dcdiag.exe

# description

Dcdiag analyzes the state of domain controllers in a forest or enterprise and reports problems to help troubleshooting. It is built into Windows Server when the AD DS or AD LDS role is installed, or available via the AD DS tools in RSAT, and must be run from an elevated command prompt.

## simple description

> ### 2026-11-21 Claude said
> dcdiag is the Domain Controller Diagnostic tool. Admins run it to test DC health: connectivity, replication, DNS registration, FSMO role holders, services, SYSVOL and more. It prints pass/fail results for each test. It is normally found on domain controllers and admin workstations with RSAT.
>
> **SOC NOTE**: Mostly benign admin activity, but attackers use it for discovery (T1018, T1482), e.g. `dcdiag /test:dns` or `/s:` to enumerate DCs and roles. Unusual on a non-admin workstation or run by a non-admin account; review 4688 / Sysmon 1 command lines and parent process.
>

# purpose

Framework that runs a series of tests against DCs selected by scope (enterprise, site, or single server) and reports abnormal behavior; includes enhanced DNS tests and DcPromo/RegisterInDNS pre-checks.

# typical use cases

- `dcdiag /s:<DC>` - health check one DC.
- `dcdiag /e /v /f:log.txt` - verbose enterprise-wide check to a file.
- `dcdiag /test:DNS /e /v` - DNS infrastructure tests.
- `dcdiag /test:DcPromo /DnsDomain:<name> /NewForest` - pre-promotion DNS check.

# options

| option | description |
| --- | --- |
| `/s:<DomainController>` | Server to run against; defaults to the local DC. Ignored for DcPromo and RegisterInDns tests. |
| `/n:<NamingContext>` | Naming context to test (NetBIOS, DNS or DN format). |
| `/u:<Domain>\<UserName> /p:{* \| <Password> \| ""}` | Alternate credentials; `*` prompts, `""` for empty password. |
| `/a` | Test all servers in this site. |
| `/e` | Test all servers in the enterprise; overrides `/a`. |
| `/q` | Quiet; print only errors. |
| `/v` | Verbose; print extended information. |
| `/i` | Ignore superfluous error messages. |
| `/fix` | MachineAccount test only: fixes SPNs on the DC machine account. |
| `/f:<LogFile>` | Redirect all output to a log file. |
| `/c` | Comprehensive: all tests except DCPromo and RegisterInDNS, including non-default tests; combine with `/skip`. |
| `{/h \| /?}` | Display help. |
| `/test:<Test>` | Run only this test (plus Connectivity). Do not combine with `/skip`. |
| `/ReplSource:<SourceDomainController>` | Test connection to a source DC (CheckSecurityError test). |
| `/DnsBasic` | DNS test: connectivity, client config, service availability, zone existence. |
| `/DnsForwarders` | DNS test: basic plus forwarder configuration. |
| `/DnsDelegation` | DNS test: basic plus delegations. |
| `/DnsDynamicUpdate` | DNS test: basic plus dynamic update on the AD zone. |
| `/DnsRecordRegistration` | DNS test: basic plus A, CNAME and SRV registration. |
| `/DnsResolveExtName [/DnsInternetName:<InternetName>]` | DNS test: basic plus resolving an Internet name. |
| `/DnsAll` | All DNS tests except DnsResolveExtName; generates a report. |
| `/x:<XMLLog.xml>` | Redirect output to XML (only with `/test:dns`). |
| `/xsl:<XSLFile.xsl>` | Add stylesheet processing instruction (only with `/test:dns /x:`). |
| `/skip:<Test>` | Skip a test; Connectivity cannot be skipped. |
