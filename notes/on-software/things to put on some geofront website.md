# these are all scraps from the thesis

## Salespitch
% With GeoFront, geoprocessing flowcharts can be created, shared and run from within a web browser.  
% The full application runs front-end in a browser, and both end results and intermediate products can be inspected in a 3D viewer.

% The tool offers functionalities such as point cloud loading, triangulation, and isocurve extraction.
% These functionalities can be expanded upon though a plugin system which utilizes the existing "Node Package Manager" infrastructure and WebAssembly.
% By using both, industry standard geoprocessing libraries such as `CGAL`, `GDAL` and `PROJ`, and data parsing libraries such as `IFC.js` and `laz-rs`, can be utilized.

% In addition to the goal of examining wasm-based geo-computation, the auxiliary goal of this thesis is to make geoprocessing more accessible. 
% By being free and open source, usable in a browser, and by focussing on the integration of existing geoprocessing libraries, GeoFront attempts to be more in line with the wider vision of cloud-native Geospatial than visual geo-computation environments, like FME or Grasshopper. 
% This is done to be in line with the aforementioned cloud native vision of eventually allowing non-expert usage of GIS.





## All sorts of design justifications

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% DESIGN CHOICES: CONTAINS SEVERAL JUSTIFICATIONS %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% \subsection{ Containerization }
% One of the most powerful concepts within computer science and software architecture is the idea of compartmentalizing complexity. This is reflected by many aspects in the field: 
% \begin{itemize}
%   \item object-oriented programming ( scopy \& complexity contained within class)
%   \item programming using pure functions (scope \& complexity contained within function)
%   \item Web components (containerized html + css + js)
%   \item WebAssembly (containerized binary runtime)
%   \item Docker (containerized environments)
%   \item do one thing, and do it well (Famous Linux Paradigm)
% \end{itemize}


\subsection{ From First Principles }
A part of this study is gathering a clear picture of the capabilities present in the browser itself. We do not perform a study on the capabilities of the \emph{Ecosystem}. it aid the results of this study if they can be detached from specific frameworks.
This study has therefore developed GeoFront with minimal dependencies in mind, and does not make use of 


\subsection{ Web based }

- accessible
    - immediately usable -> no installation
    - cross platform
    - easy to integrate with end-user applications (often web applications).
    - easy maintainability (just update website, no need to distribute installers)

- one-of-software argument

- makes conceptual sense for end-users with certain applications: 
  - "You download something from the internet by using an internet browser".

The "one of" software argument: QGIS is excellent for users who use it daily or at least weekly. 

(use the QGIS user data you found)

BUT, users who want to access and process geodata \emph{once in a while}, you ideally want something more temporary. Web Applications make more sense in this regard: No updates, no background processes, no 'presence' on the machine itself. Just go to the website, do what you need to do, and close the browser again. Similar to webshops.

This is in addition to the obvious advantages, like no need to install, easy maintainability, and cross-platform distribution by default.

Finally, using the web ensures that the code will run on all devices: native, mobile, desktop, IOT devices


Accessibility
- Findable == Accessible
- Reproduce \& validate research results 
- Interdisciplinary exchange of ideas 
- Educational Web Demo's
- "Getting a feel" for data 
   - Before / After
   - Hands-on experience

<!-- donald knuth argument: by keeping geodata raw, and posponing the consumtion of geospatial data to the last possible moment, we can  -->
Reduce web trafic


% It does not make sense to specify geofront to just one of these three fields, Just like it does not make sense to design a programming language for only one of these fields. 

% We will not split a species with internal conflicts and move them to three different islands, only to wait for Darwin to kick in and make these species completely incompatible. Instead, we will keep the species on the mainland, where the species will have to content with their differences in a mature way.

% This mature way will be by allowing geofront to be customized by different plugins. By unloading all GIS plugins, and adding all BIM plugins, we turn GeoFront from a GIS to a BIM tool.

% \subsection{Rust} 

% Cloud native represents something like a 'fresh do over'. Or, 'what would things look like if there had been built with the knowledge we now have, disregarding legacy'

% And connected to this is the shift from C++ to Rust for system level programming. 

% \m{->}Node -> Deno

% , especially in conjunction with a programming language such as Rust. 
% Rust compiled to WebAssembly could, compared to using python, java or C++, make geoprocessing more maintainable and reliable, while at the same time ensuring memory safety, security, and performance \cite{clack_standardizing_2019}. 


\subsection{WebAssembly}

Why WebAssembly? to complete the major thing geofront set out to do: making low-level scripts accessible on the web. 

To allow for the previous two (VPL + WEB) without a compromise to speed

On its own: WebAssembly is useful for being containerized binary code. 
- Binary: WebAssembly is close to machine code, making it very performant.
- Containerized: the main advantage of WebAssembly over normal binaries is security. wasm can be reasoned about in a virtual, containerized manner, since it uses virtual memory and a system of incremental privileges. WebAssembly binaries cannot access memory outside of its designated memory pool, making segmentation errors harmless. The incremental privileges also ensure that binaries cannot access anything the user did not explicitly allow for. 

Taken together, this makes WebAssembly a more secure alternative to regular binaries. This is also why browsers added support for WebAssembly, but not for regular binaries: Adding support for regular binaries would be a substantial risk to the security of all internet users.





## nice to haves for the programming bit

\section{Future Work}
Boulevard of broken dreams :) 

This thesis has only scratched the surface of all that

- Geofront as web-based version of grasshopper
- Geofront as lightweight QGIS replacement 





\subsection{App Features}

\subsubsection{ Constrain plugin support}
- Its becoming too hard to cater to both. The more constraint plugin support becomes, the more powerful and well-integrated we can make the plugins
- It would be really nice to make rust the only way of creating plugins. 
- Build a separate plugin loader for C / C++, or only support those through C++ bindings (dont know if wasm-pack can handle C bindings)


\subsubsection{Adding first-class type support to plugin types, by creating a Rust crate }
We couldn't do this, because we wanted to cater to .ts, .js and C++- based plugins.

\subsection*{Feature C: Publicability (the ability to publish / operationalize) } 
FUTURE WORK: COMPILE TO JAVASCRIPT. MORE CODE / VISUAL CODE INTEROPERABILITY

A VPL should be Publicable. What is meant by that, is that scripts designed by using the VPL should be 

\begin{lstlisting}

REASON: 
 - VPL: application life-cycle is important: how to publish & use applications created using vpl's
 - WEB: cloud-native geoprocessing: requires server-side / cloud based
   geocomputation interoperability: 
   meaning the scripts must be able to be used without any of the 
   interactivity features.

CRITERIA:
 - ease of sharing apps as a visual program
 - ease of compiling and running the app headless
\end{lstlisting}




## some scetches for applications

% To solve this problem, this study names four possible use-cases.  
% These cases are not mutually exclusive, but will be judged separately, based on specific criteria 
% During assessment, we will use these four profiles and accompanying criteria to judge how well the geo-web-vpl meets up this use-case.


% \subsection*{Case 1: Educational Sandbox}

% "
% insight within these processes are vital for communication, voor 'overdracht' 
% the 'jonathan blow educational argument' 
% "

% - This use-case can be fully realized within the current state of geofront
% - "Geoprocessing for kids"
% - "What is a delaunay triangulation?" 
% - "Let people play / experience / traverse a nef polyhedron"
% - Using something helps with understanding

% \subsection*{Case 2: Web Demo Environment}
% % # A: 1. Geofront as a geoprocessing / analysis demo tool.
% % - Frame Geofront as an expanded version of https://validator.cityjson.org/ this. 
% %   - [this](https://validator.cityjson.org/) (a wasm web demo) + jsfiddle 
% %   - Use rust, web, and c++ tools side by side, hand in hand

% - Reproducibility toolkit:
% - Workflow: 
%   - Load your own code from a CDN
%   - Build a demo setup around it
%   - load a custom graph from a public json file
%   - share a url pointing to this json (which contains the CDN address)
% - You can now share a rust / C++ program as a fully usable web demo,   
%   and analyze its performance using different datasets, test parameters, etc. 
% - interdisciplinary exchange of ideas
% - MISSING FEATURE: dependency list inside of the graph.json save file

% Within the field of geo-informatics, we want to share our end-results. 
% - Usually on git, but this has limitations:
%     - Not everybody can immediately use it ( unfamiliar language / build system),
%     - Even people who can understand, often wont go through the trouble.  
%     - "Python bindings" -> half-solves the problem, but still hard to publish to a general audience. 

% This was the exact reason for developing https://validator.cityjson.org/. This solved the issue of publication. Why? 
% - Extremely findable, usable, accessible
%   - Cross-platform
%   - No install 
%   - first point of contact is precisely where you can use it
%   - You can send a link not to a download page, but to the application itself
%   - Great for communication: blogs with embedded applications.
%   - Code sharing: you exactly know what to expect.

% \subsection*{Case 3: End User Geoprocessing Environment}
% - Lightweight FME, but open source \& on the web.
% - The tool in itself can be regarded as an end-user application:
%   - Load file, do something with the file, download resulting file
%   - REQUIRES WAY MORE SUPPORTING LIBRARIES AND TOOLS
% - Flowcharts can be exchanged by means of url's.
% - Future work: export flowchart to a process which can be run natively or server side.
  

% \subsection*{Case 4: Rapid-Prototyping Environment}
% \begin{lstlisting}
% - Web geoflow
% - To be used within a regular software development process.
% - Ravi's GeoFlow, but on the web
% - Meant to visually debug a certain process, after which this process can be 'compiled' to a normal cli tool.


%   WHY: 
%   - all three the previous use-cases combined: demo, test, educate yourself
%     on your own algorithms, then operationalize the code to use it in a 
%     serious environment.  
% \end{lstlisting}


% we are not the first to recognize the suitability of the web for publishing demo's

% We see a lot of interactive web-demo's nowadays, and many of them are embedded within a type of "Demo Hosts":

% - Scripting environments in (Science) Communication:
%   - Jupyter Notebook 
%   - Observable
%   - JsFiddle
%   - Shadertoy
%   - Wapm

% - Scripting environments in Education: 
%   - TU Delft C++ course
%   - Udemy

% - Scripting environments in Tutorials: 
%   - Rust
%   - Lit

%   <!-- - (game-jam games)
%       - more save (no virus) -->

% <!-- We also see 

% - As accessible alternative to native
%   - Overleaf -> does not use webassembly, but a classic client-server architecture
%   - Google Earth -->

% All these applications lie on a crossroad between being an interactive demonstration of a certain result or phenomenon, 
% and an open invitation for the user to edit and use this result or phenomenon. 
% (CITE A STUDY PROVING HOW INTERACTION BENEFITS LEARNING), 
% so toying around is important.

% <!-- So it is save to say the web is suitable for these types of things. 
% But is the web also suitable for more? Can we use a web-based sandbox environment to -->


