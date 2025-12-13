---
type: class
name: IPv6Network
module: ipaddress
lineno: 2300
tags:
  - python
  - class
---

# Class: IPv6Network

## Overview

This class represents and manipulates 128-bit IPv6 networks.

Attributes: [examples for IPv6('2001:db8::1000/124')]
    .network_address: IPv6Address('2001:db8::1000')
    .hostmask: IPv6Address('::f')
    .broadcast_address: IPv6Address('2001:db8::100f')
    .netmask: IPv6Address('ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff0')
    .prefixlen: 124

**Module:** [[Modules/ipaddress|ipaddress]]
**Line:** 2300

## Inheritance

**Inherits from:**
- [[Classes/_BaseV6|_BaseV6]]
- [[Classes/_BaseNetwork|_BaseNetwork]]

## Methods

### Constructors
- [[Functions/__init___3727|__init__()]] (line 2316)

### Methods
- [[Functions/hosts_3728|hosts()]] (line 2364)
- [[Functions/is_site_local_3729|is_site_local()]] (line 2377)
