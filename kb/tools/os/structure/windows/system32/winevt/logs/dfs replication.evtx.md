---
created: 2026-11-21
fullpath: 'C:\Windows\System32\winevt\Logs\DFS Replication.evtx'
generator:
  - claude
  - microsoftlearn
tags:
  - windows
  - file
  - eventlog
  - dfsr
aliases:
  - DFS Replication.evtx
  - DFS Replication event log
url:
  - https://learn.microsoft.com/windows-server/storage/dfs-replication/dfsr-faq
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/distributed-file-system-replication-not-replicate-files
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/dfsr-event-id-2213
  - https://learn.microsoft.com/troubleshoot/windows-server/networking/dfsr-diagnostics-shows-sharing-violations-events
---

**fullpath**:C:\Windows\System32\winevt\Logs\DFS Replication.evtx

# description

DFS Replication.evtx is the on-disk file for the "DFS Replication" event log (Source: DFSR), written by the DFS Replication service on Windows Server. It records conflicts, database errors, replication stops/resumes, and connectivity errors. Related tools include the DFS Replication Health Report and `dfsrdiag backlog`.

## simple description

> ### 2026-11-21 Claude said
> This is the Windows event log file for the DFS Replication service, which copies folders (including SYSVOL on domain controllers) between servers. It records when replication works, fails, hits conflicts, or recovers. Admins open it in Event Viewer under Applications and Services Logs.
>
> **SOC NOTE**: On domain controllers DFSR replicates SYSVOL, so this log helps time when malicious GPO/script changes (T1484.001) spread across DCs, and shows dirty shutdown/journal wrap or replication stops that may follow tampering or ransomware. Key IDs: 2213 (replication paused after dirty shutdown), 2004/2106 (database errors/recovery), 4302/4304 (sharing violations), 4312, 4406.
>

# purpose

Holds DFS Replication service events. Examples from Learn: informational event when a file conflict is resolved (loser moved to DfsrPrivate\ConflictandDeleted); event 2213 requiring `ResumeReplication` via WMI; events 2004 and 2106 for database failure and recovery; 4302/4304 sharing violations; 4312 (paging file on replicated volume, system log); 4406 per junction point encountered; connectivity errors when WAN links fail.
