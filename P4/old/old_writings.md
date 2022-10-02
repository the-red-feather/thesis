# intro
### Personal Motivation



- Ive worked a lot with visual programming languages
- But, know that I know how to "properly program",
  What do I do with this knowledge?

- This thesis is an attempt to maybe use this knowledge,
to improve the state of VPLs








### *why is geo-computation important?* <br><br>

Geo-computation is a process central to the whole field of GIS. 
The term 'geo-computation 'represents all types of computations performed on geographical datasets, from the calculation of an area of a polygon, to CRS transformations, or converting a raster dataset into a vectorized dataset.  
Almost all applications of GIS require geo-computation to an extend, as the raw data gathered from surveyance seldom corresponds to the precise information we wish to discover.      
This makes geo-computation a cornerstone of the entire field of GIS. 
All applications of GIS, be it ..., ... or, ..., rely on geo-computation to be fast, clear and reliable. 

### *What has happened to geo-computation?* <br><br>

The quest of making geo-computation fast, clear and reliable, has seen research and development for decades, but is still an ongoing process. 

However, geo-computation is challenging due to the nature of geodata:
- Big Data: The sizable nature of geodata makes geo-computation both computationally intensive and unwieldy. 

- Variety in formats: 

- Variety in quality

- lots of edge cases


fast not only in runtime, but fast in full usage: quick to install, to start up, to configure the process, to perform the calculations, and to visualize and examine if the calculations performed as desired. 

(offer different types of geodata transformation and manipulation)

```
Command line interfaces (GRASSGIS)
          ||
          || (cumbersome, hard to see what you are doing)
          \/
Graphical User Interfaces (argGIS, QGIS)

```
This is sort of the point we're at. 

*What is happening to geo-computation now?*

We see two promising developments emerging in the field of geo-computation: 

- Low coding -> scripting without programming, automation without having a CS-degree. 
  L Visual Scripting (FME, Grasshopper, Geoflow)

- browser-based geoprocessing
  L Operationalize workflows or processes
  L Make it easier to share

*why are vpls used for geo-computation?* 
- Parametrization: 
- Experimentation: 

*why is the web used for geo-computation?*
- Accessibility: no installment or configuration burden
- Collaboration: web applications can quickly be distributed

# problem: 

- geoprocessing using either the web or vpls is niche, underdeveloped. This leads to the disadvantages being over-emphasised, and the advantages underappreciated. 
- no way of both using the advantages of the web and a vpl, since no geo-computation web vpl exist. 


# This study 

This study explores the possibility of combining both visual programming and browser-based geo-computation. By doing so, users could benefit from the advantages of both developments, while specific shortcomings of one of these developments might be mitigated by the other one. 


these  niceties of a vpl or of the web have always had significant drawbacks




<!-- % 1) General story on geo-information. Go from data to application
% - geo-information applications are extremely valuable
% - bring the side of the gis application & geo-computation to the reader's attention. 

% Component of geo-computation.
% Overlap with other fields (CAD, medical, sfx) 
% Computational Geometry
% Examples: 
% Fit plane through 3d-points
% Triangulation
% Convex hull -->