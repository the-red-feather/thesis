# Some Introduction

Web applications have many benefits over native applications
  - cross-platform
  - easy to distribute
  - findable, accessible
  - ...

For these reasons the web has become a popular target for many applications, including geoweb applications. 
- Tools like Leaflet and Celcium are widely used.

A clear trend within these geo-web applications, is a push for increasingly complex applications. 
  - Such as the ninja cityjson web viewer
    - Proofs that the web can not only be used as viewer or end-user application, 
      but also for geodata analysis and editing.
    - Both for end-user tools, and tools used by developers.
  - Also, Modern web tools such as webassembly allow us to run native geo-analysis applications directly in a web browser
    - Leading to tools such as cj-val, a 3D city validator.

This thesis seeks to push this trend further, 
and explores to what end the capabilities of the contemorary web can facilitate the needs of geo-informatics in general, 
and geodata processing in particular. 

We introduce GeoFront, a web based, open source, geodata processing and visualization tool. 
It enables users to configure geodata pipelines using visual programming. 
Users are able to make use of native geoprocessing tools such as CGAL, visualize and debug both end results and in-between results.

Safesoft's FME, but web based & open source 


AT THE END, WE INTEND TO SAY SOME SORT OF THING ABOUT THE READYNESS OF THE COMTEMPORARY WEB FOR GEO-PROCESSING



By creating geofront, this thesis was able to discover .............

- The web is able to facilitate a visual programming language.

- disadvantage: caching. 
  - BUT, even when using emscripten, you are still caching all sorts of things

- The web is able to be used for geoprocessing, albeit with some caveats
  - TypedArrays,
  - Geometric predicates 
  - Rounding
  - ETC.

- Many of these things can be fixed with webassembly, but webassembly itself has other shortcomings
  - Differences between Rust & C++

- reasonable performance 
  (- great considering the platform)

- would not be possible without these modern web features
  - Web Assembly 
  - Typed Array's 
  - Web Workers
  - Web Components,
  - 2D Canvas API
  - Web GL

- ability to share is a true enhancement



# I must figure out how to frame this thesis more compactly. I must focus on a smaller aspect of geofront than the totality of it.



# Q: What are all the ways I can frame geofront? 

# A: 1. Geofront as a geoprocessing / analysis demo tool.
- Frame Geofront as an expanded version of https://validator.cityjson.org/ this. 
  - [this](https://validator.cityjson.org/) (a wasm web demo) + jsfiddle 

# A: 2. Geofront as an integrator
- Use rust, web, and c++ tools side by side, hand in hand

# A: 3. Geofront as a lightweight QGIS replacement
- The web is already used for geodata retrieval and visualization. If geodata processing & analysis is also possible, 
there is nothing preventing geofront for becoming a full GIS.

# A: 4. Geofront as a client-side, web based grasshopper replacement
Advantages over grasshopper: 
- No install 
- Could compile to client-side application.  



# Q: What are geofront's Standout features / what is the result of this thesis 

# A: A web based visual programming language for geoprocessing. 
That in itself does not exist yet, and should be reason enough in and of itself

# A: 

# A: 1. This workflow: 
  Locally: 
  1. Write cli geoprocessing / analysis application using a system-level language (rust, C++).
  2. Compile to `.wasm` + `d.ts` + `.js`.
  3. publish to npm (very easy to do with wasm-pack, can also be done with emscripten)
  In Geofront: 
  4. Reference the unpgk adress of this node package. 
     - Congrats, this is now a geofront plugin!
     - The CLI tool is loaded, with inputs for input parameters, and outputs for all files / data it usually writes.
  5. Build a demo script around the cli tool.
     - Publish this demo using a link with a url parameter containing the flowchart savefile

