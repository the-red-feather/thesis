TREND
- heavy clients \& Cloud-Native

<!-- this trend, what might geoprocessing look like in the future?  -->

Research question

# 0. Title: 
Geofront: A Browser-based geoprocessing platform for the era of cloud-native geodata.

# 1. Intro: 
Interactive, browser-based \ac{giss} form an indispensable component of the modern geospatial software landscape. 
-> Celcium, leaflet
A web application is cross-platform by nature, and offers ease of access and maintainability, since no installment or app-store interaction is required to run or update the app: 
As soon as it can be found, it can be used. 
These aspects have made the browser a popular host for many geographical applications, especially when developing accessible applications targeting end-users. 

In recent years, a trend towards increasingly complex and demanding web applications is noticeable. 
-> not only end-users, editing, other examples of geoprocessing clients, etc...
browser-based geoprocessinG: GeoTIFF, GeoTrellis, ModelLab.

These web app increasingly rely on 'fat clients' and 'thin servers', instead of the traditional: 'fat server', 'thin client' paradigm. 
This trend can be attributed performance upgrades of the javascript runtime, and to new browser features such as WebAssembly. 

At the same time, the Open Geospatial Concortium (OGC) has started to move towards 'Cloud native' geospatial types, 
and envisions a future of staticly hosted geospatial data (CPOC, GEOTIFF), accompanied with cloud-based geoprocessing tools similar to the Google Earth Engine.
This will be easier and cheaper for data providers, and allows for cloud-hosted geodata to be more easely be consumed by cloud-compute tools. 

It also opens up a new range of applications. We see that as soon as geodata is sufficiently findable, accessible, interoperable, and reusable, the accessibility concerns of geodata start to move more towards geodata _processing_ and _processing applications_. \Source{Modellab} Writes: _"Widespread access to frequent, high-resolution Earth observation imagery has created the need for innovative tools like ModelLab that will help individuals and organizations to effectively access, analyze, edit, and visualize remotely sensed data in transformative new ways without years of specialized training or ongoing investments in proprietary software and technology infrastructure."_. After all, FAIR geodata means little if the means to access, analyze, edit, and visualize geodata are not accessible. 


## Problem: 

<!-- The case for cloud-based geoprocessing is very easy: very fast, google earth engine  -->
<!-- With a world moving towards the cloud, it becomes ever more important to look at alternatives.  -->

These developments pose both challenges and opportunities for browser-based GISS 

If OGC standard geodata services like WMS or WFS are transformed into statically hosted, singular geodata files, 
many of the current post-processing functionalities of these web services, like reprojection or reformatting, will have to be provided somewhere else.
These post-processing & geoprocessing capabilities can either be facilitated by other, new web-services, or they can be added to the responsibilities of (web) clients.

The same dichotomy can be found in browser-based GISS that wish to use not only post-processing, but general geoprocessing capabilities. 
Developers of these applications will have to choose for either cloud-based geoprocessing, or client-based geoprocessing.  

While both options are entirely possible, this study seeks to investigate the possibility, implementation and ramifications of the second option.
This option matches the aforementioned trend of 'thin servers & fat clients', 
and the purpose of the Cloud Native movement to relieve data providers from the burden of setting up and maintaining multiple web services.
It is also cheaper to perform client-side geoprocessing on the machines of end-users, 
instead of maintaining or otherwise paying for additional geoprocessing web services. \STUDY FROM 2019
Finally, the prospect of Cloud Native geodata, combined with powerful geoprocessing additions to accessible web clients, 
opens up interesting new functionalities and use-cases for browser-based GIS. \STUDY FROM 2019

The challenges of this second option are that browser-based geoprocessing (BBG) might not be as performant as server side geoprocessing, \STUDY FROM 2015, 2016
and that the browser-based ecosystem lacks powerful geoprocessing tools like CGAL and GDAL. Additionally, how to present the complex endeavour of geoprocessing in the format of an accessible web application is unknown, and which use-cases might benefit from BBG also remains to be researched. 

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



