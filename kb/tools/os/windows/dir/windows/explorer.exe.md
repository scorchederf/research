---
created: 2026-11-21
fullpath: 'C:\Windows\explorer.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - executable
  - shell
aliases:
  - 'explorer.exe'
  - 'Windows Explorer'
  - 'File Explorer'
url:
  - https://learn.microsoft.com/windows/win32/shell/developing-with-windows-explorer
  - https://learn.microsoft.com/windows/win32/shell/nse-junction
  - https://learn.microsoft.com/windows/win32/shell/how-to-use-a-shortcut-file-to-open-a-rooted-view
---

**fullpath**: C:\Windows\explorer.exe

# description

Windows Explorer, the resource-browsing and management application of the Windows Shell. It can be spawned as a separate process with ShellExecuteEx, automated through IShellWindows / IWebBrowser2, and its client area hosted via IExplorerBrowser. It accepts command-line arguments to open folder views, rooted views and namespace extensions by CLSID.

## simple description

> ### 2026-11-21 Claude said
> explorer.exe is the Windows shell process: it draws the desktop, taskbar and Start menu and runs File Explorer windows. One instance normally runs per signed-in user, started by userinit.exe at logon. It can also be run with a folder path or shell: location to open a window.
>
> **SOC NOTE**: Common injection/masquerade target: an explorer.exe outside C:\Windows, a second long-lived instance, or one with a parent other than userinit.exe is suspicious (T1036.005, T1055). Attackers use `explorer.exe <payload>` or `explorer.exe /root,<path>` to break process lineage (T1202 Indirect Command Execution). Its children reveal what users launched.
>

# purpose

Provides the Windows Shell user interface and file browsing; can open views of folders, namespace extensions and rooted views from the command line.

# typical use cases

| usage | description |
| --- | --- |
| `%SystemRoot%\Explorer.exe /e,::{MyExtension CLSID}` | Open a view of a namespace extension with a tree view. |
| `%SystemRoot%\Explorer.exe /e,::{MyExtension CLSID},objectname` | Open a view of an object inside an extension. |
| `Explorer.exe /e,/root,[Fully qualified path to the folder]` | Open a rooted view of a file system folder. |
| `explorer.exe shell:AppsFolder\Microsoft.WindowsCalculator_8wekyb3d8bbwe!App` | Launch a packaged app by its AUMID. |

# options

| option | description |
| --- | --- |
| `/e` | Displays a tree view; separate from following arguments with a comma. Omit for no tree view. |
| `/root,<object>` | Opens a rooted view of the specified folder or CLSID junction point. |
| `::{CLSID}` | Specifies a namespace extension or system virtual folder by CLSID; must be preceded by two colons. |
