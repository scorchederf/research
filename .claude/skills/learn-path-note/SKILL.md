---
name: learn-path-note
description: Document a Windows file or directory path (exe, dll, folder) as an Obsidian markdown note using only the Microsoft Learn tools, saved under kb/tools/os/structure.
---

# Learn path note

Turn a Windows path (e.g. `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe`) into a markdown note, sourced ONLY from Microsoft Learn.

## Steps

1. **Check tools.** The Microsoft Learn MCP tools (`microsoft_docs_search`, `microsoft_docs_fetch`) must be available (configured in `.mcp.json`). If they are not, say so and stop. Never fall back to web search or memory.
2. **Classify the path:**
   - `directory` - no file extension / ends in a folder
   - `executable` - .exe, .com, .bat, .cmd, .ps1, .msc
   - `file` - anything else (.dll, .sys, .ini, .xml, .evtx, ...)
   - Paths with placeholders (`<username>`, `<SID>`, `<n>`) or wildcards (`*.lnk`) are documented as the general location/pattern.
3. **Research.** Run 2-4 `microsoft_docs_search` queries (file name, file name + "command-line options", parent product/package). Then `microsoft_docs_fetch` the most relevant pages. For executables ALWAYS fetch the full command-line options page if one exists, so the table is complete and in page order.
4. **Write the note** using the template below.
5. **Save** to `kb/tools/os/structure/` mirroring the path: drop the drive letter, replace `\` with `/`, append `.md`. Keep real folder names, spaces included. Create folders as needed.
   - `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe` -> `kb/tools/os/structure/Program Files (x86)/Windows Kits/10/Debuggers/x64/windbg.exe.md`
   - Directory `C:\Windows\System32` -> `kb/tools/os/structure/Windows/System32.md`
   - Characters not allowed in file names (`<`, `>`, `*`, `?`, `|`, `:`, `"`) are kept as-is on Linux; do not rename them.
6. Commit and push are handled by the caller (e.g. `/learn-batch`). When run alone, commit `Add Microsoft Learn note: <item>` and push to `main`.

## Rules

- Use only information from Microsoft Learn pages actually retrieved for this path.
- If a section has no Learn coverage, write `_Not documented on Microsoft Learn_`.
- Remove all `{{if}}` / `{{endif}}` lines and the sections that do not apply to the classified type.
- `created`: today's date, `YYYY-MM-DD`.
- `fullpath`: the full path exactly as given, in single quotes in the frontmatter, e.g. `fullpath: 'C:\Windows\System32\cmd.exe'`. Repeat it unquoted on the `**fullpath**:` line above `# description`.
- `aliases`: the file name plus any other names Learn uses (e.g. `WinDbg (Classic)`).
- `url`: YAML list of every Learn page used, without `#anchors` duplicates.
- `simple description`: 2-3 plain sentences.
- `description`: 2-3 sentences - what it is, which package/product ships it, related tools.
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


# purpose


{{if directory}}

# common files found

{{endif}}

{{if executable }}

# typical use cases


# options

| option    | description    |
| --- | --- |
|     |     |

{{endif}}
```
