---
type: function
name: send_message
module: smtplib
lineno: 901
is_async: False
is_method: True
tags:
  - python
  - function
categories:
  - public_method
---

# Function: send_message()

## Overview

Converts message to a bytestring and passes it to sendmail.

The arguments are as for sendmail, except that msg is an
email.message.Message object.  If from_addr is None or to_addrs is
None, these arguments are taken from the headers of the Message as
described in RFC 2822 (a ValueError is raised if there is more than
one set of 'Resent-' headers).  Regardless of the values of from_addr and
to_addr, any Bcc field (or Resent-Bcc field, when the Message is a
resent) of the Message object won't be transmitted.  The Message
object is then serialized using email.generator.BytesGenerator and
sendmail is called to transmit the message.  If the sender or any of
the recipient addresses contain non-ASCII and the server advertises the
SMTPUTF8 capability, the policy is cloned with utf8 set to True for the
serialization, and SMTPUTF8 and BODY=8BITMIME are asserted on the send.
If the server does not support SMTPUTF8, an SMTPNotSupported error is
raised.  Otherwise the generator is called without modifying the
policy.

```python
def send_message(self, msg, from_addr, to_addrs, mail_options, rcpt_options)
```

**Module:** [[Modules/smtplib|smtplib]]
**Class:** [[Classes/SMTP|SMTP]]
**Type:** Method
**Line:** 901

## Categories

- [[Taxonomy/public_method|public_method]]
