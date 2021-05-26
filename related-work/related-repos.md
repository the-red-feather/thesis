Related Geometry Libraries
==========================

| Name | Link                            | Why   | 
|----- | --------------------------------| ----- | 
| geos | https://github.com/Ylannl/geos/ | well-known               |
| cgal | https://github.com/Ylannl/cgal  | Even more well-known     |


Related visual programming languages:
=====================================

| Name                         | Link                            
|----------------------------- | --------------------------------
| Ravi Peter's `geoflow`       | https://github.com/geoflow3d/geoflow 
| Blender's `Geometry Nodes`   | https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html  
| David Rutten's `Grasshopper` | https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html  
| Autodesks's `dynamo`         | https://www.autodesk.com/products/dynamo-studio/overview?plc=DYNSTD&term=1-YEAR&support=ADVANCED&quantity=1
| Save Software's `FME`        | https://www.safe.com/fme/fme-desktop/

> Drawbacks of all of these: 
> 1. no way to compile the tool to a CLI or web-app. > not `re-usable`
> 2. always strongly tied to its host environment > not `interoperable`
> 3. plugins must always be specifically created for these environments. no way of directly using some repo, like you can with a regular programming language. > not `re-usable`

> idea to fix (3): wasm as plugin: just a collection of functions / classes / etc. 
> idea to fix (3): direct exposure: make all functions found within wasm binaries callable from visual programming canvas. 
> with these two ideas, there is no need to specifically create plugins, any wasm binary can be utilized. 

> idea to fix (1): make the flowchart compilable to javascript, or an IFC-like json format. make the flowchart loadable from javascript or IFC-like json. make the flowchart sharable using a link / hash.






