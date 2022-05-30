# TITLE
GEOFRONT: A web based visual programming environment for the era of cloud-native geo-computation

# INTRODUCTION
<!-- pov: VPL + Cloud native -> VPL's not cloud ready -->

<!-- Establish the VPL within geomatics -->
Within the field of geo informatics, Visual Programming environments (VPL)'s are popular interfaces for performing spatial analyses and geodata transformations. 
SaveSoft's FME (SOURCE) is a popular Extract Load Transform (ETL) tool for automating data integration, while mcneels's Grasshopper (SOURCE) is often used spatial analysis of buildings and cities, like solar irradiation. 
VPL's like these offers users a chance to interactively automate workflows & processing pipelines, while requiring little to no programming knowledge. 
In between results can be inspected quickly, and the processes can be changed on the fly, often with immediate feedback.
This advantage of interactive, low-code automation is why the VPL continues to be a popular interface within the field of GIS, as well as all other use-cases in need of both low-code automation and visual debugging (Shader Programming, Procedural Geometry, CAD, BIM). 
A VPL done right can make automation available for a very large audience.

<!--. -->

<!-- Establish the Cloud Native movement -->
<!-- To explain where the contribution of this internship takes
place, we must first paint a general picture of...  -->

An important development within the Open Geospatial Consortium (OGC) brings challenges and opportunities to these geospatial visual programming environments. 
The OGC envisions a "Cloud Native Geospatial" future, in which geodata formats and geoprocessing methods are primarily designed with the cloud in mind. 
This would radically simplify geodata storehouses to static servers, serving large, singular binary geodata files. All processing and analysis of this geodata can then be performed by separate cloud-based web services, which could then run on an unprecedented scale, with unprecedented speed. 

<!-- Why is it different, why does it ask for change? what type of change? -->
In order to make this vision a reality, both geodata formats and geoprocessing and -analysis methods will need to be re-examined. 
Cloud computation and cloud-based data access ask for different priorities and features over native, desktop based alternatives. Examples of these features are partial streaming capabilities (SOURCE), and containerization (SOURCE). 
These features will either have to be added to existing formats and methods, or new substitutes formats and methods will need to be developed and tested.

This brings us back to the opportunity and challenges of the visual programming language. 

The **opportunity** lies in the fact that a VPL interface is highly suitable as a configurator of cloud-computation workflows. The promise of interactive, low-code automation matches the desire of most cloud native geoprocessing providers to support users of different backgrounds, both programmers and non-programmers, both full GIS experts as well as non-experts (Source). A good example of this is ModelLab in Raster Foundry (Source). This is also evident in the fact that existing VPL's like FME and Grasshopper have added proprietary cloud-computation features like FME Cloud (SOURCE) and ShapeDiver (SOURCE), respectively.

<!-- HOWEVERRRRRRRRR -->
However, the **challenge** is that as of right now and despite these features, most proprietary VPL's fall short on a number of priorities and features required for the cloud-native movement. 
These shortcomings include their closed and proprietary nature, their distance from regular programming features and conventions (git version control, continuous integration), and the non-containerized, one to one relationship between the IDE application \& the cloud hosting platform. 

All of this hinders their suitability as cloud-computation configurers. 
<!-- making them obsolete, or dragging us down, etc. etc. -->

<!-- Additionally, it is important to emphasize that 
"Cloud-native geospatial" as a vision is more than just supporting cloud-computation.  -->


<!-- 
# Challenges (Dont know where this belongs, or if it belongs here.): 

This thesis identifies X major catagories in which popular GIS visual programming environments are misaligned with CNGS's vision and technical requirements.
 
<!-- TODO: these are the things I set out to do. Do they align with research?

<br>

## A: Not Open
popular vpl's are not open.  

```
- Closed source nature. 
- Some components are open source, but the core software of VPL's is often proprietary.
- Difficult to expand upon by the community.
- often expensive, not feasible for small-scale or 'one of' usage.
```
only open source community collaboration on the level of plugins. These plugins are highly specified to the specific VPL. 

<br>

## B: Not Flexible / Portable / Interoperable

- Often not cross-platform (Grasshopper has only recently added mac support, and has no linux support)
- Close ties to host environments
- Needs specific runtime environment
- Cloud Computing does exist, but only hostable by specific parties (Shapediver, FME's cloud computing environment)
- Not 'really' containerized
- Not 'really' save

<br>

## C: Not Aligned with regular programming languages

- The environments do not allow for regular software development features, like Git version control, unit tests, or CI / CD
- "don't play well with others": difficult to integrate 'third party scripts'.
- Plugins have to deal with the data structures of the host application
- The environments do not allow for regular programming features, like the encapsulation of repeatable actions into re-usable functions.  -->

<br>

<br>

## 1.2 THIS STUDY

Due to the need for a VPL aligned with the cloud-native geospatial movement, the goal of this thesis is to develop both a new vpl for the purpose of cloud-native geo-computation.

-> prio 1: align with regular programming. Why? How? 
   - make everything compilable to javascript. 
   - accept normal javascript libraries as plugins
-> prio 2: containerized, no env. setup, all batteries included. why? how? 
   - run in web browser
   - webassembly


Will differ from existing studies and applications by:

- vpl is created from scratch
- vpl runs in a web browser
- vpl accepts WebAssembly libraries
- vpl flowchart itself compiles to a javascript subset

Leading to: 

-> Free and open source
-> Just javascript: 
  - The javascript-subset can be used to integrate with existing javascript infrastructure: node.js for cloud-computation, git for version control, and automated testing.  

-> Fully Hybrid: 
  - the same functionality locally and in the cloud, on any platform
-> fully containerized: by using webassembly, no environmental setup is required, while at the same time being able to make use of libraries written in any language.

-> Powerful plugins: easy to make use of 'normal' software ecosystems.


QUESTIONS

- how to design and create a geo-computation VPL in line with the cloud-native geospatial vision & technical requirements?

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