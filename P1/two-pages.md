geo-vpl | geo-web-vpl

# Problems

## Problem 1 : Client-side geoprocessing is underdeveloped
Geodata processing client-side in a browser is very underdeveloped. This is a huge inhibition for many applications. Client-side geoprocessing offers tremendous potential:
 - Users will never have to install anything except a web-browser.
    - This will make geoprocessing more accessible to a large, non-geodata expert audience. It allows more people to do more interesting things with geodata, and reach more interesting conclusions. 

 - Client-side geoprocessing would offload processing to the end user, allowing the end user to tailor geodata to their exact needs. 

 - Client-side geoprocessing allows direct user feedback unlike server-side geoprocessing. Users can be on top of the calculations, look at in betweens steps, etc. 
- Instead of having large, preprocessed datasets, geodata could be processed on demand from the source. If a user is only interested in a small area of the source dataset, this could save vast amounts of time, storage space and computational resources. 
 
This gives client side geoprocessing both an ecological & economical reason. The accelerated effects of climate change gives geomatics experts a moral reason to avoid huge renderfarms and other power consuming methods whenever possible. Additionally, client-side can also be much cheaper, since all of the processing and rendering will happen on the machines of the user, and not on the servers of the organization. 


## Problem 2 : Geoprocessing overall lacks ergonomics

Geodata processing is very unfriendly to non-experts:
  - It is a notoriously hard endeavour. You pretty much require an expert.
  - Software is often hard to find, sometimes hard to install.
  - Software is often difficult to operate.

To expand upon that last point. experts often solve geo-processing problems by creating cli tools. This is fast, and makes sense from a programmer's perspective, but has a few drawbacks in terms of ergonomics:
  - Strong relationship of Problem & Solution. 
    - Hard to scale or repurpose.
    - Difficult to parameterize. (settings.json / settings.yaml)
  - Native Code: Not trivial to make cli tools cooperate with other environments.
  - difficult to debug
    - Often hard to track how algorithms are behaving, due to the difficulty of visualizing in between steps.
  - **'relatively hard' to share methodologies among colleagues,**.
  - **relatively hard to publish to end-users**.


# Solution 

This research intents to solve both problems by researching and developing a new geodata processing application. The first problem will be solved by making the application run in a web browser, client-side. The second problem will be solved by making this application operable by means of a visual programming language. The aim of this research is to give give both geomatics experts & non-expert users alike a **fast** and **ergonomic** way to process geodata. In order to make this happen, the research will approach these two aspects ....

Fast -> wasm 

ergonomic -> web-vpl


not merely to offer suggestions, but also aims to fully deliver a prototype. 


I want to explore three potential improvements over VPL's like FME / Grasshopper / houdini. 

The research will be focussed in two aspects, one technical aspect, and one ergonomic / design aspect. The application will be successful if the right balance between technical and ergonomical aspects can be found. 


# Research Question

_"How to create a web-geo-vpl?"_

## sub questions

- A : Technical Aspect
  - How to use wasm to compile an existing geoprocessing library, 
    - and to make it ready for web usage
  - How to handle types between multiple, unrelated libraries 
  - How to design a plugin ecosystem
    - Marketplace Website ?
    - Npm ?  

- B : Ergonomic Aspect
  - What lessons can be learned from existing VPL's?
    - _Who_ uses _What_ and _Why_? 
    - How do geomatics users use existing VPLs? 
    - How would geomatics users **want** to use a VPL?
  - How to design a new VPL?
    - What needs to be different for a web vpl?
  - How 


# Q/A 

## why vpl?
- I would argue that VPL's offer a perfect UI for geodata processing. 
- code is only a process. VPL's can have input, process and output within the same environment.

- input: 
  - draw a polyline on a map
  - slider to test a range of values 
  - directly use a WFS / WMS service

- process:
  - **iteration**: visualize in-between steps easely
  - quickly demonstrating the effects of certain parameters
  - quickly demonstrating the result of a tweak in the process

- output:
  - visualize geometry on a map



## what do I use this VPL for? 
- on demand geoprocessing
- see **Applications**
(- parametric modelling similar to other geo-VPL's)


## why do we need a new geo-VPL? 
why not grasshopper / FME / ravi's geo-flow? Three features: 

- 1. Web Based 
  - No need to install anything.
  - Instantly sharable with others.
  - Context-agnostic: desktop / mobile / web-client / server 


- 2. WebAssembly ready
  - Language-agnostic: 
    - plugins can be created using C++, Rust, and anything compilable to WebAssembly.
  - Wasm binaries can directly be loaded as plugins, no / minimal wrapper code needed
  - these libraries can be mixed


- 3. (Java)script interoperability
  - Graph can be saved to javascript.
  - Graph can be loaded from javascript (subset).
  - Graph has a one-to-one relationship to javascript. 
    - One Operation / Node has a one-to-one relationship to a javascript function.
  - Resulting code is just javascript: the VPL itself is not needed to run code. 
  - Best of both worlds.
    - js: Encapsulation, version control, run time, loops, if statements, 
    - geon-nodes: Insight, Overview, UI















# Applications
Geoprocessing remains a rather vague term used throughout these descriptions. I will define concrete geo-processing applications, which I aim to create using the VPL:


### Application 1: On Demand Triangulator + Isocurves: 

Input: 
- Point Cloud

Output
- Mesh

Steps: 
- Load ahn3 point-cloud (WFS Input Widget | WFS Preview Widget)
- Visualize point cloud on top of base map of the netherlands (WMS Input Widget | WMS Preview Widget)
- Only select terrain points (list filter Operation)
- Select Area of interest using a 2d polygon (Boundary Include Operation)
- Triangulate point cloud with a certain resolution (Triangulate Operation)
- Intersect the mesh surface with a series of planes (Isocurves from Mesh Operation)
- Preview data (MultiLine Preview Widget)
- Export data (MultiLine export Widget)


### Application 2: Get geometry of a street based on a street name

Input
- adress string 

Output
- Vector (center)
- Mesh

Steps
- 
- 
- 
- 






=====================================
taken from elsewhere
=====================================

### Knowledge gap 
GIS Processing should be more operational & less obscure without losing any potency.




=====================================
Moved these remarks to down here 
=====================================

Thesis = FAIR geodata processing using the `web`, `a VPL`, and `wasm`.

## Related visual programming languages focussed on geometry:

| Name            | Author                | Availability       | Source    | Audience                     | Purpose              | Link                | Notes          
|---------------- | --------------------- | ------------------ | --------- | ---------------------------- | -------------------- | ------------------- | ----------
| FME             | Save Software         | €2,000 one time    | Closed    | Geoprocessing intermediaries | Geoprocessing        | https://www.safe.com/fme/fme-desktop/ | 
| Houdini         | SideFX                | ~€1,690 p.y.       | Closed    | 3D modellers & SFX           | Procedural Modelling & Special effects | https://www.sidefx.com/ |
| Geometry Nodes  | Blender               | Free               | Open      | 3D modellers & SFX           | Procedural Modelling & Special effects | https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html   |
| Grasshopper     | David Rutten / McNeel | €995 one time      | Closed    | 3D modellers & architects    | Parametric Design    | https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html   |
| geoflow         | Ravi Peter            | Free               | Open      | Geoprocessing experts        | Geoprocessing: Rapid prototyping & Visualizing in between steps | https://github.com/geoflow3d/geoflow  |
| Dynamo          | Autodesk              | +revit €3,330 p.y. | Semi-open | Expert Revit Users           | BIM automation       | https://dynamobim.org/ | 


Drawbacks of all of these: They are not FAIR:  
1. not `findable` & `accessible`: most have a large barrier of entry: the tool needs to be installed \ Requires an account \ Requires several thousands of euros
2. not `re-usable`: plugins must always be specifically created for these environments. no way of directly using a repo, like you can with a regular programming language.
3. not `interoperable`: all vpl's are strongly tied to their host environment / no way to turn a script into a CLI or web-app.



> idea to fix (2): wasm as plugin: just a collection of functions / classes / etc. 
- automatic js library from wasm builder
- updating a list of all available plugins
> idea to fix (2): direct exposure: make all functions found within wasm binaries callable from visual programming canvas. 
> with these two ideas, there is no need to specifically create plugins, any wasm binary can be utilized. 

> idea to fix (3): make the flowchart compilable to javascript, or an IFC-like json format. make the flowchart loadable from javascript or IFC-like json. make the flowchart sharable using a link / hash.





> ravi: rapid prototyping
> fast visualizing of in-between steps
> c++ -> fast & many libraries. 








> 
geon.nl??

>
