INTRO: POV: CLOUD NATIVE

\m{->} establish web GIS context

\m{->} establish cloud native movement https://www.ogc.org/blog/4607 'radically simplify' -> love the word!

\m{->} mention FAIR

\m{->} establish the browser-based front-end client as the preferred interface for this movement, for the web GIS reasons
... This will require very different web GIS clients than we have seen up to this point. 
    -> not only visualize, but show and configure the geo process, allowing queries, etc. etc. 

\m{->} establish a need for geo-computation capabilities as a counterpart to cloud computation 


... The Cloud native movement has a question at its heart: "What would geospatial standards look like if they were built for the cloud?"
... We pose a similar question to start the investigation of this thesis: "What would geo-computation look like if it were build for a web client?"


- cloud native geospatial 

Due to ..., the goal of this thesis is to develop an application for geo-computation in a browser-based front-end.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

I LIKE THIS: THIS IS MOST IN-LINE with the truth

INTRO: pov: VPL + Cloud native

<!-- \m{->} Establish the VPL  -->
Visual Programming environments (VPL) are a popular method of performing spatial analysis and geodata transformations.
SaveSoft's FME (SOURCE) is a popular tool for automating data integration, while mcneels's Grasshopper (SOURCE) is often used spatial analysis of buildings and cities, like solar irradiation.  
VPL's like these offers users a chance to interactively automate their workflows, while requiring little to no programming knowledge. 
In between results can be inspected quickly, and workflows can be changed on the fly, with immediate feedback.
This advantage of interactive, low-code automation is why the VPL continues to be a popular interface. 
And not only for the field of GIS, but any use-case in need of both low-code automation and visual debugging (Shader Programming, Procedural Geometry, CAD, BIM)

<!-- \m{->} Establish the Cloud Native movement. -->
A recent development within the Open Geospatial Consortium brings challenges and opportunities to these vpl environments. 
The OGC envisions a \textbf{"Cloud Native Geospatial"} future, which aims to radically simplify geodata storehouses to static servers serving large, singular binary geodata files. All processing and analysis of this geodata can then be performed by separate cloud-based web services.

From the perspective of VPL's, the Cloud-Native Geospatial movement represents a strong new use-case for interactive, low-code automation. 
A service provider desires to create a platform, which allows as many (different) users as possible to create geospatial analysis and transformation workflows.
This will mean supporting users of different backgrounds, both programmers and non-programmers, both GIS experts as well as non-GIS experts. 
VPL's like FME and Grasshopper serve this role well. 

However, a cloud-native setup demands many architectural changes, and these popular VPL's fall short on a number of those aspects. 
We identify two major catagories in which these environments are misaligned with the cloud-native vision: 

- Not Accessible: 
  - Not always cross-platform (Grasshopper has only recently added mac support, and has no linux support)
  - Closed source nature. 
    - Some components are open source, but the core software of VPL's is often proprietary.
    - Difficult to expand upon by the community.
    - Cloud Computing does exist, but only hostable by specific parties (Shapediver, FME's cloud computing environment)
  - often expensive, not feasible for small-scale or 'one of' usage.

- Not Interoperable
  - Not portable
    - Close ties to host environments
    - Not containerized
    - Not save
  - difficult to integrate 'third party scripts'. "don't play well with others".
    - Plugins have to deal with the data structures of the host application

THIS STUDY

due to ... , this study will ... 


QUESTIONS

- how to design and create a geo-computation VPL in line with the cloud-native geospatial vision?

SUB QUESTIONS 

- Does making a vpl web-based improve its accessibility?
- Does WebAssembly improve the portability of the VPL's flowcharts?
- ...
- ...




2. RELATED WORK 

- Comparable visual programming languages

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

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


\chapter{Introduction}
Web \ac{gis} forms an indispensable component of the wider geospatial software landscape. 
For the average person, an interactive \ac{gis} web application is often their first and only exposure to a \acs{gis}, be it a web mapping service, a navigation system, or a pandemic outbreak dashboard. 
A web application is cross-platform by nature, and offers ease of accessibility, since no installment or app-store interaction is required to run or update the app: 
As soon as it can be found, it can be used.
The ability to share a full application with a link, or to embed it within the larger context of a webpage is also not trivial. 
Together, these aspects have made the browser a popular host for many important geographical applications, especially when accessibility is vital.

The field of web GIS is, just like the wider context of the web, subject to many changes \& developments. 
These come in the shape of a new feature reaching a consensus in the major browser vendors, or a change in commonly used standards like the \ac{http}.
These changes may lead to a 'trend': a new way of reasoning about or organizing a web service or a web application. 
% trends lead to interesting new applications which may serve new use-cases
These trends are often closely tied to certain features which made them possible. Examples of these are: 
% interplay between features and trends 
\begin{itemize}
  \item Recent improvements in the javascript runtime are a vital component of the current shift from backend-heavy to frontend-heavy web applications. 
  \item front-end Libraries like Celsium, Leaflet and D3 would be hard if not impossible to realize without HTML5 features like WebGL and the Canvas API.
  \item The cloud native geospatial movement requires the http range request feature to truly be effective.
\end{itemize}

The influence and importance of the above web features and trends are why new developments within web GIS are very important to examine.



Geofront has been created to study how recent web features and trends can have a positive effect on the accessibility of geo-computation. 
The hypothesis is that the combination of cloud-native geodata together with front-end heavy applications with industry standard geoprocessing libraries using webassembly, may lead to new, powerful types of GIS applications and use-cases. 

an experiment to capitalize on these developments within the field of web GIS. 


...
In the field of Web GIS, a pattern can be recognised between web \& browser features,  
- javascript runtime improvements -> shift from backend-heavy to frontend-heavy web applications
- HTML5 with WebGL and Canvas Api -> Celsium, Leaflet, D3
- http range request -> cloud native geospatial movement 
- WebAssembly -> ...

Now we see a new technology 

This study has been conducted for two reasons.
Firstly, this study wishes explore the possibilities \& limitations of front-end geoprocessing.
  - Web technologies have become a vital, core component of the modern geospatial software landscape.
  - However, the web is changing : cloud-native geospatial movement, move to front-end heavy applications, WebAssembly. 
  - By creating an application using these trends and technologies, we can get a better understanding.

Secondly, to experiment with making small-scale geoprocessing more accessible
accessible alternative to existing visual geo-programming environments.
