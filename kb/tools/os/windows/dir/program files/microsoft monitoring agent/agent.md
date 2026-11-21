---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft Monitoring Agent\Agent'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - monitoring
  - scom
  - log-analytics
aliases:
  - 'Agent'
  - 'Microsoft Monitoring Agent'
  - 'MMA'
  - 'Log Analytics agent'
url:
  - https://learn.microsoft.com/troubleshoot/azure/azure-monitor/azure-monitor-agent/windows-agents/erased-proxy-settings-microsoft-monitoring-agent
  - https://learn.microsoft.com/troubleshoot/azure/azure-monitor/azure-monitor-agent/windows-agents/mma-troubleshoot-basics
  - https://learn.microsoft.com/troubleshoot/azure/azure-monitor/azure-monitor-agent/windows-agents/resolve-windows-agent-installation-issues
  - https://learn.microsoft.com/system-center/scom/manage-deploy-windows-agent-manually?view=sc-om-2025
---

**fullpath**:C:\Program Files\Microsoft Monitoring Agent\Agent

# description

Default installation folder of the Microsoft Monitoring Agent (MMA), the Windows agent used by System Center Operations Manager and the legacy Azure Log Analytics agent. It is installed from `MOMAgent.msi` or the Log Analytics agent setup and runs the `HealthService.exe` and `MonitoringHost.exe` processes.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the Microsoft Monitoring Agent, which collects logs and performance data and sends it to SCOM or an Azure Log Analytics workspace (and was used to onboard older systems to Defender for Endpoint). It runs as a service with SYSTEM rights and executes management-pack scripts. The legacy Log Analytics agent has been replaced by the Azure Monitor Agent.
>
> **SOC NOTE**: MonitoringHost.exe legitimately runs PowerShell/VBScript from management packs, which creates noisy but expected script activity; attackers with SCOM/workspace control can push code to every agent. Tampering (stopping HealthService, editing proxy/workspace config, deleting the folder) can blind telemetry (T1562.001). Baseline children of MonitoringHost.exe and alert on new binaries in this folder.
>

# purpose

Contains the agent binaries, control panel applet and troubleshooting tools. `AgentControlPanel.exe` opens the Microsoft Monitoring Agent Properties dialog (Operations Manager management groups, Azure Log Analytics workspaces, proxy settings). Agent processes `HealthService.exe` and `MonitoringHost.exe` should be running when healthy.

# common files found

| file | description |
| --- | --- |
| `AgentControlPanel.exe` | Opens the **Microsoft Monitoring Agent Properties** dialog (also the Control Panel item). |
| `HealthService.exe` | Agent process checked when troubleshooting installation. |
| `MonitoringHost.exe` | Agent process checked when troubleshooting installation. |
| `Tools\StartTracing.cmd` | Enable verbose ETL trace logging (`StartTracing.cmd INF`). |
| `Tools\StopTracing.cmd` | Stop trace logging. |
| `Tools\FormatTracing.cmd` | Convert collected traces; output in `%windir%\Logs\OpsMgrTrace`. |
| `HelperObjects\OomADs.msi` | Active Directory Management Pack helper object for domain controllers. |

