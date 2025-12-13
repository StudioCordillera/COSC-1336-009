---
type: module
name: colorsys
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\colorsys.py
is_package: False
analyzed_at: 2025-12-10T03:46:22.186746
tags:
  - python
  - module
---

# Module: colorsys

## Overview

Conversion functions between RGB and other color systems.

This modules provides two functions for each color system ABC:

  rgb_to_abc(r, g, b) --> a, b, c
  abc_to_rgb(a, b, c) --> r, g, b

All inputs and outputs are triples of floats in the range [0.0...1.0]
(with the exception of I and Q, which covers a slightly larger range).
Inputs outside the valid range may cause exceptions or invalid outputs.

Supported color systems:
RGB: Red, Green, Blue components
YIQ: Luminance, Chrominance (used by composite video signals)
HLS: Hue, Luminance, Saturation
HSV: Hue, Saturation, Value

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\colorsys.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:22

## Functions

- [[Functions/rgb_to_yiq_3789|rgb_to_yiq()]] (line 40)
- [[Functions/yiq_to_rgb_3790|yiq_to_rgb()]] (line 46)
- [[Functions/rgb_to_hls_3791|rgb_to_hls()]] (line 75)
- [[Functions/hls_to_rgb_3792|hls_to_rgb()]] (line 99)
- [[Functions/_v_3793|_v()]] (line 109)
- [[Functions/rgb_to_hsv_3794|rgb_to_hsv()]] (line 125)
- [[Functions/hsv_to_rgb_3795|hsv_to_rgb()]] (line 145)
