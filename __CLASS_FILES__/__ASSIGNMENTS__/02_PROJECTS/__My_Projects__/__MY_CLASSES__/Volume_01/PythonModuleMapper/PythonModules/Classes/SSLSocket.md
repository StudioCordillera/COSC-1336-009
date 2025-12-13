---
type: class
name: SSLSocket
module: ssl
lineno: 978
tags:
  - python
  - class
---

# Class: SSLSocket

## Overview

This class implements a subtype of socket.socket that wraps
the underlying OS socket in an SSL context when necessary, and
provides read and write methods over that channel. 

**Module:** [[Modules/ssl|ssl]]
**Line:** 978

## Inheritance

**Inherits from:**
- [[Classes/socket|socket]]

## Methods

### Constructors
- [[Functions/__init___2841|__init__()]] (line 983)

### Methods
- [[Functions/_create_2842|_create()]] (line 991)
- [[Functions/context_2843|context()]] (line 1091)
- [[Functions/session_2844|session()]] (line 1102)
- [[Functions/session_reused_2845|session_reused()]] (line 1109)
- [[Functions/dup_2846|dup()]] (line 1113)
- [[Functions/_checkClosed_2847|_checkClosed()]] (line 1117)
- [[Functions/_check_connected_2848|_check_connected()]] (line 1121)
- [[Functions/read_2849|read()]] (line 1129)
- [[Functions/write_2850|write()]] (line 1150)
- [[Functions/getpeercert_2851|getpeercert()]] (line 1160)
- [[Functions/get_verified_chain_2852|get_verified_chain()]] (line 1166)
- [[Functions/get_unverified_chain_2853|get_unverified_chain()]] (line 1175)
- [[Functions/selected_npn_protocol_2854|selected_npn_protocol()]] (line 1184)
- [[Functions/selected_alpn_protocol_2855|selected_alpn_protocol()]] (line 1194)
- [[Functions/cipher_2856|cipher()]] (line 1202)
- [[Functions/shared_ciphers_2857|shared_ciphers()]] (line 1210)
- [[Functions/compression_2858|compression()]] (line 1218)
- [[Functions/send_2859|send()]] (line 1225)
- [[Functions/sendto_2860|sendto()]] (line 1236)
- [[Functions/sendmsg_2861|sendmsg()]] (line 1246)
- [[Functions/sendall_2862|sendall()]] (line 1252)
- [[Functions/sendfile_2863|sendfile()]] (line 1268)
- [[Functions/recv_2864|recv()]] (line 1278)
- [[Functions/recv_into_2865|recv_into()]] (line 1289)
- [[Functions/recvfrom_2866|recvfrom()]] (line 1308)
- [[Functions/recvfrom_into_2867|recvfrom_into()]] (line 1316)
- [[Functions/recvmsg_2868|recvmsg()]] (line 1324)
- [[Functions/recvmsg_into_2869|recvmsg_into()]] (line 1328)
- [[Functions/pending_2870|pending()]] (line 1333)
- [[Functions/shutdown_2871|shutdown()]] (line 1340)
- [[Functions/unwrap_2872|unwrap()]] (line 1346)
- [[Functions/verify_client_post_handshake_2873|verify_client_post_handshake()]] (line 1355)
- [[Functions/_real_close_2874|_real_close()]] (line 1361)
- [[Functions/do_handshake_2875|do_handshake()]] (line 1366)
- [[Functions/_real_connect_2876|_real_connect()]] (line 1376)
- [[Functions/connect_2877|connect()]] (line 1402)
- [[Functions/connect_ex_2878|connect_ex()]] (line 1407)
- [[Functions/accept_2879|accept()]] (line 1412)
- [[Functions/get_channel_binding_2880|get_channel_binding()]] (line 1425)
- [[Functions/version_2881|version()]] (line 1436)
