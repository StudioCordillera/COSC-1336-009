---
type: class
name: POP3
module: poplib
lineno: 51
tags:
  - python
  - class
---

# Class: POP3

## Overview

This class supports both the minimal and optional command sets.
Arguments can be strings or integers (where appropriate)
(e.g.: retr(1) and retr('1') both work equally well.

Minimal Command Set:
        USER name               user(name)
        PASS string             pass_(string)
        STAT                    stat()
        LIST [msg]              list(msg = None)
        RETR msg                retr(msg)
        DELE msg                dele(msg)
        NOOP                    noop()
        RSET                    rset()
        QUIT                    quit()

Optional Commands (some servers support these):
        RPOP name               rpop(name)
        APOP name digest        apop(name, digest)
        TOP msg n               top(msg, n)
        UIDL [msg]              uidl(msg = None)
        CAPA                    capa()
        STLS                    stls()
        UTF8                    utf8()

Raises one exception: 'error_proto'.

Instantiate with:
        POP3(hostname, port=110)

NB:     the POP protocol locks the mailbox from user
        authorization until QUIT, so be sure to get in, suck
        the messages, and quit, each time you access the
        mailbox.

        POP is a line-based protocol, which means large mail
        messages consume lots of python cycles reading them
        line-by-line.

        If it's available on your mail server, use IMAP4
        instead, it doesn't suffer from the two problems
        above.

**Module:** [[Modules/poplib|poplib]]
**Line:** 51

## Inheritance

**Subclasses:**
- [[Classes/POP3_SSL|POP3_SSL]]

## Methods

### Constructors
- [[Functions/__init___3292|__init__()]] (line 98)

### Methods
- [[Functions/_create_socket_3293|_create_socket()]] (line 109)
- [[Functions/_putline_3294|_putline()]] (line 114)
- [[Functions/_putcmd_3295|_putcmd()]] (line 122)
- [[Functions/_getline_3296|_getline()]] (line 132)
- [[Functions/_getresp_3297|_getresp()]] (line 153)
- [[Functions/_getlongresp_3298|_getlongresp()]] (line 163)
- [[Functions/_shortcmd_3299|_shortcmd()]] (line 179)
- [[Functions/_longcmd_3300|_longcmd()]] (line 186)
- [[Functions/getwelcome_3301|getwelcome()]] (line 193)
- [[Functions/set_debuglevel_3302|set_debuglevel()]] (line 197)
- [[Functions/user_3303|user()]] (line 203)
- [[Functions/pass__3304|pass_()]] (line 211)
- [[Functions/stat_3305|stat()]] (line 221)
- [[Functions/list_3306|list()]] (line 245)
- [[Functions/retr_3307|retr()]] (line 259)
- [[Functions/dele_3308|dele()]] (line 267)
- [[Functions/noop_3309|noop()]] (line 275)
- [[Functions/rset_3310|rset()]] (line 283)
- [[Functions/quit_3311|quit()]] (line 288)
- [[Functions/close_3312|close()]] (line 294)
- [[Functions/rpop_3313|rpop()]] (line 322)
- [[Functions/apop_3314|apop()]] (line 329)
- [[Functions/top_3315|top()]] (line 350)
- [[Functions/uidl_3316|uidl()]] (line 359)
- [[Functions/utf8_3317|utf8()]] (line 371)
- [[Functions/capa_3318|capa()]] (line 377)
- [[Functions/stls_3319|stls()]] (line 406)
