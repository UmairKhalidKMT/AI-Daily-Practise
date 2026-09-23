#Standard Function Docstring & Access via __doc__
#A docstring (documentation string) is a string literal used to document a specific Python module, class, function, or method. 
# It must be the very first statement inside the object definition, enclosed in triple quotes (""" or ''')"
#__doc__ Attribute: Python automatically compiles the docstring into the object's __doc__ attribute.

from xxlimited import new


def calculate_square(n: int) -> int:
    """Takes in a number 'n' and returns its square.
    
    Parameters:
        n (int): The numerical value to be squared.
        
    Returns:
        int: The square of 'n'.
    """
    return n ** 2

# Outputting function evaluation
print("Result:", calculate_square(5))  # Output: 25

# Accessing docstring programmatically via the __doc__ attribute
print("\n--- Reading __doc__ Attribute ---")
print(calculate_square.__doc__)


#Invalid Docstring Placement Example

def invalid_docstring_example():
    print("Executing a statement before the docstring...")
    """
    This string is NOT a valid docstring because a print statement 
    precedes it! Python will ignore this string entirely.
    """
    return True

print("\n--- Invalid Docstring Access ---")
# Output will print None because __doc__ was not registered
print("Docstring output:", invalid_docstring_example.__doc__)


# Class Docstrings

class Calculator:
    """A basic mathematical calculator class demonstrating class docstrings."""
    
    def multiply(self, a: float, b: float) -> float:
        """Multiplies two numbers and returns the product."""
        return a * b

print("\n--- Class & Method Docstrings ---")
print("Class Docstring:", Calculator.__doc__)
print("Method Docstring:", Calculator.multiply.__doc__)


# PEP 8 Easter Egg - The Zen of Python
# PEP stands for Python Enhancement Proposal
#It is an official design document used by the Python community to propose new features, processes, or environment descriptions.
#It is a style guide for writing python code.

print("\n--- Printing The Zen of Python (PEP 20) ---")
# Importing 'this' prints the philosophical guidelines of Python
import this