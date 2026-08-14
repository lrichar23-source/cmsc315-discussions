"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    # Class variable (shared across all instances)
    category = "Vehicle"

    def __init__(self, make, model):
        self.make = make      # instance variable
        self.model = model    # instance variable

    def display_info(self):
        return f"{self.category}: {self.make} {self.model}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    # New class variable
    wheels = 4

    def __init__(self, make, model, color, features=None):
        super().__init__(make, model)
        self.color = color                                  # new instance variable
        self.features = features if features is not None else []  # new instance variable (nested mutable)

    # New method
    def add_feature(self, feature):
        self.features.append(feature)
        return f"Added {feature} to {self.model}"

    # Override parent method
    def display_info(self):
        return (f"{self.category}: {self.color} {self.make} {self.model} "
                f"with {self.wheels} wheels, features: {self.features}")



# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two child objects
    car1 = ChildClass("Toyota", "Corolla", "red")
    car2 = ChildClass("Honda", "Civic", "blue")

    # Access class variable through the class
    print("Class variable via class:", ChildClass.category)

    # Access the same class variable through an object
    print("Class variable via object:", car1.category)

    # Add a new attribute to only one object
    car1.year = 2024
    print("Added 'year' attribute to car1 only")

    # Display each object's namespace
    print("car1 __dict__:", car1.__dict__)
    print("car2 __dict__:", car2.__dict__)

    # Display class namespace
    print("ChildClass namespace keys:", list(ChildClass.__dict__.keys()))

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Object with nested mutable data (the features list)
    original = ChildClass("Ford", "Mustang", "black", ["GPS", "Sunroof"])

    # Shallow copy: copies the object but shares the nested list reference
    shallow = copy(original)

    # Deep copy: recursively copies everything, including the nested list
    deep = deepcopy(original)

    # Modify the original object's nested data
    original.features.append("Heated Seats")

    print("Original features:", original.features)
    # Shallow copy reflects the change because it shares the same list
    print("Shallow copy features:", shallow.features)
    # Deep copy is unaffected because it has its own independent list
    print("Deep copy features:", deep.features)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Parent object
    parent = ParentClass("Generic", "BaseModel")
    print("\nParent object:")
    print(parent.display_info())

    # Child object
    child = ChildClass("Tesla", "Model 3", "white")
    print("\nChild object:")
    print(child.display_info())
    print(child.add_feature("Autopilot"))
    print(child.display_info())

    # Inheritance check
    print("\nIs child a ParentClass?", isinstance(child, ParentClass))

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()