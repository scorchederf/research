---
name: learn-path-note
description: Document a Windows file, directory or registry key path (exe, dll, folder, HKLM/HKCU key) as an Obsidian markdown note using only the Microsoft Learn tools, saved under kb/tools/os/structure.
---

# Learn path note

Turn a Windows path (e.g. `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe`) into a markdown note, sourced ONLY from Microsoft Learn.

## Steps

1. **Check tools.** The Microsoft Learn MCP tools (`microsoft_docs_search`, `microsoft_docs_fetch`) must be available (configured in `.mcp.json`). If they are not, say so and stop. Never fall back to web search or memory.
2. **Classify the path:**
   - `directory` - no file extension / ends in a folder
   - `executable` - .exe, .com, .bat, .cmd, .ps1, .msc
   - `file` - anything else (.dll, .sys, .ini, .xml, .evtx, ...)
   - `registry` - starts with a hive (HKLM, HKCU, HKU, HKCR, HKCC or HKEY_...). Normalise long hive names to the short form (`HKEY_LOCAL_MACHINE` -> `HKLM`).
   - Paths with placeholders (`<username>`, `<SID>`, `<n>`) or wildcards (`*.lnk`) are documented as the general location/pattern.
3. **Research.** Run 2-4 `microsoft_docs_search` queries (file name, file name + "command-line options", parent product/package). Then `microsoft_docs_fetch` the most relevant pages. For executables ALWAYS fetch the full command-line options page if one exists, so the table is complete and in page order.
4. **Write the note** using the template below.
5. **Save** to `kb/tools/os/structure/` mirroring the path: drop the drive letter, replace `\` with `/`, convert the whole path to **lowercase**, append `.md`. Keep spaces and punctuation. Create folders as needed.
   - `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe` -> `kb/tools/os/structure/program files (x86)/windows kits/10/debuggers/x64/windbg.exe.md`
   - Directory `C:\Windows\System32` -> `kb/tools/os/structure/windows/system32.md`
   - Registry: keep the short hive as the first folder: `HKCU\Software\Microsoft\Terminal Server Client\Default` -> `kb/tools/os/structure/hkcu/software/microsoft/terminal server client/default.md`
   - Characters not allowed in file names (`<`, `>`, `*`, `?`, `|`, `:`, `"`) are kept as-is on Linux; do not rename them.
6. Commit and push are handled by the caller (e.g. `/learn-batch`). When run alone, commit `Add Microsoft Learn note: <item>` and push to `main`.

## Rules

- Use only information from Microsoft Learn pages actually retrieved for this path. **Exception:** the `Claude said` blockquote under `## simple description` is written from Claude's own knowledge (see below).
- If a section has no Learn coverage, write `_Not documented on Microsoft Learn at {{yyyy/MM/dd HH:MM UTC}}_` (italics) with the current UTC time, e.g. `_Not documented on Microsoft Learn at 2026/11/21 05:17 UTC_`.
- Remove all `{{if}}` / `{{endif}}` lines and the sections that do not apply to the classified type.
- `created`: today's date, `YYYY-MM-DD`.
- `fullpath`: the full path exactly as given, in single quotes in the frontmatter, e.g. `fullpath: 'C:\Windows\System32\cmd.exe'`. Repeat it unquoted on the `**fullpath**:` line above `# description`.
- `aliases`: the file name plus any other names Learn uses (e.g. `WinDbg (Classic)`).
- `url`: YAML list of every Learn page used, without `#anchors` duplicates.
- `simple description`: a blockquote (see template) written from **Claude's own knowledge**, not limited to Learn. `{{datestamp}}` is today's date `YYYY-MM-DD`. Explain what it is in 3-5 plain sentences a junior SOC analyst can understand, then a `**SOC NOTE**:` line with security-relevant information that gives it value in an investigation (attacker abuse, MITRE ATT&CK techniques, forensic value, events or artifacts it produces). If Microsoft Learn has nothing on the item, add a final blockquote line `> _Not documented on Microsoft Learn at {{yyyy/MM/dd HH:MM UTC}}_` so readers know the explanation isn't Learn-sourced.
- `description`: 2-3 sentences - what it is, which package/product ships it, related tools.
- Code and commands: never use fenced code blocks in notes. Put every command in backticks inside a two-column table:

  | usage | description |
  | --- | --- |
  | `reg query "HKLM\SOFTWARE"` | What the command does. |

  This applies to `# typical use cases` (executables) and `# query` (registry). Escape `|` in cells as `\|`.
- Registry sections (Learn-only): `# hive` table with rows `hive`, `scope` (machine-wide / per-user) and `backing file` (e.g. `%SystemRoot%\System32\config\SOFTWARE`, `Ntuser.dat`); `# values` table (value name in backticks | type | description); `# subkeys` table (subkey in backticks | description); `# query` usage table with at least `reg query "<fullpath>"`. Omit a row rather than filling it with a not-documented line when the whole table has other content; use the italic not-documented line only when an entire section has no Learn coverage.
- Options table: every documented option, in page order; option in backticks with exact case (`` `-I[S]` ``); escape `|` in cells as `\|`; keep descriptions to one or two sentences and note mode restrictions (e.g. "(User mode only)").

## Template

```
---
created:
fullpath:
generator:
  - claude
  - microsoftlearn
tags:
aliases:
url:
---

**fullpath**:{{fullpath}}

# description


## simple description

> ### {{datestamp}} Claude said
> what is it in 3-5 sentences
>
> **SOC NOTE**: Add any security related information that makes it value in an investigation
>

# purpose


{{if directory}}

# common files found

{{endif}}

{{if executable }}

# typical use cases

| usage | description |
| --- | --- |
|     |     |

# options

| option    | description    |
| --- | --- |
|     |     |

{{endif}}

{{if registry}}

# hive

| property | value |
| --- | --- |
| hive |     |
| scope |     |
| backing file |     |

# values

| value name | type | description |
| --- | --- | --- |
|     |     |     |

# subkeys

| subkey | description |
| --- | --- |
|     |     |

# query

| usage | description |
| --- | --- |
| `reg query "{{fullpath}}"` | List the key's values. |

{{endif}}
```
