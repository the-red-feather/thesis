
[ken]
another word for the same thing: operationalizing
- the last mile problem
- putting research in the hands of end-users

Geofront: purpose: directly use libraries in an application, and subject them to a custom UI.
- focus on direct library utilization
  - library + application becomes the central theme 
unique about this thesis 
- focus on GUI
  - text inputs 
  - number inputs
  - buttons 
  - file fetchers
  - complete micro-apps (applets)
- See a VPL less as a programming language, and more as a way for 
end users to create their own UItly usable by end-users   

Lessons
==========

- give yourself clear todo's per day. 
  Not too little, not too much.
  Upon completion, the day falls apart
  

presentation
[ ] push the latest build.


add license


=========================================================================================
=========================================================================================
=========================================================================================

[ ] proof-read the full thing: destroy embarrassing errors.
[ ] send the email.










































=======================================================================================
=======================================================================================
=======================================================================================



Introduction
============

visualization and analysis

THE VPL as an end-user tool, rather than a "GIS specialist only" tool.


  <!-- - The preference slowly shifts from downloading geodata, and performing calculations locally, 
    to uploading the code itself towards the location the geodata is stored, and performing calculations there [source](one of the main cloud native papers).
  - As a consequence, we see cloud-based geocomputation platforms being developed, like the Google Earth Engine [source](Google earth engine). 
    -> offers a platform for people to create geocomputation pipelines, and run it on their servers.  -->

1. More and more geodata is becoming available online as passive, static data storage.   


-------------------------------

Taken together, 




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
Google Earth Engine offers a possible model, using a special dialect of javascript. 
In other words: **what does a platform for writing geocomputation pipelines look like, if we wish to create, edit, and run geo-pipelines in both a browser-based setting, and on the cloud?**

This question needs an answer, because the current way of constructing pipelines is not necessarily well-suited for browser and cloud platforms. 
Moreover, a proper answer to this question might lead to one, unified model for geocomputation across native, browser and cloud platforms. 

This question is non-trivial, because the specific needs for both browser-based and cloud-based geocomputation are very different from normal, native methods. 
In particular, this study chooses to focus on three principles which are vital to cloud and browser-based methods, but not necessarily for native methods:


-> Browser and cloud based geocomputation has different needs as opposed to native methods.
-> These needs have an impact on how geocomputation pipelines are required to be constructed.
-> These needs are encapsulated by the following three principles:

1. **Local Correctness principle**
2. **Portability principle**
3. **Minimum abstraction Cost principle**

### Three necessities for a scalable GIS VPL:

1. **Local Correctness**
  - A geocomputation pipeline should be "locally correct" by adhering to functional programming principles.
    - Pure functions: Functions without state or side effects.
    - Immutable variables
  - WHY: This is valuable for scalability, for it allows implicit concurrency. 
    - example: Google Earth engine had to develop a functional javascript dialect as a possible solution to this problem: 
      (https://developers.google.com/earth-engine/tutorials/tutorial_js_03)

   (- leading to: The application should be a Dataflow VPL)
   (- many other benefits: Hot code deployment, unit testing and containerization.)
   (- Analogous to the local correctness principle of a delaunay triangulation)

2. **Portability**
  - Webassembly allows an expanded definition of portable, 'cross-platform software' [mapbox.rs].
  - Given this development, both a geocomputation pipeline, as well as the platform this pipeline is created in, should be able to run on Linux, Windows, Mac, _plus_ on a web browser. (+ no OS)
  - This counts as well for all libraries and functionalities used within a geocomputation pipeline.
  - WHY: This is beneficial for the same reason as traditional cross-platform arguments: 
    - no duplicate libraries, no burden of synchronizing functionality across multiple libraries [mapbox.rs]  
  - WHY: This portability is vital for cloud-based computation, evident by the popularity of Docker Containers in cloud computation [source]

   (- Leading to: Making the application web based )
     (- The containerized nature of cloud-based geocomputation fits the containerized nature of web applications)
     (- The web improves availability)
   (- Leading to: Using native geocomputation libraries in a portable format (compiled to webassembly))

3. **Minimum abstraction Cost**
  - In order to adhere to the previous two principles, certain abstractions are required. 
  - However, these abstractions should introduce as little overhead as possible, 
    both in terms of performance costs and maintenance costs.

   (- Leading to: A unique plugin system, to use these portable libraries with as little in-between systems as possible.)
   (- Leading to: developing a compilation from and to javascript.)

<!-- It is important to recognize the interplay between these principes. 
For example, a docker container can make an application more portable, but increases the abstraction cost.  -->

Possible Solution: A web-based dataflow VPL
--------------------------

This study seeks a possible solution which is able to adhere to these principles. 



Methodology
==================


Scalability will be achieved in three ways: 
1. **Local Correctness** 
   -> The VPL prototype is designed as a Dataflow VPL, which allows implicit concurrency.
2. **Portability** 
   -> The application uses native geocomputation libraries which behave the same way in the front- and back-end. 
3. **Minimum abstraction Cost** 
   -> The application uses a unique plugin system, to offer direct usage these portable libraries. 
   -> Pipelines to offer direct usage these portable libraries.

- Dataflow models can be configured using a VPL. 
  - VPLs good fit for GIS: offers both the interface of a software application, and the composability of a software library. 



This study
==========

More precisely: Design and develop a proof of concept application which attempts to adhere to the three aforementioned principles for a browser- and cloud-ready geocomputation pipeline mentioned above.
Then, perform a series of tests and assessments to judge to what extent the implementation adheres to these principles.


Research Questions
==================

__MAIN QUESTION__: Is a GUI-rich dataflow VPL a viable option for constructing browser-based geocomputation pipelines?

1. What GUI features are required to facilitate a geocomputation VPL in a web browser?

2. Are the functional properties of a dataflow-VPL uphold by this solution?

3. How can native geocomputation libraries be compiled, loaded, and utilized within a browser-based dataflow-VPL?

4. What measures are taken to reduce the abstraction cost of this solution, and how effective are these measures?

(A: javascript, unsuccessful, Libraries, very successful, but only on a usage level. The abstractions of translating between rust and javascript are still in place.)

Conclusion
====================

__ANSWER TO MAIN QUESTION__: 
Probably. 
The unique set of features combined in this platform appears promising for browser-based geocomputation. 
Being able to directly use system-level libraries in a published, web based environment, 

However, 

Reading Guide
=============



Background
==========

### VPL

what does it mean to design a VPL?
What does it mean to design a VPL for computational geometry and Computer Graphics (CG)?
what does it mean to design a VPL for GIS?
What does it mean to design a VPL for web-based GIS?   

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


<!-- Node.js has been developed, not because there is any real use-case to running javascript natively, OTHER than making it so one language can reach all locations and platform: Frontend, Backend, Native applications (Electron).  -->
