KEY CONCEPTS :

Interactivity
- 'get a feel' for data
- Before / After
- Hands-on experience

Accessibility
- Findable == Accessible
- Reproduce & validate research results 
- Interdisciplinary exchange of ideas 
- Educational Web Demo's

---------------------------

- Educational


------------

- Geofront as **Educational Sandbox**
  - This use-case can be fully realized within the current state of geofront
  - "Geoprocessing for kids"
  - "What is a delaunay triangulation?" 
  - "Let people play / experience / traverse a nef polyhedron"
  - Using something helps with understanding


- Geofront as **Web Demo Application**
  - Reproducibility toolkit:
    - Load your own code from a CDN
    - Build a demo setup around it
    - load a custom graph from a public json file
    - share a url pointing to this json (which contains the CDN address)
  - You can now share a rust / C++ program as a fully usable web demo, and analyze its performance using different datasets.
  - MISSING FEATURE: Load in your own npm package -> IMPLEMENTED
  - MISSING FEATURE: json url -> IMPLEMENTED
  - MISSING FEATURE: dependency list inside of the graph.json save file
  
- Geofront as **End User Geoprocessing Environment**
  - FME, but open source & on the web.
  - The tool in itself can be regarded as an end-user application:
    - Load file, do something with the file, download resulting file
  - CURRENTLY MISSING FEATURE: compile to web app (take the input & output, hide the flowchart)

- Geofront as **Rapid Prototyping Environment** 
  - Ravi's GeoFlow, but on the web
    - Meant to visually debug a certain process, after which this process can be 'compiled' to a normal cli tool.
  - CURRENTLY MISSING FEATURE: compile to native cli tool (node.js script)

- Geofront as **Parametric Modelling Application**
  - OpenSCAD, but using visual programming instead of scripting.
  - Grasshopper, but open source & on the web.
  - CURRENTLY MISSING FEATURE: create new points / lines in the viewer



# other scribbles 
Web is seen as a compile target, not as an integral part of the workflow. 
 - "_if you judge a fish by its ability to climb a tree..._"
 - if you frame the web as a compilation end-target, then you start seeing the web as a very poor runtime environment. But the web has many interesting tools unavailable to 'normal' desktop apps. It comes pre-loaded with all sorts of tools, like the canvas api. These tools are usually fast, since they are implemented in C++, and using these tools do not increase the size of your project.
- imgui -> html 


