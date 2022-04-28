TREND
- heavy clients \& Cloud-Native

<!-- this trend, what might geoprocessing look like in the future?  -->

Research question

# 0. Title: 
Geofront: A first step towards browser-based geoprocessing in an era of cloud-native geodata.

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

## Problem: 

<!-- The case for cloud-based geoprocessing is very easy: very fast, google earth engine  -->

These developments pose both challenges and opportunities for browser-based GISS 

If OGC standard geodata services like WMS or WFS are transformed into statically hosted, singular geodata files, 
many of the current post-processing functionalities of these web services, like reprojection or reformatting, will have to be substituted.
These post-processing & geoprocessing capabilities can either be facilitated by other, new web-services, or they can be added to the responsibilities of (web) clients.

The same dichotomy can be found in browser-based GISS that wish to provide general geoprocessing capabilities to end users. 
Developer of these applications will have to choose for either cloud-based geoprocessing, or client-based geoprocessing.  

While both options are entirely possible, this study seeks to investigate the possibility, implementation and ramifications of the second option.
This option matches the aforementioned trend of 'fat-clients', 
and the purpose of the Cloud Native movement to relieve data providers from the burden of setting up and maintaining numerous web services.
It will also be cheaper to perform client-side geoprocessing on the machines of end-users, 
instead of maintaining or otherwise paying for additional geoprocessing web services. \STUDY FROM 2019
Finally, the prospect of Cloud Native geodata, combined with powerful geoprocessing additions to accessible web clients, 
opens up interesting new functionalities and use-cases for browser-based GIS. \STUDY FROM 2019

The challenges of this second option are that browser-based geoprocessing (BBG) might not be as performant as server side geoprocessing, \STUDY FROM 2015, 2016
and that the browser-based ecosystem lacks powerful geoprocessing tools like CGAL and GDAL. Additionally, how to present the complex endeavour of geoprocessing in the format of an accessible web application is unknown, and which use-cases might benefit from BBG also remains to be researched. 

## Case Study


## Research Question:
This study seeks to investigate browser-based transformation of geodata, 
as well as how browser-based GISS might profit from from the new opportunities.

"To which end is geofront "

##  Sub Questions
- How to design and create an accessible browser-based geoprocessing client ready for cloud native geodata? (~Old Phase 2)
- How can browser-based geoprocessing leverage existing geoprocessing libraries? (~Old Phase 3)
- Is browser-based geoprocessing performant enough? (~Old Phase 1)
- For which use-cases might such an application be beneficial? (~Old Phase 4)

## 

# Related work
...

# Methodology:

... This study will conduct this investigation by developing a browser-based geoprocessing environment. 





# Implementation 


# Discussion

# Conclusion



