---
type: module
name: ssl
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\ssl.py
is_package: False
analyzed_at: 2025-12-10T03:46:19.338440
tags:
  - python
  - module
---

# Module: ssl

## Overview

This module provides some more Pythonic support for SSL.

Object types:

  SSLSocket -- subtype of socket.socket which does SSL over the socket

Exceptions:

  SSLError -- exception raised for I/O errors

Functions:

  cert_time_to_seconds -- convert time string used for certificate
                          notBefore and notAfter functions to integer
                          seconds past the Epoch (the time values
                          returned from time.time())

  get_server_certificate (addr, ssl_version, ca_certs, timeout) -- Retrieve the
                          certificate from the server at the specified
                          address and return it as a PEM-encoded string


Integer constants:

SSL_ERROR_ZERO_RETURN
SSL_ERROR_WANT_READ
SSL_ERROR_WANT_WRITE
SSL_ERROR_WANT_X509_LOOKUP
SSL_ERROR_SYSCALL
SSL_ERROR_SSL
SSL_ERROR_WANT_CONNECT

SSL_ERROR_EOF
SSL_ERROR_INVALID_ERROR_CODE

The following group define certificate requirements that one side is
allowing/requiring from the other side:

CERT_NONE - no certificates from the other side are required (or will
            be looked at if provided)
CERT_OPTIONAL - certificates are not required, but if provided will be
                validated, and if validation fails, the connection will
                also fail
CERT_REQUIRED - certificates are required, and will be validated, and
                if validation fails, the connection will also fail

The following constants identify various SSL protocol variants:

PROTOCOL_SSLv2
PROTOCOL_SSLv3
PROTOCOL_SSLv23
PROTOCOL_TLS
PROTOCOL_TLS_CLIENT
PROTOCOL_TLS_SERVER
PROTOCOL_TLSv1
PROTOCOL_TLSv1_1
PROTOCOL_TLSv1_2

The following constants identify various SSL alert message descriptions as per
http://www.iana.org/assignments/tls-parameters/tls-parameters.xml#tls-parameters-6

ALERT_DESCRIPTION_CLOSE_NOTIFY
ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
ALERT_DESCRIPTION_BAD_RECORD_MAC
ALERT_DESCRIPTION_RECORD_OVERFLOW
ALERT_DESCRIPTION_DECOMPRESSION_FAILURE
ALERT_DESCRIPTION_HANDSHAKE_FAILURE
ALERT_DESCRIPTION_BAD_CERTIFICATE
ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE
ALERT_DESCRIPTION_CERTIFICATE_REVOKED
ALERT_DESCRIPTION_CERTIFICATE_EXPIRED
ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN
ALERT_DESCRIPTION_ILLEGAL_PARAMETER
ALERT_DESCRIPTION_UNKNOWN_CA
ALERT_DESCRIPTION_ACCESS_DENIED
ALERT_DESCRIPTION_DECODE_ERROR
ALERT_DESCRIPTION_DECRYPT_ERROR
ALERT_DESCRIPTION_PROTOCOL_VERSION
ALERT_DESCRIPTION_INSUFFICIENT_SECURITY
ALERT_DESCRIPTION_INTERNAL_ERROR
ALERT_DESCRIPTION_USER_CANCELLED
ALERT_DESCRIPTION_NO_RENEGOTIATION
ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION
ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE
ALERT_DESCRIPTION_UNRECOGNIZED_NAME
ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE
ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\ssl.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:19

## Dependencies

This module imports:
- [[Modules/calendar|calendar]]
- [[Modules/os|os]]
- [[Modules/socket|socket]]
- [[Modules/enum|enum]]
- [[Modules/errno|errno]]
- [[Modules/time|time]]
- [[Modules/collections|collections]]

## Used By

This module is imported by:
- [[Modules/ftplib|ftplib]]
- [[Modules/poplib|poplib]]
- [[Modules/imaplib|imaplib]]
- [[Modules/smtplib|smtplib]]

## Classes

- [[Classes/_Enum|_Enum]] (line 1109)
- [[Classes/_IntEnum|_IntEnum]] (line 1349)
- [[Classes/_IntFlag|_IntFlag]] (line 1645)
- [[Classes/TLSVersion|TLSVersion]] (line 160)
- [[Classes/_TLSContentType|_TLSContentType]] (line 171)
- [[Classes/_TLSAlertType|_TLSAlertType]] (line 186)
- [[Classes/_TLSMessageType|_TLSMessageType]] (line 228)
- [[Classes/socket|socket]] (line 215)
- [[Classes/_ASN1Object|_ASN1Object]] (line 394)
- [[Classes/Purpose|Purpose]] (line 415)
- [[Classes/SSLContext|SSLContext]] (line 422)
- [[Classes/SSLObject|SSLObject]] (line 792)
- [[Classes/SSLSocket|SSLSocket]] (line 978)

## Functions

- [[Functions/namedtuple_2751|namedtuple()]] (line 358)
- [[Functions/_simple_enum_2769|_simple_enum()]] (line 1737)
- [[Functions/create_connection_2790|create_connection()]] (line 822)
- [[Functions/_dnsname_match_2791|_dnsname_match()]] (line 280)
- [[Functions/_inet_paton_2792|_inet_paton()]] (line 329)
- [[Functions/_ipaddress_match_2793|_ipaddress_match()]] (line 364)
- [[Functions/get_default_verify_paths_2794|get_default_verify_paths()]] (line 380)
- [[Functions/create_default_context_2815|create_default_context()]] (line 682)
- [[Functions/_create_unverified_context_2816|_create_unverified_context()]] (line 730)
- [[Functions/_sslcopydoc_2840|_sslcopydoc()]] (line 972)
- [[Functions/cert_time_to_seconds_2882|cert_time_to_seconds()]] (line 1450)
- [[Functions/DER_cert_to_PEM_cert_2883|DER_cert_to_PEM_cert()]] (line 1483)
- [[Functions/PEM_cert_to_DER_cert_2884|PEM_cert_to_DER_cert()]] (line 1493)
- [[Functions/get_server_certificate_2885|get_server_certificate()]] (line 1506)
- [[Functions/get_protocol_name_2886|get_protocol_name()]] (line 1528)
