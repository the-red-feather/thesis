# Co-reader pre-P4 Evaluation
|          |                         |
| -------- | ----------------------- |
| date     | 2022-04-25 Monday
| present  | Hugo, Jos
| Location | Online

# Mini-presentation
- presentation
- 

cloud native OGC 

stack -> metadata -> not interesting
zarr -> -> not interesting
COPEC -> Cloud optimized point cloud
Bert Tamme something

copec: ahn3


how to add plugins 
embed it in OGC 
cloud native 

A first step 

cloud-native


a big WHY 
L OCG 

Long chapter on the future

You coded to see whats possible 

greater story


# Afterwards 
[JF]: Hugo's message is clear: The software is cool, now work on the story. He strongly suggest to tie this thesis to current developments within OCG. This matches the comments of Ken & Stelios on PDAL. 

Hi Hugo, 

Thanks again for all the suggestions yesterday.  
 
From what I can tell from 1 day of reading, is that OCG wants to partially move away from the 'web services', and to solve the problem of cloud-based geodata consumption on the level of the data format itself. Using html range request, there is no need for a web service in many cases: just a singular, huge, static file is enough. This lowers the cost and complexity for data providers, which will lead to more data more readily available. 

All of this matches really well with a story I was cooking up. I already place geofront within the context of a paradigm shift in client-server architectures: From complex servers & static (no js) clients towards static servers & complex clients. My thesis could be framed as a complimentary web client in relation to these static file servers hosting cloud native formats. 
It can show use cases, and paint a picture of what would be possible in the future with these OGC standards.  

BUT: I will still need to make another argument for browser-based geoprocessing OVER native geoprocessing specifically. Cloud native doesn't really help my case in that sense. And it might only complicate matters. ("cloud native", a very contradictory looking phrase if you ask me, now I have to specify if i'm talking about the local machine _native_, or the cloud _native_ OGC movement. Why don't they use "Cloud First" or something?)

Additionally, at the coding side of things, consuming one of these new formats will be complex. 
Ive tried just directly querying the copc using http range request. This works I think, as in I get a small .laz file. but I don't yet know which range of bytes corresponds to what octree tile, or how one would calculate that, Can't find it in the COPC specifications, they just tell you to 'use PDAL'. 
I can try to compile the newest version of PDAL to wasm to access the LAZ,  


Also suggests a strong, long chapter on the future.



# Story sketch
...OCG CLoud native story ...

OCG Slogan: FAIR: Findable, Accessible, Interoperable, Reusable.

- static files in cloud
- run scripts / models in cloud

Cloud-based geodata processing has many advantages over native geodata processing for massive queries.
- Faster
- You don't have to keep your pc running the background
- More direct if process & data live on the same server.

<!-- However, massive geodata queries are not the only type of geoprocessing.  -->
However, a use-case still exists for native geodata processing.
For smaller processes, a full client-server- roundtrip might mitigate any increase in performance cloud computation might bring to the table. 
Servers  

<!-- , native geoprocessing -->


# Interactive geodata processing is needed for many use-cases. Four are identified
- Education
  - play with geodata processing methods to better understand them.

- Exploration
  - try out a tool before fully committing.

- Rapid Prototyping:
  - Finding an empirical sweet-spot of a certain parameter ( inverse distance weighting radius )
  - Comparing different methods side by side.
  - A small 'Dry Run' of a larger query.

- End User Geodata Processing
  - 




