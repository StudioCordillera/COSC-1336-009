# User-Centered Evolutionary Software Development Using Python and Java

**Douglas Cunningham** (dougc@cmu.edu)  
**Eswaran Subrahmanian** (sub@cmu.edu)  
**Arthur Westerberg** (aw0a@cmu.edu)  
*Engineering Design Research Center, Carnegie Mellon University, Pittsburgh, PA*

**Source:** 6th International Python Conference, 1997

## 1 Introduction

Over the last decade the use and value of prototypes in design, both in software and other engineering disciplines, has been investigated and discussed by researchers. Evolutionary software development, which consists of the rapid prototyping of new components and their evolution into hardened components, offers many benefits to the object-oriented software development process. Included among these benefits is the ability to address rapidly changing software requirements. In addition, the efficiency gained from user-centered design, which consists of constant user feedback impacting the software design, has received significant attention recently.

The requirements of user-centered and evolutionary software development cycles share many similarities but also include conflicting aspects. User-centered development demands the ability to rapidly add features, modify behavior, and create new user interface components. Evolutionary software development can have these same requirements but also requires the creation of well-defined modules and stable, efficient code.

Clean module interfaces, compile-time error checking, and performance make statically typed languages such as C++ and Java useful for the creation of hardened components. Meanwhile, rapid prototyping, fast compile-test-debug cycles, and high programming flexibility make dynamically typed languages such as Python and Tcl appropriate for the rapid creation of prototype components.

Ousterhout argues that a two language approach proves both feasible and practical for software development. For example, languages such as Python and Tcl provide consistent interfaces to C to allow developers to move performance critical methods and procedures into C without modification of the calling code. In addition, the dynamic language can be used to make calls to and exchange data between existing C or C++ modules.

**The Java Python Interface (JPI)** attempts to merge the strengths of two languages which are very similar in syntax and function. The purpose of the JPI is two fold:
1. Allow for the simultaneous development of prototype components in Python and hardened components in Java
2. Allow for the addition of user-level Python scripting to Java programs

This paper will describe the motivation of such an approach, and then focus on the technical details of the JPI.

## 2 Motivation

Design practices in software engineering vary widely from usage of the waterfall model to the evolutionary development model. In addition, explorations into user-centered design in software engineering have increased over the last few years. Although a unified definition of user-centered design has not been reached, Karat offers elements of one, drawing on Gould's four high level principles of good design.

In order to carry out design in this fashion the development environment must allow for the co-existence of stable modules with well-specified interfaces and newly prototyped modules with still-changing interfaces. In addition, the ability to quickly prototype new features, particularly in a running system, with a fast compile-test-debug cycle is required, while at the same time, the ability to statically determine code validity is necessary.

### 2.1 Two Languages

Supporting the above requirements well requires a language which can support both static and dynamic components at the same time. Currently, the most widely used development languages do not allow for this type of flexibility. Instead, developers are often left to choose a language which does not satisfy all of the necessary requirements.

If developers choose to use a **statically typed language** they often encounter problems in the early prototyping and development phases:
- They may begin to define programming module interfaces prematurely which can cause delays
- They are forced to engage in long compile-test-debug cycles
- Determining the cause of an error can be difficult
- It is difficult to debug part of an incomplete program

On the other hand, if developers choose to use a **dynamically typed language** they often encounter problems in the latter phases of development:
- They may end up not defining module interfaces well
- They often encounter performance problems
- They suffer scale problems related to CPU and memory usage
- Detection of all coding errors is delayed until the actual line of code is executed

Fortunately, alternatives exist. Languages such as Python and Tcl offer the option of using both a dynamic component (the language itself) and a static component (C). This two language approach offers many benefits over using a single language.

### 2.2 Java and Python

The use of two languages does not immediately solve the challenges facing a development team. For several years, the *n*-dim project at Carnegie Mellon University has investigated the two language approach with an object system called BOS. Our experiences have shown that the main drawback is that moving code into C is a costly effort since it requires a complete reimplementation of the code and often the logic.

Python and Java share many common features:
- Both are object-oriented
- Support garbage collection
- Provide object-based exception handling
- Guarantee memory safety
- Have a similar syntax

As a result, using them together in the two language approach offers a potential solution to the barrier of converting prototype code to hardened code. The similarities allow for the transition of code from one language to the other to be extremely easy and even offer the possibility of complete automation.

## 3 The JPI Overview

The JPI is an interface between Java and Python. It allows for the dynamic manipulation of Java objects through the use of Python and vice-versa. By writing Python code one can program using existing Java classes. In addition, the syntactical similarities between Python and Java are great enough that the conversion of prototyped Python code to hardened Java code is very easy and can even be largely automated.

The JPI consists of a simple interface between the two languages, but at the same time, it is quite powerful. The JPI consists of:
- A Python C module (`java`)
- A Python C type (`JavaObject`)
- Three simple Java classes (`Python`, `PyObject`, and `PyEventListener`)

### 3.1 Basics

The `java` module and `Python` class handle the object conversions. Key features include:
- Creating Java instances
- Accessing static fields and methods
- Dynamic message lookup scheme
- Object conversion between Python and Java types

### 3.2 Java Classes

To create a Java instance a program must first obtain a class using the `findClass` method of the `java` module. Once a class is obtained, the `new` message will invoke a constructor matching the arguments provided.

### 3.3 Java Instance Methods and Variables

Messages are sent to Java through a dynamic message lookup scheme. The `JavaObject` Python C type wraps a Java object and contains a global reference to the actual Java object. When a message is sent, a dynamic lookup finds the appropriate method or variable.

### 3.4 Object Conversions

An integral aspect of the JPI is the passing of objects between Java and Python through type conversions. Supported conversions include:
- Primitive types (int, long, float, double, boolean)
- Strings
- PyObject/JavaObject wrappers
- null/None

### 3.5 Exception Handling

Exceptions are handled by converting between Python and Java exceptions as they pass up the call stack. The programmer can catch exceptions in either language. Currently, some exception information is lost during conversion, but future versions will preserve the original exception details.

### 3.6 Other Implementation Details

**Classes and Interfaces:** To have a Python class implement a Java interface, a Java class must be created that forwards messages to a Python object. The `PyEventListener` class is an example, implementing all AWT event listener interfaces.

**The (Fake) Interpreter:** The JPI provides its own interpreter because difficulties were encountered when trying to run the Python interpreter from C.

**Reserved Words:** There is a problem when sending messages which correspond to Python reserved words. The workaround is to use the `send` method defined on `JavaObject`.

## 4 Other Approaches

Other approaches exist - a language supporting both static and dynamic modules could be written, different languages could be chosen for integration, and the languages could be integrated in different ways.

The *n*-dim group has experimented with BOS, which allows for method and variable declarations to be typed or untyped. Another approach is through interfacing tools such as CORBA or ILU, which allow rigid specification of module interfaces.

Finally, this is not the only project attempting to integrate Python and Java. Kevin Butler from Brigham Young University has implemented PyJava, which also provides integration between Java and Python, though currently only allowing Python to call Java.

## 5 Future Directions

Improvements needed:
- Better exception handling
- Thread support
- Python changes to eliminate extraneous parentheses for variable access
- Java changes for privileged code status and symmetric Python calling

## 6 Conclusions

The JPI has been used extensively by the author. Despite the described shortcomings it has proven very valuable. Code can be prototyped very quickly in Python and, once it works properly, moved to Java. Programs can be interactively debugged, graphical interfaces can be prototyped using Java AWT, and user level scripts can be added to programs.

Due to the many similarities between Java and Python, the JPI is able to support the two language approach to software development in an intuitive manner. For example, in one particular case a LoginDialog class was prototyped in Python while establishing the look and feel and then reimplemented in Java once completed. The reimplementation consisted primarily of a syntax conversion and was completed in less than an hour.

## 7 References

*[Full references available in original paper]*
