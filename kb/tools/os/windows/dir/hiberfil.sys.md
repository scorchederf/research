---
created: 2026-11-21
fullpath: 'C:\hiberfil.sys'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - hibernation
  - power
aliases:
  - hiberfil.sys
  - Hiberfil.sys
  - hiberfile
  - hibernation file
url:
  - https://learn.microsoft.com/troubleshoot/windows-client/setup-upgrade-and-drivers/disable-and-re-enable-hibernation
  - https://learn.microsoft.com/windows/win32/power/system-power-states
  - https://learn.microsoft.com/windows-hardware/design/device-experiences/powercfg-command-line-options
  - https://learn.microsoft.com/windows-hardware/manufacture/desktop/compact-os
---

**fullpath**:C:\hiberfil.sys

# description

`Hiberfil.sys` is a hidden system file in the root folder of the drive where the OS is installed, reserved by the Windows Kernel Power Manager, that stores a copy of system memory for hibernation (S4), hybrid sleep and fast startup. It is managed with `powercfg /hibernate`.

## simple description

> ### 2026-11-21 Claude said
> hiberfil.sys is where Windows saves the contents of RAM when the PC hibernates, so it can resume exactly where it left off. It is also used by Fast Startup and hybrid sleep. It is a hidden file in the root of C: and can be several gigabytes. Turning hibernation off deletes it.
>
> **SOC NOTE**: Valuable for memory forensics: it can contain a compressed snapshot of RAM including processes, network connections, credentials and decrypted data from the last hibernate/fast-startup (tools like Volatility or Hibr2Bin can decompress it). Acquire it from disk images. `powercfg /h off` deletes it and destroys that evidence.
>

# purpose

Stores system memory on disk so the computer can hibernate; if the file isn't present the computer can't hibernate. Its size is roughly proportional to RAM: a full hiberfile is 40% of physical memory by default (hibernate, hybrid sleep, fast startup), a reduced one is 20% (fast startup only). `powercfg /h /type reduced` reduces it and `powercfg /h off` removes it.


