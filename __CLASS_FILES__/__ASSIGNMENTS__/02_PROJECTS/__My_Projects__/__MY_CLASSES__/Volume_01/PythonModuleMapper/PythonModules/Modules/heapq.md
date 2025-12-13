---
type: module
name: heapq
filepath: C:\Users\WORK_ADMIN\anaconda3\Lib\heapq.py
is_package: False
analyzed_at: 2025-12-10T03:46:13.491303
tags:
  - python
  - module
---

# Module: heapq

## Overview

Heap queue algorithm (a.k.a. priority queue).

Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for
all k, counting elements from 0.  For the sake of comparison,
non-existing elements are considered to be infinite.  The interesting
property of a heap is that a[0] is always its smallest element.

Usage:

heap = []            # creates an empty heap
heappush(heap, item) # pushes a new item on the heap
item = heappop(heap) # pops the smallest item from the heap
item = heap[0]       # smallest item on the heap without popping it
heapify(x)           # transforms list into a heap, in-place, in linear time
item = heappushpop(heap, item) # pushes a new item and then returns
                               # the smallest item; the heap size is unchanged
item = heapreplace(heap, item) # pops and returns smallest item, and adds
                               # new item; the heap size is unchanged

Our API differs from textbook heap algorithms as follows:

- We use 0-based indexing.  This makes the relationship between the
  index for a node and the indexes for its children slightly less
  obvious, but is more suitable since Python uses 0-based indexing.

- Our heappop() method returns the smallest item, not the largest.

These two make it possible to view the heap as a regular Python list
without surprises: heap[0] is the smallest item, and heap.sort()
maintains the heap invariant!

**Filepath:** `C:\Users\WORK_ADMIN\anaconda3\Lib\heapq.py`
**Type:** Module
**Analyzed:** 2025-12-10 03:46:13

## Used By

This module is imported by:
- [[Modules/sched|sched]]
- [[Modules/queue|queue]]

## Functions

- [[Functions/heappush_398|heappush()]] (line 132)
- [[Functions/heappop_399|heappop()]] (line 137)
- [[Functions/heapreplace_400|heapreplace()]] (line 147)
- [[Functions/heappushpop_401|heappushpop()]] (line 163)
- [[Functions/heapify_402|heapify()]] (line 170)
- [[Functions/_heappop_max_403|_heappop_max()]] (line 181)
- [[Functions/_heapreplace_max_404|_heapreplace_max()]] (line 191)
- [[Functions/_heapify_max_405|_heapify_max()]] (line 198)
- [[Functions/_siftdown_406|_siftdown()]] (line 207)
- [[Functions/_siftup_407|_siftup()]] (line 260)
- [[Functions/_siftdown_max_408|_siftdown_max()]] (line 280)
- [[Functions/_siftup_max_409|_siftup_max()]] (line 295)
- [[Functions/merge_410|merge()]] (line 316)
- [[Functions/nsmallest_411|nsmallest()]] (line 463)
- [[Functions/nlargest_412|nlargest()]] (line 523)
