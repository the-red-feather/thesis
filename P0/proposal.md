# Proposal

|||
|---|---|
| name | Jos Feenstra |
| email | me@josfeenstra.nl |
| date | 2021-05-12 - Wednesday |
| purpose | Current, work-in-process thesis proposal

<br><br>


# Thesis Proposal

<br/>

### Reason
- geometry processing is a notoriously hard endeavour. You need an expert.
- experts often solve geo-processing problems by creating cli tools.
- this is fast, and makes sense from a programmer's perspective, but has a few drawbacks:
  - One to one relationship of problem & solution.
  - Difficult to parameterize. (settings.json / settings.yaml)
  - not trivial to make cli tools cooperate with other environments.
  - difficult to debug, visualize.

Resulting in:
- **hard to share methodologies among colleagues,** 
- **hard to publish to end-users**.

### WHAT TO DO ABOUT IT
- FAIR paradigm, usually applied to geodata, should extend to geodata processing as well.

- "Collect once, use multiple times" SDI paradigm should extend to geodata processing & code: "write once, run anywhere & everywhere".
   - everywhere really means everywhere in this case. Not just cross platform: 
     - native (win / linux / mac)
     - web-client (all browsers, on mobile phones using web-wrapper-apps)
     - web-server (server-side, context-agnostic like docker)

- "geodata should be findable, accessible, usable" SDI paradigm should extend to geodata processing itself. examples:
   -  CGAL-level operations must be trivially easy to use for non-expert users. 
   - TIN from pointcloud on demand.
   - Extruding parcel polygons to pointclouds, for only the exact area you need, with exactly the precision you require for this particular dataset.

- WebAssembly + tools that play nice with WebAssembly are vital for achieving these properties. 

### THIS THESIS

- The part of this problem that I will tackle: 
  - web-client & native interoperability for processing of cityjson's

- Besides that
  - Lay groundwork. 
  - Propose workflow.
  - Improve Geomatics <> WebAssembly support



### RESEARCH QUESTION

- _"To what extend can **WebAssembly** contribute to the **accessibility** of **geodata processing**, without **sacrificing performance**?"_

------

### Notes on thesis proposal:

TODO: 
- Specify the main components of the QUESTION.
- Improve AANLEIDING.

### Specify the main components of the QUESTION.

- WebAssembly -> WebAssembly workflow / WebAssembly-based ecosystems
- Accessibility -> Accessibility & Safety & Interoperability
- Geodata Processing -> CityJson Processing
- Performance -> performance (& decades of stress-tested existing code)


This would lead to the very verbose QUESTION: 

- _"To what extend can **WebAssembly-based ecosystems** contribute to the **Accessibility & Interoperability** of **CityJson Editing & Processing**, without **sacrificing Performance & decades of stress-tested existing code**?"_

<br/><br/><br/>

--------

# Software Proposal 
Geonode. FME on the web. 
Flowcharts are sharable using nothing but a link a la: `https://geon-flow.com/share/((hash))`;


## Motivation 
A very user friendly way of doing `cjio` -level of operations.
- users load a `cityjson` by giving the link
- this city is then visible a la `ninja`, but not directly editable like `ninja`.
- users perform basic operations on this city, like a sub selection.
- users can perform advanced operations, like selecting using a polygon
- users can see what this results in. 
- users can then download the result. 


## SETUP : 3 related repositories

  - **geonode-core**
    - rust crate
    - purpose: core geometry library, with `Vector3`, ` Matrix4`, `Mesh`. and others.
      - native `cityjson` support, like `cjio`.
      - support for `georust` crates (crs translations, gdal functions).


  - **geonode-web**
    - rust crate ( / typescript package ? )
    - purpose: using geon-core in real-time on the web. 
      - meaning: change a parameter, immediately see results.
      - make results available for download

    - **Can directly be used to write (web) applications**
    - Support for rendering, user input, and file IO.
    - basic DOM.api abstractions
    

  - **geonode-flow**
    - web-application
    - visual programming language, exposing the functionalities of **geon-core** & **geon-web**.

    - exports to:
      - a link, giving you this exact flowchart
      - a geon-run application. 

    - *geon-flow itself is written as a geon-web application*



<br/><br/><br/>

