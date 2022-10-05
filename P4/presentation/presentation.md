NOTES 
==================================

Mission: 
----------------------------------

- Just go over the paper, no fancy work
- Make it MVP, then start upgrading
- Make a very straight-forward narrative
- Finish in time for mirror practice


Sunday: 
- make slide for each beat of the story


Narrative sketches:
----------------------------------

- Geocomputation

- disconnect between application and library

- VPLs are one of the ways to solve this disconnect
  - it is BOTH a programming language and an application at the same time

- VPL
  - WHY?
    - breaks the divide between 'library' and 'application'





PRESENTATION SCRIPT
==================================

0 pre-intro
==================================

- Hello everyone, thank you for coming 
- Name the title 
- I will go over the main items of the thesis

- Content will be as can be expected: 
  - intro
  - background & related studies
  - methodology
  - implementation
  - tests
  - conclusion



1 Introduction
===================================

1.1 Motivation
-----------------------------------

### Geocomputation 

### Library & Application 

### Visual Programming

### The Web

1.2 Problem 
-----------------------------------

### Library Portability

### Three aspects:

### I. Compilation

### II. Loading 

### III. Usage

1.3 Objective 
-----------------------------------

### Purpose of the study
- Goal: Solving the library portability problem for web-based Vpls. 

- In doing so: Improving the state of web-based VPLs

- How: The study is about how to correctly compile, load and use libraries 
in a web-based dataflow VPL

- Research Question: 

- Sub questions:



02 Background & 03 Related works
===============================

2.1 VPLs
----

### Types 

### Related VPLs


2.2 WebAssembly
-----------

### Rich Clients

### WebAssembly



04 Methodology
==============

( quickly the plan )
( some implementation details )

2.1 Base VPL
------------

2.2 Plugin System
-----------------

2.3 Tests
---------

05 Implementation
================

2.1 Base VPL
------------
(achieved functionality)

2.2 Plugin System
-----------------
(achieved functionality)

06 Tests 
=======

5.1

07 Conclusion
============

7.1 Answers
-----------

### sub 1 ”How to implement a browser-based dataflow-vpl for processing 3D geometry?”

Based on 4.1 & 5.1: 

It turned out that the dataflow vpl model layed out in the methodology can indeed be implemented on the web in TypeScript (JavaScript). 
This implementation had advantages and disadvantages: 

+ The big advantage of a TypeScript implementation is that a great number of features do not need to be included within the source code of the application, leading to quick load times.
    + WebGL, UI (HTML), 2D Canvas API

+ Also, Javascript’s flexibility proved to be useful to support features like dynami-
cally loading and using libraries at runtime.

- However, TypeScript does not have any runtime support for types, leading to reflection problems and problems with javascript types (no integer atomic, only number),

- Also, the absence of explicit immutability made it so that functions will need to be 'thrusted' to not alter their input data. 

### sub 2 ”How can geocomputation libraries written in system-level languages be compiled for web consumption?”

Based on 6.1: 

The conclusion is a dilemma between Rust and C++:

Rust
+ 


C++ 
- Has a strong foundation of existing geocomputation libraries compared to newer languages like Rust. However, this same legacy inhibits its portability, which makes it harder to compile to web browsers. 
- This study was not able to properly load C++ projects within the plugin system, due to the fact that the Emscripten compiler did not provide the same level of features as wasm-pack.

- A series of workarounds explained 6.1 came close, but the time frame of this study



Based on the experiments and analysis in Section 6.1, the study concludes that most con-
temporary, C++-based geocomputation libraries cannot be sufficiently compiled for web con-
sumption, at least not for the purposes of loading the functionalities within a web-VPL. This is
not due to wasm itself, but rather because of the focus of the emscripten compiler, combined
with the implementation requirements of a web VPL. Emscripten can be used to compile
full-scale C++ applications, and offers an emulation of a POSIX environment. However, it
lacks support for compiling libraries themselves, compared to other wasm-library compilers.
libraries generated with emscripten’s ’embind’ tool use irregular syntax, which troubles its
ability to be loaded programmatically. While web implementations do exist like ’GDAL-js’,
these solutions are required to work though Web Workers, and use the emscripten virtual file
systems, which again compromises their usage for the purpose of a dataflow-type vpl requir-
ing pure functions. Finally, the study was able to recognize some discrepancies between the
novelty of the WebAssembly format, juxtaposed to 50-year-old legacy of the C++ language,
leading to large wasm binaries.
Despite this, the study was able to provide a solution to these compilation shortcomings by
expanding the range of ’system-level languages’ beyond C++. The Rust programming lan-
guage offers a performance and level of control similar to C++, and has better wasm-library
support thanks to the wasm-bindgen toolkit. Using this toolkit, the study could successfully
expose a native geocomputation library in a manner properly consumable by a web-vpl. re-
grettably, not many rust-based geocomputation libraries are written in pure rust, and the
general pool of existing geocomputation libraries is limited due to the novelty of the lan-
guage.
Thus, the conclusion is a dilemma between Rust and C++. C++ has a strong foundation of
existing geocomputation libraries compared to newer languages like Rust. However, this
same legacy inhibits its portability, which makes it harder to compile to web browsers. Rust
is for the forseeable future a better choice for writing easily consumable, portable libraries,
but does not have a fully mature ecosystem of geocomputation libraries yet.
To offer a solution, the study suggests that either the ’embind’ tool must be expanded to the
level of functionality of ’wasm-bindgen’, or geocomputation libraries must be rewritten in
Rust. This second option seems counterproductive, but as stated by Ammann et al. [2022]:
”innovation often requires selectively ignoring prior work.

### sub 3 ”To what extent can a web-consumable library be loaded into a web-vpl without explicit configuration?”

Based on the method described in Section 4.2 and Section 5.2, and the analysis of Section 6.1,
it can be concluded that it is possible and even sufficiently usable to load a web-library into a
VPL without explicit configuration. It also had the desired effect of breaking down the barrier
between vpl libraries and regular text-based libraries: Using this method, only one type of li-
brary is needed to serve both. Moreover, it led to a workflow in which rapid experimentation
was possible, since this method allows users to develop a library locally, and then quickly
experiment and test its usage online.
The drawback of allowing this seamless interoperability and rapid experimentation, is that
many important properties like descriptions and library metadata do not need to be explicitly
specified, and could not be automatically extracted. These properties still had to be added to
the libraries in the shape of methods with a recognizable naming convention.
Additionally, the freedom of granted by not restricting input and output types can lead to
a confusing user experience, since there is no way of restricting libraries to use particular
type convention. Even worse, the libraries could use references pointing to the same object,
eliminating the ’immutable, no side effects’ nature of a dataflow-type VPL.

### sub 4: ”How can a ’geo-web-vpl’ be used to create geodata pipelines?”

Based on the analysis of Geofront in Section 6.2, it can be concluded that a geo-web-VPL can
be used for geocomputation to a sufficient extent. The analysis shows that many of Geofront’s
best aspects for the purpose of geocomputation are a consequence of the design decision to
use a diagram-based, dataflow-type VPL. Examples of these are how the Functional pro-
gramming paradigm leads to pure functions and immutable variables, making the graph as a
whole behave in a predicable manner, allowing for the inspection of in-between data at run-
time. However, the openness of the plugin system inhibits the consistency of these functional
aspects. Imported libraries are not forced to exclusively use pure function. As a consequence,
libraries can create functions with many side effects, or they can use inconsistent input and
output datatypes, ultimately leading to confusion for the end-user.

### main: ”How can native geocomputation libraries be compiled, loaded, and utilized within a browser-based dataflow-VPL?”

A VPL can support existing geocomputation libraries if and only if these libraries are able to
be compiled, loaded, and utilized in a dataflow VPL format.
Using a new javascript implementation of an acyclic, graph-based VPL, the study was able
to demonstrate how the web platform can be used to represent a dataflow-VPL capable of
hosting these libraries. The dataflow-properties of a graph-based VPL like this also makes
this libraries sufficiently usable, albeit with some well-known caveats of dataflow-VPLS, like
the representation of conditionals and iteration.
The current methods of compiling existing C++ geocomputation libraries to the web turned
out to be insufficient for the purposes of this study. This is due to emscripten’s focus on com-
piling full C++ applications instead of libraries. Despite this, the study w ́as able to demon-
strate how a novel method can be used to compile and load a Rust-library for usage in the VPL.
While not many contemporary geocomputation libraries are written in Rust, the study offers
this method to either offer emscripten contributors a blueprint of a desired workflow, or to
offer geocomputation library contributors a powerful use-case for the Rust language.
All in all, this means that either if the Rust ecosystem gains more mature geocomputation li-
braries, or if Emscripten’s capabilities improve, then the code portability problem & dataflow
problem of existing web-based geocomputation VPLS can be overcome.

7.2 Future work
---------------

### A: Deployment & Scalability

Scripts created with geofront should be able to be deployed as a server-side processing application. 
By running a script on a server, and ideally a server containing the geodata required in the process, one could deploy and run a Geofront scripts on a massive scale.
The overall purpose of this would be to create a Free and Open Source Software alternative to tools like the Google Earth Engine, and FME cloud compute.

The way GeoFlow achieved this is by creating a command line executable able to run the save file of a script ( a .json in our case).

However, this can also be achieved by compiling this save file to an executable language like python or javascript, and running that in a python or javascript runtime. 

  
### B: Rust, Containerization, and cloud native geospatial

An interesting aspect this study was able to touch on is using Rust for geocomputation. The
reason for this was the extensive support for webassembly, which was essential for browser-
based geocomputation. However, there are additional reasons one might want to perform
geocomputation within Rust. One is that rust is widely considered as a more stable, less
runtime error-prone language than C++, while offering similar performance and features.

Additionally, rust Wasm binaries also tend to be smaller than C++ wasm binaries.
This could be very interesting to the ”cloud-native geospatial” movement. 

This GIS movement aims to create the tools necessary to send geocomputation to servers, rather than sending geodata to the places where they are processed. 

To do this, geocomputation must become much more portable than it currently is, and Rust compiled to WebAssembly might proof to be a strong candidate for creating exchangeable, performant, compact, and error-proof binaries. 
It already sees usage on both cloud and edge servers (State of WebAssembly, 2022).
Therefore, studying Rust-based geocomputation for the purpose of cloud native and edge
computing, would be a promising topic for subsequent research.

---------


---------



