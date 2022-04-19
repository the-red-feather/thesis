# NOTE
_I just want to start writing, not spend any more time debugging latex. For some reason its not giving me a nice table of content. I will copy-paste this later_

# (0. Front)
## 

-------------------------------------------------------------------------------

#  1. INTRODUCTION 
<!-- _[JF]: I THINK I SHOULD EXCLUDE THE WHOLE IDEA OF CLIENT SIDE GEOPROCESSING._ -->
<!-- _[JF]: BE MORE HONEST. MENTION THE VISUAL PROGRAMMING LANGUAGE._ -->
<!-- ALSO: I could do a rewrite from a visual scripting perspective -->

<!-- The web could do so much more. I will proof this by making a visual programming language using almost exclusively the tools given by the browser -->

<!-- Under normal circumstances, Web applications within the field of geo-informatics are mostly used for the first and final stages of a common geodata process.  
(
If one wishes to retrieve geodata, web portals are used to discover the required datasets. After this, the OGC Web Services are often utilized to download and truly access this geodata. 

This geodata is then processed locally, using QGIS, ArcGIS, command line tools, or any other 

and at the end Tools like Leaflet and Celcium have been created to visualize the earth in both 2D and 3D , and tools like d3.js can produce interactive graphs to supplement these web pages. 

There is, however, more to the web than just visualization. Due to 
)
This thesis asks the question if the web could do more than just visualization. 

By creating the use-case application GeoFront, we ask the question if a modern web browser, and the current state of the client-side web technologies are capable of facilitating  


 -->

<!-- Geofront: Features: 
- Build by utilizing only basic web features ( excluding webpack & typescript )
- Visual Scripting on the web 
  - "A geodata processing sequence is often conceptualized as a pipeline. Then lets make it an actual pipeline. "
- 

 -->

<!-- 
Take example from 'game jam':
- web games vs local games
- prototyping stage


Take example from overleaf
 -->

## Motivation
Under normal circumstances, Web applications within the field of geo-informatics are mostly used for the first and final stages of a common geodata process: Retrieval and visualization. 
The processing stages in-between are almost always performed on the desktop using environments like QGIS or ArcGIS, or by writing and using CLI tools. 

## This Study

This thesis explores if these in-between processing steps could also be performed within a web application.  
This way, geodata processing applications could profit from the ease of accessibility and maintainability granted by the web as a platform.  

<!-- More Why's: 
- making the geoweb more feature-rich
- allowing quick demonstration (wapm)
- allowing easy access (overleaf)


 -->

(similar to how overleaf is more accessible than desktop latex installation & usage)

We ask ourselves if the current state of client-side web technologies are capable of facilitating multiple steps of geodata conversion, and what such an application would look like. 

To concretize this question, this study covers the design and creation a use-case application titled "Geofront". 

By designing and creating this environment, the study seeks to gain valuable insights in the current state of client-side core web technologies / javascript std, and how well this facilitates various geoprocessing operations.

<!-- Geofronts main interface will be a visual scripting environment.  -->

<!-- [geodata processing] LEADS TO [automation] LEADS TO [scripting]. 
[scripting] + [accessible] = visual programming  -->

<!-- (Go to visual scripting)

(the old stuff)

Interactive, browser-based giss form an indispensable component of the modern geospatial software landscape. 
Despite the popularity of geographical web applications, the range of actual gis! abilities these applications are capable of is very limited. 
This limited range of capabilities inhibits the number of users and use cases geographical web applications can serve, and with it the usefulness of web gis as a whole.
But, Why is geoprocessing within a web application as of today still nowhere to be found? -->


<!-- ## Obstacles + Problem Statement
csg is technically challenging.
csg is immature.
csg can be considered unnecessary.

## This Study

<!-- [JF]: Screw: "adjusting its methodoology to tackle key components", be more direct: -->
<!-- This study prioritizes a concrete approach. As such,  -->

<!-- Therefore, This study will make a new, wholistic attempt at actualizing client-side geoprocessing. 
It will differ from previous attempts by adjusting its methodology to tackle key components of all three obstacles, in order to enable the widespread adoption of csg. -->


## Use Case
[Explain more about geofront]

## Research Questions
[Formal structure]
-
-
-

## Scope
leave it, its perfect.

add: Web TECHNOLOGIES: not WEB ECOSYSTEM.

<br><br>







# 2. BACKGROUND

## The Web Browser & JavaScript
-  main players (chrome, safari, firefox, edge(==chrome))
- The browser js speed armsrace
- How that lead to WebAssembly

## The Geospatial Web. 
[Still relevant]

## Client-side geoprocessing 
[Still relevant]
...
BUT: most of these studies were conducted before the increase in javascript performance described in 2.1. It is therefore a valid endeavor to retry the effort of client-side geoprocessing. 

## Client-side Web Technologies 
What do we mean with this term: 
- HTML5 
- WebGL
- The Canvas API
- WebWorkers 
- WebAssembly 
- WebComponents

### HTML5
- leaflet

### WebGL
- three.js
- Celsium

### WebAssembly 
[Might not be relevant]
WebAssembly is since 2020 part of core web technologies

...

2 biggest reasons against client-side geoprocessing: 
- not performant enough
- no equivalent to industry-standard libraries (CGAL / GDAL). 

WebAssembly COULD solve both, so this study includes WebAssembly as 

## Related works on visual scripting
- FME
- GEOFLOW
- OPENSCAD
- Grasshopper

<br><br>






# 3. SOFTWARE ARCHITECTURE

## Design Principles of Geofront:

1. Model geofront after a 'normal' desktop application. 
  - Make users forget that they are looking at a website
  - Undo / Redo support
  - Cut / Copy / Paste support

2. Minimize dependencies. 
  - we want to access web technologies, not the web ecosystem, thats a whole different question

3. Separate geoprocessing tools into plugins: 
  - If you are not using rasterization tools: do not load rasterization tools. 
  - This means: Divide all needed functionalities up in plugins.
     - Then load these plugins lazily: only when needed.


Q: 1 & 2 are explainable from the introduction story. But why 3?
A: 



## Justifications 

### Why a Visual Programming interface?

To enable the interplay of the following three features: 

1. Alter the process without recompiling
2. Use UI to quickly and easily alter input data.
3. Visualize in-between products in 3D. 

Each of these steps is individually possible with regular programming. Feature 1 can be achieved using hot-reloading. For feature 2, a regular GUI debug menu can be used. For feature 3, we can write and save in-between products, and open them up a 3D viewer of choice. 

What makes a VPL special, is its ability to seamless integrate all three of these aspects, and allow interplay \emph{between} these aspects.




### Why web-based?

- accessible
    - immediately usable -> no installation
    - cross platform
    - easy to integrate with end-user applications (often web applications).
    - easy maintainability (just update website, no need to distribute installers)

- one-of-software argument

- makes conceptual sense for end-users with certain applications: 
  - "You download something from the internet by using an internet browser".

The "one of" software argument: QGIS is excellent for users who use it daily or at least weekly. 

(use the QGIS user data you found)

BUT, users who want to access and process geodata \emph{once in a while}, you ideally want something more temporary. Web Applications make more sense in this regard: No updates, no background processes, no 'presence' on the machine itself. Just go to the website, do what you need to do, and close the browser again. Similar to webshops.

This is in addition to the obvious advantages, like no need to install, easy maintainability, and cross-platform distribution by default.

Finally, using the web ensures that the code will run on all devices: native, mobile, desktop, IOT devices



### Why WebAssembly?

To allow for the previous two (VPL + WEB) without a compromise to speed

On its own: WebAssembly is useful for being containerized binary code. 
- Binary: WebAssembly is close to machine code, making it very performant.
- Containerized: the main advantage of WebAssembly over normal binaries is security. wasm can be reasoned about in a virtual, containerized manner, since it uses virtual memory and a system of incremental privileges. WebAssembly binaries cannot access memory outside of its designated memory pool, making segmentation errors harmless. The incremental privileges also ensure that binaries cannot access anything the user did not explicitly allow for. 

Taken together, this makes WebAssembly a more secure alternative to regular binaries. This is also why browsers added support for WebAssembly, but not for regular binaries: Adding support for regular binaries would be a substantial risk to the security of all internet users.



### Why Architecture use-case

- Perfect target audience of an 'edge case user group'. 
  - Users are not considered 'geodata experts', but who could benefit from tools like GDAL / CGAL, if presented in the right manner.
- Author experience with the target audience. 
- Geomatics \emph{for the Build environment}. 


### Geodata is big data. Will this web application be scalable to handle big datasets?

One of the problems to address when considering the ergonomics of geodata processing, is the fact that geodata is almost always big data. A web application cannot be expected to process huge datasets. So how does geofront address this fundamental aspect of geoprocessing? 

First, lets give the devil it's due. 
- Even when processing "smaller" datasets of, lets say 4 GB, most of the 'flowchart niceties' of geofront will cease to be useful. Inspecting this data will take more time than its worth, and reconfiguring the flowchart will take a long time. This can be mitigated by using web workers, but it will still not be very ergonomic to work with. 
- This is why performance is everything within geomatics.

BUT: 

- Even when we want to write a tool to deal with large datasets, we often test and develop this tool in a smaller context, with a smaller dataset first. The same thing is possible with geofront: 

- Geofront is mostly meant as a sandboxing tool for experimentation: An environment try out different procedures, parameters, and different datasets. 

- The flowcharts created with geofront are compilable to javascript. this allows any processing operation created with geofront to be executed from the command line using node.js. This is a way of how geofront can integrate with large-scale geodata pipelines. 

The point is that even if we use server-side / supercomputer / big-data geoprocessing, we still want to be able to be able to ergonomically and correctly configure these geoprocesses. Geofront could still assist with that.

BUT MOREOVER:

The possibility of client-side geoprocessing also allows for an entirely new geoprocessing workflow, which could replace some use-cases that now require big-data processing and storage. Instead of storing big datasets of pre-processed results, by using client-based, on demand geoprocessing, an application could take a general big-data base layer, and process it on-demand, with a scope and settings determined by the end-users. 

This type of \emph{Process Streaming} is certainly not a drop-in replacement for all big-data use cases. But, in cases which can guarantee a 'local correctness', this should be possible. Examples of this are a delaunay triangulation, TIN interpolation or image filter-based operations. This could be a more cost-effective outcome, as server farms \& Terabytes of storage are time consuming, expensive phenomenon.




### Why not some other environment / Other Client-side geoprocessing innitiatives

None suffices (But i also haven't searched a whole lot)

### Why not build everything as a local application, and publish the entire thing as wasm?

That would be:
- more performant (probably)
- Better native experience
- Better compilation to standard executable

BUT:
- The current setup allows for javascript interoperability. 
  - This is useful for the purposes of UI, GUI, Web requests \& Responses, jsons, WebGL.
  - These are all aspects that would have needed to be part of the C++ application, that we now get 'for free', since the implementation of these features are present within the browsers of clients. 
- javascript can now also serve as its scripting language, making custom, scriptable components a possibility.

% - That would be very hard to script with.




## Assessment
_How is this study assessed?_

<br><br>





# 4. SOFTWARE IMPLEMENTATION
<!-- Show how one might rewrite this -->


## Geofront
_The Geofront codebase ...._

### Framework
_explain how to create a web framework from scratch_ (Because of 2. Minimize Dependencies)
- Web Components
- Webpack + Typescript

### The Application 
_explain the file / edit / view / side menu setup_  (Because of 1. Model after normal application )

### Visual Scripting
_explain how to create a visual programming language_
- Graph representation
  - Map `Functions` to `Nodes` 
  - Map `Variables` to `Edges / Cables`
- Graph manipulation
  - Canvas 2d API
- Graph calculation
  - Dag
  - Dynamic recalculation 

### Type System 
_explain how data is exchanged, and objects are handled_ (lazy tools)
- Functional programming (exchange structs)

### Viewer 
_explain how the viewer was created from scratch_
_explain what it supports_

### STD

### Plugins
_explain the system to dynamically load plugins at runtime_

- typescript 
- wrapper functions

#### Workflow
_show the insane (rust + wasm + npm) workflow_

## WebAssembly Plugins

_explain how to use webassembly_
- compiling
- getting data within webassembly
- extracting webassembly
- how to deal with objects? 


### Startin 


### CGAL


### STD-wasm
_rust library for certain high-performance operations._

## Non WebAssembly Plugins 




<br><br>







# 5. USAGE

## User Interaction
_(basically, write a tutorial)_

## Case Studies

### Vector
_Vector data retrieval, transformation, visualization_

### Raster 
_Raster data retrieval, transformation, visualization_

### 6. Experiments 
_Performance benchmark between rust-wasm / cpp-wasm / cgal-cpp-wasm / js / cli usage_
<br><br>


## Final 
_Answer research questions ?????????_


# 6. DISCUSSION

## Accessibility
_"Is this environment truly accessible?"_


## Practical 
_"Is this environment truly a competitor to native / other methods of geoprocessing?"_





<br><br>

# 7. CONCLUSION
_"In this article we described the design and functionality of Geofront, A web-based ..."_




<br><br>

-------------------------------------------------------------------------------

# scribbles 
Web is seen as a compile target, not as an integral part of the workflow. 
 - "_if you judge a fish by its ability to climb a tree..._"
 - if you frame the web as a compilation end-target, then you start seeing the web as a very poor runtime environment. But the web has many interesting tools unavailable to 'normal' desktop apps. It comes pre-loaded with all sorts of tools, like the canvas api. These tools are fast, since they are implemented by the browser, and using these tools do not increase the size of your project.
- imgui -> html 
