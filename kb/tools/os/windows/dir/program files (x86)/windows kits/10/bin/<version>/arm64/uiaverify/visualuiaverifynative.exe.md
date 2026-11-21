---
created: 2026-11-21
fullpath: 'c:\Program Files (x86)\Windows Kits\10\bin\<version>\arm64\UIAVerify\VisualUiaVerifyNative.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - windows-sdk
  - accessibility
aliases:
  - VisualUiaVerifyNative.exe
  - Visual UI Automation Verify
  - Visual UIA Verify
  - UIA Verify
url:
  - https://learn.microsoft.com/windows/win32/winauto/ui-automation-verify
  - https://learn.microsoft.com/windows/win32/winauto/visual-ui-automation-verify
  - https://learn.microsoft.com/windows/apps/design/accessibility/accessibility-testing
---

**fullpath**:c:\Program Files (x86)\Windows Kits\10\bin\<version>\arm64\UIAVerify\VisualUiaVerifyNative.exe

# description

VisualUIAVerifyNative.exe is Visual UI Automation Verify, the GUI driver for the UI Automation Test Library used for manual testing of a control's or application's Microsoft UI Automation implementation. It is installed with the Windows SDK in the `\bin\<version>\<platform>\UIAVerify` folder (this path is the ARM64 build). It is a legacy tool; Microsoft recommends Accessibility Insights instead.

## simple description

> ### 2026-11-21 Claude said
> Visual UIA Verify is a developer test tool from the Windows SDK that inspects the accessibility (UI Automation) tree of running applications and runs checks against controls. Developers use it to make sure buttons, text boxes and windows expose correct names and patterns for screen readers. It is only present on machines where the Windows SDK is installed, typically developer workstations.
>
> **SOC NOTE**: Low abuse profile, but UI Automation tooling can read and drive other applications' UI (similar to techniques used for T1056 input/screen capture and UI manipulation). Its presence outside developer machines, or execution from an unusual path or by an unexpected user, is worth noting; legitimate copies are Microsoft-signed under the Windows Kits folder.
>

# purpose

Provides an interface to UIA Test Library functionality without coding overhead. Its panes are the Automation Elements Tree (snapshot of elements with the desktop at the top), Tests (tests by type and priority), Test Results (XML logger views: Overall, All Results, Full Log, XML) and Properties (UI Automation properties, with the ability to invoke control pattern methods). It natively supports only the UIA Verify XML logger (WUIALoggerXml.dll). It does not typically need to run as administrator.

# typical use cases

| usage | description |
| --- | --- |
| `VisualUIAVerifyNative.exe` | Start Visual UIA Verify to manually test UI Automation on elements. |
| `VisualUIAVerifyNative.exe /NOCLIENTSIDEPROVIDER` | Start without loading the original UI Automation client-side provider. |

# options

| option | description |
| --- | --- |
| `/NOCLIENTSIDEPROVIDER` | Do not load the UI Automation client-side provider that shipped with the original release of UI Automation (loaded by default). |
