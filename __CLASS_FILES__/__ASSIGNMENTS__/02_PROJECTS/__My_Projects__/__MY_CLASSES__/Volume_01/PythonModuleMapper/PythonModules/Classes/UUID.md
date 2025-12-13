---
type: class
name: UUID
module: uuid
lineno: 88
tags:
  - python
  - class
---

# Class: UUID

## Overview

Instances of the UUID class represent UUIDs as specified in RFC 4122.
UUID objects are immutable, hashable, and usable as dictionary keys.
Converting a UUID to a string with str() yields something in the form
'12345678-1234-1234-1234-123456789abc'.  The UUID constructor accepts
five possible forms: a similar string of hexadecimal digits, or a tuple
of six integer fields (with 32-bit, 16-bit, 16-bit, 8-bit, 8-bit, and
48-bit values respectively) as an argument named 'fields', or a string
of 16 bytes (with all the integer fields in big-endian order) as an
argument named 'bytes', or a string of 16 bytes (with the first three
fields in little-endian order) as an argument named 'bytes_le', or a
single 128-bit integer as an argument named 'int'.

UUIDs have these read-only attributes:

    bytes       the UUID as a 16-byte string (containing the six
                integer fields in big-endian byte order)

    bytes_le    the UUID as a 16-byte string (with time_low, time_mid,
                and time_hi_version in little-endian byte order)

    fields      a tuple of the six integer fields of the UUID,
                which are also available as six individual attributes
                and two derived attributes:

        time_low                the first 32 bits of the UUID
        time_mid                the next 16 bits of the UUID
        time_hi_version         the next 16 bits of the UUID
        clock_seq_hi_variant    the next 8 bits of the UUID
        clock_seq_low           the next 8 bits of the UUID
        node                    the last 48 bits of the UUID

        time                    the 60-bit timestamp
        clock_seq               the 14-bit sequence number

    hex         the UUID as a 32-character hexadecimal string

    int         the UUID as a 128-bit integer

    urn         the UUID as a URN as specified in RFC 4122

    variant     the UUID variant (one of the constants RESERVED_NCS,
                RFC_4122, RESERVED_MICROSOFT, or RESERVED_FUTURE)

    version     the UUID version number (1 through 5, meaningful only
                when the variant is RFC_4122)

    is_safe     An enum indicating whether the UUID has been generated in
                a way that is safe for multiprocessing applications, via
                uuid_generate_time_safe(3).

**Module:** [[Modules/uuid|uuid]]
**Line:** 88

## Methods

### Constructors
- [[Functions/__init___3483|__init__()]] (line 142)

### Magic Methods
- [[Functions/__getstate___3484|__getstate__()]] (line 228)
- [[Functions/__setstate___3485|__setstate__()]] (line 236)
- [[Functions/__eq___3486|__eq__()]] (line 243)
- [[Functions/__lt___3487|__lt__()]] (line 251)
- [[Functions/__gt___3488|__gt__()]] (line 256)
- [[Functions/__le___3489|__le__()]] (line 261)
- [[Functions/__ge___3490|__ge__()]] (line 266)
- [[Functions/__hash___3491|__hash__()]] (line 271)
- [[Functions/__int___3492|__int__()]] (line 274)
- [[Functions/__repr___3493|__repr__()]] (line 277)
- [[Functions/__setattr___3494|__setattr__()]] (line 280)
- [[Functions/__str___3495|__str__()]] (line 283)

### Methods
- [[Functions/bytes_3496|bytes()]] (line 289)
- [[Functions/bytes_le_3497|bytes_le()]] (line 293)
- [[Functions/fields_3498|fields()]] (line 299)
- [[Functions/time_low_3499|time_low()]] (line 304)
- [[Functions/time_mid_3500|time_mid()]] (line 308)
- [[Functions/time_hi_version_3501|time_hi_version()]] (line 312)
- [[Functions/clock_seq_hi_variant_3502|clock_seq_hi_variant()]] (line 316)
- [[Functions/clock_seq_low_3503|clock_seq_low()]] (line 320)
- [[Functions/time_3504|time()]] (line 324)
- [[Functions/clock_seq_3505|clock_seq()]] (line 329)
- [[Functions/node_3506|node()]] (line 334)
- [[Functions/hex_3507|hex()]] (line 338)
- [[Functions/urn_3508|urn()]] (line 342)
- [[Functions/variant_3509|variant()]] (line 346)
- [[Functions/version_3510|version()]] (line 357)
