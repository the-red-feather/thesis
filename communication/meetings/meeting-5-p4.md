Lead up to P4 hand-in: work notes: 
==========================


6 days left for handing in the P4. 





TODO
----
- [ ] Hand-in a Finished P4 draft with: 
  - [ ] an abstract 
  - [ ] sources
  - [ ] all diagrams filled
  - [ ] no comments remaining
  - [ ] 

- [ ] Fix other aspects
  - [ ] Incorporate the Rust-wasm paper
     - They frame the issue simply in terms of code portability
     


Ken Draft Comments
==================

* p.1 this effort -> what effort?
* raw data into meaningful geoinformation -> example(s)
* geocomputation -> what is the link to previous sentences?
* geoinformatics or GIS -> just choose one and make an argument based on it
* ergonomic -> it's debatable, better save it for discussion chapter
* introduce VPLs, then start with link between VPLs and geocomputation -> what do they solve?
* p.2 introduce browser-based VPLs and what they solve
* p.3 what studies?
* problem statement -> be more concise, what is exactly the problem?
* p.4 libraries? this comes too late, specify it beforehand
* support?
* first question -> you really studied it?
* I'd remove “to what extent”? it's hard to answer
* missing evaluation in questions -> performance evaluation?
* p.5 is backend geocomputation really browser-based geocomputation? I’d say no, could be used to shorten this section
* needs a better argument for usability -> technical feasibility only
* ch.2 own images? or refs needed
* not sure if all parts are necessary / useful -> not really comprehensive and also not very linked to thesis topic (2.1 intro, 2.2.1, …)
* ch.4 structure probably should be in intro?
* 4.2 not sure if it’s really studied, feels kind of improvised after the fact -> to be expanded based on what we discussed
* division between 4 and 5 is weird, 4 feels empty and 5 where the actual content is -> feels like 5 doesn’t actually implement the methodology of 4, but instead follows the actual logic of the code
* better answering questions at the end, not throughout the thesis


Stelios Draft Comments
======================

In general, I think it's going well. I think the intro is fine, although it can be improved. I like the conclusions quite a lot, tbh. You are giving proper and interesting answers to the raised questions. The rest is a bit of a very rough draft, as I see. So, some specific points:

-  It seems like you have placed several bits here and there that seem like either introduction or conclusions. I feel your enthusiasm and excitement in your writing, but I think you are bringing questions and answers in places were people would normally just expect a simple narrative of what you did and what are the results.
-  Speaking of results, we are missing the experiments so please put this at your first priority. This is because it feels like you promise things that you do not deliver.
-  In general, you are using some very bold statements and informal expressions. The latter is kinda okay, but the first one is very dangerous. I've noticed words like "crucial", "by far" or "impressive" which seem very biased and subjective, so better be avoided. You can still use them here and there (mostly in the conclusions), but I think you use them way  too much (again, I can see your enthusiasm).
-  Where you describe the implementation I made a comment about you mentioning git(hub) too much. Imo, git(hub) is just the place where you store the code, but the structure of your code and everything around the implementation is only independent from the version control system that you use. We normally just leave a sentence about this, stating that the code is available as open source in a repository. But because you have the organization and the multiple repos, maybe you can have a small paragraph about that summarizing this. But don't mix this with the actual discussion about implementation.
-  Minor thing, but I think you have confused \citet with \citep. The first one is used when the citation is part of the sentence and the latter when it's at the end of a sentence (or in a parenthesis, anyway).






