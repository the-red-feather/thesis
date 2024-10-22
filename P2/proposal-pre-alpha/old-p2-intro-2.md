\section{Introduction}

% [1]
\par


- Geodata processing is important.

- A Demand for accessible and usable geoprocessing environments exists
  - FME
  - geoflow
  ;

Client side geoprocessing is underdeveloped 


\& vpl's are not FAIR 


The most common way to distribute the end results of geodata processes is the web. 
(Several web clients exist, like google maps, osm, and things build from leaflet and celsium. 
within these environments, the post-processing of geodata is often needed. 
However, client-side geoprocessing is still insufficiently researched.






\dots



% Hmmmm... the way I frame this, dont like it...

% [2]
% [JF]: This is nice, By 'improving a VPL' I dont have to go all 'use case testing' and make a case for a vpl, 
% because I can just state in this introduction "they are useful, look, multiple people are working on them"
\par
Visual programming languages, or Vpl's for short, can make geodata processing debugable and more insightful. 

[Name some relevant VPL's, their reason of existence, their target audience.
this will be more in-depth during the 'related work' section] 


% [3]
% hmm.... I sort of dont want to do this here...
% [JF]: these criteria are Ideals, of course software falls short on meeting them, make this more nuanced)
\subsection{Problem}
The main advantage of vpl's is usability. 
However, vpl's used within the field of geomatics still fall short on certain usability aspects. 
The well established FAIR paradigm has been used to judge the usability of geodata, and geodata portals (SOURCE: GEOLEGAL). 
This paper will use this paradigm instead on vpl's, for geodata processing itself can have varying degrees of Findability, Accessibility, Interoperability, and Reusability. 
When we judge the aforementioned vpl's on these aspects, compared to regular programming languages we find the following: 


\subsubsection*{Accessibility}
Accessibility is arguably the strongest advantage of a visual programming language over a regular language. 
Users whom are not familiar with programming can often still use a VPL. 
However, many VPL's are still hard to actually acquire. 
The tool needs to be installed, an account is required, and most VPL's are not free and open source like the vast majority of programming languages are. (Study on advantage of web-based tools over native ones)

\subsubsection*{Interoperability}
Besides a large barrier of entry, Visual programming languages are also not platform agnostic. 
\dots
are usually strongly tied to their host environments
\dots
This also makes Bindings to different languages or programs harder. A regular programming language like python can accepts bindings, which makes it possible to run scripts written in C++ or Rust. Similar actions are often difficult to accomplish with VPL's.

\subsubsection*{Findability}
It is often hard to get an overview of 


\subsubsection*{Reusability}
Reusability is arguably a core concept within computer programming in general. 
A function is defined with the idea that it may be used multiple times, in multiple different contexts, with a variety of different input data.
Vpl's are often not as reusable as 'normal' code. The flowchart-scripts often cannot be turned into standalone applications or tools.



% [5] go from this to research question
\newpage
\subsection{Solution}
The aim of this research is to explore a new geoprocessing method: geoprocessing in a browser, client-side. 
This would be beneficial for several reasons. 
For one thing, users would not have to install anything besides a web browser. This way, tools can be shared, cross-platform, without having to download or build anything. 
Secondly, client-side geoprocessing can make geoprocessing more interactive and insightful. A 'sandbox environment' which can do geodata retrieval, processing, and visualization from a web browser would be a great tool for debugging, quickly looking at the effects of parameters, and finding out which algorithms work best with which dataset.

This research attempts to solve two barriers preventing successful client-side geoprocessing. The first barrier is that the client-side programming language `javascript`, together with its library ecosystem, do not offer the speed nor the tools to perform fast geoprocessing. To solve this, WebAssembly, a type of binary that runs in virtual machines, will be considered. It can be used to take an existing C++ geoprocessing library (like cgal), and to publish it in a way anyone with a browser can run it at near native speed. 

The second barrier is that an application using 'just WebAssembly' will not be very useful or insightful without a sufficient framework supporting it. This thesis will consider a framework in the form of a web-based Visual Programming Language, or VPL to facilitate this. 