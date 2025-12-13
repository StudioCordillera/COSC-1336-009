---
type: module
name: uuid
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\uuid.py
is_package: False
analyzed_at: 2025-12-10T03:46:21.163211
tags:
  - python
  - module
---

# Module: uuid

## Overview

UUID objects (universally unique identifiers) according to RFC 4122.

This module provides immutable UUID objects (class UUID) and the functions
uuid1(), uuid3(), uuid4(), uuid5() for generating version 1, 3, 4, and 5
UUIDs as specified in RFC 4122.

If all you want is a unique ID, you should probably call uuid1() or uuid4().
Note that uuid1() may compromise privacy since it creates a UUID containing
the computer's network address.  uuid4() creates a random UUID.

Typical usage:

    >>> import uuid

    # make a UUID based on the host ID and current time
    >>> uuid.uuid1()    # doctest: +SKIP
    UUID('a8098c1a-f86e-11da-bd1a-00112444be1e')

    # make a UUID using an MD5 hash of a namespace UUID and a name
    >>> uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
    UUID('6fa459ea-ee8a-3ca4-894e-db77e160355e')

    # make a random UUID
    >>> uuid.uuid4()    # doctest: +SKIP
    UUID('16fd2706-8baf-433b-82eb-8c7fada847da')

    # make a UUID using a SHA-1 hash of a namespace UUID and a name
    >>> uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
    UUID('886313e1-3b8a-5372-9b90-0c9aee199e5d')

    # make a UUID from a string of hex digits (braces and hyphens ignored)
    >>> x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')

    # convert a UUID to a string of hex digits in standard form
    >>> str(x)
    '00010203-0405-0607-0809-0a0b0c0d0e0f'

    # get the raw 16 bytes of the UUID
    >>> x.bytes
    b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'

    # make a UUID from a 16-byte string
    >>> uuid.UUID(bytes=x.bytes)
    UUID('00010203-0405-0607-0809-0a0b0c0d0e0f')

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\uuid.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:21

## Dependencies

This module imports:
- [[Modules/hashlib|hashlib]]
- [[Modules/os|os]]
- [[Modules/random|random]]
- [[Modules/socket|socket]]
- [[Modules/enum|enum]]
- [[Modules/io|io]]
- [[Modules/platform|platform]]
- [[Modules/subprocess|subprocess]]
- [[Modules/time|time]]
- [[Modules/argparse|argparse]]
- [[Modules/shutil|shutil]]

## Used By

This module is imported by:
- [[Modules/wave|wave]]

## Classes

- [[Classes/Enum|Enum]] (line 1109)
- [[Classes/SafeUUID|SafeUUID]] (line 82)
- [[Classes/UUID|UUID]] (line 88)

## Functions

- [[Functions/_simple_enum_3482|_simple_enum()]] (line 1737)
- [[Functions/_get_command_stdout_3511|_get_command_stdout()]] (line 363)
- [[Functions/_is_universal_3512|_is_universal()]] (line 409)
- [[Functions/_find_mac_near_keyword_3513|_find_mac_near_keyword()]] (line 413)
- [[Functions/_parse_mac_3514|_parse_mac()]] (line 448)
- [[Functions/_find_mac_under_heading_3515|_find_mac_under_heading()]] (line 476)
- [[Functions/_ifconfig_getnode_3516|_ifconfig_getnode()]] (line 514)
- [[Functions/_ip_getnode_3517|_ip_getnode()]] (line 524)
- [[Functions/_arp_getnode_3518|_arp_getnode()]] (line 532)
- [[Functions/_lanscan_getnode_3519|_lanscan_getnode()]] (line 560)
- [[Functions/_netstat_getnode_3520|_netstat_getnode()]] (line 565)
- [[Functions/_unix_getnode_3521|_unix_getnode()]] (line 582)
- [[Functions/_windll_getnode_3522|_windll_getnode()]] (line 588)
- [[Functions/_random_getnode_3523|_random_getnode()]] (line 594)
- [[Functions/getnode_3524|getnode()]] (line 637)
- [[Functions/uuid1_3525|uuid1()]] (line 661)
- [[Functions/uuid3_3526|uuid3()]] (line 699)
- [[Functions/uuid4_3527|uuid4()]] (line 710)
- [[Functions/uuid5_3528|uuid5()]] (line 714)
- [[Functions/main_3529|main()]] (line 723)
