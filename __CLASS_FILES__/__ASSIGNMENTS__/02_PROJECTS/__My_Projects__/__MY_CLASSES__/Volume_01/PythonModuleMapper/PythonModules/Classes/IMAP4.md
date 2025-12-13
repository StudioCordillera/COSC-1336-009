---
type: class
name: IMAP4
module: imaplib
lineno: 138
tags:
  - python
  - class
---

# Class: IMAP4

## Overview

IMAP4 client class.

Instantiate with: IMAP4([host[, port[, timeout=None]]])

        host - host's name (default: localhost);
        port - port number (default: standard IMAP4 port).
        timeout - socket timeout (default: None)
                  If timeout is not given or is None,
                  the global default socket timeout is used

All IMAP4rev1 commands are supported by methods of the same
name (in lowercase).

All arguments to commands are converted to strings, except for
AUTHENTICATE, and the last argument to APPEND which is passed as
an IMAP4 literal.  If necessary (the string contains any
non-printing characters or white-space and isn't enclosed with
either parentheses or double quotes) each string is quoted.
However, the 'password' argument to the LOGIN command is always
quoted.  If you want to avoid having an argument string quoted
(eg: the 'flags' argument to STORE) then enclose the string in
parentheses (eg: "(\Deleted)").

Each command returns a tuple: (type, [data, ...]) where 'type'
is usually 'OK' or 'NO', and 'data' is either the text from the
tagged response, or untagged results from command. Each 'data'
is either a string, or a tuple. If a tuple, then the first part
is the header of the response, and the second part contains
the data (ie: 'literal' value).

Errors raise the exception class <instance>.error("<reason>").
IMAP4 server errors raise <instance>.abort("<reason>"),
which is a sub-class of 'error'. Mailbox status changes
from READ-WRITE to READ-ONLY raise the exception class
<instance>.readonly("<reason>"), which is a sub-class of 'abort'.

"error" exceptions imply a program error.
"abort" exceptions imply the connection should be reset, and
        the command re-tried.
"readonly" exceptions imply the command should be re-tried.

Note: to use this module, you must read the RFCs pertaining to the
IMAP4 protocol, as the semantics of the arguments to each IMAP4
command are left to the invoker, not to mention the results. Also,
most IMAP servers implement a sub-set of the commands available here.

**Module:** [[Modules/imaplib|imaplib]]
**Line:** 138

## Inheritance

**Subclasses:**
- [[Classes/IMAP4_SSL|IMAP4_SSL]]
- [[Classes/IMAP4_stream|IMAP4_stream]]

## Methods

### Constructors
- [[Functions/__init___3323|__init__()]] (line 191)

### Magic Methods
- [[Functions/__getattr___3327|__getattr__()]] (line 272)
- [[Functions/__enter___3328|__enter__()]] (line 278)
- [[Functions/__exit___3329|__exit__()]] (line 281)

### Methods
- [[Functions/_mode_ascii_3324|_mode_ascii()]] (line 216)
- [[Functions/_mode_utf8_3325|_mode_utf8()]] (line 223)
- [[Functions/_connect_3326|_connect()]] (line 230)
- [[Functions/_create_socket_3330|_create_socket()]] (line 294)
- [[Functions/open_3331|open()]] (line 307)
- [[Functions/read_3332|read()]] (line 319)
- [[Functions/readline_3333|readline()]] (line 330)
- [[Functions/send_3334|send()]] (line 338)
- [[Functions/shutdown_3335|shutdown()]] (line 344)
- [[Functions/socket_3336|socket()]] (line 360)
- [[Functions/recent_3337|recent()]] (line 372)
- [[Functions/response_3338|response()]] (line 389)
- [[Functions/append_3339|append()]] (line 403)
- [[Functions/authenticate_3340|authenticate()]] (line 429)
- [[Functions/capability_3341|capability()]] (line 458)
- [[Functions/check_3342|check()]] (line 467)
- [[Functions/close_3343|close()]] (line 475)
- [[Functions/copy_3344|copy()]] (line 490)
- [[Functions/create_3345|create()]] (line 498)
- [[Functions/delete_3346|delete()]] (line 506)
- [[Functions/deleteacl_3347|deleteacl()]] (line 513)
- [[Functions/enable_3348|enable()]] (line 520)
- [[Functions/expunge_3349|expunge()]] (line 532)
- [[Functions/fetch_3350|fetch()]] (line 546)
- [[Functions/getacl_3351|getacl()]] (line 561)
- [[Functions/getannotation_3352|getannotation()]] (line 570)
- [[Functions/getquota_3353|getquota()]] (line 578)
- [[Functions/getquotaroot_3354|getquotaroot()]] (line 589)
- [[Functions/list_3355|list()]] (line 600)
- [[Functions/login_3356|login()]] (line 612)
- [[Functions/login_cram_md5_3357|login_cram_md5()]] (line 626)
- [[Functions/_CRAM_MD5_AUTH_3358|_CRAM_MD5_AUTH()]] (line 635)
- [[Functions/logout_3359|logout()]] (line 643)
- [[Functions/lsub_3360|lsub()]] (line 656)
- [[Functions/myrights_3361|myrights()]] (line 667)
- [[Functions/namespace_3362|namespace()]] (line 675)
- [[Functions/noop_3363|noop()]] (line 685)
- [[Functions/partial_3364|partial()]] (line 696)
- [[Functions/proxyauth_3365|proxyauth()]] (line 708)
- [[Functions/rename_3366|rename()]] (line 721)
- [[Functions/search_3367|search()]] (line 729)
- [[Functions/select_3368|select()]] (line 747)
- [[Functions/setacl_3369|setacl()]] (line 779)
- [[Functions/setannotation_3370|setannotation()]] (line 787)
- [[Functions/setquota_3371|setquota()]] (line 795)
- [[Functions/sort_3372|sort()]] (line 804)
- [[Functions/starttls_3373|starttls()]] (line 818)
- [[Functions/status_3374|status()]] (line 841)
- [[Functions/store_3375|store()]] (line 853)
- [[Functions/subscribe_3376|subscribe()]] (line 864)
- [[Functions/thread_3377|thread()]] (line 872)
- [[Functions/uid_3378|uid()]] (line 882)
- [[Functions/unsubscribe_3379|unsubscribe()]] (line 907)
- [[Functions/unselect_3380|unselect()]] (line 915)
- [[Functions/xatom_3381|xatom()]] (line 931)
- [[Functions/_append_untagged_3382|_append_untagged()]] (line 953)
- [[Functions/_check_bye_3383|_check_bye()]] (line 967)
- [[Functions/_command_3384|_command()]] (line 973)
- [[Functions/_command_complete_3385|_command_complete()]] (line 1050)
- [[Functions/_get_capabilities_3386|_get_capabilities()]] (line 1068)
- [[Functions/_get_response_3387|_get_response()]] (line 1077)
- [[Functions/_get_tagged_response_3388|_get_tagged_response()]] (line 1157)
- [[Functions/_get_line_3389|_get_line()]] (line 1190)
- [[Functions/_match_3390|_match()]] (line 1209)
- [[Functions/_new_tag_3391|_new_tag()]] (line 1221)
- [[Functions/_quote_3392|_quote()]] (line 1229)
- [[Functions/_simple_command_3393|_simple_command()]] (line 1237)
- [[Functions/_untagged_response_3394|_untagged_response()]] (line 1242)
- [[Functions/_mesg_3395|_mesg()]] (line 1256)
- [[Functions/_dump_ur_3396|_dump_ur()]] (line 1263)
- [[Functions/_log_3397|_log()]] (line 1270)
- [[Functions/print_log_3398|print_log()]] (line 1277)
