---
type: class
name: FTP_TLS
module: ftplib
lineno: 677
tags:
  - python
  - class
---

# Class: FTP_TLS

## Overview

A FTP subclass which adds TLS support to FTP as described
in RFC-4217.

Connect as usual to port 21 implicitly securing the FTP control
connection before authenticating.

Securing the data connection requires user to explicitly ask
for it by calling prot_p() method.

Usage example:
>>> from ftplib import FTP_TLS
>>> ftps = FTP_TLS('ftp.python.org')
>>> ftps.login()  # login anonymously previously securing control channel
'230 Guest login ok, access restrictions apply.'
>>> ftps.prot_p()  # switch to secure data connection
'200 Protection level set to P'
>>> ftps.retrlines('LIST')  # list directory content securely
total 9
drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 .
drwxr-xr-x   8 root     wheel        1024 Jan  3  1994 ..
drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 bin
drwxr-xr-x   2 root     wheel        1024 Jan  3  1994 etc
d-wxrwxr-x   2 ftp      wheel        1024 Sep  5 13:43 incoming
drwxr-xr-x   2 root     wheel        1024 Nov 17  1993 lib
drwxr-xr-x   6 1094     wheel        1024 Sep 13 19:07 pub
drwxr-xr-x   3 root     wheel        1024 Jan  3  1994 usr
-rw-r--r--   1 root     root          312 Aug  1  1994 welcome.msg
'226 Transfer complete.'
>>> ftps.quit()
'221 Goodbye.'
>>>

**Module:** [[Modules/ftplib|ftplib]]
**Line:** 677

## Inheritance

**Inherits from:**
- [[Classes/FTP|FTP]]

## Methods

### Constructors
- [[Functions/__init___3277|__init__()]] (line 711)

### Methods
- [[Functions/login_3278|login()]] (line 721)
- [[Functions/auth_3279|auth()]] (line 726)
- [[Functions/ccc_3280|ccc()]] (line 738)
- [[Functions/prot_p_3281|prot_p()]] (line 746)
- [[Functions/prot_c_3282|prot_c()]] (line 762)
- [[Functions/ntransfercmd_3283|ntransfercmd()]] (line 770)
- [[Functions/abort_3284|abort()]] (line 777)
