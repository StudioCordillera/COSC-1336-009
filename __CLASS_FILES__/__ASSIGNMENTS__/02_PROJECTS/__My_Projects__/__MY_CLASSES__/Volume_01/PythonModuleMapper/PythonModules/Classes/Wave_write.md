---
type: class
name: Wave_write
module: wave
lineno: 418
tags:
  - python
  - class
---

# Class: Wave_write

## Overview

Variables used in this class:

These variables are user settable through appropriate methods
of this class:
_file -- the open file with methods write(), close(), tell(), seek()
          set through the __init__() method
_comptype -- the AIFF-C compression type ('NONE' in AIFF)
          set through the setcomptype() or setparams() method
_compname -- the human-readable AIFF-C compression type
          set through the setcomptype() or setparams() method
_nchannels -- the number of audio channels
          set through the setnchannels() or setparams() method
_sampwidth -- the number of bytes per audio sample
          set through the setsampwidth() or setparams() method
_framerate -- the sampling frequency
          set through the setframerate() or setparams() method
_nframes -- the number of audio frames written to the header
          set through the setnframes() or setparams() method

These variables are used internally only:
_datalength -- the size of the audio samples written to the header
_nframeswritten -- the number of frames actually written
_datawritten -- the size of the audio samples actually written

**Module:** [[Modules/wave|wave]]
**Line:** 418

## Methods

### Constructors
- [[Functions/__init___3760|__init__()]] (line 444)
- [[Functions/__del___3762|__del__()]] (line 468)

### Magic Methods
- [[Functions/__enter___3763|__enter__()]] (line 471)
- [[Functions/__exit___3764|__exit__()]] (line 474)

### Methods
- [[Functions/initfp_3761|initfp()]] (line 456)
- [[Functions/setnchannels_3765|setnchannels()]] (line 480)
- [[Functions/getnchannels_3766|getnchannels()]] (line 487)
- [[Functions/setsampwidth_3767|setsampwidth()]] (line 492)
- [[Functions/getsampwidth_3768|getsampwidth()]] (line 499)
- [[Functions/setframerate_3769|setframerate()]] (line 504)
- [[Functions/getframerate_3770|getframerate()]] (line 511)
- [[Functions/setnframes_3771|setnframes()]] (line 516)
- [[Functions/getnframes_3772|getnframes()]] (line 521)
- [[Functions/setcomptype_3773|setcomptype()]] (line 524)
- [[Functions/getcomptype_3774|getcomptype()]] (line 532)
- [[Functions/getcompname_3775|getcompname()]] (line 535)
- [[Functions/setparams_3776|setparams()]] (line 538)
- [[Functions/getparams_3777|getparams()]] (line 548)
- [[Functions/setmark_3778|setmark()]] (line 554)
- [[Functions/getmark_3779|getmark()]] (line 559)
- [[Functions/getmarkers_3780|getmarkers()]] (line 564)
- [[Functions/tell_3781|tell()]] (line 569)
- [[Functions/writeframesraw_3782|writeframesraw()]] (line 572)
- [[Functions/writeframes_3783|writeframes()]] (line 585)
- [[Functions/close_3784|close()]] (line 590)
- [[Functions/_ensure_header_written_3785|_ensure_header_written()]] (line 608)
- [[Functions/_write_header_3786|_write_header()]] (line 618)
- [[Functions/_patchheader_3787|_patchheader()]] (line 639)
