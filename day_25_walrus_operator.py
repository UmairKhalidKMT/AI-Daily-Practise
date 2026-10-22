"""
CONCEPT DEFINITIONS:
1. Operator Overloading: Giving standard Python operators (+, -, *, ==) custom 
   behavior when used with user-defined objects by overriding magic methods 
   (e.g., __add__, __sub__).
2. Multiple Inheritance: A feature where a child class inherits attributes and 
   methods from more than one parent class.

"""

# OPERATOR OVERLOADING

class Vector:
    """Class demonstrating operator overloading using magic methods."""
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overloads the '+' operator to add two Vector objects together."""
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


print("--- Testing Operator Overloading ---")
v1 = Vector(3, 5)
v2 = Vector(1, 2)

# Using the overloaded '+' operator on custom objects
v3 = v1 + v2  # Internally calls v1.__add__(v2)
print(f"v1 + v2 = {v3}")  # Output: Vector(4, 7)


# ==============================================================================
# SECTION 2: MULTIPLE INHERITANCE
# ==============================================================================

class Employee:
    """Parent Class 1"""
    def __init__(self, name: str):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")


class Dancer:
    """Parent Class 2"""
    def __init__(self, dance_style: str):
        self.dance_style = dance_style

    def show(self):
        print(f"Dance Style: {self.dance_style}")


class DancerEmployee(Employee, Dancer):
    """Child Class inheriting from both Employee and Dancer (Multiple Inheritance)"""
    def __init__(self, name: str, dance_style: str):
        Employee.__init__(self, name)
        Dancer.__init__(self, dance_style)


print("\n--- Testing Multiple Inheritance ---")
emp_dancer = DancerEmployee("Alice", "Hip-Hop")
emp_dancer.show()  # Inherits from Employee (first in MRO - Method Resolution Order)
print(f"Name: {emp_dancer.name}, Style: {emp_dancer.dance_style}")