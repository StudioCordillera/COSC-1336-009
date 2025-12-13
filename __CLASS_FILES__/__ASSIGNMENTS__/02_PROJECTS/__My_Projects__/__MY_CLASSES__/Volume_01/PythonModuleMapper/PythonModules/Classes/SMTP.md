---
type: class
name: SMTP
module: smtplib
lineno: 190
tags:
  - python
  - class
---

# Class: SMTP

## Overview

This class manages a connection to an SMTP or ESMTP server.
SMTP Objects:
    SMTP objects have the following attributes:
        helo_resp
            This is the message given by the server in response to the
            most recent HELO command.

        ehlo_resp
            This is the message given by the server in response to the
            most recent EHLO command. This is usually multiline.

        does_esmtp
            This is a True value _after you do an EHLO command_, if the
            server supports ESMTP.

        esmtp_features
            This is a dictionary, which, if the server supports ESMTP,
            will _after you do an EHLO command_, contain the names of the
            SMTP service extensions this server supports, and their
            parameters (if any).

            Note, all extension names are mapped to lower case in the
            dictionary.

    See each method's docstrings for details.  In general, there is a
    method of the same name to perform each SMTP command.  There is also a
    method called 'sendmail' that will do an entire mail transaction.
    

**Module:** [[Modules/smtplib|smtplib]]
**Line:** 190

## Inheritance

**Subclasses:**
- [[Classes/SMTP_SSL|SMTP_SSL]]
- [[Classes/LMTP|LMTP]]

## Methods

### Constructors
- [[Functions/__init___3426|__init__()]] (line 229)

### Magic Methods
- [[Functions/__enter___3427|__enter__()]] (line 277)
- [[Functions/__exit___3428|__exit__()]] (line 280)

### Methods
- [[Functions/set_debuglevel_3429|set_debuglevel()]] (line 290)
- [[Functions/_print_debug_3430|_print_debug()]] (line 299)
- [[Functions/_get_socket_3431|_get_socket()]] (line 305)
- [[Functions/connect_3432|connect()]] (line 315)
- [[Functions/send_3433|send()]] (line 348)
- [[Functions/putcmd_3434|putcmd()]] (line 367)
- [[Functions/getreply_3435|getreply()]] (line 380)
- [[Functions/docmd_3436|docmd()]] (line 429)
- [[Functions/helo_3437|helo()]] (line 435)
- [[Functions/ehlo_3438|ehlo()]] (line 445)
- [[Functions/has_extn_3439|has_extn()]] (line 496)
- [[Functions/help_3440|help()]] (line 500)
- [[Functions/rset_3441|rset()]] (line 506)
- [[Functions/_rset_3442|_rset()]] (line 511)
- [[Functions/noop_3443|noop()]] (line 523)
- [[Functions/mail_3444|mail()]] (line 527)
- [[Functions/rcpt_3445|rcpt()]] (line 548)
- [[Functions/data_3446|data()]] (line 556)
- [[Functions/verify_3447|verify()]] (line 585)
- [[Functions/expn_3448|expn()]] (line 592)
- [[Functions/ehlo_or_helo_if_needed_3449|ehlo_or_helo_if_needed()]] (line 599)
- [[Functions/auth_3450|auth()]] (line 616)
- [[Functions/auth_cram_md5_3451|auth_cram_md5()]] (line 664)
- [[Functions/auth_plain_3452|auth_plain()]] (line 673)
- [[Functions/auth_login_3453|auth_login()]] (line 678)
- [[Functions/login_3454|login()]] (line 686)
- [[Functions/starttls_3455|starttls()]] (line 752)
- [[Functions/sendmail_3456|sendmail()]] (line 797)
- [[Functions/send_message_3457|send_message()]] (line 901)
- [[Functions/close_3458|close()]] (line 978)
- [[Functions/quit_3459|quit()]] (line 991)
