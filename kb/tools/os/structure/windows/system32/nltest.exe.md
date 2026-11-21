---
created: 2026-11-21
fullpath: 'C:\Windows\System32\nltest.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - nltest.exe
  - Nltest
url:
  - https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731935(v=ws.11)
---

**fullpath**:C:\Windows\System32\nltest.exe

# description

Nltest is a command-line tool that performs network administrative tasks such as listing domain controllers, querying trust status and testing or resetting the NetLogon secure channel. It is built into Windows Server and is available with the AD DS or AD LDS roles or the Active Directory Domain Services Tools in RSAT; Microsoft says to run it from an elevated command prompt.

## simple description

> ### 2026-11-21 Claude said
> Nltest is a Windows domain troubleshooting tool that talks to the NetLogon service. Admins use it to find domain controllers, check whether a computer's secure channel to the domain is healthy, list domain trusts and reset machine-account trust. It works against the local machine or a remote server with `/server:`. Its output is aimed at experienced admins.
>
> **SOC NOTE**: Nltest is a favorite discovery tool for ransomware and intrusion operators: `nltest /domain_trusts /all_trusts`, `/dclist:` and `/dsgetdc:` map trusts and domain controllers (MITRE ATT&CK T1482 Domain Trust Discovery, T1018 Remote System Discovery). Execution by a regular user workstation account, from Office/script parents, or in quick succession with `net group`/`whoami` is a strong early-stage indicator. Process creation logs (4688/Sysmon 1) with command line are the key evidence.
>

# purpose

- Get a list of domain controllers and locate DCs with specific roles.
- Force a remote shutdown.
- Query the status of trust and test trust relationships and DC replication state.
- Test and reset the NetLogon secure channel between clients and domain controllers.
- Force user-account database synchronization on Windows NT 4.0 or earlier DCs.

# typical use cases

- List DCs in a domain: `nltest /dclist:fourthcoffee`
- Show user SAM attributes: `nltest /user:"TestAdmin"`
- Verify trust with a server: `nltest.exe /server:fourthcoffee-dc-01 /sc_query:fourthcoffee`
- Find the PDC emulator: `nltest /dcname:fourthcoffee`
- List domain trusts: `nltest /domain_trusts`

# options

| option    | description    |
| --- | --- |
| `/server:<ServerName>` | Runs nltest at a remote domain controller; default is the local computer. |
| `/query` | Reports on the state of the secure channel the last time it was used. |
| `/repl` | Forces synchronization of unreplicated changes with the PDC (Windows NT 4.0 BDCs only; admin required). |
| `/sync` | Forces immediate full SAM synchronization with the PDC (Windows NT 4.0 BDCs only; admin required). |
| `/pdc_repl` | Forces the PDC to send a sync notification to all BDCs (Windows NT 4.0 PDCs only; admin required). |
| `/sc_query:<DomainName>` | Reports secure channel state and the DC queried on it. |
| `/sc_reset:[<DomainName>]` | Removes and rebuilds the NetLogon secure channel (admin required). |
| `/sc_verify:[<DomainName>]` | Checks the secure channel and rebuilds it if it does not work (admin required). |
| `/sc_change_pwd:[<DomainName>]` | Changes the trust account / computer account password for the specified domain. |
| `/dclist:[<DomainName>]` | Lists all domain controllers in the domain. |
| `/dcname:[<DomainName>]` | Lists the PDC or PDC emulator for the domain. |
| `/dsgetdc:[<DomainName>]` | Queries DNS for DCs and their IPs and checks connectivity; filters include `/PDC`, `/DS`, `/DSP`, `/GC`, `/KDC`, `/TIMESERV`, `/GTTIMESERV`, `/WS`, `/NetBIOS`, `/DNS`, `/IP`, `/FORCE`, `/Writable`, `/Avoidself`, `/LDAPOnly`, `/Backg`, `/DS_6`, `/DS_8`, `/Try_Next_Closest_Site`, `/Ret_DNS`, `/Ret_NETBIOS`. |
| `/dnsgetdc:<DomainName>` | Queries DNS for DCs and IPs; filters `/PDC`, `/GC`, `/KDC`, `/WRITABLE`, `/LDAPONLY`, `/FORCE`, `/SITE`, `/SITESPEC`. |
| `/dsgetfti:<DomainName>[ /UpdateTDO]` | Returns interforest trust information (forest-root DC only); `/UpdateTDO` updates the local copy. |
| `/dsgetsite` | Returns the site in which the DC resides. |
| `/dsgetsitecov` | Returns the sites the DC covers. |
| `/parentdomain` | Returns the parent domain of the server. |
| `/dsregdns` | Refreshes registration of all DC-specific DNS records. |
| `/dsderegdns:<DnsHostName>` | Deregisters DNS host records; values `/DOM`, `/DSAGUID`, `DOMGUID`. |
| `/whowill:<Domain>/<User>` | Finds the DC that has the specified user account. |
| `/finduser:<User>` | Finds the directly trusted domain the user account belongs to. |
| `/transport_notify` | Flushes the negative cache to force DC discovery (Windows NT 4.0 DCs only). |
| `/dbflag:<HexadecimalFlags>` | Sets a new NetLogon debug flag (commonly 0x2000FFFF). |
| `/user:<UserName>` | Displays SAM attributes for a user (not for AD-stored accounts). |
| `/time:<HexadecimalLSL> <HexadecimalMSL>` | Converts Windows NT GMT time to ASCII. |
| `/logon_query` | Queries the cumulative number of NTLM logon attempts. |
| `/domain_trusts` | Returns trusted domains; filters `/Primary`, `/Forest`, `/Direct_Out`, `/Direct_In`, `/All_Trusts`, `/v`. |
| `/dsquerydns` | Queries the status of the last update for DC-specific DNS records. |
| `/bdc_query:<DomainName>` | Lists BDCs and their sync/replication state (Windows NT 4.0 DCs only). |
| `/sim_sync:<DomainName> <ServerName>` | Simulates full synchronization replication. |
| `/list_deltas:<FileName>` | Displays the contents of a change log file (Netlogon.chg on NT 4.0 BDCs). |
| `/cdigest:<Message> /domain:<DomainName>` | Displays the client's current and previous secure channel digest. |
| `/sdigest:<Message> /rid:<RID_In_Hexadecimal>` | Displays the server's current and previous secure channel digest. |
| `/shutdown:<Reason>[ <Seconds>]` | Remotely shuts down the specified server. |
| `/shutdown_abort` | Terminates a system shutdown. |
| `{/help \| /?}` | Displays help at the command prompt. |
