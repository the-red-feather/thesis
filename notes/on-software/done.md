# Completed roadmap

<br>

## 1 Flowchart ✔️
- Create a web 'logic gate' app. Could be used stand-alone to teach about how to build a computer from first principles (AND, OR, XOR)
  - Inspired by https://www.youtube.com/watch?v=QZwneRb-zqA
- This will get the gui basics down
- I will not focus on anything else in this phase, I will just try to create a nice-to-use VPL.
- Only acceptable parameter: boolean 
- Simple gates (AND, OR, NOT, XOR), just like that video
- Dragging & clicking, deleting, etc... 
- Drawing using HTML, 2d canvas, or webgl, not sure which is better at this point

> Chose canvas API. introduces some inefficiencies, but it does the job. 
> we *COULD* also hack html to create nodes and cables, and make them stylable using regular css...
> hmmmmm...

<br>

## 2 Utility ✔️
- [✔️] Figure out how to `save` and `load` the flowchart to a `flowchart.json`.
- [✔️] Figure out how to `save` the flowchart to `flowchart.js`.
- [✔️] Figure out how to write a normal javascript function, and `publish` it like a flowchart component.
- [✔️] Figure out how to `save` from `flowchart.js`.
    - Generate multiple components, one for each element of the script.
- [✔️] Try to make some javascript library: `bool.js`, separate from `src`, and figure out how it can be loaded like a plugin

> As of right now: plugins are quite separate from the main codebase. 
> This way, we can already be very selective over which tools we expose in which environment, or even allow users to determine which plugins they want to use. 

<br>
