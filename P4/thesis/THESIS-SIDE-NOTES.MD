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

