
# Q: waarom geoflow?

A: 
- gedurende phd
- altijd wel een ketting van stapjes
- validatie was altijd lastig
- tussenproduct bestanden schrijven, een voor een inladen in QGIS
- vooal met 3d : visueel checken ongelovelijk belangrijk, Test Driven Development is niet genoeg

- 3d geodata heeft ook een complexe nature. een klein foutje vroeg in de pipeline kan hele kettingreactie aan artefacten met zich meebregen.

- interactief
- snel
- experiemntel 



# Eerste ontwerp

- python + graphic library

- maar:
  - peformance 
  - C++ is gewoon veel sneller 
  
- langzame delen zijn algoritmes zelf 




# 3d bag : geoflow 

- 2 modi:
  - als visuele programmeer tool
  - als compiled C++ command line

  Het is ongelovelijk belangrijk dat de hele flowchart gecompiled kan worden in beide een json, èn een 

- slim systeem voor alle parameters. 



- hoe werkt een loop 



- alles wordt in een json gecompiled

nest nodes

# types 

uitdaging: logica afhankelijk maken van types
- types zijn weggefiltered 
- eigen type system
- type abstractie

- generics: lijst met blobs 
  - nodes die niks weten van de types
- 


# visuals 

- eigen functies zijn nodig voor convertion en visuals


- dropdown lijstje 
- vertaal functies




# isues 
- hoe definieer je die terminals
  - negeer enkeltjes  
  - oplossing: altijd een lijst


- polygons + attributes
  - attributes have types 
- dictionary: key: naam van attr: value: standaard lijst. 

- welk niveau L 



# Rust
- wel nice, maar geen libs


- simpel mogelijk houden 





# plugin 
- 