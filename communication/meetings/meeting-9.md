# meeting 9
|          |                         |
| -------- | ----------------------- |
| date     | 2021-11-02 - Tuesday
| present  | Stelios, Jos
| Location | Cyberspace

## Things that happened since the last meeting:
- Completely rewritten introduction
- Found more relevant papers
  - Read introductions & conclusions of each
  - Added my comments & why it is relevant to the P2 prototype
- Meet up with Ravi
  - Talked about "geodata processing user experience" & the case for a geodata vpl
  - Ravi explained his design decisions while making it
  - Talked about the properties a geodata vpl should have, like being able to run GUI-less
- Internship
  - created a linalg library 😅
  - Implemented least squares circle, and some interesting heuristics



## Notes during the meeting


**Thin-client vs Thick Client**
  - The part where thin-client side is mentioned needs some work:
  - The case for a thick client is important. If this is not well-made, the whole thesis starts crumbling down
  - **Be Honest**
    - Combination of down & upsides 
  - "in certain applications"
  - Some parts are too technical
    - push the narrative closer to the user, rather than the technology 
  - Thick-client has many more **advantages**: 
    - The Scale / size of a geo-app: thick clients enable larger geo-apps
    - Better Privacy 
    - Less Storage needed
    - No connections have to be made and maintained, no session tokens, no advanced servers.

  - All in all: major advantage is a thick client means a more lean server design. 
    - This means less complexity and maintenance on the side of the server, driving down costs.
    - Not useful for all geodata applications, but it will be useful for certain scenarios.

  - Exploratory is another advantage


**Methodology**
  - Benchmark
  - Make promises 
  - Software requirements
  - It should show what to expect at P4  
  - Plan
  - Scope