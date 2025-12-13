---
type: class
name: LMTP
module: smtplib
lineno: 1040
tags:
  - python
  - class
---

# Class: LMTP

## Overview

LMTP - Local Mail Transfer Protocol

The LMTP protocol, which is very similar to ESMTP, is heavily based
on the standard SMTP client. It's common to use Unix sockets for
LMTP, so our connect() method must support that as well as a regular
host:port server.  local_hostname and source_address have the same
meaning as they do in the SMTP class.  To specify a Unix socket,
you must use an absolute path as the host, starting with a '/'.

Authentication is supported, using the regular SMTP mechanism. When
using a Unix socket, LMTP generally don't support or require any
authentication, but your mileage might vary.

**Module:** [[Modules/smtplib|smtplib]]
**Line:** 1040

## Inheritance

**Inherits from:**
- [[Classes/SMTP|SMTP]]

## Methods

### Constructors
- [[Functions/__init___3462|__init__()]] (line 1056)

### Methods
- [[Functions/connect_3463|connect()]] (line 1062)
