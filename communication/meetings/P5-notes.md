



Lessons
==========

- give yourself clear todo's per day. 
  Not too little, not too much.
  Upon completion, the day falls apart


TODO
============

high-level
----------

[ ] The intro / story needs to be altered 
    - stronger tie to Geo
    - VPL + Web

[ ] rewrite and balance research questions

mid-level
---------

[ ] Deep dive in Hugo's comments, fix those aspects 
  - [x] sort acronyms

[ ] Add a stronger web-component in the introduction (presentation)
[ ] Add cloud native / cloud-based geodata component to the introduction  

[ ] Cleanup Chapter 2 and 3.  
  - Some parts are still more relevant than other parts. 
  - Also, there are some things I say or use in chapter 4, 5, and 6, that were not properly explained in chapter 2. Examples of this are emscripten, or CGAL. 
  - However, a complete rewrite would be too much work.
  - Would love to hear your take on this.

[ ] Make chapter 4 and 5 more streamlined 
  - I've noticed that I repeat myself quite often.
  - I think this is because I was not sure if I already said something relevant in the chapter before.

[ ] Show your results more clearly, do the coding you have done justice

[ ] finish chapter 6 properly 
  - Experiments: add a section on a use-case application, using potree + startin + geofront std + obj downloader

[ ] write stronger, more clear conclusions.
  - hmm, i think they are already quite clear. But again, this is to be reconsidered when the overall story of the thesis changes  

low-level 
-------------------

- [x] Add arsclassica template to the thesis
- [x] Make the code snippets / listings work properly
- [x] replace all code screenshot with proper listings
- [ ] create all missing uml diagrams
- [ ] add proper graphs for the data you've gathered 
- [ ] Add all proper metadata to Zotero, for a nice bibliography
- [ ] Write abstract






Introduction
============

Two major developments are happening to the field of GIS: 

1. Cloud-first paradigm shift
  - More and more geodata is becoming available as a web service  
  - The preference shifts from downloading geodata, and performing calculations locally, 
    to uploading the calculation itself towards the location the data is stored. 

2. introduction and adoption of webassembly

These two phenomena taken together have many far reaching implications for the GIS software landscape. 
Two of which: 

1. The developments offer the opportunity of geocomputation in the browser, instead of native
  -> Benefits availability: 
     - No installment
     - Shared by a link
  -> Benefits reproducibility & open science:
     - Software developed is not only open source, but directly usable.
     - Developers are forced to address the openness of data used.

2. They allow a new level of 'cross-platform' libraries [mapbox.rs]
  - Windows, Mac, Linux, **and the Web**. ( and no-OS )
  - This is benefitial for the same reason as traditional cross-platform arguments: no duplicate libraries, no burden of synchronizing functionality across multiple libraries   

The novelty of these developments mean that many important details of these consequences remain unknown



Open problem: Front-end interface
---------------------------------

These developments and implications open up a vast, new space of possibilities.
One of the possibilities is a web applications which offers browser-based geocomputation.

However, while these developments offer the _opportunity_ to do so, 
the specific shape in which this should take place remains unknown.  

Ideally, a frontend in line with these developments should: 
1. Be in line with Cloud-first paradigm.
2. Should be able to utilize these unified, extra-portable libraries.


Possible solution: The Visual Programming Language
--------------------------------------------------

- Offers both the interface of a software application, and the composability of a software library. 


Promising because: 
- https://developers.google.com/earth-engine/tutorials/tutorial_js_03




This study
==========

Goal: explore the possibility of using a Visual programming language in a browser as a geocomputation platform.
  - By no means an exhaustive exploration, but after this study, it will become more clear what are and what are not good ideas for modern web front-ends.




CENTRAL IDEA
-----------------
VPL as cloud native geocomputation platform

Demands: 
- Dataflow VPL language model 
- Portable, unified geocomputation libraries
- 




Unified geo-libraries. 

simply put: One geo-library which can be used: 
- Natively by software developers
- On the web by software developers
- On the web by end-users



Unified geocomputation: 





L zero cost 



Three features:
--------------
- Dataflow programming, & "Visual programming turing completeness"
- "Zero cost abstraction" runtime
- Portable geocomputation

- A web-based system that works in three ways: 
  - at the 'design phase'
  - in a backend / some abstract service 
  - in the frontend


- 
- "the geocomputation platform of the future" 


Dataflow VPL
-----------
there are quite a few ways to frame a VPL. 
Some say it is just a nice UI, to offer 'coding for dummies'.
I wanted to frame the VPL in a different light by tying it to the balance between libraries and applications, and by tying it to dataflow programming.








Library Portability
----------------
As of right now, the GIS software landscape has a lot of overlapping libraries with the only difference being web and native:
- web and native viewers, web and native geocomputation, 








rants 
-----

Cross-platform

Node.js has been developed, not because there is any real use-case to running javascript natively, OTHER than making it so one language can reach all locations and platform: Frontend, Backend, Native applications (Electron). 