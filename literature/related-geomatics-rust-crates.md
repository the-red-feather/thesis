# Existing libraries 
|||
|---|---|
| name | Jos Feenstra |
| email | me@josfeenstra.nl |
| date | 2021-04-30 - friday |
| purpose | Preliminary research into the existing geospatial libraries rust has to offer. |

<br/>


## Note
- Rust's name for an external library is `crate`.
- Rust uses `https://crates.io` to host these crates.
- we will only look for libraries published on crates.io. 

<br/>

# searches:

## 1. Using: `geometry`:
_(https://crates.io/search?page=2&q=geometry&sort=recent-downloads)_

| Link | Crate | Number of downloads | Last Update (as of 2021-04-29) | What
|---   |---    | ---:                | ---                            | ---
|https://crates.io/crates/euclid|       euclid      | 1.5m | - | -
|https://crates.io/crates/ncollide3d|   ncollide3d  | 120k | - | -
|https://crates.io/crates/kurbo|        kurbo       | 250k | 1 month ago| 2D curves 
|https://crates.io/crates/piet|         piet        |  - | - | -  
|https://crates.io/crates/kdtree|       kdtree      |  - | - | -

<br/><br/>

## 2. Using `gis` and `geo`:
_(https://crates.io/search?page=2&q=gis&sort=recent-downloads)_


|Link   | Crate  |Number of downloads|Last Update (as of 2021-04-29) | What
|---     |--- | ---: | --- | ---
|https://crates.io/crates/geo               |geo                | 408k | 10 days ago | Geospatial Primitives, Algorithms, and Utilities   
|https://crates.io/crates/geo-types         |geo-types          | 311k | - | Geospatial Primitives (subcomponent of geo)
|https://crates.io/crates/geojson           |geojson            | 288k | 10 days ago | Wrappers around the geo-json format (included in geo)
|https://crates.io/crates/geohash           |geohash            | 100k | 3 months ago | https://en.wikipedia.org/wiki/Geohash (included in geo (I think))
|https://crates.io/crates/geographiclib-rs  |geographiclib-rs   |  87k | 12 months ago | A subset of geographiclib implemented in Rust.
|https://crates.io/crates/postgis           |postgis            |  10k | 3 months ago | An extension to rust-postgres, adds support for PostGIS.

<br/><br/>

These are the most used packages. Geo contains the usual suspects like `Point` and `LineString`.


Most of these are created in one ecosystem: GeoRust. Jackpot!

### georust
- https://github.com/georust
- https://georust.org/


### bindings & early projects
- https://lib.rs/crates/geo
- https://github.com/georust/gdal <!-- Promising! -->
- https://github.com/georust/proj
- https://github.com/georust/rstar
- https://github.com/georust/geocoding


<br/><br/>

## 3. Others notable crates

| Link | Crate | Number of downloads | Last Update (as of 2021-04-29) | What
|---   |---    | ---:                | ---                            | ---
| https://crates.io/crates/bevy | bevy | 40k | 1 month ago | a data-driven game engine, with wasm, 3d rendering, and gui support. 
| https://crates.io/crates/wgpu | wgpu | 330k | 8 days ago | idiomatic Rust wrapper over wgpu-core. It's designed to be suitable for general purpose graphics and computation needs of Rust community.
| https://crates.io/crates/lyon | lyon | 330K | 3 months ago | tesselation engine


<br/>

There are many more rust projects dealing with 3d engines, and rendering, but most of them are not focussed on webgl, webgpu, and/or WASM. 

<br/><br/>

## 4. Very Young crates but still promising

https://github.com/nannou-org/nannou
https://github.com/fintelia/terra
https://github.com/Yatekii/sailor

<br/><br/>

# Conclusion

There are libraries for most 'normal' geodata business, mostly centered around one ecosystem: georust. There is support for 3d rendering, but this is not tied yet to geodata capabilities. A project which merges these two worlds is something new. 