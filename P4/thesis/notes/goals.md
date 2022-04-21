KEY CONCEPTS :

Interactivity
- 'get a feel' for data
- Before / After
- Hands-on experience

Accessibility
- Findable == Accessible

Sharability
- Reproduce research results 
- Interdiciplinary exchange of ideas 
- Educational Web Demo's

---------------------------

- Educational
  
  - Using something helps with understanding

- Communication & Exchange of ideas


- Reproducability

  - Testing reproducability is way easier with web applications

------------

- Geofront as **Educational Sandbox**
  - This use-case can be fully realized within the current state of geofront
  - "Geoprocessing for kids"
  - "What is a delaunay triangulation?" 
  - "Let people play / experience / traverse a nef polyhedron"
  
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

- Geofront as **Geoprocessing Prototyping Environment** 
  - Ravi's GeoFlow, but on the web
    - Meant to visually debug a certain process, after which this process can be 'compiled' to a normal cli tool.
  - CURRENTLY MISSING FEATURE: compile to native cli tool (node.js script)

- Geofront as **Parametric Modelling Application**
  - OpenSCAD, but using visual programming instead of scripting.
  - Grasshopper, but open source & on the web.
  - CURRENTLY MISSING FEATURE: create new points / lines in the viewer