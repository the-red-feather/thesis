INTRO: POV: CLOUD NATIVE

\m{->} establish web GIS context

\m{->} establish cloud native movement https://www.ogc.org/blog/4607 'radically simplify' -> love the word!

\m{->} mention FAIR

\m{->} establish the browser-based front-end client as the preferred interface for this movement, for the web GIS reasons
... This will require very different web GIS clients than we have seen up to this point. 
    -> not only visualize, but show and configure the geo process, allowing queries, etc. etc. 

\m{->} establish a need for geo-computation capabilities as a counterpart to cloud computation 


... The Cloud native movement has a question at its heart: "What would geospatial standards look like if they were built for the cloud?"
... We pose a similar question to start the investigation of this thesis: "What would geo-computation look like if it were build for a web client?"


- cloud native geospatial 

Due to ..., the goal of this thesis is to develop an application for geo-computation in a browser-based front-end.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


\chapter{Introduction}
Web \ac{gis} forms an indispensable component of the wider geospatial software landscape. 
For the average person, an interactive \ac{gis} web application is often their first and only exposure to a \acs{gis}, be it a web mapping service, a navigation system, or a pandemic outbreak dashboard. 
A web application is cross-platform by nature, and offers ease of accessibility, since no installment or app-store interaction is required to run or update the app: 
As soon as it can be found, it can be used.
The ability to share a full application with a link, or to embed it within the larger context of a webpage is also not trivial. 
Together, these aspects have made the browser a popular host for many important geographical applications, especially when accessibility is vital.

The field of web GIS is, just like the wider context of the web, subject to many changes \& developments. 
These come in the shape of a new feature reaching a consensus in the major browser vendors, or a change in commonly used standards like the \ac{http}.
These changes may lead to a 'trend': a new way of reasoning about or organizing a web service or a web application. 
% trends lead to interesting new applications which may serve new use-cases
These trends are often closely tied to certain features which made them possible. Examples of these are: 
% interplay between features and trends 
\begin{itemize}
  \item Recent improvements in the javascript runtime are a vital component of the current shift from backend-heavy to frontend-heavy web applications. 
  \item front-end Libraries like Celsium, Leaflet and D3 would be hard if not impossible to realize without HTML5 features like WebGL and the Canvas API.
  \item The cloud native geospatial movement requires the http range request feature to truly be effective.
\end{itemize}

The influence and importance of the above web features and trends are why new developments within web GIS are very important to examine.



Geofront has been created to study how recent web features and trends can have a positive effect on the accessibility of geo-computation. 
The hypothesis is that the combination of cloud-native geodata together with front-end heavy applications with industry standard geoprocessing libraries using webassembly, may lead to new, powerful types of GIS applications and use-cases. 

an experiment to capitalize on these developments within the field of web GIS. 


...
In the field of Web GIS, a pattern can be recognised between web \& browser features,  
- javascript runtime improvements -> shift from backend-heavy to frontend-heavy web applications
- HTML5 with WebGL and Canvas Api -> Celsium, Leaflet, D3
- http range request -> cloud native geospatial movement 
- WebAssembly -> ...

Now we see a new technology 

This study has been conducted for two reasons.
Firstly, this study wishes explore the possibilities \& limitations of front-end geoprocessing.
  - Web technologies have become a vital, core component of the modern geospatial software landscape.
  - However, the web is changing : cloud-native geospatial movement, move to front-end heavy applications, WebAssembly. 
  - By creating an application using these trends and technologies, we can get a better understanding.

Secondly, to experiment with making small-scale geoprocessing more accessible
accessible alternative to existing visual geo-programming environments.
