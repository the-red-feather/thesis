<!-- GEOFRONT: visual, browser based geo-computation  -->
This thesis presents GeoFront, a free, web-based alternative to tools like Grasshopper & FME. 
With GeoFront, geoprocessing & computational design flowcharts can be viewed, run, and shared using the web.  
The full flowchart runs client-side in a browser, and both end results and intermediate products can be inspected in a 3D viewer.

GeoFront offers several functionalities such as the parametric creation of 2D and 3D primitives, triangulation, isocurve extraction, and more. 
These functionalities can be expanded upon though a plugin system which utilizes the existing "Node Package Manager" infrastructure.
Together with WebAssembly, this enables the utilization of industry standard geoprocessing libraries such as `CGAL`, `GDAL` and `PROJ`, and data parsing libraries such as `IFC.js` and `laz-rs`.

Geofront has been created as an experiment to explore if visual, browser-based geo-computation can make geo-computation more accessible. 
The advantages and disadvantages of browser based geo-computation, compared to native or server-side geo-computation, are examined in several scenario's. 
Both quantitative indicators, like loading and runtime performance, as well as qualitative indicators, like the fitness for an intended use-case, are measured in each of these cases.
This study concludes that based on these measurements, browser-based geo-computation is not only possible, but fast, and an enabler of many promising use-cases, such as on-demand geodata processing apps, educational demo apps, and code sharing. However, extensive user-group testing is required before any definitive statements on accessibility and fitness for geo-computation can be made.  






