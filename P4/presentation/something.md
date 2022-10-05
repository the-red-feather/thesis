<!-- 
- **Three challenges are identified** to using native library in a vpl: 
    - Firstly, **I. Compilation**:   
      -  the most viable option for using a non-js library in a web browser, is by compiling it to **WebAssembly** [Haas et al., 2017].
      - WebAssembly is a binary instruction set meant for virtual machine execution.
        - It has multiple use cases, one of which is safely executing software written in a variety of languages on the web.  
      - However, wasm compilation may pose challenges:
        - There are differences between programming languages 
          - in the level of support granted by their specific **wasm compilers**. 
          - (Novelty of the language)       
        - **Not** all code can be compiled **unconditionally**
          - (examples: no file system access, no multithreading support) 

    - Secondly, **II. Loading**:
      - In order to load system level libraries in a web VPL, one needs to: 
        - Interoperate between the language models of the compiled WebAssembly binary and Javascript.
        - Interoperate between the language models of Javascript and the Visual Language.
      - This is complicated by the fact that the WebAssembly binary can be created from different languages.   
      - Designing an interconnected binding system, in which all three languages have to be taken into account, forms the content of this second challenge  

    - Lastly **III. Utilization**: 
      - Finally, It might be the case that a web-based VPL is able to **load and run** functions from WebAssembly **compiled** libraries. 
      And yet, one might not be able to successfully **use** these libraries.
      - The challenge is to connect the language model of the web-based VPL to the models of these libraries on a software design level rather than a technical Loading level.  -->

