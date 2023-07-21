# SOLID

## Single-Responsibility prinicple

There should never be more than one reason for a class to change. In other words, every class should have only one responsibility
Do one thing and do it well

## Open-closed principle

Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification

You can use class inheritance to extend functionality without modifying the superclass


## Liskov substitution principle

An object (such as a class) may be replaced by a sub-object (such as a class that extends the first class) without breaking the program.

You should be able to use the subclass in every scenario where you can use the parent class

In order for a subtype to exist, it must adhere to all the same properties (behaviors) as the supertype.

Subtle errors are introduced when a class inherits from a base class but does not behave exactly as that base class does.

When you’re subtyping from other types, the subtypes must preserve all invariants invariants (truths about your types that must not be violated).

Preconditions: A precondition is anything that must be true before interacting with a type’s property (such as calling a function). If the supertype defines preconditions that happen, the subtype must not be more restrictive.

If at any time you break an invariant, precondition, or postcondition in an overridden function, you are begging for an error to show up. Here are some red flags that I look for in the derived class’s overridden functions when evaluating inheritance relationships: 

- Conditionally checking arguments: A good way to know if a precondition is more restrictive is to see if there are any if statements at the beginning of the function checking the arguments being passed in. If there are, there’s a good chance they are different from the base class’s checks, typically meaning that the derived class is restricting the arguments further.  

- Early return statements: If a subtype’s function returns early (in the middle of the function block), this indicates that the latter part of the function is not going to execute. Check that latter part for any postcondition guarantees; you don’t want to omit those by returning early.  

- Throwing an exception: Subtypes should only throw exceptions that match what the supertype throws (either exactly or a derived exception type).

- Not calling super(): By definition of substitutability, the subtype must offer the same behavior as the supertype. If you aren’t calling super() as part of your subtype’s overridden functions, your subtype has no defined relationship to that behavior in code. Even if you were to copy-paste the supertype’s code into your subtype, there’s no guarantee that these will stay synchronized; a developer could make an innocuous change to the supertype’s function and not even realize that there is a subtype that needs to change as well.


Every overridden method should contain super() If you don’t call super() in an overridden method, you have no guarantee that your subclass is behaving exactly like the base class, especially if the base class changes at all in the future. If you are going to override a method, make sure you call super(). The only time you can get away with this is when the base method is empty (such as an abstract base class) and you are sure it will remain empty for the remainder of the codebase’s life cycle.


Composition is preferable to inheritance as a reuse mechanism because it is a weaker form of coupling, which is another term for dependencies between entities. If classes have high coupling between them, changes in one more directly affect the behavior of the other.

Subclasses should only be used if they are directly substitutable for their supertype. If this isn’t the case, reach for composition instead.



## Interface integration principle



## Dependency Inversion principle