> (I know keeping old things around is very un-`git`, but I like to put things side by side once in a while)

> [JF] NOTE: maybe this should even be more concrete. Like: CGAL in a browser would be nice. Can we do that? 

> [JF] NOTE2: the introduction definitely takes too long to get going. get to the point quicker

<br> --- *Standards*

Geodata experts are often concerned with the creation and adoption of common standards. (WFS WMS, cityJSON). 
This is done to prevent an *interrelating mess*: a graph with each node connecting to every other node.
Software engineers are taught to avoid O(n^2) algorithms as much as possible, and this is a similar phenomenon. 
Sometimes, this problem can be solved by introducing one intermediary node, after which all different nodes only need to be concerned about its read-write relationship to only that intermediary. (name a vivid example + SOURCE)

[DIARGAM: INTERRELATION PROBLEM]

<br>--- *WebAssembly*

WebAssembly is an emergent technology / standard which the exact same goal (SOURCE: WASM paper). 
It is a compilation target meant to be platform & source independent. 
It attempts to be the ultimate intermediary between software and hardware, which would be a dream for developers in that sense: "Run Anything Anywhere". (SOURCE: WASM PAPER | NUANCE THIS STATEMENT)

"Run Anything" means that a platitude of languages (C, C++, Rust) can be compiled to WebAssembly, with the promise that these wasm-binaries are almost as fast as native binary compilations of those same languages. 

"Run Anywhere" means that it is possible to run a wasm-binary on Windows, Mac & Linux Desktops, natively on mobile devices, on servers, and even client-side in web-browsers. 
This runtime is also containerized, improving privacy, security against malware, and user control. 

<br>--- *Applications*

<!-- The possibility to run a system-level language in the browser already existed before, but it involved a compilation to an optimized type of javascript. Now that WebAssembly, which is specifically meant as a compilation target, runs in a browser too, this has become unnecessary.  -->

A save, platform-independent binary target which also targets the web gives makes many interesting things now possible. 
Like Docker, it can be used to run foreign software in a save, containerized manner (SOURCE: DOCKER, WASI).
This is one of the reasons why wasm is also supported by most major browsers, making it the 4th type of 'code' to run in a browser, alongside javascript, css and html. 

This means that all existing libraries written in any language are now able to be distributed by the web, enabling applications which are both powerful and accessible. 
The Google Earth web application uses WebAssembly for example (SOURCE: Google Earth). 
This way, the C++ codebase used for the desktop application could be re-used and repurposed for the web, instead of starting over again. 

[DIAGRAM: EXPLAINING CONCEPTS OF WASM]

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
Many aspects of WebAssembly remain, however, uncertain. 
The performance gain over compiling to javascript, or native development of javascript, are highly application dependent (SOURCE: NOT SO FAST). 
The performance lost by using a 'virtual binary' like wasm over a native binary optimized specifically for certain hardware is also application dependent (SOURCE: NOT SO FAST). 
Lastly, since WebAssembly is very bare-bones and does not make many assumptions about its host environment, it is unclear how 'usable' wasm is in practice.
Many tools around it exist to make working with wasm easier (wasm-pack & emscriptem), but it remains unsure what practical troubles could arise when using WebAssembly for certain applications. 

<br>--- *Problem statement*
<!-- ( Bring it back to geomatics) -->

[DIAGRAM: PROBLEM STATEMENT]

It is unclear what WebAssembly exactly means for the geospatial community. 
It could potentially fix many problems:
- What if the exact same code could be used client-side and server-side?
- What if all C++ based libraries such as CGAL could be accessed from a browser, without needing to be installed? 
- What if processes which were previously hard to chain together could suddenly work together perfectly? 

At the same time, we do not know if these advantages mean anything if it turns out that wasm is too difficult to use in practice, or just not performant enough to be a viable alternative to native geoprocessing tools. 
Websites with many wasm files could take too long to load, or accessing certain old C++ libraries on the web might not yield any real benefits for end-users. 

The potential benefits of WebAssembly, together with the many uncertainties, make research into utilizing wasm a crucial endeavour for the geospatial community. 
Both the technical capabilities of wasm for geomatics purposes need to be researched, as well as the capabilities in practical utilization. 


<br>--- *The Paper*

This paper attempts to judge the 'fitness' of WebAssembly for web-geo-processing purposes. 

This fitness will be defined technically / quantitatively by means of a performance analysis, as well as practically / qualitatively, by documenting the creation of a web-based geoprocessing application, and judging its capabilities and effectiveness in relation to other geoprocessing methods. 

The research into the technical effectiveness of WebAssembly will involve compiling C++ geoprocessing libraries such as CGAL & GDAL into WebAssembly, and then comparing the performance of these libraries against their compilation by other means (native / asm.js). 

The research into the practical effectiveness of WebAssembly will be done by creating a case study geoprocessing environment using these wasm-compiled geoprocessing libraries. 
The environment will take the shape of a visual programming language, or VPL for short. 
This, together with the web's advantage of accessibility, will hypothetically demonstrate how WebAssembly can make complex geoprocessing more easy to distribute, access and use. 
