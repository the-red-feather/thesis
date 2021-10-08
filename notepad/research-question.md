<!-- Create research questions that result in the desired answers:

"How can someone one do this?" is answered by showing how this was implemented


 -->

## testable hypotheses

**RESEARCH QUESTION:**

**How well does WebAssembly support a client-side geoprocessing vpl?**

1. **GEO-WEB-VPL**: How to make a web-based, client-side, vpl geoprocessing environment?
    - 1a. **GEO**: What basic features does a geoprocessing environment need?
      - *answer: MOSKOW*
    - 1b. **WEB**: What options and limitations does a HTML5, CSS & JS based environment give us?
      - *answer: Canvas, HTML as ui, webgl*
    - 1c. **VPL**: What are the advantages and disadvantages of using a vpl?
      - *answer from the vpl papers* 

2. **GEO-WASM**: How well can C++ geoprocessing libraries such as CGAL & 3dfier be used within a web browser without needing to be installed, by using WebAssembly?
    - 2a: How well do WebAssembly compiled geoprocessing (geo-wasm) libraries perform compared to native, cli usage?
    - 2b: How to handle types / data models between multiple, unrelated `wasm` libraries?
    - 2c: How do C++ geoprocessing libraries differ from all other C++ libraries?
    - 2d: What does this difference mean for `wasm` compilation and usage? 

3. **GEO-WEB-VPL + GEO_WASM**: How well can geo-wasm libs be used within the context of a geo-web-vpl?
    - 3a: What data must a geo-wasm provide in order to become usable within a geo-web-vpl?
      - *answer: descriptors of operations and variables, how many inputs and outputs, etc.*
    - 3b: How can this data be utilized by the geo-web-vpl? 
      - "
    - 3c: How are the geo-wasm libraries distributed?
      - *answer: web service like npm or pip? Something like an app store?*
    


  - How to design a `wasm` plugin ecosystem?
    - Marketplace Website ?
    - Npm ?  

  - 


<!-- 
- A web-based geo-vpl equipped with these libraries will be more \emph{Usable} for the given case study than a conventional method using Python
    - Right, the web-geo-vpl scores better on all FAIR usability criteria.
    - Half right, it scores better on some of the FAIR criteria.
    - wrong, this way of working scores worse on all FAIR criteria. -->
