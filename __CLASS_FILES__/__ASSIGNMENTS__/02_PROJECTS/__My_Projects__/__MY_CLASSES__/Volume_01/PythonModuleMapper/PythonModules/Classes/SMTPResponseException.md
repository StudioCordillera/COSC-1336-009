---
type: class
name: SMTPResponseException
module: smtplib
lineno: 90
tags:
  - python
  - class
---

# Class: SMTPResponseException

## Overview

Base class for all exceptions that include an SMTP error code.

These exceptions are generated in some instances when the SMTP
server returns an error code.  The error code is stored in the
`smtp_code' attribute of the error, and the `smtp_error' attribute
is set to the error message.

**Module:** [[Modules/smtplib|smtplib]]
**Line:** 90

## Inheritance

**Inherits from:**
- [[Classes/SMTPException|SMTPException]]

**Subclasses:**
- [[Classes/SMTPSenderRefused|SMTPSenderRefused]]
- [[Classes/SMTPDataError|SMTPDataError]]
- [[Classes/SMTPConnectError|SMTPConnectError]]
- [[Classes/SMTPHeloError|SMTPHeloError]]
- [[Classes/SMTPAuthenticationError|SMTPAuthenticationError]]

## Methods

### Constructors
- [[Functions/__init___3418|__init__()]] (line 99)
