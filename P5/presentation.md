# Geofront : presentation



Front
================================================================


Introduction -> Why
Objective -> What
Methodology -> How 
Results -> To what extent 
Conclusion



01 Introduction
================================================================

## Motivation 

### GIS

- Gis concerns itself with this

- One of the goals of GIS is to provide these end-users both with the 
  data and tools they require. 

- This side of the tools is the subject of this study.

- These tools, like all software, possess one of two forms:
  - Software application
  - Software Library



## Problem Statement

This thesis concerns itself with the latter: Providing tools. The problem this study
seeks to address, is that the core transformation and analysis tools found in certain
GIS software libraries, are normally not directly accessible by practitioners in the
fields mentioned above: governance, infrastructure, urban planning, etc. A small
number of native software Libraries, like CGAL or GDAL [Fabri and Pion, 2009;
Dohler, 2016], play a foundational role in many GIS tools. However, end users with
a profession different than software developer, are often unable to directly access
these libraries. The tools can only be used indirectly, and only when a software
developer has incorporated these functionalities in an application. Similarly, if re-
search leads to a new GIS library, end users are at the mercy of a software developer
implementing the functionalities of said library as a usable application, or as a plu-
gin for an existing GIS environment like QGIS [QGIS Community, 2022]. Moreover,
even if these capabilities are added to an application, the tools are almost always
less feature rich, and non-composable: The output of one procedure cannot auto-
matically be used as input for another. This leads to labor intensive procedures and
repetitive workflows, as opposed to automated, re-usable procedures. At the same
time, maintainers of a GIS library often find themselves in the situation of having
to maintain and synchronize a great number of bindings and plugins, which limits
innovation (Figure 1).

It is safe to say that the limited reach of these libraries translate to a reduced societal
impact, and with it, the GIS research these libraries are based upon.

### summarized
However, the societal impact of these tools is often limited,
as most end users only access these libraries via indirect means: Through bindings
in other languages, through plugin in applications, or both. Additionally, the tools
end-users end up with are often not composable, and may contain other hurdles
like installation or configuration



## To summarize, the problem statement: 

End users, who are not software developers, only have indirect access to "core" GIS libraries

- Indirect access, leading to



02 Objective
================================================================

## Goal 

- The goal of this study is to allow GIS practitioners without a background in soft-
ware development, to access the full potential of core transformation and analysis
capabilities found in native GIS libraries.

- The study attempts to meet this goal by combining concepts and technologies from two domains of research. 

designing and implementing 

## Proposed Solution

The study attempts to meet this goal by studying two domains in the field of GIS,
and developing a possible solution from them. The goal of composability is ad-
dressed by using the knowledge found within the field of visual programming.
The goal of direct accessibility is met by studying the field of static web applica-
tions. To make the research goals of this study more precise, these two domains
must briefly be addressed.

## WEB (assembly) -> tackle

- To find an answer for 'direct accessibility', the web is a good place to start.
  - A web application quality: Distribution
  - can be used without installation.
  - can be used by multiple platforms
    - Windows, Mac, Linux, Ios, Android

  - STATIC web applications
    - More composable (no ties to backend) 
    - Cheap to host 

- WebAssembly

## VPL Composability 



## Objective 

The goal of this study is to make core GIS libraries more directly available and com-
posable to end-users. 
This study presents and prototypes a novel method, centered around a visual programming language to host the functionalities of GIS libraries from within an application, and in a composable manner. 
Additionally, the visual language is used to connect these libraries to a user-definable Graphical User Inter-
face (GUI). 
This prototype is implemented as a static web application, so that these libraries are directly accessible to end users without installation.  
GIS libraries are compiled to WebAssembly, making the library theoretically usable in any language, including this web based visual language by using a ’no boilerplate’ plugin system. 
Finally, both scalability to handle sizable datasets, and a rich GUI (3D viewers, file inputs,
sliders), are primary design considerations and assessment criteria.



## Research Questions

The objectives outlined above lead to the following main and supporting research
questions:

Is a web based VPL a viable method for directly accessing native GIS libraries with a
composable interface?

### Supporting Questions
- What GUI features are required to facilitate this method, and to what extent does the
web platform aid or hurt these features?

- To what extent does this method intent to address the discrepancies between software
applications and libraries, as described by Elliott (2007)? Does it succeed in doing
so?

- What are the differences between compiling a GIS library written in C++ to We-
bAssembly, compared to compiling a GIS library written in Rust?

- What measures are taken to make this VPL scalable to large geo-datasets, and how
effective are these measures?

- How does this method compare to existing, alternative VPLs and browser-based geo-
computation methods, regarding the properties relevant to the goal of direct accessibility?

03 Methodology
================================================================

## features

## aspects

### Web VPL

### Plugin system 

04 Tests 
================================================================
(show the extend to which things work)

## Compilation 

## Usage 

## Features


05 Conclusion
================================================================

## Answers

The results show that this specific web-based VPL appears to be a feasible method
for providing direct access to some native GIS libraries, and does offer a unique
set of features not found in comparable visual languages. The significance of this
method, compared to other web-based geometry VPLs, lies in the fact that it of-
fers a lenient plugin system, in combination with a range of different GUI nodes,
certain "dataflow VPL" properties, and a proposed zero-cost abstraction runtime.
All of these features combined lead to a VPL which is able to directly connect GUI
components with native GIS libraries, all while remaining scalable in principle.
On a practical level, more work remains to proof this feasibility. The methodol-
ogy developed by this study is only theoretically accessible and composable, based
on achieved features. User-testing is required to confirm if this method indeed im-
proves workflows, and actually saves time and energy of developers and end users.
Moreover, the prototypical software implementation used is limited and not pro-
duction ready. Both the fact that the ’no-boilerplate’ plugin system cannot be used
with C / C++ GIS libraries, and that backend execution is not possible yet, must
be improved upon in future work. 

## Future Work

### More Feature-complete VPL

- natively implemented, compiled to WebAssembly

### 

Despite this, visual programing, distribution
using WebAssembly, and Rust-based geocomputation, all proved to be valuable
directions of future GIS research.

Back 
================================================================

## Thank you!

## Questions?