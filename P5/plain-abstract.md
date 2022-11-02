In the field of Geographical Information Science (GIS), geodata transformation and analysis tools often take the shape of software libraries written in system level programming languages. 
However, the societal impact of these tools is often limited, as most end users only access these libraries via indirect means: Through bindings in other languages, through plugin in applications, or both. 
Additionally, the tools end users end up with are often not composable, and may contain other hurdles like installation or configuration.

The goal of this study is to make core GIS libraries more directly available and composable to end users. 
This study presents and prototypes a novel method, centered around a visual programming language to host the functionalities of GIS libraries from within an application, and in a composable manner. 
Additionally, the visual language is used to connect these libraries to a user-definable Graphical User Interface (GUI). 
This prototype is implemented as a static web application, so that these libraries are directly accessible to end users without installation. 
GIS libraries are compiled to WebAssembly, making the library usable in any language, including
this web based visual language by using a ’no boilerplate’ plugin system. 
Finally, both scalability to handle sizable datasets, and a rich GUI (3D viewers, file inputs, sliders), are primary design considerations and assessment criteria.

The results show that this specific web based VPL appears to be a feasible method for providing direct access to some native GIS libraries, and does offer a unique set of features not found in comparable visual languages. 
The significance of this method, compared to other web based geometry VPLs, lies in the fact that it offers a lenient plugin system, in combination with a range of different GUI nodes, certain "dataflow VPL" properties, and a proposed zero cost abstraction runtime.
All of these features combined lead to a VPL which is able to directly connect GUI components with native GIS libraries, all while remaining scalable in principle.

On a practical level, more work remains to proof this feasibility. 
The methodology developed by this study is only theoretically accessible and composable, based on achieved features. 
User testing is required to confirm if this method indeed improves workflows, and actually saves time and energy of developers and end users.
Moreover, the prototypical software implementation used is limited and not production ready. Both the fact that the ’no boilerplate’ plugin system cannot be used with C / C++ GIS libraries, and that backend execution is not possible yet, must be improved upon in future work. 
Despite this, visual programing, distribution using WebAssembly, and Rust based geocomputation, all proved to be valuable directions of future GIS research.