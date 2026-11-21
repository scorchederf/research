---
created: 2026-11-21
fullpath: 'C:\Windows\System32\curl.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - network
  - lolbin
aliases:
  - curl.exe
  - curl
url:
  - https://learn.microsoft.com/windows/curl/
  - https://learn.microsoft.com/aspnet/core/mobile/native-mobile-backend
  - https://learn.microsoft.com/windows/wsl/install-manual
---

**fullpath**:C:\Windows\System32\curl.exe

# description

curl is a command-line tool for transferring data to and from a server, included with Windows and built from the upstream curl project, supporting HTTP, HTTPS, FTP, SFTP and more. In Windows PowerShell 5.1 `curl` is an alias for `Invoke-WebRequest`, so the real tool must be called as `curl.exe`; PowerShell 7+ has no such alias. Its sibling tool is `tar.exe`.

## simple description

> ### 2026-11-21 Claude said
> curl.exe is the standard open-source curl program that Microsoft ships in Windows 10 (1803) and later. It downloads and uploads data over many protocols and is used to test web APIs and fetch files from the command line. Because it is signed by Microsoft and always present, it is trusted by many security tools.
>
> **SOC NOTE**: A popular living-off-the-land binary for Ingress Tool Transfer (T1105) and exfiltration (T1048/T1567, e.g. `-T` / `-F` / `-d @file` uploads). Alert on curl.exe spawned by Office, scripts, mshta, rundll32 or services, downloads to %TEMP%/%PUBLIC%/ProgramData followed by execution, use of `-k`, raw IPs, or paste/file-sharing domains. Capture command lines via 4688/Sysmon 1 and network via Sysmon 3/DNS 22.
>

# purpose

Calls REST APIs, downloads files and tests endpoints without installing extra tools; the same flags and behavior as curl on Linux and macOS apply. The full list of options is available from `curl --help` or the official curl documentation.

# typical use cases

| usage | description |
| --- | --- |
| `curl -O https://example.com/file.zip` | Download a file, keeping its remote name. |
| `curl https://api.example.com/data` | Make a GET request and print the response. |
| `curl -X POST https://api.example.com/items -H "Content-Type: application/json" -d '{"name":"widget"}'` | Send a JSON POST request. |
| `curl.exe -LR -o ubuntu-2404.AppxBundle <url>` | Download a file to a named output file from PowerShell, invoking the real curl instead of the alias. |
| `curl -v -X GET 'https://localhost:5001/api/todoitems/'` | Verbose GET request for API testing and troubleshooting. |
| `Remove-Item Alias:curl` | Remove the Windows PowerShell 5.1 alias so `curl` runs curl.exe. |

# options

| option | description |
| --- | --- |
| `-O` | Download a file (used in the Learn download example). |
| `-X` | Specifies the HTTP method for the request, e.g. `-X GET` or `-X POST`. |
| `-H` | Adds a request header, e.g. Content-Type. |
| `-d` | Sends request body data. |
| `-v` | Activates verbose mode, showing detailed information about the HTTP response. |
| `-o` | Writes output to the named file (used with `-LR` in the WSL download example). |
| `--help` | Lists the full set of options. |
