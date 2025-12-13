---
type: class
name: IMAP4_SSL
module: imaplib
lineno: 1293
tags:
  - python
  - class
---

# Class: IMAP4_SSL

## Overview

IMAP4 client class over SSL connection

Instantiate with: IMAP4_SSL([host[, port[, ssl_context[, timeout=None]]]])

        host - host's name (default: localhost);
        port - port number (default: standard IMAP4 SSL port);
        ssl_context - a SSLContext object that contains your certificate chain
                      and private key (default: None)
        timeout - socket timeout (default: None) If timeout is not given or is None,
                  the global default socket timeout is used

for more documentation see the docstring of the parent class IMAP4.

**Module:** [[Modules/imaplib|imaplib]]
**Line:** 1293

## Inheritance

**Inherits from:**
- [[Classes/IMAP4|IMAP4]]

## Methods

### Constructors
- [[Functions/__init___3399|__init__()]] (line 1310)

### Methods
- [[Functions/_create_socket_3400|_create_socket()]] (line 1317)
- [[Functions/open_3401|open()]] (line 1322)
