geo-vpl | geo-web-vpl

# problem


### Reason 1: workflow 
- geometry processing is a notoriously hard endeavour. You need an expert.
- experts often solve geo-processing problems by creating cli tools.
- this is fast, and makes sense from a programmer's perspective, but has a few drawbacks:
  - One to one relationship of problem & solution.
  - Difficult to parameterize. (settings.json / settings.yaml)
  - not trivial to make cli tools cooperate with other environments.
  - difficult to debug, visualize.
  - **hard to share methodologies among colleagues,**.
  - **hard to publish to end-users**.

### Reason 2: on-demand geodata processing



### Reason 3: 


# research question
- 

## sub questions

- How to design VPL? 
- How to use wasm to compile an existing library
- How to design a plugin ecosystem
- ????

# What



# how 
I want to give both geomatics experts & non-expert users alike a web-vpl for geodata processing.   
I want to explore three potential improvements over VPL's like FME / Grasshopper / houdini. 


# Q/A 

## why vpl?
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






-----------
taken from elsewhere

-----------

### Knowledge gap 
GIS Processing should be more operational & less obscure without losing any potency.



