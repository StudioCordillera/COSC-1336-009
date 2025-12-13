---
type: class
name: _BaseNetwork
module: ipaddress
lineno: 672
tags:
  - python
  - class
---

# Class: _BaseNetwork

## Overview

A generic IP network object.

This IP class contains the version independent methods which are
used by networks.

**Module:** [[Modules/ipaddress|ipaddress]]
**Line:** 672

## Inheritance

**Inherits from:**
- [[Classes/_IPAddressBase|_IPAddressBase]]

**Subclasses:**
- [[Classes/IPv4Network|IPv4Network]]
- [[Classes/IPv6Network|IPv6Network]]

## Methods

### Magic Methods
- [[Functions/__repr___3621|__repr__()]] (line 679)
- [[Functions/__str___3622|__str__()]] (line 682)
- [[Functions/__iter___3624|__iter__()]] (line 697)
- [[Functions/__getitem___3625|__getitem__()]] (line 703)
- [[Functions/__lt___3626|__lt__()]] (line 716)
- [[Functions/__eq___3627|__eq__()]] (line 728)
- [[Functions/__hash___3628|__hash__()]] (line 736)
- [[Functions/__contains___3629|__contains__()]] (line 739)

### Methods
- [[Functions/hosts_3623|hosts()]] (line 685)
- [[Functions/overlaps_3630|overlaps()]] (line 751)
- [[Functions/broadcast_address_3631|broadcast_address()]] (line 759)
- [[Functions/hostmask_3632|hostmask()]] (line 764)
- [[Functions/with_prefixlen_3633|with_prefixlen()]] (line 768)
- [[Functions/with_netmask_3634|with_netmask()]] (line 772)
- [[Functions/with_hostmask_3635|with_hostmask()]] (line 776)
- [[Functions/num_addresses_3636|num_addresses()]] (line 780)
- [[Functions/_address_class_3637|_address_class()]] (line 785)
- [[Functions/prefixlen_3638|prefixlen()]] (line 793)
- [[Functions/address_exclude_3639|address_exclude()]] (line 796)
- [[Functions/compare_networks_3640|compare_networks()]] (line 871)
- [[Functions/_get_networks_key_3641|_get_networks_key()]] (line 919)
- [[Functions/subnets_3642|subnets()]] (line 929)
- [[Functions/supernet_3643|supernet()]] (line 982)
- [[Functions/is_multicast_3644|is_multicast()]] (line 1024)
- [[Functions/_is_subnet_of_3645|_is_subnet_of()]] (line 1036)
- [[Functions/subnet_of_3646|subnet_of()]] (line 1047)
- [[Functions/supernet_of_3647|supernet_of()]] (line 1051)
- [[Functions/is_reserved_3648|is_reserved()]] (line 1056)
- [[Functions/is_link_local_3649|is_link_local()]] (line 1068)
- [[Functions/is_private_3650|is_private()]] (line 1079)
- [[Functions/is_global_3651|is_global()]] (line 1096)
- [[Functions/is_unspecified_3652|is_unspecified()]] (line 1107)
- [[Functions/is_loopback_3653|is_loopback()]] (line 1119)
