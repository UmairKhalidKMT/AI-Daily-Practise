"""
================================================================================
CONCEPT DEFINITIONS:
1. Operator Overloading: The ability to extend Python's operators (+, -, *, ==, etc.) 
   to work with user-defined objects by defining corresponding magic methods 
   (e.g., __add__ for +, __sub__ for -, __mul__ for *).
================================================================================
"""

class Number:
    """Class demonstrating operator overloading."""
    
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        """Overloads the '+' operator."""
        return Number(self.value + other.value)

    def __sub__(self, other):
        """Overloads the '-' operator."""
        return Number(self.value - other.value)

    def __str__(self):
        return f"Number({self.value})"


print("--- Testing Operator Overloading ---")
num1 = Number(50)
num2 = Number(30)

# Using overloaded operators
added_result = num1 + num2  # Calls num1.__add__(num2)
sub_result = num1 - num2    # Calls num1.__sub__(num2)

print(f"num1 + num2 = {added_result}")  # Output: Number(80)
print(f"num1 - num2 = {sub_result}")    # Output: Number(20)

"""
================================================================================
CONCEPT DEFINITIONS:
1. Method Overriding: A feature in Object-Oriented Programming where a child class 
   provides a specific implementation of a method that is already defined in its parent class.
2. super() Keyword: A built-in function that allows child class methods to reference 
   and invoke methods and constructors defined in the parent class.
================================================================================
"""

# ==============================================================================
# SECTION 1: METHOD OVERRIDING & THE super() KEYWORD
# ==============================================================================

class Employee:
    """Parent (Base) Class"""
    def __init__(self, name: str, emp_id: int):
        self.name = name
        self.emp_id = emp_id

    def get_role_description(self):
        """Base method for general employees."""
        return f"General Employee: {self.name} (ID: {self.emp_id})"


class Manager(Employee):
    """Child (Derived) Class inheriting from Employee"""
    def __init__(self, name: str, emp_id: int, department: str):
        # Use super().__init__() to invoke the parent class constructor
        super().__init__(name, emp_id)
        self.department = department

    # Method Overriding: Redefining get_role_description to include department info
    def get_role_description(self):
        # We can also call the parent's original method using super() inside the override!
        base_description = super().get_role_description()
        return f"{base_description} | Role: Manager of {self.department} Department"


print("--- Testing Method Overriding & super() ---")
# Instantiating parent class
generic_emp = Employee("Rohan", 101)
print(generic_emp.get_role_description())

# Instantiating child class with overridden method
tech_manager = Manager("Harry", 102, "Engineering")
print(tech_manager.get_role_description())