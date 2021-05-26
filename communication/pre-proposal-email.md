## Dear Stelios, Ken & Hugo,


First of all, Long time no see! And congratulations on the 3D Bag release! I know several friends studying architecture who immediately started using it.

I wish I could've asked you the content of this email face-to-face at the faculty, but alas, no such luck. An email will have to suffice im afraid :).

I am currently preparing a thesis subject, and I would like to ask your help in developing this raw idea into an actual, worthy thesis proposition, and if you would be willing to supervise this thesis. I chose you because I have learned the most from your courses. DTs, Nef-polyhedra, Medial axis transform, all these subjects and algorithms were fascinating, and your expertise with these subjects was inspiring. Since you are all busy individuals, supervising many students already, it seemed appropriate to contact all three of you, to see who has room for one more :).


## Why

This idea started as a wish: 

> The ability to demonstrate algorithms and the effect of certain parameters in real-time, viewable, usable and distributable, without sacrificing performance.

This wish did not come about overnight. It has been chasing me for years in various fields, be it the bachelor of Architecture, my job as software developer, and during my time here as Geomatics student. I found several tools which came close, but they never cover the complete scope. To fill this gap, and for my own enjoyment, I've been working on a 3D engine from scratch, 0 dependencies, written in typescript:

- https://github.com/josfeenstra/geon-engine
- https://josfeenstra.nl/demo/geon/#sphericalone
- https://josfeenstra.nl/demo/geon/#leastsquares
- https://josfeenstra.nl/demo/geon/#meshinspector

This environment contains several translated algorithms implemented during the geomatics courses, including a linalg library created during Photogrammetry, least-squares scripts using knowledge from Lemmen's course, a delaunay triangulator, a 3D half-edge-mesh believe it or not, work-in-progress marching cubes, and more. 

Creating and using this environment has been a blast. Gone are the days of screen recordings & screenshots. I can now send clients & colleagues work-in-progress reports by giving them a link, so programmer & non-programmers alike can get a feel for the algorithms themselves. Live demonstrations have also never been easier.  

## What

I wish to have this same experience during my thesis. I am agnostic about the actual use-case or algorithms which a subject requires, but I would like to utilize this environment, or create something similar, or at the very least, do something with a similar workflow (work-in-progress algorithms sharable with a simple link, hot reloading & compiling, etc). I would also like to incorporate all algorithms, data structures and data models created back into this environment. 

## Thesis

based on these personal requirements, I have come up with a thesis proposition. 

I'm currently following the Geoweb course, and I think huge steps can be taken in developing this field. If geo-processing can be done straight in the client's browser, web applications can become way more than simple viewers. Cutting geometry (in 3D) exactly to the boundaries the user selected, generating TINs from pointclouds before any file is downloaded, so the user can check if this TIN is according to his/her needs, or even basic QGis-like activities directly in the browser. 

These activities would need more horsepower than something like typescript. I have been eyeing both Rust & WebAssembly for a long time as a way of improving the performance of client-side code. basic demo: https://josfeenstra.github.io/rustgeon/. While WebAssembly is very new, utilizing it like this is not unheard of. Google Earth for example already runs using WebAssembly.  

My working title is:

> improving 
> client-side performance of geometry processing & modelling 
> in web applications by utilizing WebAssembly

## Disclaimer

I am fully aware that reinventing the wheel like I've done with that engine is considered bad practice, and utilizing bleeding edge technologies like WebAssembly is also dangerous. Additionally, I know that this "code-first" way of thinking of a thesis is also not the best. I would just like to align my thesis with what I am working & thinking about in my spare time, so that what I want to do, and what I need to do, become the exact same thing. Nothing has been as empowering this past year for me professionally, and educational for me personally, as building that engine, and I just wish to continue that, or something like that. 

## Conclusion

Thank you so much for reading this far! This mail has become longer than expected, like usual :). I would love to know what you think about all of this, and if this proposition perhaps matches something you are working on, or I can assist with. Have a nice day!



<br/>
Best regards,

Jos

