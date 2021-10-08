(semi-formal attempt at an introduction)

# introduction

## Standards

Geodata experts are often concerned with the creation and adoption of common standards. (WFS WMS, cityJSON). This is done to prevent an *interrelating mess*: a graph with each node connecting to every other node.

Software engineers are taught to avoid O(n^2) algorithms as much as possible, and this is a similar phenomenon. Sometimes, this problem can be solved by introducing one intermediary node,  after which all different nodes only need to be concerned about its read-write relationship to only that intermediary. (name a vivid example)

## WebAssembly

WebAssembly is an emergent technology / standard which the exact same goal (SOURCE: WASM paper). 
It is a compilation target meant to be platform & source independent. 
It attempts to be the ultimate intermediary between software and hardware, which would be a dream for developers in that sense: "Run Anything Anywhere". 

"Run Anything" means that a platitude of languages (C, C++, Rust) can be compiled to WebAssembly, with the promise that these wasm-binaries are almost as fast as native binary compilations of those same languages. 

"Run Anywhere" means that it is possible to run wasm-binaries on Windows & Mac & Linux Desktops, natively on mobile devices, on servers, and even client-side in web-browsers. 
This runtime is containerized, improving privacy, security against malware, an user control. 

## Applications

These two properties together give WebAssembly many interesting applications. 
Like Docker, it can be used to run foreign software in a save, containerized manner (SOURCE: WASI). 
This is why it is now officially supported by all major browsers, making it the 4th type of code to run in a browser, alongside javascript, css and html. 

Why is that interesting? Well, Google Earth for example is using WebAssembly(SOURCE: ...). 
They could just take the desktop application of Google Earth, compile it to WebAssembly, and then publish it on the web.


## Geomatics

It is unclear what WebAssembly means for the geospatial community. The potential is promising: What if the exact same code could be used client-side and server-side? What if all C++ based libraries such as CGAL could be utilized without needing to be installed?  
<!-- 
(WebAssembly could be just a buzzword, a hype-based virus which hops from conference to conference. )
It could be too impractical in practice. Websites with many wasm files could take too long to load, or compiling certain old C++ programs might not yield any real benefit. 

Many different C++ libraries and applications exist which generate, process and visualize geo-information. 

What happens when commonly used geospatial libraries are compiled to wasm? 

This paper will attempt to answer a part of that question. 
 -->

Both the technical possibilities of `wasm` for geomatics purposes need to be research, as well as the possibilities in utilization. 

This paper will attempt to answer a part of that question. 

## FAIR

The FAIR principles are a collection of four well-established assessment criteria used for judging software applications (SOURCE). They stand for Findable, Accessible, Interoperable, and Reusable. 








<!-- hypothesis 

I Hypothese that WASM will indeed be useful. The question is a matter of degree. It could be just a nifty gimick, or it could be something fantastic.  -->