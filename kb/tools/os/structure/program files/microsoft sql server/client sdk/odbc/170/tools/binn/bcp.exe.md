---
created: 2026-11-21
fullpath: 'C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\bcp.exe'
generator:
  - claude
  - microsoftlearn
tags:
  - sql-server
  - executable
aliases:
  - bcp.exe
  - bcp
  - bulk copy program utility
url:
  - https://learn.microsoft.com/sql/tools/bcp/bcp-utility?view=sql-server-ver17
  - https://learn.microsoft.com/sql/tools/bcp/bcp-use-utility?view=sql-server-ver17
---

**fullpath**:C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\170\Tools\Binn\bcp.exe

# description

The bulk copy program utility (bcp) bulk copies data between an instance of the SQL Server Database Engine and a data file in a user-specified format. This copy is installed with the SQL Server command-line utilities on top of ODBC Driver 17 (`ODBC\170`); related tools include sqlcmd.

## simple description

> ### 2026-11-21 Claude said
> bcp.exe is Microsoft's command-line tool for moving large amounts of data in or out of SQL Server tables. It can export a table or the result of a query to a flat file, import a file into a table, or create format files. It ships with SQL Server and the "Microsoft Command Line Utilities for SQL Server" package. DBAs use it for bulk loads and ETL.
>
> **SOC NOTE**: bcp `out`/`queryout` is an effective data-exfiltration and collection tool (MITRE ATT&CK T1005/T1213, staging for T1048) - a single command dumps whole tables (e.g. credentials, PII) to a file. `-P` puts SQL passwords in the process command line (Event 4688/Sysmon 1). Hunt for bcp launched by sqlservr.exe via xp_cmdshell, by web shells, or writing to temp/share paths, and for `queryout` against sensitive tables.
>

# purpose

Import large numbers of new rows into Database Engine tables or export data out of tables into data files. Except with `queryout`, it requires no knowledge of Transact-SQL. Syntax: `bcp [database_name.]schema.{table_name | view_name | "query"} {in data_file | out data_file | queryout data_file | format nul} [options]`.

# typical use cases

- Export a table: `bcp dbo.T1 out T1.txt -T -S <server_name> -d tempdb -w -t ,`.
- Import a data file into a table (`in`), optionally with `-h "TABLOCK"` or `-b` batching.
- Export the results of a query with `queryout`.
- Generate a format file with `format nul -f <file> [-x]`.

# options

| option    | description    |
| --- | --- |
| `database_name` | Database containing the table or view; defaults to the user's default database. |
| `schema` | Owner of the table or view. |
| `table_name` | Destination table (`in`) or source table (`out`). |
| `view_name` | Destination view (`in`, only if all columns refer to the same table) or source view (`out`). |
| `"query"` | Transact-SQL query returning a result set; requires `queryout`. |
| `in` | Copies data from a file into the database table or view. |
| `out` | Copies data from the table or view to a file; an existing file is overwritten. |
| `data_file` | Full path of the data file (1-255 characters). |
| `queryout` | Copies data from a query. |
| `format` | Creates a format file based on `-n`, `-c`, `-w` or `-N`; requires `-f` and `nul` as value. |
| `-q` | Executes `SET QUOTED_IDENTIFIER ON`; use for names containing spaces or single quotes. |
| `-S [server_name[\instance_name]]` | SQL Server instance to connect to, or a DSN when `-D` is used. |
| `-d database_name` | Database to connect to. |
| `-U login_id` | Login ID used to connect. |
| `-P password` | Password for the login ID; prompts if omitted. |
| `-G` | Authenticate with Microsoft Entra ID (Azure SQL, Fabric, Synapse, SQL Server 2022+). |
| `-D` | Interprets the `-S` value as a data source name (DSN). |
| `-K application_intent` | Application workload type; only `ReadOnly` (needed for readable secondary replicas). |
| `-l login_timeout` | Login timeout in seconds (default 15; 0 = infinite). |
| `-H hostname_in_certificate` | Host name used to validate the server certificate. |
| `-J server_certificate` | Path to a PEM file with the server certificate to trust. |
| `-T` | Trusted connection using integrated security; otherwise `-U` and `-P` are needed. |
| `-Y[s\|m\|o]` | TLS encryption: Strict, Mandatory (default) or Optional (bcp 18+). |
| `-u` | Trust server certificate (bcp 18+). |
| `-c` | Character data type; tab field separator and `\r\n` row terminator; incompatible with `-w`. |
| `-C { ACP \| OEM \| RAW \| code_page }` | Code page of the data in the data file (Windows only). |
| `-n` | Uses native (database) data types. |
| `-N` | Native types for noncharacter data and Unicode for character data (Windows only). |
| `-w` | Uses Unicode characters (nchar); incompatible with `-c`. |
| `-z[0\|1]` | Enables native vector data type support; `-z0` float32, `-z1` float16. |
| `-f format_file` | Full path of a format file to create (with `format`) or use (with `in`/`out`). |
| `-x` | Generates an XML format file; used with `format` and `-f` (Windows only). |
| `-a packet_size` | Bytes per network packet, 4096-65535 (default 4096). |
| `-b batch_size` | Rows per batch of imported data, each committed as a separate transaction. |
| `-h "hints [, ...n]"` | Bulk import hints: ORDER, ROWS_PER_BATCH, KILOBYTES_PER_BATCH, TABLOCK, CHECK_CONSTRAINTS, FIRE_TRIGGERS (Windows only). |
| `-m max_errors` | Maximum syntax errors before the operation is canceled (default 10). |
| `-F first_row` | First row to export or import (1-based). |
| `-L last_row` | Last row to export or import. |
| `-r row_term` | Row terminator (default `\n`). |
| `-t field_term` | Field terminator (default `\t`). |
| `-k` | Empty columns keep a null value instead of default values. |
| `-E` | Uses identity values from the imported data file. |
| `-i input_file` | Response file with answers to interactive prompts (Windows only). |
| `-o output_file` | File that receives redirected command-prompt output (Windows only). |
| `-e err_file` | Error file storing rows that couldn't be transferred. |
| `-V (80 \| 90 \| ... \| 170)` | Uses data types from an earlier SQL Server version (Windows only). |
| `-R` | Uses client regional format for currency, date and time data. |
| `-v` | Reports the bcp version number and copyright. |
