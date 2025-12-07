# Implementing a Selective Undo Framework in Python

**Monty Zukowski**  
*Zero to One Software Design*  
jamz@cdsnet.net

**Source:** 6th International Python Conference, 1997

## Abstract

I've implemented in Python the undo algorithm found in "Undoing Actions in Collaborative Work: Framework and Experience" by Prakash and Knister. Their approach helps structure the objects that make up a "document". Those same objects are well suited for use in an embedded language like Python: with them you can write scripts that can be undone! I've implemented standard file operations as a simple concrete example of using the framework.

## Introduction

I've always wondered how to design the objects which work together to represent a document, the *model* of the model-view-controller paradigm. How to design them to be easily scriptable? Undoable? Well, when I stumbled onto "Undoing Actions in Collaborative Work: Framework and Experience" by Prakash and Knister I struck a goldmine. Their paper gives a great overview of undo algorithms and when and why to use them. The "selective undo" algorithm presented by them lets the user undo *any* previous action, not just the last. So in a groupware application, she or he can undo her or his last action, not just the last action applied to the document by someone else.

As an adminstrator of hundreds of thousands of multimedia files, I wrote many Python scripts to move them around, rename them and tweak them for our build process to turn them into CD-ROMs. Every now and then I'd get cocky, run a script without testing it, and rename all the files to the same filename, or do other stupid file tricks. "If only I could undo that script!" I would think. Well, now I can since I've written undoable copy, move, link and delete operations as a simple application of the selective undo algorithm.

At first I sat down to write a general purpose undo module. You, the programmer, could just drop it into your application, add some glue, and get undo for free. I wish! It turned out that how the undo algorithm works is tightly linked to how the building block objects are designed. Or rather the other way around: the building block objects need to be designed to fit into the undo framework. Since undo is one of those things I would normally want in an application, I was glad to learn how to write objects that behave well with the undo algorithm.

I have written a general purpose `History` module which implements the selective undo algorithm. It isn't and cannot be a black box module. You need to understand how it works in order too use it. That's why I'm presenting it as a *literate program* as described by Knuth to explain how it works. Literate programming lets me write my code and documentation in one file and in any order I want, so I can explain what I'm doing in the order I think best, not the order imposed by the programming language. The same literate program file creates this document as well as the machine readable source code.

## Selective Undo Overview

Please do read Prakash and Knister to understand *why* their algorithm works. Here's a quick overview of *how* it works. Define operations that affect your state (the document). All such operations must define an inverse operation. Applying this inverse immediately after the operation nullifies it and returns the document to the state before applying the operation. At this point you have the Command pattern as described in *Design Patterns*.

If you, the programmer, want to undo an operation that was not the last one, you can't always get away with applying the inverse of that operation to the current state. Say my document is the sentence "Python rocks!". I select "rocks" and type in "rules". Call that *op1*, an `InsertText` operation which stores the selection which was modified: in this case chars `[7:12]`, the inserted text "rules" and the replaced text "rocks". The `InsertText` object needs the replaced text so it can create the proper inverse operation, which in this case would be `InsertText([7:12], "rocks")`. Next I type "really " in front of "rules". This will be *op2*, another `InsertText` operation with selection of `[7:7]`, inserted text of "really ", and replaced text "". Now what's required to undo *op1*?

Just applying the inverse of *op1* to the current document of "Python really rules!" would result in "Python rocksy rules!" because "rules" moved without *op1* knowing about it. The approach in Prakash and Knister is to have a `Transpose(a,b)` function which modifies `a` to make it as if `a` was applied after `b`, instead of before `b`. In the case of *op1* and *op2*, transposing would involve recognizing that op2 shifted any character positions >= 7 by 7 characters. That would mean the range `[7:12]` of *op1* would change to `[14:19]`. Now the inverse of *op1* would correctly create "Python really rocks!".

In practice the algorithm doesn't actually apply the `Transpose()` function to the history list directly. Instead it copies the list and transposes the operation to undo to the end. Since the history list includes everything done to a document, the end of the history list represents the current state of the document. Then the algorithm takes the inverse of the transposed operation and applies that to the document.

There are cases where a previous operation can't be undone. What if after *op2*, instead of undoing *op1*, I delete the entire sentence as *op3*? After that it wouldn't make much sense to revert "rules" to "rocks" since "rules" no longer exists! To detect such conflicts, a `Conflict(a,b)` function is defined. The reason the algorithm needs the `Conflict(a,b)` function is because not all conflicts will prevent an undo. Consider applying *op4* as the inverse of *op3*. There is still a conflict between *op1* and *op3*, but *op4* cancels out *op3*, so it still should be able to undo *op1*. A method called `removeDoUndoPair` handles these situations.

In summary the algorithm to undo any previous operation first copies the history list from the point of the operation to be undone. Then it transposes that operation to the end of the list copy. This brings the operation into the current state of the document. Then it takes the inverse of that transposed operation and applies it to the document to undo the original operation.

## The History Module

The `History` module defines three objects: `History`, the actual history list, `HistoryNode`, a single element in the history list, and `AbstractOperation`, which you, the programmer, subclass to create your own document operations.

## Conclusion

So what have I learned about structuring document objects for undo? One thing is that it is not easy to structure the undo objects into a separate module. They need to be tied directly to the implementation of the operations that modify documents because the document data and the operations that work on it need to know about each other to be able to define `Conflict` and `Transpose` properly.

The prototypical modules I've presented do work. I've tested them but have not used them extensively, so they are not mature by any means. In a real application I would improve them by customizing or subclassing `AbstractOperation`. Note that once you have all your operations behaving as described above you've nearly got a domain specific language! You or your users can write functions using these operations and get undo for free. With a little extra bookeeping you could record which function invocation caused which operations in the history list and use that information to undo the entire thing at once.

For groupware applications, the objects would be written the same way, but the `context` object would have to synchronize with a central server. The `Conflict` function would help identify problems when users simultaneously do things that aren't compatible.

Ever since I started programming graphical user interfaces I've been curious about how to implement undo and macro languages. With Prakash and Knister's paper I've finally discovered and implemented a serious undo framework. Their approach is like defining your own algebra for manipulating documents because it lets you switch around events in the history so you can undo anything, not just the last action. Now I'm ready to do a really killer app! Any ideas?

## Availability

The source code for `History.py` and `UndoableFileOperations.py` will be available by the time this paper is published. Check either on the Python home page, http://www.python.org/ or look for my quarters on the Python starship, http://starship.skyport.net/crew.html.

## References

- **[GOF]** Erich Gamma, et al. *Design Patterns: Elements of Reusable Object-Oriented Software.* Addison-Wesley, 1994
- **[Knuth]** D.E. Knuth. *Literate Programming*. Stanford University, 1992
- **[PK94]** Atul Prakash and Michael J. Knister. Undoing actions in collaborative work: Framework and experience. Technical Report CSE-TR-196-94, University of Michigan, March 1994
