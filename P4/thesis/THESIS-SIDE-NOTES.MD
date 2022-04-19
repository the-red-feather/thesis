# I must figure out how to frame this thesis more compactly. I must focus on a smaller aspect of geofront than the totality of it.

# wHAT ARE THE MOST AMAZING THINGS THIS GEOFRONT ENVIRONMENT CAN DO?


# 1. Geofront as a geoprocessing / analysis demo tool.
- Frame Geofront as an expanded version of https://validator.cityjson.org/ this. 

- THE result of this research? This workflow: 
  Locally: 
  1. Write cli geoprocessing / analysis application using a system-level language (rust, C++).
  2. Compile to `.wasm` + `d.ts` + `.js`.
  3. publish to npm (very easy to do with wasm-pack, can also be done with emscripten)
  In Geofront: 
  4. Reference the unpgk adress of this node package. 
     - Congrats, this is now a geofront plugin!
     - The CLI tool is loaded, with inputs for input parameters, and outputs for all files / data it usually writes.
  5. Build a demo script around the cli tool.
     - Publish 

### Storyboard 

1. Introduction: 
  
  _A story about how web applications promote accessibility & science communication._

  Within the field of geo-informatics, we (of course) want to share our end-results. 
    - Usually on git, but limitations
      - Not everybody can immediately use it ( unfamiliar language / build system),
      - Even people who can understand, often wont go through the trouble.  
      - "Python bindings" -> half-solves the problem, but still hard to publish to a general audience. 
  
  This leads to the development of small web demo's https://validator.cityjson.org/. 
  
  why?: 
  - Extremely findable, usable, accessible
    - Cross-platform
    - No install 
    - first point of contact is precisely where you can use it
    - You can send a link not to a download page, but to the application itself
    - Open Communication
    - (Code sharing (send a link to someone with your application + its code))

  we are not the first to recognize the suitability of the web for publishing demo's
  We see a lot of interactive web-demo's nowadays, and many of these demo's contain code:

  - In Science communication:
    - Jupyter Notebook 
    - Observable
    - JsFiddle

  - In Courses: 
    - TU Delft C++ course
    - Udemy
    
  - In Tutorials: 
    - Rust
    - Lit

  - As Demo: 
    - WAPM
    - (game-jam games)
       - more save (no virus)

  All these applications lie on a crossroad between being an interactive demonstration of a certain result or phenomenon, 
  and an open invitation for the user to edit and use this result or phenomenon. 
  (CITE A STUDY PROVING HOW INTERACTION BENEFITS LEARNING), 
  so toying around is important.

  But this poses a problem. Applications like this: https://validator.cityjson.org/ are rigid in a fashion, 
  not at all like the examples named above. 

  we want to examine and edit the geodata flow 

  THE GOAL OF THIS THESIS IS TO IMPROVE THE INTERACTIVITY OF GEOMATICS WEB-DEMO'S. 
  - (EDITABLE, MORE DYNAMIC, MORE GENERAL & LESS SPECIFIC). 

  It will do this by developing a web-based flowchart application, so that the dataflow can be edited by means of visual scripting.  
  We will test how well contemporary web technologies support such an application, as well as judge aspects such as accessibility.  


  THIS THESIS PRESENT GEOFRONT, 

<!-- 
  These features could all be implemented by normal means ( buttons, panels, sliders ) -->
  
  How to create a web-demo

  ....la la la so what are we gonna do with this thesis? ....

  <!-- So it is save to say the web is suitable for these types of things. 
  But is the web also suitable for more? Can we use a web-based sandbox environment to -->
  




  CHOICE: do something in-between python bindings, and a full fletched end-user application. 
  Ergo: Visual programming



...

6. Future work 
  _This thesis has only scratched the surface of all that _
  
  - Geofront as web-based version of grasshopper
  - Geofront as lightweight QGIS replacement 




