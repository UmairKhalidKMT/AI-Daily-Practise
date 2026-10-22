"""

CONCEPT DEFINITIONS:
1. Magic / Dunder Methods: Special built-in methods in Python surrounded by double 
   underscores (e.g., __init__, __str__, __repr__, __len__, __call__).
2. Purpose: They allow user-defined classes to integrate seamlessly with Python's 
   built-in functions and syntax (like len(), print(), or direct object calling).
"""

class Employee:
    """Class demonstrating Magic (Dunder) Methods in Python."""
    
    def __init__(self, name: str, salary: int, position: str):
        self.name = name
        self.salary = salary
        self.position = position

    def __str__(self):
        """Returns a user-friendly string representation of the object (used by print())."""
        return f"Employee: {self.name} ({self.position})"

    def __repr__(self):
        """Returns an official, developer-friendly string representation to recreate the object."""
        return f"Employee('{self.name}', {self.salary}, '{self.position}')"

    def __len__(self):
        """Customizes the behavior of the built-in len() function based on name length."""
        return len(self.name)

    def __call__(self):
        """Allows an instance of the class to be called directly like a function!"""
        print(f"Hey! {self.name} has been called directly as a function.")


# DEMONSTRATION IN VS CODE

if __name__ == "__main__":
    emp = Employee("Harry", 85000, "Instructor")

    # 1. __str__ in action (triggered by print() or str())
    print("--- 1. __str__ Output ---")
    print(emp)  # Output: Employee: Harry (Instructor)

    # 2. __repr__ in action (triggered in interactive shell or repr())
    print("\n--- 2. __repr__ Output ---")
    print(repr(emp))  # Output: Employee('Harry', 85000, 'Instructor')

    # 3. __len__ in action (triggered by len())
    print("\n--- 3. __len__ Output ---")
    print(f"Length of employee name (len): {len(emp)}")  # Output: 5

    # 4. __call__ in action (invoking the object instance as a function)
    print("\n--- 4. __call__ Output ---")
    emp()  # Output: Hey! Harry has been called directly as a function.


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