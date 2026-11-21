---
created: 2026-11-21
fullpath: 'c:\windows\system32\psr.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - troubleshooting
aliases:
  - "psr.exe"
  - "Steps Recorder"
  - "Problem Steps Recorder"
url:
  - https://learn.microsoft.com/microsoft-365/enterprise/performance-troubleshooting-plan
---

**fullpath**: c:\windows\system32\psr.exe

# description

psr.exe is Steps Recorder (Problem Steps Recorder), a built-in Windows tool that records a user's actions as a sequence of screenshots with descriptions and timestamps. It is used to document and reproduce issues for support, alongside traces such as Network Monitor and HTTPWatch.

## simple description

> ### 2026-11-21 Claude said
> Steps Recorder captures what a user clicks and types, taking a screenshot for each step, and saves it all as a zipped MHT report. Support teams ask users to run it to show how a problem happens. It is built into Windows (being deprecated in newer releases). The output includes timestamps that help correlate with other logs.
>
> **SOC NOTE**: psr.exe can be abused as a stealthy screen-capture tool (T1113 Screen Capture), e.g. `psr /start /gui 0 /output <file>.zip` records silently in the background. Alert on psr.exe started with /gui 0 or by scripts, and on zip outputs written to unusual locations.
>

# purpose

Records the steps a user takes to reproduce an issue. Start it via Start > Run > PSR.exe, click Start Record, reproduce the issue (optionally Add Comments), click Stop Record, then Save. The date and time is recorded, linking the recording to other traces in time.

# typical use cases

| usage | description |
| --- | --- |
| `psr.exe` | Open Steps Recorder to start, comment, stop and save a recording. |

# options

_Not documented on Microsoft Learn at 2026/11/21 08:48 UTC_
