# meeting 22
|          |                         |
| -------- | ----------------------- |
| date     | 2022-04-19 Tuesday
| present  | Ken, Stelios, Jos
| Location | Cyberspace

# Huishoudelijke Mededelingen (bookkeeping)
- Moving P5 
- Meet with Hugo
- Something else? 

# Recap week 10
Main todo's:

WRITING
- [X] Figure out the narative of the written thesis 
  - [/]write down chapters & subchapters \

CODING
- [/] Finish up geofront
  - [X] Sliders 
  - [X] Convert all experimental doodling into a proper STD.
  - [ ] Finish up CGAL / startin business

# Commentary
- I was getting really stuck and disheartened by the middle of last week by just the sheer amount of work left to do. I'm behind schedule in terms of writing, and geofront is half-finished. I don't like the fact that I have to split my attention between both. I decided to get out of this slump by just trying to do SOMETHING meaningful, to achieve some sort of progress, in a simple way. This is why I focussed on geofront. 
- have experimented a lot with different STD's, settled on just an internal one. Bit more annoying to develop, 
  but it was the easiest to just get working, and the easiest to integrate with the rest of geofront.
- I Finally figured out how to 'organize' the std. 'organize', since I wouldn't dare call the current setup organized, But at the very least, I can now add more and more things to geofront without the feeling like things are getting out of hand. 
  - I solved this issue by constraint relaxation: I'm forgoing typechecking or type-auto-conversion for the time being, but i'm setting things up so they can be added incrementally later, without too much trouble.

# Discussion during meeting 
...

During speaking, we discovered 3 real use-cases (plus 1 I also need to mention):

- Geofront as **Web Demo Application**

  > This use-case is the easiest to realize with the current state of geofront

  - "Geoprocessing for kids"
  - "What is a delaunay triangulation?" 
  - "Let people play / experience / traverse a nef polyhedron"
  - CURRENTLY MISSING FEATURE: Load in your own npm package

- Geofront as **End User Geoprocessing Environment** 
  - FME, but open source & on the web.
  - The tool in itself can be regarded as an end-user application:
    - Load file, do something with the file, download resulting file
  - CURRENTLY MISSING FEATURE: compile to web app (take the input & output, hide the flowchart)

- Geofront as **Geoprocessing Prototyping Environment**.
  - Ravi's GeoFlow, but on the web
    - Meant to visually debug a certain process, after which this process can be 'compiled' to a normal cli tool.  
  - CURRENTLY MISSING FEATURE: compile to native cli tool (node.js script)

- Geofront as **Parametric Modelling Application**
  - OpenSCAD, but using visual programming instead of scripting.
  - Grasshopper, but open source & on the web.
  - CURRENTLY MISSING FEATURE: create new points / lines in the viewer

The "MISSING FEATURES" indicate that all use cases are just one feature away from being TRULY useful.

...

- I am once again over-analyzing and overthinking the writing bit
- Writing has to get priority for now

...

# TODO Week 11
WRITING
- [ ] cleanup the latex project (references / acronyms are giving errors, packages used are not the same as P2). 
- [ ] refine and narrow the narrative, 
- [ ] write / edit introduction
- [ ] write / edit preliminary work
- [ ] fun task: make a nice cover

CODING
- [ ] Geofront: continue the cleanup & STD
  - Add Json & XYZ again
  - 
- [ ] add Startin properly, figure out how to integrate types
   - Can easely be done with [inspectable](https://rustwasm.github.io/docs/wasm-bindgen/reference/attributes/on-rust-exports/inspectable.html)

(- [ ] add the cgal demo-project properly
   - Not sure, maybe [this](https://emscripten.org/docs/api_reference/preamble.js.html#preamble-js))

()

# TODO coming weeks 

## Week 12 
- write methodology 
- write conclusion

## Week 13 
writing !

## Week 14
- At the meeting: Finish a draft P4, something with all chapters & sections present
- continue writing & improving

## Week 15
- At tuesday: DEADLINE: FINAL HAND-IN DATE OF P4
- Prepare presentation

## Week 16
- At tuesday: PRESENT 

---------------------------------------------------------------------------------------------------