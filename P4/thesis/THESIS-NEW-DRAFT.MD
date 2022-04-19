# NOTE
_I just want to start writing, not spend any more time debugging latex. For some reason its not giving me a nice table of content. I will copy-paste this later_

# 0. Front
## Abstract 

-------------------------------------------------------------------------------

# 1. INTRODUCTION: 


## The Problem



_name the cityjson web tool_

_name web based demo environments, such as jupyter notebook_

_web demo's like these promote accessibility & science communication._

_name the importance of interactivity, make a case for visual programming_

_make the case for a new web based demo environments, to house applications such as the cityjson web tool_

<br><br>

## Problems with publication

Within the field of geo-informatics, we want to share our end-results. 
- Usually on git, but this has limitations:
    - Not everybody can immediately use it ( unfamiliar language / build system),
    - Even people who can understand, often wont go through the trouble.  
    - "Python bindings" -> half-solves the problem, but still hard to publish to a general audience. 

This was the exact reason for developing https://validator.cityjson.org/. This solved the issue of publication. Why? 
- Extremely findable, usable, accessible
  - Cross-platform
  - No install 
  - first point of contact is precisely where you can use it
  - You can send a link not to a download page, but to the application itself
  - Great for communication: blogs with embedded applications.
  - Code sharing: you exactly know what to expect.

<br><br>

## Web Demo & Scripting environments

we are not the first to recognize the suitability of the web for publishing demo's

We see a lot of interactive web-demo's nowadays, and many of them are embedded within a type of "Demo Hosts":

- Scripting environments in (Science) Communication:
  - Jupyter Notebook 
  - Observable
  - JsFiddle
  - Shadertoy
  - Wapm

- Scripting environments in Education: 
  - TU Delft C++ course
  - Udemy

- Scripting environments in Tutorials: 
  - Rust
  - Lit

  <!-- - (game-jam games)
      - more save (no virus) -->

<!-- We also see 

- As accessible alternative to native
  - Overleaf -> does not use webassembly, but a classic client-server architecture
  - Google Earth -->

All these applications lie on a crossroad between being an interactive demonstration of a certain result or phenomenon, 
and an open invitation for the user to edit and use this result or phenomenon. 
(CITE A STUDY PROVING HOW INTERACTION BENEFITS LEARNING), 
so toying around is important.

<!-- So it is save to say the web is suitable for these types of things. 
But is the web also suitable for more? Can we use a web-based sandbox environment to -->

But this poses a problem. Applications like this: https://validator.cityjson.org/ are rigid in a fashion, 
not at all like the examples named above. 

we want to examine and edit the geodata flow, see for example, where these errors occur, try to get to that data, see if we can make hotfixes, etc. etc. 

(MAKE MORE OF A CASE)

<br><br>

## This thesis 


The goal of this thesis is to improve the functionality and interactivity of geoprocessing & geo-analysis web demos. 

This will be done by providing a web-based Demo Hosts to embed these demo's within. 

...

By means of visual scripting, a user will be able to reconfigure the dataflow interactively, and 'toy' with the tools & data provided. 

We will test how well contemporary web technologies support such an application, as well as judge aspects such as accessibility & performance of said application. We will also judge if this type of application is indeed beneficial and usable as a scripting / demo environment.  


<!-- 
These features could all be implemented by normal means ( buttons, panels, sliders ) -->

CHOICE: do something in-between python bindings, and a full fletched end-user application. 
Ergo: Visual programming



...



# 2. BACKGROUND

## 2.1 The Web Browser & JavaScript
-  main players (chrome, safari, firefox, edge(==chrome))
- The browser js speed armsrace
- How that lead to WebAssembly

## 2.2 The Geospatial Web. 
[Still relevant]

## 2.3 Related works on visual scripting
- FME
- GEOFLOW
- OPENSCAD
- Grasshopper

## 2.4 Related works on Demo Hosts


## 2.5 Client-side geoprocessing 
[Still relevant]
...
BUT: most of these studies were conducted before the increase in javascript performance described in 2.1. It is therefore a valid endeavor to retry the effort of client-side geoprocessing. 

## 2.6 Client-side Web Technologies 
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


<br><br>






# 3. SOFTWARE ARCHITECTURE

## Software Design Principles:

1. Maximize usage of standard HTML5 features.


2. Minimize dependencies. 
  - We want to access core web technologies, not the javascript ecosystem, thats a whole different question. 
  - We are also under the presupposition that the less this project depends on existing project, the more portable this project, or portions of it, will become.

3. Separate geoprocessing tools into plugins: 
  - ideally, if you are not using rasterization tools: do not load rasterization tools. 
  - This means: Divide all needed functionalities up in plugins.
     - Then load these plugins lazily: only when needed.


Q: 1 & 2 are explainable from the introduction story. But why 3?
A: This is meant as a demo-ing application. We want to be able to demo different things, using precisely enough information to 

## Application Design

_Nielsen and Molich's 10 User Interface Design Guidelines
https://theomandel.com/resources/golden-rules-of-user-interface-design/
https://www.interaction-design.org/literature/article/user-interface-design-guidelines-10-rules-of-thumb
(old rules, but still relevant)_

1. Model geofront after a 'normal' desktop application. 
  - Make users forget that they are looking at a website
  - Undo / Redo support
  - Cut / Copy / Paste support

2. Introduce Visual Scripting as the main UI
 - Programming & interface in one

## Justifications 

_No clue where else to put these, or to even include these_

### Why a Visual Programming interface?

To enable the interplay of the following three features: 

1. Alter the process without recompiling
2. Use UI to quickly and easily alter input data.
3. Visualize in-between products in 3D. 

Each of these steps is individually possible with regular programming. Feature 1 can be achieved using hot-reloading. For feature 2, a regular GUI debug menu can be used. For feature 3, we can write and save in-between products, and open them up a 3D viewer of choice. 

What makes a VPL special, is its ability to seamless integrate all three of these aspects, and allow interplay \emph{between} these aspects. 

...
VPL's pop up all the time in all fields of computer science, But they intent to stick within 3d applications. (blender, rhino, unity, unreal)

Why? 3d visual debugging. ( I would say)

...



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
- Containerized: the main advantage of WebAssembly over normal binaries is security. wasm can be reasoned about in a virtual, containerized manner, since it uses virtual memory and a system of incremental privileges. WebAssembly binaries cannot access memory outside of its designated memory pool, making segmentation errors harmless. The incremental privileges also ensure that binaries cannot access anything the user did not explicitly allow for, like a file system.

Taken together, this makes WebAssembly a more secure alternative to regular binaries. This is also why browsers added support for WebAssembly, but not for regular binaries: Adding support for regular binaries would be a substantial risk to the security of all internet users.

<!-- ### Why Architecture use-case

- Perfect target audience of an 'edge case user group'. 
  - Users are not considered 'geodata experts', but who could benefit from tools like GDAL / CGAL, if presented in the right manner.
- Author experience with the target audience. 
- Geomatics \emph{for the Build environment}.  -->


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
_explain the file / edit / view / side menu setup_  (Because of Design rule 1. Model after normal application )

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

## Final 
_Answer research questions ????_


<br><br>


# 6. DISCUSSION
_Answer research questions !!!!_


## Accessibility
_"Is this environment truly accessible?"_


## Practical 
_"Is this environment truly a competitor to native / other methods of geoprocessing?"_

## As Demo / Scripting Environment 
_"Is this environment a good demo host?"_


<br><br>

# 7. CONCLUSION
_"In this article we described the design and functionality of Geofront, A web-based ..."_


<br><br>

# 8. FUTURE WORK 

_This thesis has only scratched the surface of all that _

- Geofront as web-based version of grasshopper
- Geofront as lightweight QGIS replacement 

<br><br>

-------------------------------------------------------------------------------

# scribbles 
Web is seen as a compile target, not as an integral part of the workflow. 
 - "_if you judge a fish by its ability to climb a tree..._"
 - if you frame the web as a compilation end-target, then you start seeing the web as a very poor runtime environment. But the web has many interesting tools unavailable to 'normal' desktop apps. It comes pre-loaded with all sorts of tools, like the canvas api. These tools are usually fast, since they are implemented in C++, and using these tools do not increase the size of your project.
- imgui -> html 


