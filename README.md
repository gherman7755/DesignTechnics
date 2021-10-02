# DesignTechnics
## Author: Gherman Artiom
The topic of this laboratory work was to implement project with use of design patterns for the chosen domain (in this case it is restaurant).
## Theory:
In software engineering, the creational design patterns are the general solutions that deal with object creation, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or added complexity to the design. Creational design patterns solve this problem by optimizing, hiding or controlling the object creation.
Some examples of this kind of design patterns are:
- Singleton
- Builder
- Prototype
- Factory Method
- Abstract Factory
## Implementation
There was taken as a domain restaurant. So the Menu of this restaurant was implemented with help of Abstract Factory, cause of a lot of type of dishes. I also connected some modules like _abc_. This module is python built-in module for abstract methods.
So Tables was implemented with help of Prototype Pattern, cause of tables are all the same.
So Workers was implemented with help of Factory Method, because I have two classes like ordinary worker and chief of the restaurant. They both has their abstract methods.
