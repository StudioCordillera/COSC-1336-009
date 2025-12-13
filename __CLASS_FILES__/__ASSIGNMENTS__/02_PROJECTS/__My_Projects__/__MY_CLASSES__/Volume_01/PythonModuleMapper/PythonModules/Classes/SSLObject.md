---
type: class
name: SSLObject
module: ssl
lineno: 792
tags:
  - python
  - class
---

# Class: SSLObject

## Overview

This class implements an interface on top of a low-level SSL object as
implemented by OpenSSL. This object captures the state of an SSL connection
but does not provide any network IO itself. IO needs to be performed
through separate "BIO" objects which are OpenSSL's IO abstraction layer.

This class does not have a public constructor. Instances are returned by
``SSLContext.wrap_bio``. This class is typically used by framework authors
that want to implement asynchronous IO for SSL through memory buffers.

When compared to ``SSLSocket``, this object lacks the following features:

 * Any form of network IO, including methods such as ``recv`` and ``send``.
 * The ``do_handshake_on_connect`` and ``suppress_ragged_eofs`` machinery.

**Module:** [[Modules/ssl|ssl]]
**Line:** 792

## Methods

### Constructors
- [[Functions/__init___2817|__init__()]] (line 807)

### Methods
- [[Functions/_create_2818|_create()]] (line 814)
- [[Functions/context_2819|context()]] (line 831)
- [[Functions/session_2820|session()]] (line 840)
- [[Functions/session_reused_2821|session_reused()]] (line 844)
- [[Functions/server_side_2822|server_side()]] (line 849)
- [[Functions/server_hostname_2823|server_hostname()]] (line 854)
- [[Functions/read_2824|read()]] (line 859)
- [[Functions/write_2825|write()]] (line 871)
- [[Functions/getpeercert_2826|getpeercert()]] (line 879)
- [[Functions/get_verified_chain_2827|get_verified_chain()]] (line 888)
- [[Functions/get_unverified_chain_2828|get_unverified_chain()]] (line 902)
- [[Functions/selected_npn_protocol_2829|selected_npn_protocol()]] (line 913)
- [[Functions/selected_alpn_protocol_2830|selected_alpn_protocol()]] (line 923)
- [[Functions/cipher_2831|cipher()]] (line 929)
- [[Functions/shared_ciphers_2832|shared_ciphers()]] (line 934)
- [[Functions/compression_2833|compression()]] (line 940)
- [[Functions/pending_2834|pending()]] (line 945)
- [[Functions/do_handshake_2835|do_handshake()]] (line 949)
- [[Functions/unwrap_2836|unwrap()]] (line 953)
- [[Functions/get_channel_binding_2837|get_channel_binding()]] (line 957)
- [[Functions/version_2838|version()]] (line 963)
- [[Functions/verify_client_post_handshake_2839|verify_client_post_handshake()]] (line 968)
