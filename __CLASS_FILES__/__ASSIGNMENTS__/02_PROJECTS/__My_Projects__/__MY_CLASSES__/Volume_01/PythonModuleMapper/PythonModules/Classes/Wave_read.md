---
type: class
name: Wave_read
module: wave
lineno: 217
tags:
  - python
  - class
---

# Class: Wave_read

## Overview

Variables used in this class:

These variables are available to the user though appropriate
methods of this class:
_file -- the open file with methods read(), close(), and seek()
          set through the __init__() method
_nchannels -- the number of audio channels
          available through the getnchannels() method
_nframes -- the number of audio frames
          available through the getnframes() method
_sampwidth -- the number of bytes per audio sample
          available through the getsampwidth() method
_framerate -- the sampling frequency
          available through the getframerate() method
_comptype -- the AIFF-C compression type ('NONE' if AIFF)
          available through the getcomptype() method
_compname -- the human-readable AIFF-C compression type
          available through the getcomptype() method
_soundpos -- the position in the audio stream
          available through the tell() method, set through the
          setpos() method

These variables are used internally only:
_fmt_chunk_read -- 1 iff the FMT chunk has been read
_data_seek_needed -- 1 iff positioned correctly in audio
          file for readframes()
_data_chunk -- instantiation of a chunk class for the DATA chunk
_framesize -- size of one frame in the file

**Module:** [[Modules/wave|wave]]
**Line:** 217

## Methods

### Constructors
- [[Functions/__init___3740|__init__()]] (line 279)
- [[Functions/__del___3741|__del__()]] (line 292)

### Magic Methods
- [[Functions/__enter___3742|__enter__()]] (line 295)
- [[Functions/__exit___3743|__exit__()]] (line 298)

### Methods
- [[Functions/initfp_3739|initfp()]] (line 248)
- [[Functions/getfp_3744|getfp()]] (line 304)
- [[Functions/rewind_3745|rewind()]] (line 307)
- [[Functions/close_3746|close()]] (line 311)
- [[Functions/tell_3747|tell()]] (line 318)
- [[Functions/getnchannels_3748|getnchannels()]] (line 321)
- [[Functions/getnframes_3749|getnframes()]] (line 324)
- [[Functions/getsampwidth_3750|getsampwidth()]] (line 327)
- [[Functions/getframerate_3751|getframerate()]] (line 330)
- [[Functions/getcomptype_3752|getcomptype()]] (line 333)
- [[Functions/getcompname_3753|getcompname()]] (line 336)
- [[Functions/getparams_3754|getparams()]] (line 339)
- [[Functions/getmarkers_3755|getmarkers()]] (line 344)
- [[Functions/getmark_3756|getmark()]] (line 349)
- [[Functions/setpos_3757|setpos()]] (line 354)
- [[Functions/readframes_3758|readframes()]] (line 360)
- [[Functions/_read_fmt_chunk_3759|_read_fmt_chunk()]] (line 381)
