# Existing libraries 
_This document contains preliminary research into the existing geospatial libraries rust has to offer. _

## Note
- Rust's name for an external library is `crate`.
- Rust uses `https://crates.io` to host these crates.
- we will only look for libraries published on crates.io. 
  - It makes sense to do so. if it is on crates.io, we can ensure the library is properly open source. If a library exists, but it is not properly open source, then it should be disregarded.


# searches:

## 




## Using: `geometry`:
_(https://crates.io/search?page=2&q=geometry&sort=recent-downloads)_

| Link | Crate | Number of downloads | Last Update (as of 2021-04-29) | What
|---   |---    | ---:                | ---                            | ---
|https://crates.io/crates/euclid|       euclid      | 1.5m 
|https://crates.io/crates/ncollide3d|   ncollide3d  | 120k
|https://crates.io/crates/kurbo|        kurbo       | 250k | 1 month ago| 2D curves 
|https://crates.io/crates/piet|         piet        |  | 
|https://crates.io/crates/kdtree|       kdtree      | 

<br/><br/>

## Using `gis` and `geo`:
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

...

Aha, most of these are created in one ecosystem: GeoRust. Jackpot!

## georust: https://github.com/georust / https://georust.org/
https://lib.rs/crates/geo



## bindings & early projects
- https://github.com/georust/gdal <!-- Promising! -->
- https://github.com/georust/proj
- https://github.com/georust/rstar
- https://github.com/georust/geocoding



# Conclusion

There are libraries for most 'normal' geodata business. 

- Little to no support for 3D. 