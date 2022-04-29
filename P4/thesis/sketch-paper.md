# 0. Title: 
Geofront: A Browser-based geoprocessing platform for the era of cloud-native geodata.


# Introduction

```markdown
- Web GIS 

- Cloud native movement

- Thick client movement

- The cloud-native movement will bring both opportunities and challenges to Web GIS. 
  
  - Accessible data like this leads to need for equally accessible means to access, analyze, edit, visualize.
    - This is logical: The more accessible geodata becomes, the more accessible the tools to _use_ geodata will need to become.    
    - This is evident: We already see this happening with certain applications like GeoTiff & ModelLab.
    
  - A re-examination of client-server models 
    -   
```

## Context
Interactive web \ac{giss} form an indispensable component of the modern geospatial software landscape. 
For the average person, a web application is often their first and only exposure to a \acs{gis}, be it a web mapping service, a navigation system, or a pandemic outbreak dashboard. 
A web application is cross-platform by nature, and offers ease of accessibility, since no installment or app-store interaction is required to run or update the app: 
As soon as it can be found, it can be used.
The ability to share a full application with a link, or to embed it within the larger context of a webpage is also not trivial. 
Together, these aspects have made the browser a popular host for many important geographical applications, especially when accessibility is vital.
<!-- THIS ALSO MAKES IT EXTREMELY IMPORTANT TO DEVELOP WEB TOOLS -->
<!-- %  Tools like Leaflet and Celcium are widely used. -->

A significant development within the Open Geospatial Consortium (OGC) is the "Cloud Native" Movement. It envisions a future of statically hosted geospatial data accompanied with cloud-based geoprocessing tools similar to the Google Earth Engine. 
This will be easier and cheaper for data providers, and allows for cloud-hosted geodata to be more easily be consumed by cloud-compute tools. 
 
At the same time, a trend within web applications in general shows an ever growing preference for so called 'fat clients' and 'thin servers', as opposed to 'thin clients' and 'fat servers' \cite{panidi_hybrid_2015}. This means that certain responsibilities, such as navigation, increasingly are being performed by the client rather than the server. As a consequence, applications are more quick to react on a user's input. 


The trend can be attributed to new browser features such as WebAssembly, and performance upgrades of the javascript runtime (V8, JIT compiler, etc.).
<!-- This movement contains aspects of the ungoing trend of 'thin server' 'thick client'. -->

This trend is visible within web GIS 
towards more complex clients and simpler servers .
Whereas before the client was mainly use to visualize end results (leaflet, Celsium), now applications arise allowing users to edit (ninja) and validate (cjval) geodata, directly from within the browser. 
EXTREME EXAMPLES: GEOTIFF.

<!-- 
% A clear trend within these geo-web applications, is a push for increasingly complex applications. 
%   - Such as the ninja cityjson web viewer
%     - Proofs that the web can not only be used as viewer or end-user application, 
%       but also for geodata analysis and editing.
%     - Both for end-user tools, and tools used by developers.
%   - Also, Modern web tools such as webassembly allow us to run native geo-analysis applications directly in a web browser
%     - Leading to tools such as cj-val, a 3D city validator.

% TREND : HEAVY CLIENT-SIDE FOR INTERACTIVITY 
% client-side heavy web applications  

% One of the biggest benefits of this setup is \emph{Interactivity}. 
% If logic runs in the client, it can more quickly react to behavior of the user. 
% A full client-server roundtrip containing lots of geodata will in many situations take longer.

Within the field of geo-informatics, the move towards client-side heavy applications also caused academic and commercial interest for the prospect of \emph{client-side geoprocessing}.  -->



------------------------------------------------------------------------------- 

<!-- The case for cloud-based geoprocessing is very easy: very fast, google earth engine  -->
<!-- With a world moving towards the cloud, it becomes ever more important to look at alternatives.  -->
## Problem: 

When viewing these two trends together, a pattern emerges: New opportunities and challenges are approaching the field of Web GIS. 

If OGC standard geodata services like WMS or WFS are slowly replaced by statically hosted, singular geodata files, 
many of the current post-processing functionalities of these web services, like reprojection or reformatting, will all have to be provided elsewhere.
These post-processing & geoprocessing capabilities can either be facilitated by other, new web-services, or they can be added to the responsibilities of (web) clients.

The same dichotomy can be found in advanced web GIS applications allowing the usage of general geoprocessing capabilities. 
Developers of these applications will have to choose for either cloud-based geoprocessing, or client-, browser-based geoprocessing.  

With both the possibility of cloud-native geoprocessing servers, and highly advanced clients,  

While both options are entirely possible, 


While both options are entirely possible, this study seeks to investigate the possibility, implementation and ramifications of the second option.
This option matches the aforementioned trend of 'thin servers & fat clients', 
and the purpose of the Cloud Native movement to relieve data providers from the burden of setting up and maintaining multiple web services. 
It is also cheaper to perform client-side geoprocessing on the machines of end-users, 
instead of maintaining or otherwise paying for additional geoprocessing web services. \STUDY FROM 2019. 
<!-- argue early data consumption promotes interactivity -->
Finally, the prospect of Cloud Native geodata, combined with powerful geoprocessing additions to accessible web clients, 
opens up interesting new functionalities and use-cases for browser-based GIS. \STUDY FROM 2019

The challenges of this second option are that browser-based geoprocessing (BBG) might not be as performant as server side geoprocessing, \STUDY FROM 2015, 2016
and that the browser-based ecosystem lacks powerful geoprocessing tools like CGAL and GDAL. Additionally, how to present the complex endeavour of geoprocessing in the format of an accessible web application is unknown, and which use-cases might benefit from BBG also remains to be researched. 


### Secondly 
Secondly, a move towards cloud-native geospatial data leads to a re-examination of the traditional client \& server model. The cloud-native initiative aims to radically simplify geodata storehouses to just static file servers. All processing and analysis of this geodata can then be performed by separate cloud-based web services.


## The Case

This thesis explores the opportunity of adding these geoprocessing capabilities to the client instead. By not relying on additional web services, operational costs could be lowered for certain applications, making geodata processing more accessible \cite. Additionally, if calculations can be done locally,  

The challenges of this second option are that browser-based geoprocessing (BBG) might not be as performant as server side geoprocessing, STUDY FROM 2015, 2016
and that the browser-based ecosystem lacks powerful geoprocessing tools like CGAL and GDAL.



The wider goal of this study is to discover the possibilities and limitations of browser-based geoprocessing, in order to help developers make the decision between browser-based geoprocessing and cloud-based geoprocessing. 
This is, however, too large of an undertaking for the scope of one thesis. Geoprocessing is a multifaceted phenomenon, containing for example map algebra, crs transformation, vector to raster translations, raster to vector translations, point cloud filtering and interpolation, just to name a few. 

Therefore, this study will develop a use case application to contextualize the research, and to force the research to solve the practical challenges of how \ac{bbg} can actually be used. The type of application chosen is a web-based geoprocessing environment, similar to GEOTIFF, GeoTrellis + ModelLab. These types of applications seek to present geoprocessing capabilities in an accessible manner: 

It also opens up a new range of applications. We see that as soon as geodata is sufficiently findable, accessible, interoperable, and reusable, the accessibility concerns of geodata start to move more towards geodata _processing_ and _processing applications_. \Source{Modellab} Writes: _"Widespread access to frequent, high-resolution Earth observation imagery has created the need for innovative tools like ModelLab that will help individuals and organizations to effectively access, analyze, edit, and visualize remotely sensed data in transformative new ways without years of specialized training or ongoing investments in proprietary software and technology infrastructure."_. After all, FAIR geodata means little if the means to access, analyze, edit, and visualize geodata are not accessible. 

<!-- donald knuth argument: by keeping geodata raw, and porsponing the consumtion of geospatial data to the last possible moment, we can  -->




## Use Case
This study introduces GeoFront, a web based, open source, geodata processing and visualization tool. 




```latex

....



It becomes clear that developers of web GISS will have to make important decisions. 



<!-- find some altruistic good -->

These developments have far reaching consequences for web GIS as a whole. 


% POINT 1   
Firstly, this thesis anticipates that OGC Cloud native geospatial types, together with the trend of complex clients, will lead to a need for  



"Widespread access to frequent, high-resolution Earth observation imagery has created the need for innovative tools like ModelLab that will help individuals and organizations to effectively access, analyze, edit, and visualize remotely sensed data in transformative new ways without years of specialized training or ongoing investments in proprietary software and technology infrastructure. " 
% \cite{ModelLab}.


% Similar trends can be found with GEOTIFF.IO and MODELLAB 
A similar need arose when in the field of rasters, ...
leading to the development of tools like geotiff.io and modellab.

% Investigate what it means to create an accessible geoprocessing environment

The adoption of COPC could mean the same for point cloud data, but it remains unknown what accessible analyze, edit, and visualize means for point cloud processing. 
How to present the complex endeavour of point-cloud processing in the format of an accessible web application is unknown. 


% POINT 2



Academic sources 

\cite{kulawiak_analysis_2019, panidi_hybrid_2015, hamilton_client-side_2014}. 
Interactive geospatial data manipulation and online geospatial data processing techniques where described as "highly valuable trends in evolution of the Web mapping and Web GIS" (\cite{panidi_hybrid_2015}).


Commercial sources 




\section{This Study}

% CONTENT OF STUDY
This study introduces GeoFront, a web based, open source, geodata processing and visualization tool. 
It enables users to configure geodata processing pipelines using visual programming. 
Users are able to make use of native geoprocessing tools such as CGAL, visualize and debug both end results and in-between results.


% GOAL OF STUDY
Finally, this study intends to use the design, creation, and evaluation of geofront to gain insight into the broader topic of client-side geoprocessing. 
Geofront will be used as a proxy / experiment to assess: 
- The fitness of the web in general for client-side geoprocessing
- If client-side geoprocessing in its current state has any meaningful use-cases
- If new features of modern browsers mean anything for the field of geo-informatics at large (webassembly in particular). 




% Explain geofront
% The entire application runs client-side in a browser, and uses a visual programming language as its primary \ac{gui}.
% The main goal and feature of geofront is to take existing low level geoprocessing libraries, and to make these interactively usable on the web. 
% These libraries include a limited set of CGAL operations, complied from C++, and various geoprocessing algorithms such as Startin, written in Rust. 
% Being a visual programming language, GeoFront can be used to interactively alter the geodata pipeline. 
% In between products can quickly be inspected using a 3D viewer.

% PATH TOWARDS RESEARCH QUESTION
\todo{MAAK EEN DUIDELIJK LINK NAAR RESEARCH QUESTIONS \& ASSESSMENT CRITERIA}


% ## This thesis 


% This will be done by providing a web-based Demo Hosts to embed these demo's within. 

% ...

% By means of visual scripting, a user will be able to reconfigure the dataflow interactively, and 'toy' with the tools & data provided. 

% We will test how well contemporary web technologies support such an application, as well as judge aspects such as accessibility & performance of said application. We will also judge if this type of application is indeed beneficial and usable as a scripting / demo environment.  


% <!-- 
% These features could all be implemented by normal means ( buttons, panels, sliders ) -->

% CHOICE: do something in-between python bindings, and a full fletched end-user application. 
% Ergo: Visual programming




% For input, the environment offers \ac{wms} and \ac{wfs} support, as well as ways for users to load locally stored geodata. Parameters can be specified using various ui components, such as sliders. 
% For output, the environment can be used to either save data to the user's local machine, or to visualize the results within the geofront application using a WebGL based viewport.

% Accessibility
% - Shareability
% - Reproducibility

% Interactivity 
% - Visual programming 
% - Visual feedback & insight
% - Sliders

% # Some Introduction

% Web applications have many benefits over native applications
%   - cross-platform
%   - easy to distribute
%   - findable, accessible
%   - ...

% For these reasons the web has become a popular target for many applications, including geoweb applications. 
% - Tools like Leaflet and Celcium are widely used.

% A clear trend within these geo-web applications, is a push for increasingly complex applications. 
%   - Such as the ninja cityjson web viewer
%     - Proofs that the web can not only be used as viewer or end-user application, 
%       but also for geodata analysis and editing.
%     - Both for end-user tools, and tools used by developers.
%   - Also, Modern web tools such as webassembly allow us to run native geo-analysis applications directly in a web browser
%     - Leading to tools such as cj-val, a 3D city validator.

% This thesis seeks to push this trend further, 
% and explores to what end the capabilities of the contemorary web can facilitate the needs of geo-informatics in general, 
% and geodata processing in particular. 

% We introduce GeoFront, a web based, open source, geodata processing and visualization tool. 
% It enables users to configure geodata pipelines using visual programming. 
% Users are able to make use of native geoprocessing tools such as CGAL, visualize and debug both end results and in-between results.

% The input and output of the functions exposed by these libraries 

% the aspect of interactivity is 

% - The web gives us great \emph{Accessibility}, and making it client-side promises us great \emph{Interactivity}

% Browser based \ac{geoprocessing}, hereby known as \ac{bbg}, ... 


% 'interactive geo-processing'
% - Insight 
% - Reproducibility

% GOAL: - explore new use-cases of the web for interactive geo-processing.
    %   - explore the 'fitness' of the web for many different geoprocessing use cases. 

% 1. Build a general purpose web geoprocessing environment 

% 2. Study to which end different needs can be fulfilled / different use-case requirements can be met 

% Safesoft's FME, but web based & open source 




This study intends to discover if contemporary web technologies can facilitate a full-scale client-side geoprocessing tool, by seeking an answer to the following question: 




In recent years, a trend towards increasingly complex and demanding web applications is noticeable. 
-> not only end-users, editing, other examples of geoprocessing clients, etc...
browser-based geoprocessinG: GeoTIFF, GeoTrellis, ModelLab.

These web app increasingly rely on 'fat clients' and 'thin servers', instead of the traditional: 'fat server', 'thin client' paradigm. 
This trend can be attributed performance upgrades of the javascript runtime, and to new browser features such as WebAssembly. 




```




----------------------------------------






% Similar trends can be found with GEOTIFF.IO and MODELLAB 
% Investigate what it means to create an accessible geoprocessing environment




##
## This study
The goal of this study is to discover the possibilities and limitations of browser-based geoprocessing, in order to help developers make the decision between browser-based geoprocessing and cloud-based geoprocessing. 


This study investigates browser-based transformation of geodata, 
as well as how browser-based GISS might profit from from the new opportunities. 


## Use Case
The goal of "discovering the possibilities and limitations of browser-based geoprocessing" is too large of an undertaking for the scope of one thesis. Geoprocessing is a complex and multifaceted phenomenon, containing for example map algebra, crs transformation, vector to raster translations, raster to vector translations, point cloud filtering and interpolation, and much more. 

Therefore, this study will develop a use case application to assist this research. This application serves to contextualize the research, and to force the research to solve the practical challenges of how \ac{bbg} can actually be used. The type of application chosen is a web-based geoprocessing environment, similar to GEOTIFF, GeoTrellis + ModelLab. These types of applications seek to present geoprocessing capabilities in an accessible manner: "Widespread access to frequent, high-resolution Earth observation imagery has created the need for innovative tools like ModelLab that will help individuals and organizations to effectively access, analyze, edit, and visualize remotely sensed data in transformative new ways without years of specialized training or ongoing investments in proprietary software and technology infrastructure. " \Source{ModelLab}.

This study introduces GeoFront, a web based, open source, geodata processing and visualization tool. 
It enables users to configure geodata processing pipelines using visual programming. 
Users are able to make use of native geoprocessing tools such as CGAL, visualize and debug both end results and in-between results within a browser.
Instead of using cloud-based geoprocessing services, all calculations will be performed within the browser itself, in order to examine browser based geoprocessing.

Where ModelLab is build on top of recent improvements to the accessability of satellite imagery, GeoFront is build in anticipation to a similar development for point cloud datasets with the introduction of COPC. The focus of Geofront is therefore on point cloud processing, and point-cloud based modelling, such as Digital Terrain Models (DTM). 


## Research Question:
This study seeks to investigate browser-based transformation of geodata, 
as well as how browser-based GISS might profit from from the new opportunities.

"What are the advantages and disadvantages of browser-based geoprocessing within GeoFront?"

##  Sub Questions
- How to design and create an accessible browser-based geoprocessing client ready for cloud native geodata? (~Old Phase 2)
- How can browser-based geoprocessing leverage existing geoprocessing libraries? (~Old Phase 3)
- Is browser-based geoprocessing performant enough for this use case? (~Old Phase 1)
- Which use-cases might geofront serve? (Old Phase 4)

## 

# Related work
...

# Methodology:

... This study will conduct this investigation by developing a browser-based geoprocessing environment. 





# Implementation 


# Discussion

# Conclusion



