A. ( 'no-it-footprint' geoprocessing applications )
- The way we make maps is rapidly changing. 
- The applications we build our maps in as well. 
- The Geo-industry is moving to a cloud-based, 'no IT footprint' system of applications. 
  - many advantages to cloud-based workflows:
    - no installments, updates, etc.
    - no local files
    - version control 
    - cloud processing
    - cloud storage

  - examples: 
    - Google Earth Engine
    - Cloud-native movement. 
    - Raster Foundry
    - CAD: Onshape https://www.onshape.com/en/platform

C. ( speed of light argument )
- However, these cloud-based geoprocessing workflows have a big disadvantage which remains largely unaddressed: The speed of light. 
  - During development: lots of traffic of intermediate results back and forth. 
  - Cloud processing is slower than local processing when using small datasets. 
  - Data storage access is a lot cheaper to host in the cloud than processing functionalities. 
  - Expensive to spin up a specific web services per client. 

D. ( Leads to a need for hybridization & containerization )
- So, in order to contribute to the cloud native geospatial movement, while at the same time addressing the 'speed of light problem', 
  geoprocessing must be hybridized, and containerized.

E. 
- Additionally, 

- Why this web-based stuff? -> IT-footprint story.
- Why vpl? -> a big goal of cloud-native is accessibility, This is why rasterFoundry is creating Modelbuilder. 
     VPL's can potentially make automation accessible to a very large audience. 

-> why not just C++ / python + docker? this is the same argument as "Why use FME instead of C++ or python?" different advantages and disadvantages, use-cases, different target audiences. 
-> we wish to pursuit containerized, browser-based geoprocessing in the format of a visual programming language application. 

# This thesis 
- This is a theoretical exercise, to shape the conceptualization of geoprocessing in a cloud-native geospatial future.
- This is a practical exercise, to example a specific method of facilitating .









# Geofront
- geofront has been created to fill this niche. 