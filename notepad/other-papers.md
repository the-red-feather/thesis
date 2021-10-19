# Karin

|||
|---|---|
| What / Subject    | MongoDB, PostgreSQL and GraphQL for cityjson              |
| Why / Use Case    | 
| Question          | **How suitable** are **mongodb & postgresQL** for **the storage and querying** of **cityJSON** using **GraphQL**?.
| Question 2        | **What are the differences** between **the storage of CityJSON in PostgreSQL** and **the storage of CityGMLin PostgreSQL with 3DCityDB?** |
| How / Methodology | - Modelling & Implementing relational schema | 
| How / Experiments |

> To me, this thesis truly looks like a 'study on implementation': 'how can we put cityjson's in a database in the most performant, usable way possible?' Lots of implementation details, impact of formulation of queries, impact of different models, impact of different databases, etc. 
 
> overall: I will be checking this thesis some more in the future, once i need to figure out how to describe things like 'workflow' in a format which is professionally presentable.

<br/><br/><br/>

# Linda van den brink

|||
|---|---|
| What / Subject    | PHD : geodata on the web
| Why / Use Case    | FAIR principles remain (partially) unadressed in geospatial data on the web + The Geospatial community is too isolated from the general web community > [JF] I'm paraphrasing, but this is the general sense im picking up from the intro & conclusion & future work. 
| Problem 1         | Lack of standard hinders reuse of geospatial data:  example: of 3D data
| Problem 2         | Independently  developed  domain  models  model  similarconcepts in di erent ways, which makes reuse of data in other domains dicult > basically, semantic jargon obfuscates interoperability 
| Problem 3         | **Geospatial data disseminated via SDI methods cannot befound, accessed and used by non-geospatial experts** > [JF] Very relevant to me
| Problem 4         | Geospatial data disseminated with linked data technolo-gies are not easy to use by users who are not linked data experts. > [JF] Partially relevant to me
| Question          | How  to  reuse  geospatial  data,  from  different,  heterogeneous  sources, via the web across communities?




# Ravi Peters' Msc Thesis

> Ravi's thesis heeft een heel duidelijk ankerpunt: de "four hydrographic generalization constraints". Hiermee kan hij zijn eigen werk en andermans werk beoordelen. Vind zo'n zelfde ankerpunt






> [JF] FAIR: findability, **accessibility**, interoperability, reusability

> [JF] quite a broad topic

> [JF] geojson is related to this research: updating xml encodings to the 21st century & making it 'fit' better with the current state of the web. 

> [QUOTE] Decades of work and a large, international standardization effort have resulted in a lot of geospatial data now being available for reuse on the web.  However, because the semantics, formats, and dissemination methods used are still very specific to the geospatial domain, a lot of this data is only findable  and  usable  by  geospatial  ICT  experts.   And  yet,  there  is  a  huge potential  for  the  use  of  geospatial  data  in  other  domains.   To  achieve  the wide reuse of geospatial data, i.e.  beyond the geospatial domain, data users need to be able to  find, access, and use geospatial data on the web without expert knowledge of geospatial standards.  Geospatial data needs to become a common part of the web of data.


> ... When published in accordance to the best practices, is spatial data actually indexed by search engines?  And are web data users actually able to  find,  access,  and use the data more easily,when  compared  to  spatial  data  only  available  through  an  OGC-standards compliant SDI?

> If this is the case, this will open up new ways for the reuse of geospatial data via the web across communities.  While the geospatial web of data is growing, new technological developments will create unforeseen possibilities for its use.  One such development is the availability of ever greater bandwith(5G) combined with more effcient handling of heavy data loads and tasks in web browsers.  New standards such as **WebAssembly** (Rossberg, 2018) will support this. Thus it will, for example, become possible in the near future to work with voluminous, 3D geospatial data natively in a browser | perhaps supported by CityJSON. Augmented and virtual reality applications, using 3D and other geospatial data, will be implemented in web browsers.

> overall: very nice paper! I truly agree with most of her statements, and in the introduction of this wasm thesis, I will be refering to this. I think this wasm thesis can be considered part of her 'future fork'.




<br/><br/><br/>

# Ken Stelios Jantien

(TODO)





<br/><br/><br/>

# Relating to this Thesis: 


## Possible Usecases 
--------------------

- Enables Clientside geometry (post) processing.
- Client & Server Interoperability: use the exact same data models & processes: less conversions. 





## Possible Questions
---------------------

**What are the differences** between **wasm-based geoprocessing on the web** and **'normal' geoprocessing locally** both using **[some library]**.

> [JF] I kind of like 'what are the differences' questions for a thesis like mine. 

**How Suitable** is ...

> [JF] I think a question starting with 'how suitable' doesn't lead to strong answers. A comparison is much more interesting.





## Possible Methodologies
-------------------------

- Create the software proposed 
- Make it comparable to other software packages





## Possible Experiments
-----------------------

- Benchmarks -> so we can say something about speed & consistency
- User Testing -> so we can say something concrete about 'how accessible it is to use'
  - lets not do this 


