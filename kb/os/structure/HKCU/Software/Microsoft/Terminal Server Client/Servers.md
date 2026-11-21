---
created: 2026-11-21
fullpath: 'HKCU\Software\Microsoft\Terminal Server Client\Servers'
generator:
  - claude
  - microsoftlearn
tags:
  - registry/terminal-server-client
aliases:
  - Servers
  - HKCU\Software\Microsoft\Terminal Server Client\Servers
  - HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers
url:
  - https://learn.microsoft.com/troubleshoot/windows-server/remote/remove-entries-from-remote-desktop-connection-computer
  - https://learn.microsoft.com/windows/win32/termserv/virtual-channel-client-registration
---

**fullpath**:HKCU\Software\Microsoft\Terminal Server Client\Servers

# description

_Not documented on Microsoft Learn_ — no Learn page describes the `Servers` subkey itself. Its parent, `HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client`, is the per-user registry location for the Windows Remote Desktop Connection client. Learn documents two sibling subkeys: `Default` (holds the MRU list of computers shown in the Remote Desktop Connection **Computer** box) and `Default\Addins` / `<connection>\Addins` (virtual channel client DLL registration).

## simple description

A per-user registry key under the Remote Desktop Connection client's settings. Microsoft Learn does not document what the `Servers` subkey stores. Its sibling `Default` key holds the history of computers you have connected to.

# purpose

_Not documented on Microsoft Learn_ for the `Servers` subkey.

Related, documented behaviour of the parent key:

- **`...\Terminal Server Client\Default`**: every new Remote Desktop Connection destination is written as `MRU0`, and older entries shift down (`MRU1`, `MRU2`, ...). Values are `REG_SZ` and can hold an FQDN or an IP address, e.g. `MRU0 REG_SZ 192.168.16.60`, `MRU1 REG_SZ computer.domain.com`. The client has no built-in way to clear this list; entries are removed by deleting the `MRUnumber` values in Registry Editor.
- **`...\Terminal Server Client\Default\Addins`**: subkeys here register virtual channel client DLLs for all connections (`Name = DLLname`, `REG_SZ` or `REG_EXPAND_SZ`).
- **`...\Terminal Server Client\<connection>\Addins`**: same as above, but applies only to the named connection.
- On the Mac client, the equivalent history is the file `Users:Username:Library:Preferences:Microsoft:RDC Client:Recent Servers`.

# common files found

_Not documented on Microsoft Learn_ — no subkeys or values under `Servers` are listed on Learn.
