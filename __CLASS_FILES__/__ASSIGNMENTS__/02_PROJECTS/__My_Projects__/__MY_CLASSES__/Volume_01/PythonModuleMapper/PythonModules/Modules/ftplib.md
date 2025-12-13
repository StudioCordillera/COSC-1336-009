---
type: module
name: ftplib
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\ftplib.py
is_package: False
analyzed_at: 2025-12-10T03:46:20.557155
tags:
  - python
  - module
---

# Module: ftplib

## Overview

An FTP client class and some helper functions.

Based on RFC 959: File Transfer Protocol (FTP), by J. Postel and J. Reynolds

Example:

>>> from ftplib import FTP
>>> ftp = FTP('ftp.python.org') # connect to host, default port
>>> ftp.login() # default, i.e.: user anonymous, passwd anonymous@
'230 Guest login ok, access restrictions apply.'
>>> ftp.retrlines('LIST') # list directory contents
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
>>> ftp.quit()
'221 Goodbye.'
>>>

A nice test that reveals some of the network dialogue would be:
python ftplib.py -d localhost -l -p -l

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\ftplib.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:20

## Dependencies

This module imports:
- [[Modules/re|re]]
- [[Modules/socket|socket]]
- [[Modules/ssl|ssl]]
- [[Modules/netrc|netrc]]

## Classes

- [[Classes/Error|Error]] (line 57)
- [[Classes/error_reply|error_reply]] (line 58)
- [[Classes/error_temp|error_temp]] (line 59)
- [[Classes/error_perm|error_perm]] (line 60)
- [[Classes/error_proto|error_proto]] (line 61)
- [[Classes/FTP|FTP]] (line 74)
- [[Classes/FTP_TLS|FTP_TLS]] (line 677)

## Functions

- [[Functions/parse150_3285|parse150()]] (line 792)
- [[Functions/parse227_3286|parse227()]] (line 812)
- [[Functions/parse229_3287|parse229()]] (line 831)
- [[Functions/parse257_3288|parse257()]] (line 852)
- [[Functions/print_line_3289|print_line()]] (line 874)
- [[Functions/ftpcp_3290|ftpcp()]] (line 879)
- [[Functions/test_3291|test()]] (line 901)
