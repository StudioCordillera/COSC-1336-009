---
type: module
name: smtplib
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\smtplib.py
is_package: False
analyzed_at: 2025-12-10T03:46:21.012771
tags:
  - python
  - module
---

# Module: smtplib

## Overview

SMTP/ESMTP client class.

This should follow RFC 821 (SMTP), RFC 1869 (ESMTP), RFC 2554 (SMTP
Authentication) and RFC 2487 (Secure SMTP over TLS).

Notes:

Please remember, when doing ESMTP, that the names of the SMTP service
extensions are NOT the same thing as the option keywords for the RCPT
and MAIL commands!

Example:

  >>> import smtplib
  >>> s=smtplib.SMTP("localhost")
  >>> print(s.help())
  This is Sendmail version 8.8.4
  Topics:
      HELO    EHLO    MAIL    RCPT    DATA
      RSET    NOOP    QUIT    HELP    VRFY
      EXPN    VERB    ETRN    DSN
  For more info use "HELP <topic>".
  To report bugs in the implementation send email to
      sendmail-bugs@sendmail.org.
  For local information send email to Postmaster at your site.
  End of HELP info
  >>> s.putcmd("vrfy","someone@here")
  >>> s.getreply()
  (250, "Somebody OverHere <somebody@here.my.org>")
  >>> s.quit()

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\smtplib.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:21

## Dependencies

This module imports:
- [[Modules/datetime|datetime]]
- [[Modules/re|re]]
- [[Modules/socket|socket]]
- [[Modules/base64|base64]]
- [[Modules/io|io]]
- [[Modules/ssl|ssl]]
- [[Modules/hmac|hmac]]
- [[Modules/copy|copy]]

## Classes

- [[Classes/SMTPException|SMTPException]] (line 72)
- [[Classes/SMTPNotSupportedError|SMTPNotSupportedError]] (line 75)
- [[Classes/SMTPServerDisconnected|SMTPServerDisconnected]] (line 82)
- [[Classes/SMTPResponseException|SMTPResponseException]] (line 90)
- [[Classes/SMTPSenderRefused|SMTPSenderRefused]] (line 104)
- [[Classes/SMTPRecipientsRefused|SMTPRecipientsRefused]] (line 117)
- [[Classes/SMTPDataError|SMTPDataError]] (line 130)
- [[Classes/SMTPConnectError|SMTPConnectError]] (line 133)
- [[Classes/SMTPHeloError|SMTPHeloError]] (line 136)
- [[Classes/SMTPAuthenticationError|SMTPAuthenticationError]] (line 139)
- [[Classes/SMTP|SMTP]] (line 190)
- [[Classes/SMTP_SSL|SMTP_SSL]] (line 1003)
- [[Classes/LMTP|LMTP]] (line 1040)

## Functions

- [[Functions/encode_base64_3417|encode_base64()]] (line 73)
- [[Functions/quoteaddr_3421|quoteaddr()]] (line 146)
- [[Functions/_addr_only_3422|_addr_only()]] (line 159)
- [[Functions/quotedata_3423|quotedata()]] (line 167)
- [[Functions/_quote_periods_3424|_quote_periods()]] (line 176)
- [[Functions/_fix_eols_3425|_fix_eols()]] (line 179)
- [[Functions/prompt_3464|prompt()]] (line 1093)
