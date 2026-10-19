"""

CONCEPT DEFINITIONS:
1. Object Introspection: The ability to determine the type or properties of an 
   object at runtime. Python provides built-in tools to inspect methods and attributes.
2. dir(): Returns a list of all valid attributes and methods associated with an object.
3. __dict__: Returns a dictionary representation of an object's changeable attributes.
4. help(): Invokes the built-in help system to view documentation for a class, 
   module, function, or method.

"""

#   
#  OBJECT INTROSPECTION WITH dir(), __dict__, AND help()
#   

class Person:
    """A sample class representing a Person with name and age."""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


print("--- 1. Using dir() ---")
# dir() returns all attributes and methods available on an object (including dunder methods)
numbers_list = [1, 2, 3]
print(f"Sample available methods on a list (first 5): {dir(numbers_list)[:5]}")


print("\n--- 2. Using __dict__ ---")
# __dict__ stores an object's instance attributes as a key-value dictionary
p1 = Person("Alice", 28)
print(f"Object attributes dictionary (__dict__): {p1.__dict__}")


print("\n--- 3. Using help() ---")
# help() provides interactive documentation or docstrings for modules, classes, or functions
# (Uncomment below to run interactive help in terminal/VS Code console)
# help(Person)
# help(str.upper)

print("Introspection tools successfully demonstrated!")