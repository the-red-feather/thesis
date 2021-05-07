# IDEA 
Geon, stands for GEOometry Nodes. FME on the web. 
Flowcharts are sharable using nothing but a link a la: `https://geon-flow.com/share/((hash))`;


## USE CASE  
A very user friendly way of doing `cjio` -level of operations.
- users load a `cityjson` by giving the link
- this city is then visible a la `ninja`, but not directly editable like `ninja`.
- users perform basic operations on this city, like a sub selection.
- users can perform advanced operations, like selecting using a polygon
- users can see what this results in. 
- users can then download the result. 


## SETUP : 3 related repositories

  - **geon-core**
    - rust crate
    - core geometry library, with `Vector3`, ` Matrix4`, `Mesh`. and others.
      - native `cityjson` support, like `cjio`.
      - support for `georust` crates (crs translations, gdal functions).


  - **geon-web**
    - rust crate ( / typescript package ? )
    - purpose: using geon-core in real-time on the web. 
      - meaning: change a parameter, immediately see results.
      - make results available for download

    - **Can directly be used to write (web) applications**
    - Support for rendering, user input, and file IO.
    - basic DOM.api abstractions
    

  - **geon-flow**
    - web-application
    - visual programming language, exposing the functionalities of **geon-core** & **geon-web**.

    - exports to:
      - a link, giving you this exact flowchart
      - a geon-run application. 

    - *geon-flow itself is written as a geon-web application*