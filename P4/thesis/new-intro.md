
This thesis introduces GeoFront, a first step towards a web based, open source, geodata processing and visualization environment in an era of cloud-native geodata. 
In this thesis, the motivation, requirements, technical aspects, and achieved functionality of geofront are covered. 

GeoFront has been developed for two reasons. Firstly, this thesis anticipates that OGC Cloud native geospatial types, and specifically the Cloud Optimized Point Cloud, will create 
a need for equally accessible means to access, analyze, edit, and visualize this data. A similar need arose when in the field of rasters, ...
leading to the development of tools like geotiff.io and modellab.

The adoption of COPC could mean the same for point cloud data, but it remains unknown what accessible analyze, edit, and visualize means for point cloud processing. 
How to present the complex endeavour of point-cloud processing in the format of an accessible web application is unknown. 

% Similar trends can be found with GEOTIFF.IO and MODELLAB 
% Investigate what it means to create an accessible geoprocessing environment


Secondly, a move towards cloud-native geospatial data leads to a re-examination of the traditional client \& server model. The cloud-native initiative aims to radically simplify geodata storehouses to just static file servers. All processing and analysis of this geodata can then be performed by separate cloud-based web services.
This thesis explores the opportunity of adding these geoprocessing capabilities to the client instead. By not relying on additional web services, we could drive down operational costs for certain applications, making geodata processing more accessible. 

The challenges of this second option are that browser-based geoprocessing (BBG) might not be as performant as server side geoprocessing, STUDY FROM 2015, 2016
and that the browser-based ecosystem lacks powerful geoprocessing tools like CGAL and GDAL.



The wider goal of this study is to discover the possibilities and limitations of browser-based geoprocessing, in order to help developers make the decision between browser-based geoprocessing and cloud-based geoprocessing. 

The goal of "discovering the possibilities and limitations of browser-based geoprocessing" is too large of an undertaking for the scope of one thesis. Geoprocessing is a complex and multifaceted phenomenon, containing for example map algebra, crs transformation, vector to raster translations, raster to vector translations, point cloud filtering and interpolation, and much more. 

Therefore, this study will develop a use case application to assist this research. This application serves to contextualize the research, and to force the research to solve the practical challenges of how \ac{bbg} can actually be used. The type of application chosen is a web-based geoprocessing environment, similar to GEOTIFF, GeoTrellis + ModelLab. These types of applications seek to present geoprocessing capabilities in an accessible manner: "Widespread access to frequent, high-resolution Earth observation imagery has created the need for innovative tools like ModelLab that will help individuals and organizations to effectively access, analyze, edit, and visualize remotely sensed data in transformative new ways without years of specialized training or ongoing investments in proprietary software and technology infrastructure. " \Source{ModelLab}.

This study introduces GeoFront, a web based, open source, geodata processing and visualization tool. 

