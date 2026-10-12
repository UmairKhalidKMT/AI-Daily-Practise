"""

CONCEPT DEFINITIONS:
1. Constructor (__init__): A special magic/dunder method automatically called 
   when a new object of a class is instantiated. Used to initialize instance attributes.
2. Decorators: A design pattern in Python that allows you to modify or extend 
   the behavior of a function or method without permanently changing its source code.

"""

# SECTION 1: CONSTRUCTORS IN PYTHON (__init__)

class Employee:
    """Class representing an Employee with a built-in constructor."""
    
    # The Constructor Method
    def __init__(self, name: str, salary: float, department: str):
        """Initializes instance attributes automatically upon object creation."""
        self.name = name
        self.salary = salary
        self.department = department
        print(f"Constructor called: Employee object created for {self.name}")

    def get_details(self):
        """Method to display employee details."""
        print(f"Name: {self.name} | Salary: ${self.salary} | Dept: {self.department}")


print("--- Creating Objects with Constructors ---")
# Instantiating objects automatically triggers the __init__ constructor
emp1 = Employee("Alice", 75000, "Engineering")
emp2 = Employee("Bob", 62000, "Marketing")

emp1.get_details()
emp2.get_details()



# SECTION 2: PYTHON DECORATORS

"""
DECORATOR DEFINITION:
A function that takes another function as input, adds some functionality, 
and returns a new wrapper function.
Syntax shortcut: Use the '@decorator_name' syntax above the target function.
"""

def greet_decorator(func):
    """A simple decorator that prints messages before and after a function runs."""
    def wrapper(*args, **kwargs):
        print("--- [Decorator START] Execution initiated ---")
        
        # Execute the original function
        result = func(*args, **kwargs)
        
        print("--- [Decorator END] Execution finished ---\n")
        return result
    return wrapper


# Applying the decorator using the '@' syntax shortcut
@greet_decorator
def say_hello(name: str):
    print(f"Hello, welcome back {name}!")


@greet_decorator
def calculate_sum(a: int, b: int):
    print(f"Calculating sum of {a} and {b}...")
    return a + b


print("--- Testing Decorated Functions ---")
say_hello("Harry")

sum_result = calculate_sum(15, 25)
print(f"Final Return Value: {sum_result}")