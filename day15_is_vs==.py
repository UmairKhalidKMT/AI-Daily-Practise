"""

CONCEPT DEFINITIONS:
1. 'is' vs '==':
   - '==' (Equality Operator): Compares the VALUES of two objects to check if 
     their content is identical.
   - 'is' (Identity Operator): Compares the MEMORY ADDRESSES (identity/location) 
     of two objects to check if they point to the exact same object in RAM.
2. Class: A blueprint/template for creating user-defined objects.
3. Object (Instance): An individual instantiation of a class containing real data.
4. Instance Attributes: Variables tied to specific instances of a class.
5. 'self' Parameter: Represents the current instance of the class, enabling access 
   to its variables and methods.

"""

# 'is' VS '==' OPERATORS

# Case 1: Mutable Objects (Lists)
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a  # Direct reference copy

print("--- Mutable Objects (Lists) ---")
print(f"list_a == list_b: {list_a == list_b}")  # True -> Values match
print(f"list_a is list_b: {list_a is list_b}")  # False -> Different memory addresses
print(f"list_a is list_c: {list_a is list_c}")  # True -> Points to identical object

# Case 2: Immutable Objects & Python Interning (Strings/Integers)
# Python optimizes memory by reusing immutable objects for small numbers and strings
x = 5
y = 5
str1 = "hello"
str2 = "hello"

print("\n--- Immutable Objects (Integers & Strings) ---")
print(f"x is y: {x is y}")            # True -> Python reuses integer objects
print(f"str1 is str2: {str1 is str2}")  # True -> String interning reuses memory address


#  CLASSES, OBJECTS, AND METHODS

class Person:
    """Class blueprint defining attributes and methods for a Person."""
    
    # Class attributes (shared across all instances)
    species = "Homo sapiens"

    # Methods inside a class must take 'self' as their first argument
    def display_info(self):
        """Method to display details of the individual person object."""
        print(f"Name: {self.name}, Occupation: {self.occupation}, Age: {self.age}")


# Creating Instances (Objects) of the Person class
person1 = Person()
person1.name = "Harry"
person1.occupation = "Software Developer"
person1.age = 28

person2 = Person()
person2.name = "Rohan"
person2.occupation = "Data Analyst"
person2.age = 25

print("\n--- Displaying Object Properties ---")
# Calling instance methods
person1.display_info()  # Equivalent to Person.display_info(person1)
person2.display_info()  # Equivalent to Person.display_info(person2)


# Checking Identity with Custom Class Objects
person3 = person1

print("\n--- Object Identity Checks ---")
print(f"person1 == person2: {person1 == person2}")  # False -> Different values/objects
print(f"person1 is person2: {person1 is person2}")  # False -> Different memory locations
print(f"person1 is person3: {person1 is person3}")  # True -> Both point to same instance