---
type: class
name: Random
module: random
lineno: 103
tags:
  - python
  - class
---

# Class: Random

## Overview

Random number generator base class used by bound module functions.

Used to instantiate instances of Random to get generators that don't
share state.

Class Random can also be subclassed if you want to use a different basic
generator of your own devising: in that case, override the following
methods:  random(), seed(), getstate(), and setstate().
Optionally, implement a getrandbits() method so that randrange()
can cover arbitrarily large ranges.

**Module:** [[Modules/random|random]]
**Line:** 103

## Inheritance

**Subclasses:**
- [[Classes/SystemRandom|SystemRandom]]
- [[Classes/SystemRandom|SystemRandom]]

## Methods

### Constructors
- [[Functions/__init___824|__init__()]] (line 119)

### Magic Methods
- [[Functions/__getstate___828|__getstate__()]] (line 213)
- [[Functions/__setstate___829|__setstate__()]] (line 216)
- [[Functions/__reduce___830|__reduce__()]] (line 219)
- [[Functions/__init_subclass___831|__init_subclass__()]] (line 225)

### Methods
- [[Functions/seed_825|seed()]] (line 128)
- [[Functions/getstate_826|getstate()]] (line 176)
- [[Functions/setstate_827|setstate()]] (line 180)
- [[Functions/_randbelow_with_getrandbits_832|_randbelow_with_getrandbits()]] (line 245)
- [[Functions/_randbelow_without_getrandbits_833|_randbelow_without_getrandbits()]] (line 255)
- [[Functions/randbytes_834|randbytes()]] (line 288)
- [[Functions/randrange_835|randrange()]] (line 295)
- [[Functions/randint_836|randint()]] (line 336)
- [[Functions/choice_837|choice()]] (line 345)
- [[Functions/shuffle_838|shuffle()]] (line 354)
- [[Functions/sample_839|sample()]] (line 363)
- [[Functions/choices_840|choices()]] (line 458)
- [[Functions/uniform_841|uniform()]] (line 498)
- [[Functions/triangular_842|triangular()]] (line 509)
- [[Functions/normalvariate_843|normalvariate()]] (line 534)
- [[Functions/gauss_844|gauss()]] (line 555)
- [[Functions/lognormvariate_845|lognormvariate()]] (line 593)
- [[Functions/expovariate_846|expovariate()]] (line 603)
- [[Functions/vonmisesvariate_847|vonmisesvariate()]] (line 623)
- [[Functions/gammavariate_848|gammavariate()]] (line 665)
- [[Functions/betavariate_849|betavariate()]] (line 734)
- [[Functions/paretovariate_850|paretovariate()]] (line 766)
- [[Functions/weibullvariate_851|weibullvariate()]] (line 773)
- [[Functions/binomialvariate_852|binomialvariate()]] (line 787)
