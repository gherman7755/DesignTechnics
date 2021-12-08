# DesignTechnics
## Author: Gherman Artiom
The topic of this laboratory work was to implement project with use of design patterns for the chosen domain (in this case it is restaurant).
## Theory for lab 1:
In software engineering, the creational design patterns are the general solutions that deal with object creation, trying to create objects in a manner suitable to the situation. The basic form of object creation could result in design problems or added complexity to the design. Creational design patterns solve this problem by optimizing, hiding or controlling the object creation.
Some examples of this kind of design patterns are:
- Singleton
- Builder
- Prototype
- Factory Method
- Abstract Factory
## Theory for lab 2:
In software engineering, the Structural Design Patterns are concerned with how classes and objects are composed to form larger structures. Structural class patterns use inheritance to create a hierarchy of classes/abstractions, but the structural object patterns use composition which is generally a more flexible alternative to inheritance.
- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

## Theory for lab 3:
In software engineering, behavioral design patterns have the purpose of identifying common communication patterns between different software entities. By doing so, these patterns increase flexibility in carrying out this communication. Some examples from this category of design patterns are :
- Chain of Responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Observer
- Strategy

## Implementation
#### Lab 1
There was taken as a domain restaurant. So the Menu of this restaurant was implemented with help of Abstract Factory, cause of a lot of type of dishes. I also connected some modules like _abc_. This module is python built-in module for abstract methods.
So Tables was implemented with help of Prototype Pattern, cause of tables are all the same.
So Workers was implemented with help of Factory Method, because I have two classes like ordinary worker and chief of the restaurant. They both has their abstract methods.
#### Lab 2
In this laboratory work I used three Structural Design Patterns:
- Adapter
- Facade
- Proxy
##### Adapter
```Cheque.py``` in controllers is my Adapter. It has three classes. First class ```Service```, this class is the Parent class
for others classes. It uses to be like target class that calls interface.

The next class is ```Cheque```. This class is usual class without any special features.
It has his method that returns all information about taken order and cheque.
For client there is no needs to see all the information from order, so here
appears Adapter.

The next class is ```ParsedCheque```. This class makes output more clear and 
friendly for client. It has inherited method request which helps it to
edit output.

And there is ```client_request``` function that receive as an argument
target with class ```Service```. This was done to demonstrate that user
can actually work with this class.

##### Facade
```Delivery.py``` is my Facade. I have as usual three classes.
First class is ```OnlineOrder```. This class is my Facade.
It makes all the work for client, while client only give 
to this class some information. This class takes as arguments ```Kitchen```
and ```Tranport``` classes to work with them after that. The ```make_order``` method
just does some operations that client doesn't have to see.

Classes ```Kitchen``` and ```Transport``` just simulate that they are working,
but actually they only prints some info.

Function ```client_order``` just starts main method ```make_order```
in ```OnlineOrder``` class. As you can see there is no needs for client to write
all functions from ```Kitchen``` and ```Transport``` classes.
He has only to write ordered food and his address.

##### Proxy
Finally, ```DataBase.py``` is my Proxy. As usual, I have three classes.
First class is ```General```, thanks to this class the information can be
protected from unauthorised access. 

```DataBase``` class contains information about cookers. This information
can be output with method ```request```. And as you can see it inherits
```General``` class.

```Check``` is my Proxy. When it is initialized, it takes as arguments ```DataBase``` instance, login and
password for authorised access. The method ```request``` accepts or deny access to ```DataBase```. From here
it calls method ```check_access```. This method checks if client has rights to enter in
```DataBase```.

And there is ```client_access``` that requests information from ```DataBase```.
Cause of Proxy we can now instead of giving ```DataBase```, we give client ```Check``` that checks if
client has rights to access it.

#### Lab 3
In this laboratory work I implemented Observer. This is a behavioral pattern that allows objects to notify other objects about changes in their state. In my project Observer is `Subscirber`, those who subscribed for some notifications from my restaurant. Publisher is `RestaurantJournal` class that notify about some changes about restaurant, subcribes and unsubscribes people and change state of the all restaurant. `Subscriber` is an interface. Class `WantsToVisit` notify only those people who wants to know if restaurant is `Opened`, has `Free Food` or has `Event`. Class `Other` notify only those people who wants to know about closing and repairing restaurant.  
