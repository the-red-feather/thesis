# WebAssembly
|||
|---|---|
| name | Jos Feenstra |
| email | me@josfeenstra.nl |
| date | 2021-05-07 - Friday |
| purpose | Notes on webassembly related talks 

# 1

_Guy Royse from Redis Labs_
_https://www.youtube.com/watch?v=3sU557ZKjUs_


## notes 
- Very nice general introduction to wasm in general
- Guy Royse: WebAssembly works out of the box with rust, and is considered to have better support because of this 
- wasm doesn't know what a string is -> needs a lot of bindings 
- wasm cant talk directly to the DOM
- 


# 2 

_Rust, WebAssembly, and the future of Serverless by Steve Klabnik_
_https://www.youtube.com/watch?v=CMB6AlE1QuI&t=1732s_

## notes 
- Browsers & Docker & Cloud computing become the same thing with wasm. 
- Write once, run anywhere
  -> old slogan for Java, now becomes true of wasm
  -> write once, run **everywhere** -> deploy your code in 1000x servers, parallel computing
  -> analogue to SDI: "Collect once, use multiple times"


# 3 

_Michael Yuan — Tensorflow inference on WebAssembly_

_https://www.youtube.com/watch?v=poe0Z7GR8uI_


## notes
- clearly states the advantages of something like wasm, and the philosophy behind it.
- shows webassembly benefits to advanced computation use cases like machine learning. 


### from the slides: 

- WebAssembly
  - high performance
  - sandbox safety
  - capability-based security 
  - language-agnostic
  - product-community fit
  
  - Better than native apps, because native apps ...
    - are not portable (Tied to specific OS or hardware platforms)
    - cannot be integrated into web or application frameworks 
    - cannot be managed or orchestrated
    - crashes from bugs & attacks 
    - unsafe: coursely grained, OS-level access control

  - Better than python, beause python ...
    - 60.000x slower than C 
    - does not run on edge devices and platforms
    - limited support in web & application frameworks




