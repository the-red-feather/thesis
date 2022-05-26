# TITLE
geofront: A web based visual programming environment for the era of cloud-native geo-computation

# INTRODUCTION
<!-- pov: VPL + Cloud native -> VPL's not cloud ready -->

<!-- I LIKE THIS: THIS IS MOST IN-LINE with the truth -->

<!-- \m{->} Establish the VPL  -->
Visual Programming environments (VPL) are a popular interface for ETL applications, and for performing spatial analysis and geodata transformations.
SaveSoft's FME (SOURCE) is a popular tool for automating data integration, while mcneels's Grasshopper (SOURCE) is often used spatial analysis of buildings and cities, like solar irradiation. 
VPL's like these offers users a chance to interactively automate workflows, while requiring little to no programming knowledge. 
In between results can be inspected quickly, and workflows can be changed on the fly, often with immediate feedback.
This advantage of interactive, low-code automation is why the VPL continues to be a popular interface within the field of GIS, as well as all other use-cases in need of both low-code automation and visual debugging (Shader Programming, Procedural Geometry, CAD, BIM).

<!-- A VPL done right can make very powerful features available for a very large audience. -->

<!-- \m{->} Establish the Cloud Native movement, and what this means for VPL's -->
An important development within the Open Geospatial Consortium (OGC) brings challenges and opportunities to these vpl environments. 
The OGC envisions a "Cloud Native Geospatial" future, which aims to radically simplify geodata storehouses to static servers serving large, singular binary geodata files. All processing and analysis of this geodata can then be performed by separate cloud-based web services.

The Cloud-Native Geospatial movement represents a strong new use-case for interactive, low-code automation. 
A cloud native processing provider desires to create a platform which allows as many (different) users as possible to create geospatial analysis and transformation workflows.
This will mean supporting users of different backgrounds, both programmers and non-programmers, both GIS experts as well as non-GIS experts. 

<!-- TODO improve this lead-up -->

This is why cloud-native applications choose for either a very high-level scripting language, like javascript for the Google Earth Engine, or a VPL, like ModelLab in Raster Foundry. Additionally, this is why existing VPL's like FME and Grasshopper have added cloud-computation features like FME Cloud (SOURCE) and ShapeDiver (SOURCE), respectively.

<br>

<!-- HOWEVERRRRRRRRR -->
**However**, in order to properly use a VPL for cloud computation, many challenges need to be overcome.
Especially proprietary VPLs fall short on a number of technical aspects, hindering their suitability for the configuration of cloud-computation workflows. 
Additionally, it is important to emphasize that "cloud-native geospatial" as a vision is more than just cloud-computation. 

This thesis identifies X major catagories in which popular GIS visual programming environments are misaligned with CNGS's vision and technical requirements.

<!-- TODO: these are the things I set out to do. Do they align with research? -->

## A: Not Open
popular vpl's are not open.  

```
- Closed source nature. 
- Some components are open source, but the core software of VPL's is often proprietary.
- Difficult to expand upon by the community.
- Cloud Computing does exist, but only hostable by specific parties (Shapediver, FME's cloud computing environment)
- often expensive, not feasible for small-scale or 'one of' usage.
```

only open source community collaboration on the level of plugins. These plugins are highly specified to the specific VPL. 

## B: Not Flexible / Portable / Interoperable

- Often not cross-platform (Grasshopper has only recently added mac support, and has no linux support)
- Close ties to host environments
- Needs specific runtime environment
- Not 'really' containerized
- Not 'really' save
- If designed with cloud in mind, can the script still be used and run offline? 

## C: Not Aligned with regular programming languages

- "don't play well with others": difficult to integrate 'third party scripts'.
- Plugins have to deal with the data structures of the host application
- The environments do not allow for regular programming features, like the encapsulation of repeatable actions into re-usable functions. 

- The environments do not allow for regular software development features, like Git Version Control, unit tests, CI / CD

<br>

<br>

## 1.2 THIS STUDY

due to ... , this study will ... 

Will differ from existing studies and applications by attempting to: 

  -> vpl is created from scratch
  -> vpl runs in a web browser
  -> vpl accepts WebAssembly libraries
  -> vpl compiles to javascript subset

Leading to: 
-> Free and open source
-> Just javascript: 
  -> The javascript-subset can be used to integrate with existing javascript infrastructure: node.js for cloud-computation, git for version control, and automated testing.  

-> Fully Hybrid: the same functionality locally and in the cloud, on any platform
-> fully containerized: by using webassembly, no environmental setup is required, while at the same time being able to make use of libraries written in any language.

-> Powerful plugins: easy to make use of 'normal' software ecosystems.


QUESTIONS

- how to design and create a geo-computation VPL in line with the cloud-native geospatial vision?

SUB QUESTIONS 

- Does making a vpl web-based improve its accessibility?
- Does WebAssembly improve the portability of the VPL's flowcharts?
- ...
- ...




# 2. RELATED WORK 

# 2.1 CLOUD NATIVE 

visions are fuzzy phenomena. 
We will nontheless try to further define the cloud native vision to properly frame this study. We will base ourselves on the writing of Chris Holmes, because ....


- open platforms ("alternative to google earth engine") 
- open standards ("COPC", etc. etc. )
- interchangeable components (we see a push to add all data centrally, but at the same time make sure to not monopolize certain aspects)
- KISS / radical simplification / rule of least powerful 

Summerized: FAIR geodata and Geoprocessing.

lots of existing 

this study will primarly focus on the application side of things



# 2.2 VISUAL PROGRAMMING LANGUAGES WITHIN GEO / GIS

what is out there
how will this study differ

- Geometry Nodes
  - Open Source -> CHECK
  - Plugin System -> CHECK
  - best implementation of an open source vpl.
  - still inhibited by portability issues: 

- GeoFlow
  - Open Source -> CHECK
  - Run Headless -> CHECK
  - Run containerized -> not really
  - Plugin System -> CHECK
  
  - Our appoach will differ, since we start at the web as a containerized environment. 
    We build everything containerized-first.
  - Everything will compile to plain javascript, making use of normal npm libraries.  

- SourceFoundry
  - only raster based 


2 possible containerization method:

- wasm
  + runs in web browser 
  + just small binaries
  + best for containerizing small pieces of logic.

- docker 
  + a fully containerized environment
  + best for for containerizing an entire workflow or setup



VPL environments

... VPL's are often more than only an interface. An application like FME is what in normal environments would be separate applications or features. It is a language, the IDE / editor, a compiler, and the runtime, all at the same time. 

In normal computer programming, these are all distinct. 


METHODOLOGY 

How do we define a cloud-native vpl?

A cloud-native-ready VPL:
- must be very findable and accessible -> web based, free and open source,
- must offer containerization & portability of the script, -> webassembly 
- well connected to text-based programming languages. -> js <-> flowchart interoperability
- must extremely open to additions / plugins,
- must offer 'dry run' capabilities: the vpl must work standalone, for debugging, or just straight up utilization of the algorithm for non-massive datasets.


- we will not only adhere to the current cloud-native-required features
- We will attempt to align this project with the core philosophy of the movement.
  - this core philosophy shines through the text of Chris with words like 'radically simplify', 'its just a laz'. 
    - The idea is something like 'do not build new things, but try to enhance / reuse existing infrastructure as much as possible'
  - Because of this, we aim to fully compile the flowchart to javascript, with all libraries becomming nothing more than normal npm libraries. 
    - 'just javascript & wasm'.
    - This shows that we are doing 'nothing special' in some sense. We are just using the existing infrastructure in a new way. 


# METHODOLOGY 

# IMPLEMENTATION 

# EXPERIMENTS 

# DISCUSSION

# CONCLUSION

# POST-CONCLUSION