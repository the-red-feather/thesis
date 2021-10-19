<!-- 

[ ------- FROM THE GEO2020 WEBSITE ------- ]

P2 template

The document for P2 is a research proposal that must contain:
- all the elements listed in the template available in the graduation manual (Appendix 2).
- You are free to write your project plan with the word processor of your choice (including LaTeX), as long as all the asked parts are present, in the same order. You can use that simple LaTeX template as starting point.
  - (LaTeX is strongly recommended tho...) [JF]: Ill try to use markdown for the time being. I think I will not need the advanced features of LaTeX (just yet). 
- We expect a project plan to be around 10-15 pages (maximum). 
- It should show that you clearly know the problem you plan to solve, 
- and that you master the related work. 
- We expect you to present the methodology you will use to solve your scientific problem(s), and to present preliminary results. 
- Also, this is a scientific proposal, so references are mandatory (even if there is no specific section in the template).

As an example, here’s a good project plan from a previous year. It contains:
    - an introduction in which the relevance of the project and its place in the context of geomatics is described, along with a clearly-defined problem statement;
    - a related work section in which the relevant literature is presented and linked to the project;
    - the research questions are clearly defined, along with the scope (ie what you will not be doing); to help you define a “good” research question, read this document
    - overview of the methodology to be used;
    - time planning—having a 'Gantt chart' is probably a better idea than just a list;
    - since specific data and tools have to be used, it’s good to present these concretely, so that the mentors know that you have a grasp of all aspects of the project;
    - the references.
'


MY NOTES

WebAssembly for geomatics?
- Why should we want to use it for geomatics?
- Can we technically use it for geomatics?
- Can we practically use if for geomatics? 






 -->

1.- INTRODUCTION
===============================================================================

> [JF] NOTE: maybe this should even be more concrete. Like: CGAL in a browser would be nice. Can we do that? 

<br> --- *Standards*

Geodata experts are often concerned with the creation and adoption of common standards. (WFS WMS, cityJSON). 
This is done to prevent an *interrelating mess*: a graph with each node connecting to every other node.
Software engineers are taught to avoid O(n^2) algorithms as much as possible, and this is a similar phenomenon. 
Sometimes, this problem can be solved by introducing one intermediary node, after which all different nodes only need to be concerned about its read-write relationship to only that intermediary. (name a vivid example + SOURCE)

<br>--- *WebAssembly*

WebAssembly is an emergent technology / standard which the exact same goal (SOURCE: WASM paper). 
It is a compilation target meant to be platform & source independent. 
It attempts to be the ultimate intermediary between software and hardware, which would be a dream for developers in that sense: "Run Anything Anywhere". 

"Run Anything" means that a platitude of languages (C, C++, Rust) can be compiled to WebAssembly, with the promise that these wasm-binaries are almost as fast as native binary compilations of those same languages. 

"Run Anywhere" means that it is possible to run a wasm-binary on Windows, Mac & Linux Desktops, natively on mobile devices, on servers, and even client-side in web-browsers. 
This runtime is also containerized, improving privacy, security against malware, and user control. 

<br>--- *Applications*

<!-- The possibility to run a system-level language in the browser already existed before, but it involved a compilation to an optimized type of javascript. Now that WebAssembly, which is specifically meant as a compilation target, runs in a browser too, this has become unnecessary.  -->

A save, platform-independent binary target which also targets the web gives makes many interesting things now possible. 
Like Docker, it can be used to run foreign software in a save, containerized manner (SOURCE: DOCKER, WASI).
This is one of the reasons why wasm is also supported by most major browsers, making it the 4th type of 'code' to run in a browser, alongside javascript, css and html. 

This means that all existing libraries written in any language are now able to be distributed by the web, enabling applications which are both powerful and accessible. The Google Earth web application uses WebAssembly for example (SOURCE: Google Earth). This way, the C++ codebase used for the desktop application could be re-used and repurposed for the web, instead of starting over again. 

<br>--- *FAIR*

An important side-note is the relationship of WebAssembly and the FAIR principles. The FAIR principles are a collection of four well-established assessment criteria used for judging the usability of software applications (SOURCE). They stand for Findable, Accessible, Interoperable, and Reusable. WebAssembly has the potential to improve all four of those criteria for a piece of software:  

WASM web apps: 
There is no delay between Findability and Accessibility. 
As soon as it can be found, it can be accessed. 

WASM containerized:
If the core logic of something is compiled into a wasm library, than this logic becomes Interoperable and Reusable. 
We can be sure that it will produce the same results, wherever it is run. 
Write once, use anywhere <-> Collect once, use multiple times

<br>--- *Uncertainty* 
<!-- ( WebAssembly is not all sunshine and rainbows ) -->
Many aspects of WebAssembly remain, however, uncertain. The performance gain over compiling to javascript, or native development of javascript, are highly application dependent (SOURCE: NOT SO FAST). 
The performance lost by using a 'virtual binary' like wasm over a native binary optimized specifically for certain hardware is also application dependent (SOURCE: NOT SO FAST). 
Lastly, since WebAssembly is very bare-bones and does not make many assumptions about its host environment, it is unclear how 'usable' wasm is in practice.
Many tools around it exist to make working with wasm easier (wasm-pack & emscriptem), but it remains unsure what practical troubles could arise when using WebAssembly for certain applications. 

<br>--- *Relevance*
<!-- ( Bring it back to geomatics) -->

It is unclear what WebAssembly exactly means for the geospatial community. The potential of improving the FAIR qualities of geoprocessing software seems very promising: 
- What if the exact same code could be used client-side and server-side?
- What if all C++ based libraries such as CGAL could be accessed from a browser, without needing to be installed? 
- What if processes which were previously hard to chain together could suddenly work together perfectly? 

At the same time, we do not know if these advantages mean anything if it turns out that wasm is too difficult to use in practice, or just not performant enough to be a viable alternative to native geoprocessing tools. Websites with many wasm files could take too long to load, or accessing certain old C++ libraries on the web might not yield any real benefits for end-users. 

The potential benefits of WebAssembly, together with the many uncertainties, make research into utilizing wasm a crucial endeavour for the geospatial community. 
Both the technical capabilities of wasm for geomatics purposes need to be researched, as well as the capabilities in practical utilization. 


<br>--- *The Paper*

This paper attempts to judge the 'fitness' of WebAssembly for web-geo-processing purposes. 

This fitness will be defined technically / quantitatively by means of a performance analysis, as well as practically / qualitatively, by documenting the creation of a web-based geoprocessing application.
 
<!-- [JF] Increase granularity, now this is just a copy  -->
The research into the technical effectiveness of WebAssembly will involve compiling C++ geoprocessing libraries such as CGAL & GDAL into WebAssembly, and then comparing the performance of these libraries against their compilation by other means (native / asm.js). 

The research into the practical effectiveness of WebAssembly will be done by creating a case study geoprocessing environment using these wasm-compiled libraries. The environment will take the shape of a visual programming language, or VPL for short. 
This, together with the web's advantage of accessibility, will demonstrate 


 using WebAssembly-compiled geoprocessing libraries


<br><br><br><div class="page">

2.- RELATED WORK
===============================================================================

The execution of this research requires adequate background knowledge on:
- wasm itself 
- wasm performance in diverse circumstances 
- Relevant wasm based applications
- wasm's surrounding tools and compilers

In addition, since the case study application 

<br><br><br>

## x.x On WebAssembly


### x.x.x Bringing the Web up to Speed with WebAssembly
This is the original paper introducing WebAssembly



The


### x.x.x Not So Fast WebAssembly Paper 
Paper on general performance of webassembly


### x.x.x Michael Yuan — Tensorflow inference on WebAssembly

_Michael Yuan — Tensorflow inference on WebAssembly_



_https://www.youtube.com/watch?v=poe0Z7GR8uI_


This talk by Dr. Michael Yuan explains the advantages of WebAssembly for especially the utilization (inference) of trained AI models. 
This is relevant, since the field of AI is, like the field of geo-informatics, concerned with complex calculations and the efficient processing of large datasets. 
Dr. Yuan states that, while python might be a fine choice for training AI models, the actual inference / usage of those models is very inefficient using contemporary tools. 
Python is very slow, does not run on edge devices, and offers limited support in (web) application frameworks. 
A native application ís fast, but offers different challenges. 
A native app is tied to its specific hardware platform, cannot be orchestrated, is very sensitive to bugs or attacks, is not save since it has OS-level access, and just like python, cannot easily be integrated in web or application frameworks.

The lecturer claims that WebAssembly solves these problems because it is containerized and thus save, while at the same time being very performant. Additionally, the fact that is is a language agnostic compile target, and can be used together with many (web) applications, makes it an excellent solution to the earlier mentioned problems.

this talk further supports the claims made that geodata processing would benefit from adopting WebAssembly. At the same time, it is mainly concerned with improving server side performance, which is outside the scope of this paper. 

<!-- 

related article 
https://www.secondstate.io/articles/why-webassembly-server/

related paper 
https://arxiv.org/abs/2010.07115


related company (supported by the linux foundation)
https://www.secondstate.io/ 

why relevant: 
this talk further supports the claims made that geodata processing would benefit from WebAssembly. 

notes:
- clearly states the advantages of something like wasm, and the philosophy behind it.
- focus on INFERENCE
  - Very important point to me as well: inference represents the operational step, what I started calling the "last mile problem".
- shows webassembly benefits to advanced computation use cases like machine learning. 

from the slides: 

- WebAssembly
  - high performance
  - sandbox safety
  - capability-based security 
  - language-agnostic
  - product-community fit
  
  - Better than native apps, because native apps ...
    - are not portable (Tied to specific OS or hardware platforms)
    - cannot be integrated into web or application frameworks 
    - cannot be managed or orchestrated
    - crashes from bugs & attacks 
    - unsafe: coursely grained, OS-level access control

  - Better than python, because python ...
    - 60.000x slower than C 
    - does not run on edge devices and platforms
    - limited support in web & application frameworks 
    -->






<br><br><br>

## x.x Relevant WebAssembly Tools


### x.x.x Emscriptem
Emscriptem is a tool 

### x.x.x Wasm-Pack 
wasm-pack can be seen as the emscriptem equivalent, but created to serve the `Rust` programming language. 

## x.x Relevant 

### x.x.x CGAL 


### x.x.x 3dfier ???? 


<br><br><br>

## x.x On VPLs
Lastly, the third topic requiring background knowledge is the topic of visual programming languages



### x.x.x The relevant vpl paper



### x.x.x Existing VPL's






<br><br><br>

3- RESEARCH QUESTIONS
===============================================================================

## 3.1 Objectives

This paper's main objective is to judge the fitness of WebAssembly for client-side geo-processing purposes. 
This fitness will be judged quantitatively by means of a performance analysis, as well as qualitatively by documenting the creation of a web-based geoprocessing application using WebAssembly. 

The main research question goes: 

> ***How well does WebAssembly support a client-side geoprocessing vpl?***

This question contains two main components: WebAssembly for geo-processing, and a visual programming language. It then asks how well the one supports the other. These components are reflected in the sub-questions: 

<!-- Create research questions that result in the desired answers:
"How can someone one do this?" is answered by showing how this was implemented
 -->

1. **GEO-WASM**: How well can C++ geoprocessing libraries such as CGAL & 3dfier be used within a web browser without needing to be installed, by using WebAssembly?
    - 2a: How well do WebAssembly compiled geoprocessing (geo-wasm) libraries perform compared to native, cli usage?
    - 2b: How to handle types / data models between multiple, unrelated `wasm` libraries?
    - 2c: How do C++ geoprocessing libraries differ from all other C++ libraries?
    - 2d: What does this difference mean for `wasm` compilation and usage? 


2. **GEO-WEB-VPL**: How to make a web-based, client-side, vpl geoprocessing environment?
    - 1a. **GEO**: What basic features does a geoprocessing environment need?
      <!-- - *answer: MOSKOW* -->
    - 1b. **WEB**: What advantages and limitations does a HTML5, CSS & JS based environment and interface give us?
      <!-- - *answer: Canvas, HTML as ui, webgl limitations, javascript as scripting, JIT compiler, etc* -->
    - 1c. **VPL**: What are the advantages and disadvantages of using a vpl?
      <!-- - *answer from the vpl papers*  -->


3. **GEO_WASM + GEO-WEB-VPL**: How well can geo-wasm libs be used within the context of a geo-web-vpl?
    - 3a: What data must a geo-wasm provide in order to become usable within a geo-web-vpl?
      <!-- - *answer: descriptors of operations and variables, how many inputs and outputs, etc.* -->
    - 3b: How can this data be utilized by the geo-web-vpl? 
      <!-- - " -->
    - 3c: How are the geo-wasm libraries distributed?
      <!-- - *answer: web service like npm or pip? Something like an app store?* -->
    




## 3.2 Scope 

LIMITED TO:
- WebAssembly for web-usage 
- Geo-processing client-side

NOT:
- web processing services or server orchestration 
- WASI

<!-- 
(WebAssembly could be just a buzzword, a hype-based virus which hops from conference to conference. )
 -->


<br><br><br><div class="page"></div>

4- MOTIVATION 
===============================================================================

## 4.1 'higher level' questions. 

The research questions chosen for this research are part of a set of larger questions. While the research will not completely answer the following questions, I believe the questions are nonetheless important to adress.

> What should the field of geomatics do with WebAssembly?
> - Why should the field of geomatics be interested? 
>   <!-- A: Yes  -->
> - Can we technically use it for geomatics? 
>   <!-- A: Probably  -->
> - Can we practically use if for geomatics? 
>   <!-- A: Unsure -->

This also further explains the need for the vpl application within this research. I believe it necessary to develop an application whom's existence serves as a starting point for answering the more complicated "why should we", and "practical" sub-questions.

<br><br><br>

## 4.2 Additional problems the software tries to solve, and features it tries to present:

I would like to state an additional range of 

### - Real-time geodata processing

- A number of use-cases exist with a growing need for real-time geodata processing. (SOURCE: INCIDENT MAPPER)

- Moving tools like CGAL closer to the final product (Web Application) can create more dynamic applications. 

### - Improved Geoprocessing Ergonomics

- Insightful debugging: Client-side geoprocessing together with a VPL allows direct user feedback unlike server-side geoprocessing. Users can be on top of the calculations, look at in betweens steps, reconfigure the procedure without recompilation, see the immediate effects of parameter changes. 

- Improved communications: Users will be able to share demo's and procedures with a link.

- Improved accessibility: Users will not have to install anything except a web-browser.
  This will make geoprocessing more accessible & operational to a larger audience. It allows more people to do more things with geodata, and reach more interesting conclusions quicker. 

### - Just In Time / Personal Geodata

- JIT: Instead of having large, preprocessed datasets, geodata could be processed on demand from the source client-side. If a user is only interested in a small area of the source dataset, this could save vast amounts of time, storage space and computational resources. 

- Personal: It also allows the end user to tailor geodata to their exact needs. 






<br><br><br><div class="page"></div>

5- METHODOLOGY
===============================================================================


(utilize pre-work)

## 5.1 Software


## 5.2 Tests


## 5.3 Case Study

> ### *Demo Application: On Demand Triangulator + Isocurves* 
> 
> ### Input: 
> - Point Cloud
> 
> ### Output
> - Line Curves / .png render of line curves
> 
> ### Steps: 
> - Load ahn3 point-cloud (WFS Input Widget | WFS Preview Widget)
> - Visualize point cloud on top of base map of the netherlands (WMS Input Widget | WMS > Preview Widget)
> - Only select terrain points (list filter Operation)
> - Construct a 2d polygon by clicking points on a map (Polygon Input Widget)
> - Select Area of interest using a 2d polygon (Boundary Include Operation)
> - Triangulate point cloud with a certain resolution (Triangulate Operation)
> - Intersect the mesh surface with a series of planes (Isocurves from Mesh Operation)
> - Preview data (MultiLine Preview Widget)
> - Export data (MultiLine export Widget)


<br><br><br><div class="page">

6- PLANNING
===============================================================================


TODO
- write P2 presentation
- build the VPL
- apply VPL to Case Study
- build a similar application using python + jupyler, or some other conventional method
- perform tests and compare the two

<br><br><br><div class="page">

7- TOOLS USED
===============================================================================

Languages
  - WebAssembly
    - As compile target 

  - C++
    - 
  - Typescript / Javascript 
    - Front-end code
    - WebGl & javascript Canvas api
      - visualization 

  - Rust ????


Libraries & Tools 

- Emscriptem

- Wasm-Pack

- SSVM ???
  - : WebAssembly high performant virtual machine meant for server side



Data
  - WMS \& WFS services hosted by PDOK.
  - sample Geojsons from the geojson site 
