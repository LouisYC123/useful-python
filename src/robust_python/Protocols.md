# Protocols

In Python, a "protocol" refers to a concept or informal interface that defines a set of methods, attributes, or behaviors that a class can implement. It is not a formal construct like an interface in other programming languages, but rather a way to define a common understanding of how objects of different classes should behave when certain methods are called on them.  

Its a way of saying during type checking - this doesnt need to be a certain object, it just needs to implement a certain set of behaviours defined in the protocol.

Protocols are used to support duck typing in Python. Duck typing is a programming concept that focuses on an object's behavior rather than its type. If an object implements the methods required by a particular protocol, it can be treated as if it belongs to that protocol, regardless of its actual class or inheritance hierarchy.  

For example, a common protocol in Python is the "Iterable" protocol, which defines that an object should implement the __iter__ method to be considered iterable. If an object has this method, it can be used in a for loop or with functions that expect iterables.  

```
from typing import Protocol

class EatsBread(Protocol):
    def eat_bread(self):
        pass

def feed_bread(animal: EatsBread):
    animal.eat_bread()

class Duck:
    def eat_bread(self):
        ...

feed_bread(Duck())  # <-- OK
```  

In the above code, Duck is implicitly considered to be a subtype of EatsBread. There is no need to explicitly inherit from the protocol. Any class that implements all attributes and methods defined in the protocol (with matching signatures) is seen as a subtype of that protocol.

The typechecker will detect that an object is a protoco type just by virtue of the fields and method it has defined. This simplifies class hierarchies immensely. You don’t need a complicated tree structure, even as you add more protocols. You can simply define a different protocol for each set of required behaviors,
