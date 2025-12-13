---
type: class
name: BaseRequestHandler
module: socketserver
lineno: 742
tags:
  - python
  - class
---

# Class: BaseRequestHandler

## Overview

Base class for request handler classes.

This class is instantiated for each request to be handled.  The
constructor sets the instance variables request, client_address
and server, and then calls the handle() method.  To implement a
specific service, all you need to do is to derive a class which
defines a handle() method.

The handle() method can find the request as self.request, the
client address as self.client_address, and the server (in case it
needs access to per-server information) as self.server.  Since a
separate instance is created for each request, the handle() method
can define other arbitrary instance variables.

**Module:** [[Modules/socketserver|socketserver]]
**Line:** 742

## Inheritance

**Subclasses:**
- [[Classes/StreamRequestHandler|StreamRequestHandler]]
- [[Classes/DatagramRequestHandler|DatagramRequestHandler]]

## Methods

### Constructors
- [[Functions/__init___3573|__init__()]] (line 760)

### Methods
- [[Functions/setup_3574|setup()]] (line 770)
- [[Functions/handle_3575|handle()]] (line 773)
- [[Functions/finish_3576|finish()]] (line 776)
