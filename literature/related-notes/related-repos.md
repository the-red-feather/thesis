Related Geometry Libraries
==========================

| Name | Link                            | Why   | 
|----- | --------------------------------| ----- | 
| geos | https://github.com/Ylannl/geos/ | well-known               |
| cgal | https://github.com/Ylannl/cgal  | Even more well-known     |


Related visual programming languages:
=====================================

| Name                         | Company | Link                            
|----------------------------- | ------- |-----------------------------
| Ravi Peter's `geoflow`       | | https://github.com/geoflow3d/geoflow 
| Blender's `Geometry Nodes`   | | https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html  
| David Rutten's `Grasshopper` | | https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html  
| Autodesks's `dynamo`         | | https://www.autodesk.com/products/dynamo-studio/overview?plc=DYNSTD&term=1-YEAR&support=ADVANCED&quantity=1
| Save Software's `FME`        | | https://www.safe.com/fme/fme-desktop/
| SideFX's Houdini 



Drawbacks of all of these: They are not FAIR:  
> 1. not `findable` & `accessible`: the tool needs to be installed | requires an account | requires payment > entry barrier 
> 2. not `interoperable`: always strongly tied to its host environment | no way to run a script without the tool to a CLI or web-app
> 3. not `re-usable`: plugins must always be specifically created for these environments. no way of directly using a repo, like you can with a regular programming language.

> idea to fix (3): wasm as plugin: just a collection of functions / classes / etc. 
- automatic js library from wasm builder
- updating a list of all available plugins
> idea to fix (3): direct exposure: make all functions found within wasm binaries callable from visual programming canvas. 
> with these two ideas, there is no need to specifically create plugins, any wasm binary can be utilized. 

> idea to fix (1): make the flowchart compilable to javascript, or an IFC-like json format. make the flowchart loadable from javascript or IFC-like json. make the flowchart sharable using a link / hash.





> ravi: rapid prototyping
> fast visualizing of in-between steps
> c++ -> fast & many libraries. 








> 
geon.nl??

>
