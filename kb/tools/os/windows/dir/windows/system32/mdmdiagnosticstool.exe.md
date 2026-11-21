---
created: 2026-11-21
fullpath: 'C:\Windows\System32\mdmdiagnosticstool.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - mdm
aliases:
  - mdmdiagnosticstool.exe
  - MDM Diagnostic Information
url:
  - https://learn.microsoft.com/windows/client-management/mdm-collect-logs
  - https://learn.microsoft.com/troubleshoot/mem/intune/device-enrollment/understand-troubleshoot-esp
  - https://learn.microsoft.com/intune/device-management/actions/collect-diagnostics
---

**fullpath**:C:\Windows\System32\mdmdiagnosticstool.exe

# description

`mdmdiagnosticstool.exe` is a built-in Windows tool that collects MDM Diagnostic Information logs for enrollment, provisioning and Autopilot troubleshooting. It is the command-line equivalent of **Settings > Accounts > Access work or school > Create report**, and Intune's Collect diagnostics device action runs it.

## simple description

> ### 2026-11-21 Claude said
> MdmDiagnosticsTool is a Windows program that gathers logs and configuration about how a device is managed by MDM (such as Intune). It packages event logs, ETL traces, registry dumps and an HTML report into a zip or cab file. Admins use it to troubleshoot enrollment, Autopilot and policy problems. It is normally run by IT staff or by Intune, not by end users.
>
> **SOC NOTE**: The output contains a dump of MDM registry keys, certificates, management URLs and policies, which is useful reconnaissance data; unexpected runs or output copied off-host deserve review. Its reports are also a fast forensic snapshot of a device's management and policy state.
>

# purpose

Collects MDM diagnostic logs from Windows devices by area and writes them to a zip or cab file. Output includes `MDMDiagHtmlReport.html`, `MDMDiagReport.xml`, `MdmDiagReport_RegistryDump.reg`, `MdmDiagLogMetadata.json`, `MdmLogCollectorFootPrint.txt`, area ETLs and `.evtx` logs (mainly `microsoft-windows-devicemanagement-enterprise-diagnostics-provider-admin.evtx`). Reports are viewed under `C:\Users\Public\Documents\MDMDiagnostics`.

# typical use cases

| usage | description |
| --- | --- |
| `mdmdiagnosticstool.exe -area "DeviceEnrollment;DeviceProvisioning;Autopilot" -zip "c:\users\public\documents\MDMDiagReport.zip"` | Collect enrollment, provisioning and Autopilot logs into a zip. |
| `mdmdiagnosticstool.exe -area Autopilot -cab <pathToOutputCabFile>` | Collect Autopilot/ESP logs for user-driven mode. |
| `mdmdiagnosticstool.exe -area Autopilot;TPM -cab <pathToOutputCabFile>` | Collect Autopilot and TPM logs for self-deploying or pre-provisioned devices. |
| `mdmdiagnosticstool.exe -area DeviceProvisioning -cab <pathToOutputCabFile>` | Collect runtime provisioning logs. |

# options

| option | description |
| --- | --- |
| `-area` | Semicolon-separated areas to collect, such as `DeviceEnrollment`, `DeviceProvisioning`, `Autopilot`, `TPM`. |
| `-zip` | Writes the collected logs to the specified zip file. |
| `-cab` | Writes the collected logs to the specified cab file. |
