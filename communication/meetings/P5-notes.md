P5 Corrections / Changelog
=================

I have no reference point of how much theses normally change between P4 and P5, but I think i've made relatively significant changes. This document explains what was changed where, and why.


P4 Feedback & Response
----------------------

(These are not exact quotes, I am paraphrasing)
 
- _"You 'sell yourself short' by focusing in on only the library portability aspect on the thesis. You should document the other topics of your thesis, like the GUI aspects, by choosing different main and / or supporting research questions"_

A new main research question, and completely new supporting questions have been chosen. 
I've expanded the purpose of this thesis beyond 'library portability' to something more in line with the original goal: Direct availability, and composability. 
"Direct availability" and "composability"  were specifically chosen to dodge UX / usability, and instead focus on tangible aspects. I hope the new introduction will explain this clearly.

- _"What is the 'Geo' aspect of this thesis?"_

I've introduced a sub-question to explicitly address this aspect. 
The necessities of a VPL intended for GIS are layed out at page 4.
The methodology and section 5.3 explain how these necessities have been addressed,
And the conclusion provides an answer to this new sub question.

- _"What is the exact problem you are encountering regarding C++? Why not use GDAL.js, and why did they succeed and you failed?"_

I have changed the writing in chapter 6.1 to more clearly explain what was 'missing' in the emscripten compiler. This is summarized in the answer to the third sub-research question, p 96.

- _"In your (P4) presentation, you left out the web aspect of the thesis"_

This is addressed in how the goal and problem statement are reframed.

- _"Please be more straight-forward about 'What is the problem you are trying to address', 'How are you going to address the problem' and 'What are your results'. All three of those questions should be answerable given a minute for each."_

I hope that the newly written abstract, and the fact that the problem the thesis tries to address is stated on page 1, shows that despite the reframing of the thesis, and the consequential inclusion of many additional aspects, the 'story' of the thesis is more straight-forward than it was during my P4.

- _"Try to reduce the 'essay-like' quality of the conclusion. Nuance your statements, and base these statements on data, graphs, tables, etc."_

I have added chapter 6.2 and 6.3, and changed chapter 6.1, to be able to show more concrete results.
These results are referenced by the new conclusion.
The 7.1 part of the conclusion is completely rewritten due to new sub-research questions, and I think what was written this time is less "essay-like".

Changes 
-------

### Front
- abstract: **new**

### 1 Introduction 
- 1.1 / 1.2 / 1.3 **new**: Completely rewritten
- 1.4: edit

### 2 Background
- minor edit: improved phrasing, but kept mostly the same

### 3 Related works 
- minor edit: improved phrasing, but kept mostly the same

### 4 Methodology
- **new**: Reframed the chapter to show exactly how the research questions lead into requirements, lead into the design choices of the methodology.
- edit: UML to present an overview of the proposed application.
- 4.6 edit: A more clear explanation on the plugin system.
- 4.7 edit: Added the new tests

### 5 Implementation
- 5.3: **new**

### 6 Tests 
- 6.1: edit: Improved the writing, added graphs 
- 6.2: **new**
- 6.3: **new**

### 7 Conclusion
- **new**: Answers to research questions completely rewritten, because there are new research questions.
- 7.5: edit: Future Works is now more nuanced in certain areas. 

### Back
- appendix: new: links to the repo & application







