---
created: 2026-11-21
fullpath: 'C:\Program Files\Azure Advanced Threat Protection Sensor\<version>'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - directory
  - defender-for-identity
aliases:
  - Azure Advanced Threat Protection Sensor
  - Microsoft Defender for Identity sensor
  - Azure ATP sensor
url:
  - https://learn.microsoft.com/defender-for-identity/troubleshooting-using-logs
  - https://learn.microsoft.com/defender-for-identity/sensor-settings
  - https://learn.microsoft.com/defender-for-identity/deploy/install-sensor
  - https://learn.microsoft.com/defender-for-identity/deploy/configure-sensor-settings
---

**fullpath**:C:\Program Files\Azure Advanced Threat Protection Sensor\<version>

# description

This is the version-specific folder of the Microsoft Defender for Identity (formerly Azure Advanced Threat Protection) sensor, under the default installation path `%programfiles%\Azure Advanced Threat Protection Sensor`. The sensor is installed with `Azure ATP sensor Setup.exe` on domain controllers, AD FS, AD CS and Microsoft Entra Connect servers. Each sensor update is extracted to a new version folder.

## simple description

> ### 2026-11-21 Claude said
> This folder holds the program files of one specific version of the Microsoft Defender for Identity sensor, a security agent installed on domain controllers and identity servers. The sensor watches Active Directory traffic and events and sends them to Microsoft's cloud to detect identity attacks. Each time the sensor updates, a new folder named after the version number is created. Its Logs subfolder is the first place to look when the sensor is unhealthy.
>
> **SOC NOTE**: Attackers who reach a DC may try to stop or tamper with the sensor services (MITRE ATT&CK T1562.001), so monitor service stops and file changes here. The `Logs` folder (Microsoft.Tri.Sensor.log, -Errors.log) helps confirm sensor health gaps during an incident timeline. Unexpected executables in this path, or files not signed by Microsoft, are suspicious.
>

# purpose

During an update, the sensor updater service pulls the new version from the cloud service as a .cab file, validates its signature and extracts it to a new folder named after the version number in the sensor's installation folder; the sensor service then points to the new files and is restarted. The sensor logs are in the `Logs` subfolder of this version folder, and the real sensor version can be seen in the executable path or file version.

# common files found

| file | description |
| --- | --- |
| `Logs\Microsoft.Tri.Sensor.log` | Everything that happens in the sensor, including resolution and errors, in chronological order. |
| `Logs\Microsoft.Tri.Sensor-Errors.log` | Only errors caught by the sensor; used for health checks. |
| `Logs\Microsoft.Tri.Sensor.Updater.log` | Log of the sensor updater process. |
| `Logs\Microsoft.Tri.Sensor.Updater-Errors.log` | Only errors caught by the sensor updater. |
| `Logs\<log name>-Archived-00000` | Archived log created when a log reaches 50 MB; by default only 10 archives are kept per log. |
