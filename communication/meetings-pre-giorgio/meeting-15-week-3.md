# Recap week 2-3

- Started out to load a geomatics wasm module (the cityjson validator) to force myself to see what is immediately needed to make the software functional and useful from a geomatics perspective

- This lead me to an adventure of importing "d.ts" header files, 
  and the challenge of making the Flow type-save.

## Resulted in: 

- module loading improvements. 
  - No more hacky js regex operations
  - now loads 'd.ts' header files, and based on that determines what to do
  - It progressed enough that we can even start loading wasm modules
  - All std libraries are now converted to typescript projects. As long as the typescript modules export **pure, root level functions**, the std libraries can contain any and all logic. Same counts for Wasm.

- The flow is now type save in theory.
  - new modular type system which allows for Objects, references, nested types, lists, lists within list, Objects within lists within lists, etc.  
  - cables now wont connect between two incompatible types.

- Refactors
  - Introduced the concept of 'Shim' objects throughout the code. Shims are wrappers around some aspect of 'normal' computer programming. Right now, there is a TypeShim, FunctionShim, ModuleShim. These help a lot when reasoning about the Flow. I can go into various implementation details.

# Plan for week 3-4

- [ ] The question of Object Oriented Programming -> Procedural Programming.
  - [ ] _Should_ we convert it automatically?
     - IF YES: 
        - [ ] _How_ to convert automatically?
     - IF NO: We could always just force people to write a pure function wrapper library around an existing codebase. 

- [ ] Improve Input & Output
  - The next thing we REALLY need is a major 'widget' improvement. We want special types of input, and special types of output (visualizers)

- [ ] _week 4 / 5:_ Add Geon Engine as STD
  - We need some base types like vectors, meshes, and whatnot, and some basic functions to do meaningful things with these objects
  - [ ] what to do with js TypedArray's ? these will be crucial for all geoprocessing, and translation between Wasm / processing on the one hand, and Js / Visuals on the other 

- [ ] _week 4 / 5:_ What to do with Flow management in the flowchart (especially the loop and if statement)  

- After these things, Phase 2 and  Phase 3 are sort of done (I want to shorten Phase 3 ). We can start Phase 1. 

# Notes During meeting



### Questions regarding the recap? 


- [SV] : Think about gdal types <> or any plugin type, how will that convert
- [SV] : Adapter

- [KO] : ~~Pure Functional Programming~~ Procedural Programming 


### Questions regarding the plan?


...


# For next week 
- [JF] : Move the meeting to monday / friday maybe? I would love that

...

<!-- 
- [SV] : 
- [KO] :   
-->
