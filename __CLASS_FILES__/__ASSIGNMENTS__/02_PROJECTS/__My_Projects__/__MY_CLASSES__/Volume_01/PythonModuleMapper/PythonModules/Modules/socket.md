---
type: module
name: socket
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\socket.py
is_package: False
analyzed_at: 2025-12-10T03:46:19.234760
tags:
  - python
  - module
---

# Module: socket

## Overview

This module provides socket operations and some related functions.
On Unix, it supports IP (Internet Protocol) and Unix domain sockets.
On other systems, it only supports IP. Functions specific for a
socket are available as methods of the socket object.

Functions:

socket() -- create a new socket object
socketpair() -- create a pair of new socket objects [*]
fromfd() -- create a socket object from an open file descriptor [*]
send_fds() -- Send file descriptor to the socket.
recv_fds() -- Receive file descriptors from the socket.
fromshare() -- create a socket object from data received from socket.share() [*]
gethostname() -- return the current hostname
gethostbyname() -- map a hostname to its IP number
gethostbyaddr() -- map an IP number or hostname to DNS info
getservbyname() -- map a service name and a protocol name to a port number
getprotobyname() -- map a protocol name (e.g. 'tcp') to a number
ntohs(), ntohl() -- convert 16, 32 bit int from network to host byte order
htons(), htonl() -- convert 16, 32 bit int from host to network byte order
inet_aton() -- convert IP addr string (123.45.67.89) to 32-bit packed format
inet_ntoa() -- convert 32-bit packed format IP to string (123.45.67.89)
socket.getdefaulttimeout() -- get the default timeout value
socket.setdefaulttimeout() -- set the default timeout value
create_connection() -- connects to an address, with an optional timeout and
                       optional source address.
create_server() -- create a TCP socket and bind it to a specified address.

 [*] not available on all platforms!

Special objects:

SocketType -- type object for socket objects
error -- exception raised for I/O errors
has_ipv6 -- boolean value indicating if IPv6 is supported

IntEnum constants:

AF_INET, AF_UNIX -- socket domains (first argument to socket() call)
SOCK_STREAM, SOCK_DGRAM, SOCK_RAW -- socket types (second argument)

Integer constants:

Many other constants may be defined; these may be used in calls to
the setsockopt() and getsockopt() methods.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\socket.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:19

## Dependencies

This module imports:
- [[Modules/os|os]]
- [[Modules/errno|errno]]
- [[Modules/enum|enum]]
- [[Modules/io|io]]
- [[Modules/array|array]]

## Used By

This module is imported by:
- [[Modules/ssl|ssl]]
- [[Modules/mailbox|mailbox]]
- [[Modules/ftplib|ftplib]]
- [[Modules/poplib|poplib]]
- [[Modules/imaplib|imaplib]]
- [[Modules/smtplib|smtplib]]
- [[Modules/uuid|uuid]]
- [[Modules/socketserver|socketserver]]

## Classes

- [[Classes/IntEnum|IntEnum]] (line 1349)
- [[Classes/IntFlag|IntFlag]] (line 1645)
- [[Classes/_GiveupOnSendfile|_GiveupOnSendfile]] (line 212)
- [[Classes/socket|socket]] (line 215)
- [[Classes/SocketIO|SocketIO]] (line 677)

## Functions

- [[Functions/_intenum_converter_2709|_intenum_converter()]] (line 100)
- [[Functions/fromfd_2730|fromfd()]] (line 542)
- [[Functions/send_fds_2731|send_fds()]] (line 554)
- [[Functions/recv_fds_2732|recv_fds()]] (line 566)
- [[Functions/fromshare_2733|fromshare()]] (line 586)
- [[Functions/_fallback_socketpair_2734|_fallback_socketpair()]] (line 598)
- [[Functions/socketpair_2735|socketpair()]] (line 653)
- [[Functions/getfqdn_2746|getfqdn()]] (line 793)
- [[Functions/create_connection_2747|create_connection()]] (line 822)
- [[Functions/has_dualstack_ipv6_2748|has_dualstack_ipv6()]] (line 873)
- [[Functions/create_server_2749|create_server()]] (line 889)
- [[Functions/getaddrinfo_2750|getaddrinfo()]] (line 960)
