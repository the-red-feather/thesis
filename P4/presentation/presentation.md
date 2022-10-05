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

- background and related studies are integrated within the methodology.
  - However, numbering is kept the same with the chapters of the written thesis, 
    to make the relation between the presentation and thesis more clear. 

1 Introduction
===================================

1.1 Motivation
-----------------------------------


- **GEOCOMPUTATION** 
  - (or Geoprocessing)
  - is one of the CORNERSTONES of GIS and all modern mapping needs.
  - It is a broad topic, almost to broad to consider.
  - The term 'geocomputation' is used to represent all types of computations performed on geographical datasets. 
    - Anything from: 
      - the calculation of the area of a region, 
      - to a Coordinate Reference System (CRS) transformations
      - or converting a raster dataset into a vectorized dataset,
    - can be regarded as geocomputation.


- **GEOCOMPUTATION SOFTWARE NORMALLY COMES IN TWO FORMS**: Applications, and Libraries [REF: Elliott, 2007]
  - PROPERTIES: different intentions & strengths
    - APP: 
      - User-friendly 
      - usable
      - concrete
      - visual

    - LIBRARY
      - programmer-friendly
      - composable
      - abstract
      - syntactic

  - HOWEVER: This split in intensions has drawbacks:
    - applications are not programmer friendly: 
      - applications limit access to functionality
      - applications are not usually composable
    
    - libraries are not end-user friendly:
      - functionalities are not directly accessible.
      - no GUI \ visualization support out of the box

    - THIS IS EXTRA IMPORTANT FOR GIS
      - Visualization is a necessity
      - Composability is a necessity
    
    - THE DREAM: unlimited access to the functionality, composability, and usability of software.
   

- **THERE ARE MULTIPLE WAYS** researchers and developers have tried to bring software applications and libraries closer together.
    (Unix Pipes, Jupyter notebook, GUI algebra [REF: Elliott, 2007])

- **ARE ONE OF THESE WAYS IS THE VISUAL PROGRAMMING LANGUAGE** 
  - VPL: Constructing a program by using a GUI. 
  - This makes a VPL BOTH a programming language and an application at the same time.
  - Some examples within the field of GIS are: FME, Grasshopper, Geoflow.

  - **new development: Web VPLS**
    - 'live' alongside web GIS (as more and more GIS applications are starting to become web-based, it makes sense that 'configuring automation' in a web browser becomes a need).
    - Accessibility advantages: (no installation, easier distribution and licensing)
      (- Overleaf) 
    - GIS example: mobius modeller

1.2 Problem 
-----------------------------------

- **PROBLEM: library portability**
    - The same software libraries which we could use with native VPLs can now suddenly not be used anymore on the web.
    - This hinders the original goal of 'bringing Libraries and (Web) Applications closer together'
    - web based alternatives exist, but
      - time consuming to synchronize and test features [Ref: mapbox.rs]
      - which in turn hinders innovation


- **Goal: Solving the library portability problem for web-based VPLs.**
  - make it so native, system level libraries can be used in a web-based VPL. 
  - but how? 
  

- **Three challenges are identified** to using native library in a vpl: 
    - Firstly, **I. Compilation**:   
      -  the most viable option for using a non-js library in a web browser, is by compiling it to **WebAssembly** [Haas et al., 2017].
      - WebAssembly is a binary instruction set meant for virtual machine execution.
        - It has multiple use cases, one of which is safely executing software written in a variety of languages on the web.  
      - However, wasm compilation may pose challenges:
        - There are differences between programming languages 
          - in the level of support granted by their specific **wasm compilers**. 
          - (Novelty of the language)       
        - **Not** all code can be compiled **unconditionally**
          - (examples: no file system access, no multithreading support) 

    - Secondly, **II. Loading**:
      - In order to load system level libraries in a web VPL, one needs to: 
        - Interoperate between the language models of the compiled WebAssembly binary and Javascript.
        - Interoperate between the language models of Javascript and the Visual Language.
      - This is complicated by the fact that the WebAssembly binary can be created from different languages.   
      - Designing an interconnected binding system, in which all three languages have to be taken into account, forms the content of this second challenge  

    - Lastly **III. Utilization**: 
      - Finally, It might be the case that a web-based VPL is able to **load and run** functions from WebAssembly **compiled** libraries. 
      And yet, one might not be able to successfully **use** these libraries.
      - The challenge is to connect the language model of the web-based VPL to the models of these libraries on a software design level rather than a technical Loading level. 


1.3 Objective 
-----------------------------------

- **The Objective of the study** is to attempt to solve the library portability problem for web-based VPLs.
  - In doing so: Contributing to the state of web-based VPLs
  - And: Contributing to closing the gap between library and (web) applications.


- **How**: Design, implement, examine and discuss a possible solution for \
  compiling, loading and using industry-standard geo-libraries in a web based VPL.  


- **Research Question**: 
  - How can native geocomputation libraries be compiled, loaded, and utilized within a browser-based dataflow-VPL?


- **Sub questions**:
  - The following supporting questions are defined to aid in answering the main question. The first question serves as a prerequisite for attempting to answer the remaining three. The other three research questions are based upon the three main categories of challenges of the library portability problem. 

  - How to implement a browser-based dataflow-vpl for processing 3D geometry?

  - How can geocomputation libraries written in system-level languages be **compiled** for web consumption?

  - How can a web-consumable library be **loaded** into a web-vpl without explicit configuration?

  - To what extent can a Web based vpl equipped with native libraries be used to create geodata pipelines?


02 Background 
=============

VPL
---
- VPLs are often researched as part of the field of "End User Development".
- Show some different type of VPLs

Dataflow modelling
------------------
- Dataflow modelling is a field of study which offers a different perspective on VPLs. 
- Where the wider field of End User Development regard VPLs mostly from a UI / GUI / UX point of view, 
  - Dataflow modelling focusses more on the language model of VPls. 
  
- A special type of VPL is regarded. 
  - This study calls this type a 'Dataflow VPL'.

- Dataflow VPL are defined as Graph based VPL, 
  - with only pure, stateless, functions without side-effects.
    ( not triggering anything special, using global properties, etc. ) 
  - and with immutable variables, 
    ( meaning that variables are not allowed to change after initialization )

- If this sounds familiar to you, you are right: 
  - The observation of research in the field of dataflow modelling, 
    is that dataflow VPL starts to look like a Functional Programming model, 
    (but without 'first class functions'). 
  - As such, dataflow VPLs enjoy similar advantages as functional programming: 
    -
    


An important aspect of the dataflow-VPL is the connection to the field of dataflow programming, which is also a more general field than VPLs in particular.
Dataflow programming is a programming paradigm which internally, represents a program as a DAG. 
A graphical, editable representation of a dataflow program would result into a Dataflow VPL.

The big computational advantage of this model, is that it allows for implicit concurrently [Sousa, 2012]. 
In other words, every node of a program written using dataflow programming can be executed in isolation of any other nodes, 
as long as the direct dependencies (the inputs) are met. 
No global state or hidden side effects means no data-race issues, 
which allows parallel execution of the program by default. 
When using other paradigms, programmers need to manually spawn and manage threads to achieve the same effect.

This also leads into an interesting side-effect of using dataflow programming / a diagram-based VPL: 
By only permitting pure, stateless functions with no side-effect, and only immutable
variables, end users automatically adopt a functional programming style (albeit without
lambda functions). 
Functional programming has many benefits of its own besides concurrency, such as:
- clear unit testing
- hot code deployment
- debugging advantages,
- and lending itself well for compile time optimizations.

All that to say, creating a VPL is not just a matter of designing a stylistic, user-friendly GUI
alternative to regular programming. 
This might be true for other types of VPLs, but not for diagram-based ones. 
By closely resembling dataflow itself, and because of its functional programming nature, 
diagram-based VPLs can actually lead to faster and more reliable software.



04 Methodology
==============

- The methodology used to find answers to these questions is defined as follows: 
  - First, a **custom web VPL** is designed and implemented as a **host** for the libraries. 
  - Second, a **plugin system** is designed and implemented.
    - The system consists of: 
      - A Plugin Loader on the side of this VPL, and 
      - A Plugin model the libraries must adhere to. 
  - Finally, Two sets of **tests** are performed to analyse to what extent this solution allows for proper utilization of native libraries. 


05 Solution
===========

Base VPL
--------

- **WHY**
  - A VPL was required as a host for all subsequent steps of the methodology.
    - More specifically, A Dataflow-type VPL was deemed the most suited fit for geocomputation 

    - Building a custom implementation would also allow more degrees of freedom, in
terms of designing a VPL which takes hosting geocomputation libraries from multiple hosts
into account from the start.
    - Additionally, no existing web-based VPLs were implemented as Dataflow VPLs.




the related works review of Chapter 3 showcased that  The Mobius Modeller [Janssen, 2021] came closest,
but the sizable nature of this project makes aligning its goals with the goals of this study chal-
lenging.
The following approach was deemed as the most fitting method for implementing this VPL.
First, the requirements of a dataflow-VPL handling geometry have to be made clear. Secondly,
in order to know what tools may be used to implement this VPl, a small analysis of ”widely
supported browser features” is made. Then, with both these constraints known, a design for
a web VPL can be layed out, which can be subsequently implemented.



2.2 Plugin System Design
------------------------


2.3 WebAssembly
-----------

### Rich Clients

### WebAssembly -->




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

+ Also, Javascript’s flexibility proved to be useful to support features like dynamically loading and using libraries at runtime.

- However, TypeScript does not have any runtime support for types, leading to reflection problems and problems with javascript types (no integer atomic, only number),

- Also, the absence of explicit immutability made it so that all functions will need to be 'thrusted' to not alter their input data. 



### sub 2 ”How can geocomputation libraries written in system-level languages be compiled for web consumption?”

Based on the first set of tests: 
The conclusion is a dilemma between Rust and C++:

**Rust** 
- The study could successfully expose multiple native geocomputation library in a manner properly consumable by a web-vpl. 

- This lead to a variety of applications, like loading a `.laz / .copc` point cloud, and triangulating it.

- Regrettably, the Rust language is too new to contain libraries which can be considered 'industry standard'.


**C++** 
- C++ based geocomputation libraries cannot be sufficiently compiled for web consumption, at least not for the purposes of loading the functionalities within a web-VPL. 

- The Emscripten compiler did not provide the same level of features as Rust's `wasm-pack`.

- A series of workarounds had to be created. These workarounds came close to successful utilization, 
  but the time frame of this study did not allow a final workaround to be implemented.

- C++ Has a strong foundation of existing geocomputation libraries compared to newer languages like Rust. 
  - However, this same legacy inhibits its portability, which makes for Larger binaries, less performant 'wrapper' features, 
    and makes it overall harder to compile to web browsers.

<!-- 
- To offer a solution, the study suggests that either the ’embind’ tool must be expanded to the
level of functionality of ’wasm-bindgen’, or geocomputation libraries must be rewritten in
Rust.  -->

<!-- This second option seems counterproductive, but as stated by Ammann et al. [2022]:
”innovation often requires selectively ignoring prior work. -->

### sub 3 ”To what extent can a web-consumable library be loaded into a web-vpl without explicit configuration?”

- It can be concluded that it is possible and even sufficiently usable to load a web-library into a VPL without explicit configuration. 

- Additionally, Using this method, only one type of library is needed to serve **Three formats**: as **VPL plugin**, as **native C++ / Rust library**, and as **Js library**. 

- Moreover, it led to a workflow in which **rapid experimentation** was possible, since this method allows users to develop a library locally, and then quickly
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

- Using a new javascript implementation of an acyclic, graph-based VPL, the study was able
to demonstrate how the web platform can be used to represent a dataflow-VPL capable of
hosting these libraries. 

- The dataflow-properties of a graph-based VPL like this also makes
this libraries sufficiently usable, albeit with some well-known caveats of dataflow-VPLs, like
the representation of conditionals and iteration.



The current methods of compiling existing C++ geocomputation libraries to the web turned
out to be insufficient for the purposes of this study. 
This is due to emscripten’s focus on com-
piling full C++ applications instead of libraries. Despite this, the study w ́as able to demon-
strate how a novel method can be used to compile and load a Rust-library for usage in the VPL.
While not many contemporary geocomputation libraries are written in Rust, the study offers
this method to either offer emscripten contributors a blueprint of a desired workflow, or to
offer geocomputation library contributors a powerful use-case for the Rust language.
All in all, this means that either if the Rust ecosystem gains more mature geocomputation li-
braries, or if Emscripten’s capabilities improve, then the code portability problem & dataflow
problem of existing web-based geocomputation VPLS can be overcome.

<!-- 
Discussion
----------

- Dataflow modelling? 
  - Not fully. 
  - Difficult to create a true dataflow-VPL in javascript. 
  
- Divide between Library and Application? 
  - The plugin system counts as an interesting contribution to this aspect.
  - However, ability for this VPL to be regarded as a tool for automation is still limited by multiple implementation aspects:
    - No way to 'export' a geofront script as a standalone application, without the VPL.
    - No way to run a Geofront script natively -->



