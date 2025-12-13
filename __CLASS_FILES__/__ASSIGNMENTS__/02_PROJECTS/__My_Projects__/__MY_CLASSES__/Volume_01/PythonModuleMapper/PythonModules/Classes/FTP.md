---
type: class
name: FTP
module: ftplib
lineno: 74
tags:
  - python
  - class
---

# Class: FTP

## Overview

An FTP client class.

To create a connection, call the class using these arguments:
        host, user, passwd, acct, timeout, source_address, encoding

The first four arguments are all strings, and have default value ''.
The parameter ´timeout´ must be numeric and defaults to None if not
passed, meaning that no timeout will be set on any ftp socket(s).
If a timeout is passed, then this is now the default timeout for all ftp
socket operations for this instance.
The last parameter is the encoding of filenames, which defaults to utf-8.

Then use self.connect() with optional host and port argument.

To download a file, use ftp.retrlines('RETR ' + filename),
or ftp.retrbinary() with slightly different arguments.
To upload a file, use ftp.storlines() or ftp.storbinary(),
which have an open file as argument (see their definitions
below for details).
The download/upload functions first issue appropriate TYPE
and PORT or PASV commands.

**Module:** [[Modules/ftplib|ftplib]]
**Line:** 74

## Inheritance

**Subclasses:**
- [[Classes/FTP_TLS|FTP_TLS]]

## Methods

### Constructors
- [[Functions/__init___3236|__init__()]] (line 109)

### Magic Methods
- [[Functions/__enter___3237|__enter__()]] (line 125)
- [[Functions/__exit___3238|__exit__()]] (line 129)

### Methods
- [[Functions/connect_3239|connect()]] (line 139)
- [[Functions/getwelcome_3240|getwelcome()]] (line 165)
- [[Functions/set_debuglevel_3241|set_debuglevel()]] (line 172)
- [[Functions/set_pasv_3242|set_pasv()]] (line 181)
- [[Functions/sanitize_3243|sanitize()]] (line 188)
- [[Functions/putline_3244|putline()]] (line 195)
- [[Functions/putcmd_3245|putcmd()]] (line 205)
- [[Functions/getline_3246|getline()]] (line 211)
- [[Functions/getmultiline_3247|getmultiline()]] (line 229)
- [[Functions/getresp_3248|getresp()]] (line 243)
- [[Functions/voidresp_3249|voidresp()]] (line 257)
- [[Functions/abort_3250|abort()]] (line 264)
- [[Functions/sendcmd_3251|sendcmd()]] (line 278)
- [[Functions/voidcmd_3252|voidcmd()]] (line 283)
- [[Functions/sendport_3253|sendport()]] (line 288)
- [[Functions/sendeprt_3254|sendeprt()]] (line 298)
- [[Functions/makeport_3255|makeport()]] (line 311)
- [[Functions/makepasv_3256|makepasv()]] (line 324)
- [[Functions/ntransfercmd_3257|ntransfercmd()]] (line 336)
- [[Functions/transfercmd_3258|transfercmd()]] (line 391)
- [[Functions/login_3259|login()]] (line 395)
- [[Functions/retrbinary_3260|retrbinary()]] (line 421)
- [[Functions/retrlines_3261|retrlines()]] (line 444)
- [[Functions/storbinary_3262|storbinary()]] (line 479)
- [[Functions/storlines_3263|storlines()]] (line 505)
- [[Functions/acct_3264|acct()]] (line 536)
- [[Functions/nlst_3265|nlst()]] (line 541)
- [[Functions/dir_3266|dir()]] (line 550)
- [[Functions/mlsd_3267|mlsd()]] (line 565)
- [[Functions/rename_3268|rename()]] (line 593)
- [[Functions/delete_3269|delete()]] (line 600)
- [[Functions/cwd_3270|cwd()]] (line 608)
- [[Functions/size_3271|size()]] (line 621)
- [[Functions/mkd_3272|mkd()]] (line 629)
- [[Functions/rmd_3273|rmd()]] (line 638)
- [[Functions/pwd_3274|pwd()]] (line 642)
- [[Functions/quit_3275|quit()]] (line 651)
- [[Functions/close_3276|close()]] (line 657)
