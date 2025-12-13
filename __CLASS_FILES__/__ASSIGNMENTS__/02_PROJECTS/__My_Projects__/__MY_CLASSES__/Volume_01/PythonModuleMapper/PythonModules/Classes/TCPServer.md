---
type: class
name: TCPServer
module: socketserver
lineno: 392
tags:
  - python
  - class
---

# Class: TCPServer

## Overview

Base class for various socket-based server classes.

Defaults to synchronous IP stream (i.e., TCP).

Methods for the caller:

- __init__(server_address, RequestHandlerClass, bind_and_activate=True)
- serve_forever(poll_interval=0.5)
- shutdown()
- handle_request()  # if you don't use serve_forever()
- fileno() -> int   # for selector

Methods that may be overridden:

- server_bind()
- server_activate()
- get_request() -> request, client_address
- handle_timeout()
- verify_request(request, client_address)
- process_request(request, client_address)
- shutdown_request(request)
- close_request(request)
- handle_error()

Methods for derived classes:

- finish_request(request, client_address)

Class variables that may be overridden by derived classes or
instances:

- timeout
- address_family
- socket_type
- request_queue_size (only for stream sockets)
- allow_reuse_address
- allow_reuse_port

Instance variables:

- server_address
- RequestHandlerClass
- socket

**Module:** [[Modules/socketserver|socketserver]]
**Line:** 392

## Inheritance

**Inherits from:**
- [[Classes/BaseServer|BaseServer]]

**Subclasses:**
- [[Classes/UDPServer|UDPServer]]
- [[Classes/ForkingTCPServer|ForkingTCPServer]]
- [[Classes/ThreadingTCPServer|ThreadingTCPServer]]
- [[Classes/UnixStreamServer|UnixStreamServer]]

## Methods

### Constructors
- [[Functions/__init___3547|__init__()]] (line 450)

### Methods
- [[Functions/server_bind_3548|server_bind()]] (line 463)
- [[Functions/server_activate_3549|server_activate()]] (line 481)
- [[Functions/server_close_3550|server_close()]] (line 489)
- [[Functions/fileno_3551|fileno()]] (line 497)
- [[Functions/get_request_3552|get_request()]] (line 505)
- [[Functions/shutdown_request_3553|shutdown_request()]] (line 513)
- [[Functions/close_request_3554|close_request()]] (line 523)
