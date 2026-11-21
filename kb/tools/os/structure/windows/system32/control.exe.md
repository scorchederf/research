---
created: 2026-11-21
fullpath: 'C:\Windows\System32\control.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - control-panel
aliases:
  - control.exe
  - Control Panel
url:
  - https://learn.microsoft.com/windows/win32/shell/executing-control-panel-items
  - https://learn.microsoft.com/windows/win32/shell/controlpanel-canonical-names
  - https://learn.microsoft.com/windows/win32/shell/how-to-register-dll-control-panel-item-registration-
  - https://learn.microsoft.com/windows/client-management/mdm/policy-csp-admx-controlpanel
---

**fullpath**:C:\Windows\System32\control.exe

# description

control.exe is the Windows Control Panel launcher. It opens Control Panel itself or starts a specific Control Panel item, either by module name (a .cpl file) or, on Windows Vista and later, by its canonical name. Items are registered in the registry (Cpls key, System.ApplicationName) and can be restricted with the RestrictCpls policy.

## simple description

> ### 2026-11-21 Claude said
> control.exe is the program that opens the Windows Control Panel. When given an argument it opens a specific applet, such as `control.exe sysdm.cpl` for System Properties or `control.exe /name Microsoft.WindowsUpdate`. Control Panel applets (.cpl files) are really DLLs that control.exe loads through rundll32/shell32. It is a normal, signed Windows binary used every day by users.
>
> **SOC NOTE**: Attackers abuse control.exe to proxy-execute malicious code by passing a crafted .cpl (DLL) file, e.g. `control.exe C:\Users\Public\evil.cpl` (MITRE ATT&CK T1218.002 System Binary Proxy Execution: Control Panel). Malicious items can also be registered for persistence under `HKCU/HKLM\Software\Microsoft\Windows\CurrentVersion\Control Panel\Cpls`. Hunt for control.exe loading .cpl files from user-writable paths, child rundll32.exe with odd .cpl paths, and new Cpls registry values.
>

# purpose

Opens Control Panel or starts a Control Panel item directly from the command line or programmatically (e.g. via WinExec). In Windows Vista and later, the preferred method is the item's canonical name, a non-localized string declared in the registry (convention "CorporationName.ControlPanelItemName"), which abstracts the item's module name.

# typical use cases

- Open Control Panel: `control.exe`.
- Open a .cpl item: `control.exe MyCpl.cpl`.
- Open a specific tab of a legacy item: `control.exe sysdm.cpl,,3`.
- Open an item by canonical name: `control.exe /name Microsoft.WindowsUpdate`.
- Open a sub-page: `control.exe /name Microsoft.Mouse /page 2` (pages listed in Canonical Names of Control Panel Items).

# options

| option    | description    |
| --- | --- |
| `<module>.cpl[,,<tab>]` | Starts the Control Panel item implemented by the named .cpl file, optionally opening a particular tab (tab numbering may differ between Windows versions). |
| `/name <canonicalName>` | Starts a Control Panel item by its canonical name (Windows Vista and later). |
| `/page <pageName>` | Used with `/name` to open a specific sub-page in the item. |
