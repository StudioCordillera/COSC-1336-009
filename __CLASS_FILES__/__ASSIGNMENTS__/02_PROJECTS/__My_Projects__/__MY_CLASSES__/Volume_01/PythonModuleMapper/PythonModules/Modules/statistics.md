---
type: module
name: statistics
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\statistics.py
is_package: False
analyzed_at: 2025-12-10T03:46:14.665912
tags:
  - python
  - module
---

# Module: statistics

## Overview

Basic statistics module.

This module provides functions for calculating statistics of data, including
averages, variance, and standard deviation.

Calculating averages
--------------------

==================  ==================================================
Function            Description
==================  ==================================================
mean                Arithmetic mean (average) of data.
fmean               Fast, floating-point arithmetic mean.
geometric_mean      Geometric mean of data.
harmonic_mean       Harmonic mean of data.
median              Median (middle value) of data.
median_low          Low median of data.
median_high         High median of data.
median_grouped      Median, or 50th percentile, of grouped data.
mode                Mode (most common value) of data.
multimode           List of modes (most common values of data).
quantiles           Divide data into intervals with equal probability.
==================  ==================================================

Calculate the arithmetic mean ("the average") of data:

>>> mean([-1.0, 2.5, 3.25, 5.75])
2.625


Calculate the standard median of discrete data:

>>> median([2, 3, 4, 5])
3.5


Calculate the median, or 50th percentile, of data grouped into class intervals
centred on the data values provided. E.g. if your data points are rounded to
the nearest whole number:

>>> median_grouped([2, 2, 3, 3, 3, 4])  #doctest: +ELLIPSIS
2.8333333333...

This should be interpreted in this way: you have two data points in the class
interval 1.5-2.5, three data points in the class interval 2.5-3.5, and one in
the class interval 3.5-4.5. The median of these data points is 2.8333...


Calculating variability or spread
---------------------------------

==================  =============================================
Function            Description
==================  =============================================
pvariance           Population variance of data.
variance            Sample variance of data.
pstdev              Population standard deviation of data.
stdev               Sample standard deviation of data.
==================  =============================================

Calculate the standard deviation of sample data:

>>> stdev([2.5, 3.25, 5.5, 11.25, 11.75])  #doctest: +ELLIPSIS
4.38961843444...

If you have previously calculated the mean, you can pass it as the optional
second argument to the four "spread" functions to avoid recalculating it:

>>> data = [1, 2, 2, 4, 4, 4, 5, 6]
>>> mu = mean(data)
>>> pvariance(data, mu)
2.5


Statistics for relations between two inputs
-------------------------------------------

==================  ====================================================
Function            Description
==================  ====================================================
covariance          Sample covariance for two variables.
correlation         Pearson's correlation coefficient for two variables.
linear_regression   Intercept and slope for simple linear regression.
==================  ====================================================

Calculate covariance, Pearson's correlation, and simple linear regression
for two inputs:

>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> y = [1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> covariance(x, y)
0.75
>>> correlation(x, y)  #doctest: +ELLIPSIS
0.31622776601...
>>> linear_regression(x, y)  #doctest:
LinearRegression(slope=0.1, intercept=1.5)


Exceptions
----------

A single exception is defined: StatisticsError is a subclass of ValueError.

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\statistics.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:14

## Dependencies

This module imports:
- [[Modules/decimal|decimal]]
- [[Modules/math|math]]
- [[Modules/random|random]]
- [[Modules/fractions|fractions]]
- [[Modules/collections|collections]]
- [[Modules/bisect|bisect]]
- [[Modules/numbers|numbers]]

## Classes

- [[Classes/Fraction|Fraction]] (line 179)
- [[Classes/itemgetter|itemgetter]] (line 271)
- [[Classes/Counter|Counter]] (line 548)
- [[Classes/StatisticsError|StatisticsError]] (line 152)
- [[Classes/NormalDist|NormalDist]] (line 1494)

## Functions

- [[Functions/bisect_left_905|bisect_left()]] (line 74)
- [[Functions/bisect_right_906|bisect_right()]] (line 21)
- [[Functions/reduce_907|reduce()]] (line 238)
- [[Functions/namedtuple_941|namedtuple()]] (line 358)
- [[Functions/_sum_942|_sum()]] (line 158)
- [[Functions/_ss_943|_ss()]] (line 212)
- [[Functions/_isfinite_944|_isfinite()]] (line 253)
- [[Functions/_coerce_945|_coerce()]] (line 260)
- [[Functions/_exact_ratio_946|_exact_ratio()]] (line 291)
- [[Functions/_convert_947|_convert()]] (line 337)
- [[Functions/_fail_neg_948|_fail_neg()]] (line 355)
- [[Functions/_rank_949|_rank()]] (line 363)
- [[Functions/_integer_sqrt_of_frac_rto_950|_integer_sqrt_of_frac_rto()]] (line 417)
- [[Functions/_float_sqrt_of_frac_951|_float_sqrt_of_frac()]] (line 429)
- [[Functions/_decimal_sqrt_of_frac_952|_decimal_sqrt_of_frac()]] (line 442)
- [[Functions/mean_953|mean()]] (line 472)
- [[Functions/fmean_954|fmean()]] (line 494)
- [[Functions/geometric_mean_955|geometric_mean()]] (line 530)
- [[Functions/harmonic_mean_956|harmonic_mean()]] (line 565)
- [[Functions/median_957|median()]] (line 621)
- [[Functions/median_low_958|median_low()]] (line 645)
- [[Functions/median_high_959|median_high()]] (line 667)
- [[Functions/median_grouped_960|median_grouped()]] (line 686)
- [[Functions/mode_961|mode()]] (line 758)
- [[Functions/multimode_962|multimode()]] (line 788)
- [[Functions/kde_963|kde()]] (line 808)
- [[Functions/quantiles_964|quantiles()]] (line 1057)
- [[Functions/variance_965|variance()]] (line 1111)
- [[Functions/pvariance_966|pvariance()]] (line 1155)
- [[Functions/stdev_967|stdev()]] (line 1196)
- [[Functions/pstdev_968|pstdev()]] (line 1214)
- [[Functions/_mean_stdev_969|_mean_stdev()]] (line 1232)
- [[Functions/_sqrtprod_970|_sqrtprod()]] (line 1244)
- [[Functions/covariance_971|covariance()]] (line 1273)
- [[Functions/correlation_972|correlation()]] (line 1301)
- [[Functions/linear_regression_973|linear_regression()]] (line 1352)
- [[Functions/_normal_dist_inv_cdf_974|_normal_dist_inv_cdf()]] (line 1413)
- [[Functions/_newton_raphson_1001|_newton_raphson()]] (line 1719)
- [[Functions/_quartic_invcdf_estimate_1002|_quartic_invcdf_estimate()]] (line 1728)
- [[Functions/_triweight_invcdf_estimate_1003|_triweight_invcdf_estimate()]] (line 1740)
- [[Functions/kde_random_1004|kde_random()]] (line 1766)
