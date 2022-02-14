# DESIGN 

- Augmented coding!

## Fundamendal design idea of the flowchart: 
- functional programming ❤️ wasm containerization 
  - Oversight: Closed reasoning of individual components 
  - Memory safety
  - Serves as debugging environment
    - Error handling : You can throw an error on one component 
    - Error handling : You can visually show where this error occurred, at what part of the dataset. It can then immediately be inspected
    - You can visually indicate a component is busy calculating, or fetching some data online.
    - All of this is VERY helpful when integrating tools from multiple sources, you can reason about misbehaving components dynamically


## Q: Why the grid & line style?
- A: Cartography inspired: The designers of metro network maps have discovered, over the years, that maps where **connectivity** is the most important information to convey, a certain abstract depiction with as many straight lines as possible is advantageous over maps with curves. Since both this flowchart and metro railway maps are essentially just depicting a graph, using this style seemed very appropriate. 
- Snap / grid based. Because code is always monospace, this should be as monospace as possible
- For the naming of features, we need to rely as much as possible on names common in computer programming. No reason to reinvent these names. 
  - ~Cables~ -> Variables | 
  - ~operations~ -> Functions
- Chipset inspired / cyberpunk inspired. Because this will give off a 'cool, computery feel'. The tool should inspire, and should not be boring if we can help it



## Q: Why the details 
- Minimum height of Function Nodes is 2, to separate functions visually from variables (whose height is usually 1)
- 



## Questions 
- how to store the graph?
- will we have something like layers \ turning previews on and off?
- how to do QGIS-like interactions? 

## Naming 

| Graph | Normal Programming   |
|-------|----------------------|        
| Cable | Variable             | 
| Gizmo | Method on 1 variable | 
| Node  | Pure Function        | 

