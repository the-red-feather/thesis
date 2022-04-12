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
- WebGL
- The Canvas API
- WebWorkers 
- WebAssembly 
- WebComponents

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
