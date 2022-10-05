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

- Content will be as can be expected: 
  - Introduction
  - Problem statement
  - Solution
  - Conclusion

- the time constraints of only 10 minutes will 

- background and related studies are integrated within the methodology.
  - However, numbering is kept the same with the chapters of the written thesis, 
    to make the relation between the presentation and thesis more clear. 

- I will go over the main items of the thesis

1 Introduction
===================================

1.1 Motivation
-----------------------------------
<!-- 
- **GEOCOMPUTATION** 
  - (or Geoprocessing)
  - is one of the CORNERSTONES of GIS and all modern mapping needs.
  - It is a broad topic, almost to broad to consider.
  - The term 'geocomputation' is used to represent all types of computations performed on geographical datasets. 
    - Anything from: 
      - the calculation of the area of a region, 
      - to a Coordinate Reference System (CRS) transformations
      - or converting a raster dataset into a vectorized dataset,
    - can be regarded as geocomputation. -->

- **GIS SOFTWARE NORMALLY COMES IN TWO FORMS**: Applications, and Libraries [REF: Elliott, 2007]
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

- Three challenges are identified** to using native library in a vpl: 
    - Firstly, **I. Compilation**:
    - Secondly, **II. Loading**:
    - Lastly **III. Utilization**: 


- **Goal: Solving the library portability problem for web-based VPLs.**
  - make it so native, system level libraries can be used in a web-based VPL. 
  
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


Background 
==========

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

Methodology
===========

- The methodology used to find answers to these questions is defined as follows: 
  - First, a **custom web VPL** is designed and implemented as a **host** for the libraries. 
  - Second, a **plugin system** is designed and implemented.
    - The system consists of: 
      - A Plugin Loader on the side of this VPL, and 
      - A Plugin model the libraries must adhere to. 
  - Finally, Two sets of **tests** are performed:
     - one set to analyse to what extent this plugin system allows for the compilation of native libraries.
     - one set of tests to analyse to what extent this solution allows for proper utilization of those native libraries. 


Results
=======

Results : Base VPL
------------------
- The study opted for designing a custom implementation,
  - which takes hosting geocomputation libraries from multiple sources into account from the start.
  - Additionally, no existing web-based VPLs were implemented as true dataflow-VPLs 
    - (Möbius modeller only is a graph-based VPL).

It turned out that this design could indeed be implemented on the web in TypeScript (JavaScript). 
This implementation had advantages and disadvantages: 

+ The big advantage of a TypeScript implementation is that a great number of features do not need to be included within the source code of the application, leading to quick load times.
    + WebGL, UI (HTML), 2D Canvas API
+ Also, Javascript’s flexibility proved to be useful to support features like dynamically loading and using libraries at runtime.

- However, TypeScript does not have any runtime support for types, leading to reflection problems and problems with javascript types (no integer atomic, only number),

- Also, javascript is not a good host for enforcing dataflow-VPL constraints. 
  - for example, the absence of explicit immutability made it so that all functions will need to be 'thrusted' to not alter their input data. 


Results : Plugin System
-----------------------

- A novel plugin system was designed to load a library compiled to WebAssembly into this prototype VPL almost without explicit configuration. 
  - This method allows one library to serve **Three formats**: as **VPL plugin**, as **native C++ / Rust library**, and as **Js library**. 
  - Moreover, this method allows users to develop a library locally, and then quickly experiment and test its usage online.

- This design was implemented successfully, albeit with some limitations, and certain aspects which did need explicit configuration. 

- The biggest drawback was that by designing a lenient, non-restrictive loader, the 'dataflow' qualities could again not be enforced. 
   (Libraries loaded can produce side effects, can point some object loaded in memory, there is no way of preventing them)


Results : Compilation Tests
---------------------------

### ”How can geocomputation libraries written in system-level languages be compiled for web consumption?”

The aforementioned plugin system was tested by attempting to load multiple libraries. 
The conclusion of these tests raise a dilemma between Rust and C++:

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


Results : Usage Tests
---------------------

### ”How can a ’geo-web-vpl’ be used to create geodata pipelines?”

Based on the analysis of Geofront in Section 6.2, it can be concluded that a geo-web-VPL can
be used for geocomputation to a sufficient extent. 

- The analysis shows that many of Geofront’s best aspects for the purpose of geocomputation are a consequence of the design decision to
use a diagram-based, dataflow-type VPL. 
  - Examples of this are how immutable variables allow in-between data to be cached and inspected at runtime. 

- However, as stated by the previous results, certain implementation details led to compromises to this model, 
  ultimately leading to confusion for the end-user
