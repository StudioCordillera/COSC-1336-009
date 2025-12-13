---
type: class
name: BaseServer
module: socketserver
lineno: 155
tags:
  - python
  - class
---

# Class: BaseServer

## Overview

Base class for server classes.

Methods for the caller:

- __init__(server_address, RequestHandlerClass)
- serve_forever(poll_interval=0.5)
- shutdown()
- handle_request()  # if you do not use serve_forever()
- fileno() -> int   # for selector

Methods that may be overridden:

- server_bind()
- server_activate()
- get_request() -> request, client_address
- handle_timeout()
- verify_request(request, client_address)
- server_close()
- process_request(request, client_address)
- shutdown_request(request)
- close_request(request)
- service_actions()
- handle_error()

Methods for derived classes:

- finish_request(request, client_address)

Class variables that may be overridden by derived classes or
instances:

- timeout
- address_family
- socket_type
- allow_reuse_address
- allow_reuse_port

Instance variables:

- RequestHandlerClass
- socket

**Module:** [[Modules/socketserver|socketserver]]
**Line:** 155

## Inheritance

**Subclasses:**
- [[Classes/TCPServer|TCPServer]]

## Methods

### Constructors
- [[Functions/__init___3530|__init__()]] (line 203)

### Magic Methods
- [[Functions/__enter___3545|__enter__()]] (line 385)
- [[Functions/__exit___3546|__exit__()]] (line 388)

### Methods
- [[Functions/server_activate_3531|server_activate()]] (line 210)
- [[Functions/serve_forever_3532|serve_forever()]] (line 218)
- [[Functions/shutdown_3533|shutdown()]] (line 247)
- [[Functions/service_actions_3534|service_actions()]] (line 257)
- [[Functions/handle_request_3535|handle_request()]] (line 276)
- [[Functions/_handle_request_noblock_3536|_handle_request_noblock()]] (line 305)
- [[Functions/handle_timeout_3537|handle_timeout()]] (line 328)
- [[Functions/verify_request_3538|verify_request()]] (line 335)
- [[Functions/process_request_3539|process_request()]] (line 343)
- [[Functions/server_close_3540|server_close()]] (line 352)
- [[Functions/finish_request_3541|finish_request()]] (line 360)
- [[Functions/shutdown_request_3542|shutdown_request()]] (line 364)
- [[Functions/close_request_3543|close_request()]] (line 368)
- [[Functions/handle_error_3544|handle_error()]] (line 372)
