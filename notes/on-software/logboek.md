# WEEK 00 / 15

## FRI | 5 nov 2021 | Halting development

![state of the art](../images/10-45_05-11-2021.PNG)

Prototype status: all sorts of different things are possible at the moment. js - script conversion, saving to and loading from json. Objects, button gizmo's, log console, text input, etc. 

Right now, mostly working on P2 paper. consequently, little progress with the flowchart application. 

I am considering a do-over of the flow-chart rendering. We need svg based rendering in my opinion.  SVG's would allow us to: 
- Re-render things less. We can just rely on browser-based scrolling. This has got to be more efficient than the Canvas based scrolling we are doing right now. 
- This plays nicer with the browser as a GUI environment. canvas API is great for rendering images dynamically, but we will be dealing with vector graphics. 
- use CSS for styling the components, allowing easy re-skins
- clicking on things using the svg boundaries, cuz why not

<br><br><br><br>

# WEEK 01 / 15 | generate momentum again to start development

- You are now finally allowed to continue development, but the writing introduced many considerations, resulting in choice paralysis. Find a component small enough to continue development, and make something

## TODO:
- [ ] Make configuring the graph feature complete, fun and intuitive
- [ ] 

## TUE | 08 feb 2021 | Picking up the pieces | FOCUS: UI

Finally picking up where I left off. The Thesis proposal and presentation are finished, quite satisfied with both. The writing did generate a ton of new ideas which now make it hard to continue the work. 


## THU | 10 feb 2022 | Starting up 
quite pleased with the cyberpunky look




# WEEK 02 / 15 -> UI

## Tuesday
Today the cables where reworked. Cable objects complicated too many things, and were hard to reason about. The new system just adds the connectivity state to the nodes themselves. As a consequence, the 'cable' class was deleted. Something called "CableVisual" was created, to in the future, house the visual aspects of the connection, such as the polyline generation, and selection
- Huge simplification of code. Easier to see where things go right and where things go wrong
- BUT: this was a huge conversion. Still requires a ton of testing and debugging to get the cables to where they were before the changes 
- Still a lot of legacy code here and there. Try to clean up after thi  ngs are working nicely again. 
- AFTER: add cables to history. 


## Wednesday 
- Cables are now sort of working again. Cable history working, just weird sometimes, cant be bothered to fix it right now 


## Thursday -> Loading Plugins
TODAY, let us truly begin...
Flow editor is fine for now, we need to get started with the real deal.
- But where do we start? 
  - [Ken] push this project to geomatics as fast as possible
  - [Stelios] Types!

- I will try to load a geomatics wasm module (the cityjson validator) to force myself to see what is immediately needed to make the software functional and useful from a geomatics perspective
- This lead me to an adventure of importing "d.ts" header files, which we need to create a type-save environment. 



> ### Some cool links
> [ts-to-json](https://stackoverflow.com/questions/39588436/how-to-parse-typescript-definition-to-json)
>
> [ast](https://ts-ast-viewer.com/#)

## Friday : NOPE

<br><br><br>

===============================================================================

# Week 3 

# Monday
- types are sort of done! a recursive system is implemented within a `ParameterShim`, to provide type safety to the whole flow

# Tuesday
- [X] add Object types, see if that works
- [X] create simple type conversion components
- [X] continue types : prevent cables between incompatible types 
- [X] object types
- [X] actual type checking 
- [X] non-literal object types

# Wednesday 
- [X] Make a recap for Ken & Stelios
  - [X] Move the meeting to monday maybe? I would love that
- [X] DTS-Loader
  - [X] how to add constructors and destructors?
  - [X] add constructors 
  - [X] add methods 

# Thursday
- No progress...

# Friday
- Progress, but on the side of webassembly

- [X] create a Rust `wasm-pack` library, and dynamically integrate it within the geofront

- [ ] continuation on html components 
    - [ ] (input file loader, output visualization using Geon for the time being)
    - [ ] 

- milestone: compiled a very basic rust library into webassembly, and loaded it dynamically. The add and subtract code are running wasm!
- whats more, is that we can load these geofront plugins straight from npm if we want to, using the unpkg service


===============================================================================

# Week 4

Theme Of The Week: html & css are the main course. Its time to upgrade the looks, 
but especially, to lay the architectural foundation for dealing with html and the more standard elements of 
ui, such as right click drop down menu's, buttons, pop-up screens, etc. 

__at the end of this week, we will have:__

- prettier GUI
- a visualization screen OR visualization component
- advanced html widgets.

# Monday 
- Html / Css 
    - Which framework / no framework shall we use ? 
       - Add FAST-elements as our ui framework. it is exactly what I would expect of a modern html UI system.
          - This will get us started with buttons and stuff 
          - [FAILED] figure out how to change colors and other aspects
          
       - [X] add also plain Web Components using html templates, for we do not always need a framework.  

  Q: how to get basic buttons, sliders and whatnot? 
  A: bootstrap, probably. FAST was to hard easier to use, but is very hard to configure and dont play well inside of nested shadowDOM.

- [X] html components 
    - [X] lay down the foundation 

# Tuesday 
- [x] make the basics of everything: header, footer, side menu's, main canvas, buttons
   - [ ] add a dropdown menu button 
- [x] make an entire menu
- [x] make a canvas component which renders a normal geon-app 
- [x] add this UI to the main coding project
- [x] add the nodes canvas

# Wednesday 
- [X] select a component, visualize the settings 
- [X] make viewer accept a 'view this' & 'drop this' message 
- [X] select a component. If output data is visualizable, visualize it.  
- [X] try to visualize two points, 
- [X] and a line between two points

# Thursday
- [X] create a typesave event system
- [X] create menu abstraction

- [ ] widgets
    - [ ] input number slider
    - [ ] input file picker
    - [ ] output image visualizer
- [ ] screen next to each other
- [ ] make it fun, quick and intuitive

# Friday
- variables 
  - [ ] auto type convertion? 
  - [x] caching
  - [x] looking at cached data?
  - [x] selecting cables ?




===============================================================================

# WEEK 05 / 15

Theme of the Week: stabilize

all sorts of things are broken or missing at this point. 
Once the 'main geo-vpl loop' is done (create something visually, and render it)
Its time to solve these stability concerns.


Additionally, I wish to get some sort of usable STD in here, to expand visualization and basic usefulness.




__at the end of this week, we will have:__
- the full app, working and stable. 

__components__

- stability
  - menu 
    - [x] dropdown menu html component 
    - [x] `File` menu
    - [x] `Edit` menu
    - [x] `Add` menu
    - [x] `Settings` menu
    - [x] `View` menu
  - `file`
    - [x] fix all saving & loading procedures
  - `Edit`
    - [x] fix all undo / redo behavior
    - [x] fix copy-pasting behavior
  - `Add`
    - Make sure we have a nice add menu again
  - side-menu
    - [X] publish settings to a side menu 
    - [X] show settings for input, output, process, and canvas
    - this can be a stepping stone for the html nodes

  - ``

- std
  - include as much of the `geon-engine` as possible
  - figure out how to organize this

# Monday
# Tuesday
# Wednesday
# Thursday
The stability issues raised many things, which are now all fixed. 

# Friday
Get a head start on week 6


- [ ] Render selection


===============================================================================

# WEEK 06 / 15

There are a number of things to expand upon. What is wisdom?

Three main trajectories: 

- I GEOFRONT Features: _We are *so* close to many features which I would love to add_
  - basic Profiler
  - List support
  - Json / Dictionary support
  - Array / Buffer support
  - *STD type registry*


- II GEOFRONT-STD _Use Rust to create an std library._ _Compare it to the same library, all written in plain js / ts_
  - Matrix
  - Pointcloud
  - Mesh
  - Delaunay
  - Random 
  - *STD type registry*


- III CGAL / GDAL: _At some point, we would like to use existing third-party code. This needs to be easy to configure, and easy to integrate with the rest_
  - See to the npm integration
  - *See to the integration of types*
  - Determine how to integrate the found GDAL wasm project 
  - Use emscriptem to convert the OGR component of GDAL


__TODO: STD__
- [ ] Matrix support
- [ ] Render mesh 
- [ ] Render pointcloud


__TODO: Features__
- [X] Render selection
- [X] HTML widgets 
- [.] better looking at data in side-menu
- [ ] Array support
- [ ] List support
- [ ] Object / Json support

- Matrix types

# Wednesday
- [X] get the setup over at this side 
- [X] figure out how to return a tuple from rust 
  -> this is hard. 
  -> option 1: make it all rust objects. They can be converted, and are fine to use when using 'inspectable'
  -> option 2: foreign objects.
  -> I Think [this][game-of-life] is our best chance forward. retrieving a pointer, and buffer size, creating the buffer on the javascript side

- [X] make a very dumb, basic type encoding
  - just based around string enums, and 'thrusting' that the any type contains what we need when it has 'typename'
  - TODO typechecking! 
  -> THIS IS HARD AND IMPORTANT 
  -> we cant do this naively, we will require some sort of extra ensurance that we are dealing with the right types. 
  -> Edit: came up with a 'trait' idea, where foreign types can 'earn' the right to be treated as if it were a `Point`, `Vector`, or `Mesh`, if it contains the right data.


- [X] make some sort of data import widget, or a random list of points generator 

[game-of-life]: https://rustwasm.github.io/book/game-of-life/implementing.html#rendering-to-canvas-directly-from-memory

RNG 

- [ ] return points as { buffer: Float64Array, typename: "multi-point-3"}
- [ ] return triangles as { buffer: Uint32Array, typename: "int-matrix-3"}
- [ ] return mesh as { typename: "Mesh", vertices: {... typename: MultiPoint}, triangles: {typename: IntMatrix-3}}
- [ ] visualize the shit out of it! 


# Thursday

- [X] text file input 
- [X] text file output
- [X] get a nice xyz file, visualize it using something else to know what it is 
- [X] xyz string to multiVector
- [X] visualize multiVector 
- [X] multiVector to xyz string
- [X] test that these are the same strings
- [X] multiVector to list<vector>
- [X] list<vector> to multiVector 
- [X] expand traits 
- [X] do better trait checking 
- [X] fix the trait bugs

> The way the traits are actually being used right now are waaaayyy dumber than the whole trait system now implemented
> This suggest that this might be over-engineered. Maybe we just need to do some minor, runtime type checking, if all 
> field are present, of the correct type, instead of some weird connection-time type checking 
> ohwell...

# friday

- [ ] move the list of vectors left
- [X] add lists to the visualizer
- [X] refactor graph a bit
- [x] expand full graph recalculation starters to inputless nodes
- [X] reintroduce cables 
- [X] implement the cables a bit , remove the workaround code
- [X] make widgets more 'normal' compared to operations: remove the excessive 'ifs'
- [X] fix bugs
- [X] detect list at connect-time
  - [ ] make this better
- []

- implement the 'list comparrison' thing
- [X] generate random vectors
- [X] apply the DT to these poin ts 

- apply more runtime / connection-time list


- [X] callback & calculation overhaul
   - [ ] list calculation overhaul 
   - [ ] how to specify a list? 
   - [ ] how to take items from a list? 
   - [ ] Nodes do not like variation of their input & output sockets. This is also troublesome for graph's multilinkedlist reasons





  TODO
- [X] internal (widget) operations



===============================================================================

# WEEK 07 / 15

...

That was the original idea

geoprocessing
- data modelling
- complex data model

- qgis 
  - features 
  - attributes 
  - geometries

- PDAL 

- full pipeline geoprocessing 
  - what library to integrate 
  - how would it work


# Monday

# Tuesday

Challenge for the coming 3 days: figure out how to load and visualize a geojson
- [X] find and integrate a triangulator 
- [X] figure out how to organize STD and STD types
- [X] load and decode a geojson
- [X] make a 'get' component
- [ ] make sure we can loop over the get component

# Wednesday
- [ ] make a 'get' component
- [ ] 

- SUCCES! already completed the challenge! 






# WEEK 08 / 15

Theme Of The Week: WASM 
Its time to truly start the WASM part of this thesis, now that the other ingredients are at the very least present.
- GDAL 


# WEEK 09 / 15

Starting writing...


## Wednesday 

Found a bunch of very useful Cpp -> wasm video's 
https://www.youtube.com/watch?v=skK8aId86E0
https://www.youtube.com/watch?v=qZ_zyxxXaAM
https://www.youtube.com/watch?v=WHwl8mqVRUg
https://www.youtube.com/watch?v=9lxnm9a-Yi8




## Thursday

Initial demo's using cgal on the web are FINALLY working! 

- [ ] cleanup
- [ ] try to do something more complex with CGAL 
- [ ] new wasm demo: GDAL
- [ ]


# WEEK 10 / 15

## Monday : Toying around with C++ & wasm, still an unruly beast | Meeting
More emscripten business, not really getting anywhere. Meeting was very nice, very productive

## Tuesday : Writing


## Wednesday : more writing | Geofront : Sliders & Bug fixes 
Based on what Ken said, I wanted to get started on making a structured story, 

## Thursday : 

## Friday & Weekend : Geofront STD 
This friday and weekend, I've spend ALOT of time developing the geofront standard library, a library which will always be present within geofront. 


# WEEK 11 / 15

## Monday : 
Finishing up the STD. created a delaunay + perlin noise script. 

## Tuesday : 
Tried continuing writing

## Wednesday : 


## Thursday : 
Fun Fact: i'm at 25.949 lines of code currently


## Friday : 
Major writing 

## Weekend : 

# WEEK 12 / 15

# WEEK 13 / 15

# WEEK 14 / 15

# WEEK 15 / 15





=================================================================


