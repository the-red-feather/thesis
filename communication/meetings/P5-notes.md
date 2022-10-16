



Lessons
==========

- give yourself clear todo's per day. 
  Not too little, not too much.
  Upon completion, the day falls apart


TODO
============

high-level
----------

[ ] The intro / story needs to be altered 
    - stronger tie to Geo & web
    - VPL + Web

[ ] rewrite and balance research questions

- [ ] than trickle down the consequences of those changes throughout the thesis
- [ ] and fix all that needs to be fixed (images and stuff)

mid-level
---------

[ ] Deep dive in Hugo's comments, fix those aspects 
  - [x] sort acronyms

[ ] Add a stronger web-component in the introduction (presentation)
[ ] Add cloud native / cloud-based geodata component to the introduction  

[ ] Cleanup Chapter 2 and 3.  
  - Some parts are still more relevant than other parts. 
  - Also, there are some things I say or use in chapter 4, 5, and 6, that were not properly explained in chapter 2. Examples of this are emscripten, or CGAL. 
  - However, a complete rewrite would be too much work.
  - Would love to hear your take on this.

[ ] Make chapter 4 and 5 more streamlined 
  - I've noticed that I repeat myself quite often.
  - I think this is because I was not sure if I already said something relevant in the chapter before.

[ ] Show your results more clearly, do the coding you have done justice

[ ] finish chapter 6 properly 
  - Experiments: add a section on a use-case application, using potree + startin + geofront std + obj downloader

[ ] write stronger, more clear conclusions.
  - hmm, i think they are already quite clear. But again, this is to be reconsidered when the overall story of the thesis changes  

low-level 
-------------------

- [x] Add arsclassica template to the thesis
- [x] Make the code snippets / listings work properly
- [x] replace all code screenshot with proper listings
- [ ] create all missing uml diagrams
- [ ] add proper graphs for the data you've gathered 
- [ ] Add all proper metadata to Zotero, for a nice bibliography





=========================================================================================
=========================================================================================
=========================================================================================



Introduction
============

[The current geocomputation intro]

Two major developments to the GIS software landscape are changing how and were we are performing geocomputations: 

1. Cloud-first paradigm shift
  - More and more geodata is becoming available online, either as an active web service, or as passive, static data storage.   
  - The preference slowly shifts from downloading geodata, and performing calculations locally, 
    to uploading the code itself towards the location the geodata is stored, and performing calculations there [source](one of the main cloud native papers).

Impact: We see cloud-based geocomputation platforms being developed, like the Google Earth Engine [source](Google earth engine). 
  -> offers a platform for people to create geocomputation pipelines, and run it on their servers. 

2. introduction and adoption of webassembly (webassembly papers)
  - run native code on the web. 

Impact: Webassembly allows an expanded definition of 'cross-platform libraries' [mapbox.rs]
  - Windows, Mac, Linux, **and the Web**. ( and no-OS )
  - This is benefitial for the same reason as traditional cross-platform arguments: 
    - no duplicate libraries, no burden of synchronizing functionality across multiple libraries   

-------------------------------

These two developments together also offer the opportunity of geocomputation in the browser, instead of native
  -> Benefits availability and distribution: 
     - No installment
     - Shared by a link
  -> Benefits reproducibility & open science:
     - Software developed is not only open source, but directly usable.
     - Developers are forced to address the openness of data used.


Problem: 
-----------------------------

<!-- (Pipeline or platform?) -->

<!-- (
  These developments and implications open up a vast, new space of possibilities.
One of the possibilities is a web applications which offers browser-based geocomputation.

  However, while these developments offer the _opportunity_ to do so, 
the specific shape in which this should take place remains unknown.  
Also, no free and open source solution exist yet which offers this new way of geocomputation to end-users.
) -->

The novelty of these developments mean that many important details and implications of these developments remain unknown.
One such detail is what geocomputation platform aligned with these developments should look like. 
Google Earth Engine offers a possible model, 
In other words: **what does a platform for writing geocomputation pipelines look like, if we wish to create, edit, and run geo-pipelines in both a browser-based setting, and on the cloud?**

This question needs an answer, because the current way of constructing pipelines is not necessarily well-suited for browser and cloud platforms. 
Moreover, a proper answer to this question might lead to one, unified model for geocomputation across native, browser and cloud platforms. 

This question is non-trivial, because the specific needs for both browser-based and cloud-based geocomputation are very different from normal, native methods. 
In particular, this study chooses to focus on three principles which are vital to cloud and browser-based methods, but not necessarily for native methods:

-> 
-> Browser and cloud based geocomputation has different needs as opposed to native methods.
-> These needs have an impact on how pipelines are required to be constructed.
-> These needs are encapsulated by the following three principles:

1. **Local Correctness principle**
2. **Portability principle**
3. **Minimum abstraction Cost principle**

### Three necessities for a browser- and cloud-ready geocomputation platform:

1. **Local Correctness principle**
  - A geocomputation pipeline should be "locally correct" by adhering to functional programming principles.
    - Pure functions: Functions without state or side effects.
    - Immutable variables
  - This is valuable for cloud computation, for it allows implicit concurrency. 
    - example: Google earth engine developed a functional javascript dialect: (https://developers.google.com/earth-engine/tutorials/tutorial_js_03)


   (- leading to: The application should be a Dataflow VPL)
   (- many other benefits: Hot code deployment, unit testing and containerization.)
   (- Analogous to the local correctness principle of a delaunay triangulation)

2. **Portability principle**
  - an extended definition on "cross-platform"
  - Both a geocomputation pipeline, as well as the platform this pipeline is created in, should be able to run on Linux, Windows, Mac, _plus_ the web. 
  - This counts as well for all libraries and functionalities used within a geocomputation pipeline.

   (- Leading to: Making the application web based )
     (- The containerized nature of cloud-based geocomputation fits the containerized nature of web applications)
     (- The web improves availability)
   (- Leading to: Using native geocomputation libraries in a portable format (compiled to webassembly))

3. **Minimum abstraction Cost principle**
  - In order to adhere to the previous two principles, certain abstractions are required. 
  - However, these abstractions should introduce as little overhead as possible, 
    both in terms of performance costs and maintenance costs.

   (- Leading to: A unique plugin system, to use these portable libraries with as little in-between systems as possible.)
   (- Leading to: as well as developing a compilation from and to javascript.)

<!-- It is important to recognize the interplay between these principes. 
For example, a docker container can make an application more portable, but increases the abstraction cost.  -->

Possible Solution: A web-based dataflow VPL
--------------------------

This study seeks a possible solution which is able to adhere to these principles. 

1. **Local Correctness principle** 
   -> The application is a Dataflow VPL, which adheres to functional programming principles.
2. **Portability principle** 
   -> The application is web based.
   -> The application uses native geocomputation libraries in a portable format.
3. **Minimum abstraction Cost principle** 
   -> The application uses a unique plugin system, to offer direct usage these portable libraries. 
   -> Pipelines to offer direct usage these portable libraries.

- Dataflow models can be configured using a VPL. 
  - VPLs good fit for GIS: offers both the interface of a software application, and the composability of a software library. 



This study
==========

Goal:  
Three principles for a browser- and cloud-ready geocomputation pipeline:
  <!-- - By no means an exhaustive exploration, but after this study, it will become more clear what are and what are not good ideas for modern web front-ends. -->


How: Explore the possibility of using a browser-based dataflow VPL as a cloud-ready geocomputation platform.
How: Design and develop a proof of concept application which attempts to adhere to the three principles for a browser- and cloud-ready geocomputation pipeline mentioned above.
Then, perform a series of tests and assessments to judge to what extend the implementation adheres to these principles.

and perform a series of test on this application.



Research Questions
==================

__MAIN__: Is a web-based dataflow VPL a viable option for constructing browser- and cloud-ready geocomputation pipelines?

Additionally the following set of sub-research questions are defined:





1. How can native geocomputation libraries be compiled, loaded, and utilized within a browser-based dataflow-VPL?

2. Are those characterizations respected in the Voronoi- and surface-based approach?

3. Does the Voronoi- and surface-based approach perform well for heterogeneously distributed input data?

4. To what extent can the Voronoi- and surface-based approach be automated?

5. Is the Voronoi- and surface-based approach well scalable to big datasets?



__How well does a web-based Dataflow VPL

__How can native geocomputation libraries be compiled, loaded, and utilized within a browser-based dataflow-VPL?__

To what extent is a browser-based application able to facilitate a generic 3D geometry vpl?}}

\newcommand{\mySubRQOne}{\textit{How to implement a browser-based dataflow-vpl for processing 3D geometry?}}

% \newcommand{\mySubRQOne}{\textit{How to implement a visual programming environment in a browser which able to facilitate geo-computation?}}
\newcommand{\mySubRQTwoTitle}{Compilation}
\newcommand{\mySubRQTwo}{\textit{How can geocomputation libraries written in system-level languages be \textbf{compiled} for web consumption?}}
\newcommand{\mySubRQThreeTitle}{Loading}
\newcommand{\mySubRQThree}{\textit{To what extent can a web-consumable library be \textbf{loaded} into a web-vpl without explicit configuration?}}
\newcommand{\mySubRQFourTitle}{Utilization}
% \newcommand{\mySubRQFour}{\textit{What are the advantages and disadvantages of \textbf{using} an existing geoprocessing library through a geo-web-vpl, as opposed to native utilization of said library?}}
\newcommand{\mySubRQFour}{\textit{How can a 'geo-web-vpl' be \textbf{used} to create geodata pipelines?}}


__MAIN__: Is the Voronoi- and surface-based approach a viable option for the automatic generation of depth-contours for hydrographic charts?

Additionally the following set of sub-research questions are defined:

1. What characterizes surfaces that lead to good depth contours for hydrographic charts and what is needed in terms of interpolation and generalization to achieve such a surface?

2. Are those characterizations respected in the Voronoi- and surface-based approach?

3. Does the Voronoi- and surface-based approach perform well for heterogeneously distributed input data?

4. To what extent can the Voronoi- and surface-based approach be automated?

5. Is the Voronoi- and surface-based approach well scalable to big datasets?



Reading Guide
=============



Background
==========

### VPL

what does it mean to design a VPL?
What does it mean to design a VPL for computational geometry and Computer Graphics (CG)?
what does it mean to design a VPL for GIS?
What does it mean to design a VPL for web-based, cloud-native GIS?   

The 3 principles:
- 


### VPL: Dataflow programming 

Dataflow programming

there are quite a few ways to frame a VPL. 
Some say it is just a nice UI to offer 'coding for dummies'.
I wanted to frame the VPL in a different light by tying it to the balance between libraries and applications, and by tying it to dataflow programming.

- Functional programming benefits
  
  - Many benefits thanks to "Local correctness principle":
  - Concurrency 
  - Debugging
  - Hot code deployment
  - Unit testing
  - etc. etc.
  


### Portability & WebAssembly

As of right now, the GIS software landscape has a lot of overlapping libraries with the only difference being web and native:
- web and native viewers, web and native geocomputation, 

simply put: One and the same geo-library which can be used: 
- Natively by software developers
- On the web by software developers
- On the web by end-users

Conclusion
==========

While the implementation is still an experimental proof of concept, the results of this study are nonetheless promising:
Based on the explorations and findings of this study, it has become clear that the theoretical concepts introduced by this thesis are practically feasible.
...
...





======================================================================================================================================

_"Make a sketch for what you are truly trying to achieve personally. Then convert it to 'acceptable' form"_ 









<!-- Node.js has been developed, not because there is any real use-case to running javascript natively, OTHER than making it so one language can reach all locations and platform: Frontend, Backend, Native applications (Electron).  -->




==========================================================

_Alright, now how to tie this with the application and library dichotomy?_

VPL + WEB + GEO

wasm + cloud = bbg


1. web + cloud = bbg.
2. looking for ways 

VPL: the way?





