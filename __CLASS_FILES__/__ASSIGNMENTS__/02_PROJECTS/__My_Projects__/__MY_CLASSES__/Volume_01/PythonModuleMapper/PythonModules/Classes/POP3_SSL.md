---
type: class
name: POP3_SSL
module: poplib
lineno: 430
tags:
  - python
  - class
---

# Class: POP3_SSL

## Overview

POP3 client class over SSL connection

Instantiate with: POP3_SSL(hostname, port=995, context=None)

       hostname - the hostname of the pop3 over ssl server
       port - port number
       context - a ssl.SSLContext

See the methods of the parent class POP3 for more documentation.

**Module:** [[Modules/poplib|poplib]]
**Line:** 430

## Inheritance

**Inherits from:**
- [[Classes/POP3|POP3]]

## Methods

### Constructors
- [[Functions/__init___3320|__init__()]] (line 442)

### Methods
- [[Functions/_create_socket_3321|_create_socket()]] (line 449)
- [[Functions/stls_3322|stls()]] (line 455)
