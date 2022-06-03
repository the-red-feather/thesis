# TITLE
GEOFRONT: A web based point cloud processing environment for the era of cloud-native geo-computation.

# INTRODUCTION
<!-- pov: VPL + Cloud native -> VPL's not cloud ready -->

<!--. -->

<!-- Establish the Cloud Native movement -->
<!-- To explain where the contribution of this internship takes
place, we must first paint a general picture of...  -->

<!-- the NEED for -->
<!-- Containerization is one of these features, and is vital for successful cloud computation. 
- Required when distributing some processing functionality on hundreds of edge computing devices: then the setup MUST be the same
- Cross-platform
- Docker often used
- WebAssembly not so much, much newer technology
- Webassembly could fix the 'speed of light' issue hybridize the processing methods. 
 -->

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
<!-- 
<br>

<br>

again: what are the issues????
1. NOT INTEGRATED

- one to one relationship between application and cloud platform
- not well-connected to existing, 'normal' software infrastructures. 
  - reflected in the difficulty of plugins, interoperability issues, etc. 
- closed nature (not open source)

2. NOT CONTAINERIZED

to make VPLs work for cloud native geospatial, they need to be more integrated with regular programming languages, and more **containerized** in order to make processes run on the cloud. -->

## 1.2 THIS STUDY

Due to the need for a VPL aligned with the cloud-native geospatial movement, the goal of this thesis is to develop a new VPL featuring containerized, context-agnostic geo-computation. 



MAIN ATTEMPT: use browser-based web features (WebAssembly, CDN's, javascript features, html5 features)


<!-- It will do this by developing a web-based vpl  -->

-> prio 1: INTEGRATED with regular programming. Why? How? 
   - make everything compilable to javascript. 
   - accept normal javascript libraries as plugins
   - accept wasm libraries as plugins
-> prio 2: CONTAINERIZED, no env. setup, all batteries included. why? how? 
   - run in web browser
   - webassembly

by attempting to develop a new method fixing both integration and containerization


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

<!-- Can WebAssembly enable containerized, hybridized geoprocessing? -->

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


# 2.3 Browser-based geo-computation
- This is what we are essentially also researching
- research topic in of itself. 
- (Source) sees this as a promising, cost-saving alternative to expensive cloud-computation alternatives 
- good Monetization setup: free to use, pay to make your code run quicker on our cloud services. (similar to notorious web games)

# METHODOLOGY 

# IMPLEMENTATION 

# EXPERIMENTS 

# DISCUSSION

# CONCLUSION

# POST-CONCLUSION