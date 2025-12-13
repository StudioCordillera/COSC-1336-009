---
type: module
name: random
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\random.py
is_package: False
analyzed_at: 2025-12-10T03:46:14.573612
tags:
  - python
  - module
---

# Module: random

## Overview

Random variable generators.

    bytes
    -----
           uniform bytes (values between 0 and 255)

    integers
    --------
           uniform within range

    sequences
    ---------
           pick random element
           pick random sample
           pick weighted random sample
           generate random permutation

    distributions on the real line:
    ------------------------------
           uniform
           triangular
           normal (Gaussian)
           lognormal
           negative exponential
           gamma
           beta
           pareto
           Weibull

    distributions on the circle (angles 0 to 2pi)
    ---------------------------------------------
           circular uniform
           von Mises

    discrete distributions
    ----------------------
           binomial


General notes on the underlying Mersenne Twister core generator:

* The period is 2**19937-1.
* It is one of the most extensively tested generators in existence.
* The random() method is implemented in C, executes in a single Python step,
  and is, therefore, threadsafe.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\random.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:14

## Dependencies

This module imports:
- [[Modules/math|math]]
- [[Modules/bisect|bisect]]

## Used By

This module is imported by:
- [[Modules/statistics|statistics]]
- [[Modules/tempfile|tempfile]]
- [[Modules/secrets|secrets]]
- [[Modules/imaplib|imaplib]]
- [[Modules/uuid|uuid]]

## Classes

- [[Classes/Random|Random]] (line 103)
- [[Classes/SystemRandom|SystemRandom]] (line 880)

## Functions

- [[Functions/_index_823|_index()]] (line 87)
- [[Functions/_test_generator_858|_test_generator()]] (line 954)
- [[Functions/_test_859|_test()]] (line 971)
- [[Functions/_parse_args_860|_parse_args()]] (line 1003)
- [[Functions/main_861|main()]] (line 1030)
