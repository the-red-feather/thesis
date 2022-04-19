# meeting 19
|          |                         |
| -------- | ----------------------- |
| date     | 2022-04-11 Monday
| present  | Ken, Stelios, Jos
| Location | Cyberspace

# What has been done / Am I doing
1. writing has started! 
  - intro & related works are copy-pasted from the P2.  

-> Now in te process of setting up the other chapters, and discovering the narative.

2. cgal succesfully compiled! 
  - several C++ -> wasm demo projects have been created, with increasing complexity. 
  - This will be use

but:
  - Haven't figured out how to compile the ENTIRE library 
  - Can only use cartesian kernel for now. Boost lib is also giving me troubles
  - When CGAL uses external libraries like LAStools, we still have some complications. 
  - requires some wrapper code, both in C++ and probably also on the javascript side. 
- I did managed to find the tools and settings to make it look and act like a 'normal' javascript ES6 Module. This helps geofront's dynamic loading scheme, and makes us able to eventually publish wasm-compiled libraries as normal npm modules.  

-> i'm now in the process of building some wrappers at the side of C++, to capture a certain geoprocessing capability, like making a DSM / DTM from a PC.
-> Also, i'm in the process of building a very small-scale LAStools app, to figure out how to compile a complete library from a cmake file, and deal with the virtual file system
-> I need to learn way more about how emscripten interacts with cmake. I have not found examples that BOTH use existing libraries AND edit the C++ source the way I do... 

3. Made some improvements to geofront in the weekend
  - partial recalculation: It now only recalculates what it needs to recalculates after something changes. 
  - You can see the effects when loading [geofront.nl](http://geofront.nl), and toying with the sliders which are not part of the 'heavy' calculation  

# TWO BIG QUESTIONS: 
# 1. What is the study? What am I studying? 
Q: I'm struggling again with framing the study. 
In other words, I feel like I can do many very interesting things now, things with a real impact: 
- For example, by compiling LAStools and building some UI around it, I could make a webapp which does everything LAStools can do.
- I can also build a wrapper around it, and make it act like a normal javascript ES6 module. 
- If you JUST want to convert some `.LAZ` file to `.xyz`, and don't care about other features (& the file isn't larger than, say 5 gb), this might be very valuable.

But that still leaves me at the issue that keeps popping up: "Building useful tools for geomatics " =/= "Research". I must figure out a way to frame all of this work in an academic way, and I'm still slightly confused about it. What is my data? How to I proof anything that I'm saying? I'm making educated decisions, but ...

A: read some of the sample papers (konstantinos, karin, qgis plugin). Those papers deal with a similar narative. I'm just gonna copy-paste some of those phrases, see how they fit, and use those phrases as a 'springplank'. 

# 2. How far will I take the C++ & wasm adventure? What will I do with it? 
Q: I have figured out some of the 'hows'. Now it is time to step back and ask why.

A: But I do think I have an answer for this question. I will just wrap some small cgal PC->DSM procedure, one of the demo's. The most important part I think is just getting it to Geofront, and just showing something like: This would not be possible without CGAL. 




# This week : 
- make a planning for the coming 6 weeks up to the P4. 
- figure out the story & structure of the paper
- finish the cpp -> wasm project, so that we can put our full attention on 'geofront' itself again
  - Figure out how to correctly compile projects 
    - [emscripten doc](https://emscripten.org/docs/compiling/Building-Projects.html#building-projects)
    - [some practical clarification](https://thatonegamedev.com/cpp/programming-a-c-game-for-the-web-emscripten/) 








# Some random notes:
- There are major differences between the `emscripten` project and rust's `wasm-pack` and `wasm-bindgen` projects. 

I feel mislead by [this](https://emscripten.org/docs/compiling/Building-Projects.html#building-projects) page of the emscripten doc, stating "Building a large project with emscripten is very easy". They are somewhat right, things do compile. But if you want to do these things precise and right, it is not so 'easy'. You really do need to know how all the tools you use are built BEFORE you can even begin to convert these projects to wasm properly. 
- By means of trial and error, I am starting to figure out which parts of the documentation are true in all cases and which aren't. 

