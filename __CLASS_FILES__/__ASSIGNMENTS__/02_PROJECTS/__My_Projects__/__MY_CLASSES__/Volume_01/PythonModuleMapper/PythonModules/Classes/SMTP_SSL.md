---
type: class
name: SMTP_SSL
module: smtplib
lineno: 1003
tags:
  - python
  - class
---

# Class: SMTP_SSL

## Overview

This is a subclass derived from SMTP that connects over an SSL
encrypted socket (to use this class you need a socket module that was
compiled with SSL support). If host is not specified, '' (the local
host) is used. If port is omitted, the standard SMTP-over-SSL port
(465) is used.  local_hostname and source_address have the same meaning
as they do in the SMTP class.  context also optional, can contain a
SSLContext.

**Module:** [[Modules/smtplib|smtplib]]
**Line:** 1003

## Inheritance

**Inherits from:**
- [[Classes/SMTP|SMTP]]

## Methods

### Constructors
- [[Functions/__init___3460|__init__()]] (line 1016)

### Methods
- [[Functions/_get_socket_3461|_get_socket()]] (line 1025)
