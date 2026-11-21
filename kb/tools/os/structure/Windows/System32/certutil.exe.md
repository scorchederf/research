---
created: 2026-11-21
fullpath: 'C:\Windows\System32\certutil.exe'
generator:
  - claude
  - microsoftlearn
tags:
aliases:
  - certutil.exe
  - certutil
url:
  - https://learn.microsoft.com/windows-server/administration/windows-commands/certutil
  - https://learn.microsoft.com/windows/security/application-security/application-control/app-control-for-business/design/applications-that-can-bypass-appcontrol
---

**fullpath**:C:\Windows\System32\certutil.exe

# description

Certutil.exe is a command-line program installed as part of Certificate Services. It displays certification authority (CA) configuration, configures Certificate Services, backs up and restores CA components, and verifies certificates, key pairs and certificate chains. Microsoft notes it isn't recommended for production code and that not every version supports every verb; run `certutil -?` or `certutil -v -uSAGE` for the full list.

## simple description

> ### 2026-11-21 Claude said
> Certutil is a command-line tool built into Windows for working with certificates. Admins use it to view certificate details, check that certificates and their chains are valid, and manage a certificate authority (CA). It can also convert files between formats, such as encoding or decoding a file. Run with no options on a normal machine, it simply dumps information.
>
> **SOC NOTE**: Microsoft lists certutil.exe as an application that attackers can use to bypass App Control allow policies, and recommends blocking it where it isn't needed. Its encode and decode verbs (`-encodehex`, `-decodehex` and others) can transform files, and its `-GetKey` and `-RecoverKey` verbs can retrieve archived private keys, so any unexpected certutil run on an endpoint is worth checking.
>

# purpose

- Display and configure CA settings, back up and restore CA components.
- Dump, verify and decode certificates, CRLs, PFX files and ASN.1 data.
- Manage certificate stores (machine, user, enterprise, Group Policy) and smart card roots.
- Retrieve and recover archived private keys.

# typical use cases

- Dump a certificate or file: `certutil -dump File`
- Retrieve domain controller certificates: `certutil -dc cpandl-dc1 -DCInfo cpandl`
- Check whether a certificate is valid on the CA: `certutil -isvalid SerialNumber`
- Ping the AD CS request interface: `certutil -ping`
- Show all verbs, including hidden ones: `certutil -v -uSAGE`

# options

### Verbs

| option    | description    |
| --- | --- |
| `-dump` | Dumps the configuration information or files. |
| `-dumpPFX` | Dumps the PFX structure. |
| `-asn` | Parses and displays the contents of a file using Abstract Syntax Notation (ASN.1) syntax. File types include .CER, .DER and PKCS #7 formatted files. |
| `-decodehex` | Decodes a hexadecimal-encoded file. |
| `-encodehex` | Encodes a file in hexadecimal. |
| `-decode` | Decodes a Base64-encoded file. |
| `-encode` | Encodes a file to Base64. |
| `-deny` | Denies a pending request. |
| `-resubmit` | Resubmits a pending request. |
| `-setattributes` | Sets attributes for a pending certificate request. |
| `-setextension` | Set an extension for a pending certificate request. |
| `-revoke` | Revokes a certificate. |
| `-isvalid` | Displays the disposition of the current certificate. |
| `-getconfig` | Gets the default configuration string. |
| `-getconfig2` | Gets the default configuration string via ICertGetConfig. |
| `-getconfig3` | Gets configuration via ICertConfig. |
| `-ping` | Attempts to contact the Active Directory Certificate Services Request interface. |
| `-pingadmin` | Attempts to contact the Active Directory Certificate Services Admin interface. |
| `-CAInfo` | Displays information about the certification authority. |
| `-CAPropInfo` | Displays CA Property Type information. |
| `-ca.cert` | Retrieves the certificate for the certification authority. |
| `-ca.chain` | Retrieves the certificate chain for the certification authority. |
| `-GetCRL` | Gets a certificate revocation list (CRL). |
| `-CRL` | Publishes new certificate revocation lists (CRLs) or delta CRLs. |
| `-shutdown` | Shuts down the Active Directory Certificate Services. |
| `-installCert` | Installs a certification authority certificate. |
| `-renewCert` | Renews a certification authority certificate. |
| `-schema` | Dumps the schema for the certificate. |
| `-view` | Dumps the certificate view. |
| `-db` | Dumps the raw database. |
| `-deleterow` | Deletes a row from the server database. |
| `-backup` | Backs up the Active Directory Certificate Services. |
| `-backupDB` | Backs up the Active Directory Certificate Services database. |
| `-backupkey` | Backs up the Active Directory Certificate Services certificate and private key. |
| `-restore` | Restores the Active Directory Certificate Services. |
| `-restoredb` | Restores the Active Directory Certificate Services database. |
| `-restorekey` | Restores the Active Directory Certificate Services certificate and private key. |
| `-exportPFX` | Exports the certificates and private keys. For more information, see the `-store` parameter in this article. |
| `-importPFX` | Imports the certificates and private keys. For more information, see the `-store` parameter in this article. |
| `-dynamicfilelist` | Displays a dynamic file list. |
| `-databaselocations` | Displays database locations. |
| `-hashfile` | Generates and displays a cryptographic hash over a file. |
| `-store` | Dumps the certificate store. |
| `-enumstore` | Enumerates the certificate stores. |
| `-addstore` | Adds a certificate to the store. For more information, see the `-store` parameter in this article. |
| `-delstore` | Deletes a certificate from the store. For more information, see the `-store` parameter in this article. |
| `-verifystore` | Verifies a certificate in the store. For more information, see the `-store` parameter in this article. |
| `-repairstore` | Repairs a key association or update certificate properties or the key security descriptor. For more information, see the `-store` parameter in this article. |
| `-viewstore` | Dumps the certificates store. For more information, see the `-store` parameter in this article. |
| `-viewdelstore` | Deletes a certificate from the store. |
| `-UI` | Invokes the certutil interface. |
| `-TPMInfo` | Displays Trusted Platform Module Information. |
| `-attest` | Specifies that the certificate request file should be attested. |
| `-getcert` | Selects a certificate from a selection UI. |
| `-ds` | Displays directory service (DS) distinguished names (DNs). |
| `-dsDel` | Deletes DS DNs. |
| `-dsPublish` | Publishes a certificate or certificate revocation list (CRL) to Active Directory. |
| `-dsCert` | Displays DS certificates. |
| `-dsCRL` | Displays DS CRLs. |
| `-dsDeltaCRL` | Displays DS delta CRLs. |
| `-dsTemplate` | Displays DS template attributes. |
| `-dsAddTemplate` | Adds DS templates. |
| `-ADTemplate` | Displays Active Directory templates. |
| `-Template` | Displays the certificate enrollment policy templates. |
| `-TemplateCAs` | Displays the certification authorities (CAs) for a certificate template. |
| `-CATemplates` | Displays templates for the Certificate Authority. |
| `-SetCATemplates` | Sets the certificate templates that the Certificate Authority can issue. |
| `-SetCASites` | Manages site names, including setting, verifying, and deleting Certificate Authority site names. |
| `-enrollmentServerURL` | Displays, adds, or deletes enrollment server URLs associated with a CA. |
| `-ADCA` | Displays the Active Directory Certificate Authorities. |
| `-CA` | Displays the enrollment policy Certificate Authorities. |
| `-Policy` | Displays the enrollment policy. |
| `-PolicyCache` | Displays or deletes enrollment policy cache entries. |
| `-CredStore` | Displays, adds, or deletes Credential Store entries. |
| `-InstallDefaultTemplates` | Installs the default certificate templates. |
| `-URL` | Verifies certificate or CRL URLs. |
| `-URLCache` | Displays or deletes URL cache entries. |
| `-pulse` | Pulses an autoenrollment event or NGC task. |
| `-MachineInfo` | Displays information about the Active Directory machine object. |
| `-DCInfo` | Displays information about the domain controller. The default displays DC certificates without verification. |
| `-EntInfo` | Displays information about an enterprise Certificate Authority. |
| `-TCAInfo` | Displays information about the Certificate Authority. |
| `-SCInfo` | Displays information about the smart card. |
| `-SCRoots` | Manages smart card root certificates. |
| `-key` | Lists the keys stored in a key container. |
| `-delkey` | Deletes the named key container. |
| `-DeleteHelloContainer` | Deletes the Windows Hello container, removing all associated credentials that are stored on the device, including any WebAuthn and FIDO credentials. |
| `-verifykeys` | Verifies a public or private key set. |
| `-verify` | Verifies a certificate, certificate revocation list (CRL), or certificate chain. |
| `-verifyCTL` | Verifies the AuthRoot or Disallowed Certificates CTL. |
| `-syncWithWU` | Syncs certificates with Windows Update. |
| `-generateSSTFromWU` | Generates a store file that is synced with Windows Update. |
| `-generatePinRulesCTL` | Generates a Certificate Trust List (CTL) file that contains a list of pinning rules. |
| `-downloadOcsp` | Downloads the OCSP responses and writes to the directory. |
| `-generateHpkpHeader` | Generates the HPKP header using certificates in a specified file or directory. |
| `-flushCache` | Flushes the specified caches in selected process, such as, lsass.exe. |
| `-addEccCurve` | Adds an ECC Curve. |
| `-deleteEccCurve` | Deletes the ECC Curve. |
| `-displayEccCurve` | Displays the ECC Curve. |
| `-csplist` | Lists the cryptographic service providers (CSPs) installed on this machine for cryptographic operations. |
| `-csptest` | Tests the CSPs installed on this machine. |
| `-CNGConfig` | Displays CNG cryptographic configuration on this machine. |
| `-sign` | Re-signs a certificate revocation list (CRL) or certificate. |
| `-vroot` | Creates or deletes web virtual roots and file shares. |
| `-vocsproot` | Creates or deletes web virtual roots for an OCSP web proxy. |
| `-addEnrollmentServer` | Adds an Enrollment Server application and application pool if necessary for the specified Certificate Authority. This command doesn't install binaries or packages. |
| `-deleteEnrollmentServer` | Deletes an Enrollment Server application and application pool if necessary for the specified Certificate Authority. This command doesn't install binaries or packages. |
| `-addPolicyServer` | Add a Policy Server application and application pool, if necessary. This command doesn't install binaries or packages. |
| `-deletePolicyServer` | Deletes a Policy Server application and application pool, if necessary. This command doesn't remove binaries or packages. |
| `-Class` | Displays COM registry information. |
| `-7f` | Checks certificate for 0x7f length encodings. |
| `-oid` | Displays the object identifier or sets a display name. |
| `-error` | Displays the message text associated with an error code. |
| `-getsmtpinfo` | Gets Simple Mail Transfer Protocol (SMTP) information. |
| `-setsmtpinfo` | Sets SMTP information. |
| `-getreg` | Displays a registry value. |
| `-setreg` | Sets a registry value. |
| `-delreg` | Deletes a registry value. |
| `-importKMS` | Imports user keys and certificates into the server database for key archival. |
| `-ImportCert` | Imports a certificate file into the database. |
| `-GetKey` | Retrieves an archived private key recovery blob, generates a recovery script, or recovers archived keys. |
| `-RecoverKey` | Recovers an archived private key. |
| `-mergePFX` | Merges PFX files. |
| `-add-chain` | Adds a certificate chain. |
| `-add-pre-chain` | Adds a pre-certificate chain. |
| `-get-sth` | Gets a signed tree head. |
| `-get-sth-consistency` | Gets signed tree head changes. |
| `-get-proof-by-hash` | Gets proof of a hash from a timestamp server. |
| `-get-entries` | Retrieves entries from an event log. |
| `-get-roots` | Retrieves the root certificates from the certificate store. |
| `-get-entry-and-proof` | Retrieves an event log entry and its cryptographic proof. |
| `-VerifyCT` | Verifies a certificate against the Certificate Transparency log. |
| `-?` | Displays the list of parameters. |

### Options

| option    | description    |
| --- | --- |
| `-admin` | Use ICertAdmin2 for CA properties. |
| `-anonymous` | Use anonymous SSL credentials. |
| `-cert CertId` | Signing certificate. |
| `-clientcertificate clientCertId` | Use X.509 Certificate SSL credentials. For selection UI, use `-clientcertificate`. |
| `-config Machine\CAName` | Certificate Authority and computer name string. |
| `-csp provider` | Provider:**KSP** - Microsoft Software Key Storage Provider **TPM** - Microsoft Platform Crypto Provider **NGC** - Microsoft Passport Key Storage Provider **SC** - Microsoft Smart Card Key Storage Provider |
| `-dc DCName` | Target a specific Domain Controller. |
| `-enterprise` | Use the local machine enterprise registry certificate store. |
| `-f` | Force overwrite. |
| `-generateSSTFromWU SSTFile` | Generate SST by using the automatic update mechanism. |
| `-gmt` | Display times using GMT. |
| `-GroupPolicy` | Use the group policy certificate store. |
| `-idispatch` | Use IDispatch instead of COM native methods. |
| `-kerberos` | Use Kerberos SSL credentials. |
| `-location alternatestoragelocation` | `(-loc)` AlternateStorageLocation. |
| `-mt` | Display machine templates. |
| `-nocr` | Encode text without CR characters. |
| `-nocrlf` | Encode text without CR-LF characters. |
| `-nullsign` | Use the hash of the data as a signature. |
| `-oldpfx` | Use old PFX encryption. |
| `-out columnlist` | Comma-separated column list. |
| `-p password` | Password |
| `-pin PIN` | Smart card PIN. |
| `-policyserver URLorID` | Policy Server URL or ID. For selection U/I, use `-policyserver`. For all Policy Servers, use `-policyserver *` |
| `-privatekey` | Display password and private key data. |
| `-protect` | Protect keys with password. |
| `-protectto SAMnameandSIDlist` | Comma-separated SAM name/SID list. |
| `-restrict restrictionlist` | Comma-separated Restriction List. Each restriction consists of a column name, a relational operator, and a constant integer, string, or date. One column name may be preceded by a plus or minus sign to indicate the sort order. For example: `requestID = 47`, `+requestername >= a, requestername`, or `-requestername > DOMAIN, Disposition = 21`. |
| `-reverse` | Reverse Log and Queue columns. |
| `-seconds` | Display times using seconds and milliseconds. |
| `-service` | Use service certificate store. |
| `-sid` | Numeric SID:**22** - Local System**23** - Local Service**24** - Network Service |
| `-silent` | Use the `silent` flag to acquire crypt context. |
| `-split` | Split embedded ASN.1 elements, and save to files. |
| `-sslpolicy servername` | SSL Policy matching ServerName. |
| `-symkeyalg symmetrickeyalgorithm[,keylength]` | Name of the Symmetric Key Algorithm with optional key length. For example: `AES,128` or `3DES`. |
| `-syncWithWU DestinationDir` | Sync with Windows Update. |
| `-t timeout` | URL fetch timeout in milliseconds. |
| `-Unicode` | Write redirected output in Unicode. |
| `-UnicodeText` | Write output file in Unicode. |
| `-urlfetch` | Retrieve and verify AIA Certs and CDP CRLs. |
| `-user` | Use the HKEY\_CURRENT\_USER keys or certificate store. |
| `-username username` | Use named account for SSL credentials. For selection UI, use `-username`. |
| `-ut` | Display user templates. |
| `-v` | Provide more detailed (verbose) information. |
| `-v1` | Use V1 interfaces. |
