**Unit 1: Object-Oriented Programming in Python**

**Overview**

This project explores core object-oriented programming (OOP) concepts in Python through a hands-on implementation. 
Using a vehicle-themed class hierarchy, it demonstrates how inheritance, namespaces, and object copying work in practice. 
The goal was to show not just how to write OOP code, but why these concepts matter for building maintainable and reusable software.
The program is organized into a parent class, a child class that extends it, and two demonstration functions 
that illustrate Python's namespace model and the distinction between shallow and deep copying.

**Implementation Summary**

ParentClass — A base Vehicle class containing one class variable (category), two instance variables (make, model), 
a constructor, and a display_info() method that returns a formatted description of the object.
ChildClass — Inherits from ParentClass and extends it with a new class variable (wheels), two new instance variables 
(color and a nested mutable features list), a new add_feature() method, and an overridden display_info() method that 
incorporates the additional attributes. demonstrate_namespaces() — Creates two child objects and shows the difference 
between class and instance namespaces. It accesses a class variable through both the class and an instance, 
adds an attribute to a single object, and prints each object's __dict__ alongside the class namespace to 
make the distinction visible.
demonstrate_copying() — Builds an object with nested mutable data, then creates a shallow copy and a deep copy. 
By modifying the original's nested list and printing all three objects, it shows that the shallow copy shares the nested 
reference while the deep copy remains fully independent.
main() — Instantiates parent and child objects, calls their methods to demonstrate inheritance and method overriding, 
verifies the inheritance relationship with isinstance(), and runs both demonstration functions.

**Reflection:**

This assignment reinforced how inheritance lets a child class extend a parent's behavior without duplicating it — 
Router reused NetworkDevice's constructor via super().init__() while adding its own attributes and overriding display_info(). 
Working through namespaces clarified a subtlety I hadn't internalized: class variables live in one shared space, but instance 
variables get their own entry in each object's dict the moment they're set. My main challenge was the shallow vs. deep copy 
demonstration — my first instinct was that copy() would fully duplicate an object, and I had to trace through the nested list 
manually to see why the shallow copy's networks attribute still reflected changes made to the original.
Compared to procedural programming, where data and functions are separate and passed around explicitly, OOP bundles state and 
behavior together, which makes relationships between components more explicit. The practical payoff is maintainability: 
fixing or extending shared behavior in one parent class propagates everywhere it's inherited, instead of requiring changes in 
a dozen scattered functions. That reduces long-term overhead and makes the codebase easier to extend as requirements grow.