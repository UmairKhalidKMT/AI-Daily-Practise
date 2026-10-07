"""

CONCEPT DEFINITIONS:
1. Lambda Functions: Small, anonymous (nameless) functions defined in a single line 
   using the 'lambda' keyword. Useful for short, throwaway logic.
2. Higher-Order Functions: Functions that accept other functions as arguments or 
   return them as output (e.g., map, filter, reduce).
3. map(func, iterable): Applies a function to every item in an iterable and 
   returns an iterator yielding transformed elements.
4. filter(func, iterable): Evaluates each item through a boolean function and 
   yields only items where the condition returns True.
5. reduce(func, iterable): Repeatedly applies a binary function to elements in a 
   sequence, reducing the entire collection to a single scalar value.

"""

from functools import reduce


# LAMBDA FUNCTIONS (Anonymous Functions)

"""
SYNTAX: lambda arguments: expression
- No 'def' keyword required.
- Implicitly returns the result of the expression.
- Cannot contain multi-line statements or complex logic.
"""

# Standard function syntax
def double_def(x):
    return x * 2

# Equivalent Lambda function syntax
double_lambda = lambda x: x * 2

# Multi-argument Lambda
cube = lambda x: x ** 3
sum_two = lambda a, b: a + b
average = lambda x, y, z: (x + y + z) / 3

print(f"Double of 5: {double_lambda(5)}")
print(f"Cube of 3: {cube(3)}")
print(f"Sum of 10 and 20: {sum_two(10, 20)}")
print(f"Average: {average(3, 6, 9)}")


# Passing a Lambda function into another function as a parameter
def apply_operation(func, value):
    """Executes any passed function on the provided value."""
    return func(value)

res = apply_operation(lambda x: x * x * x, 2)  # Passes an inline cube operation
print(f"Result from passed inline lambda: {res}")


# THE map() FUNCTION

"""
DEFINITION: map(function, iterable)
Transforms a collection element-by-element without writing explicit loops.
Returns a map object (iterator), so wrap with list() or tuple() to inspect.
"""

numbers = [1, 2, 3, 4, 5]

# Transforming list items using a lambda inside map()
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"\nOriginal Numbers: {numbers}")
print(f"Squared Numbers (map): {squared_numbers}")


# SECTION 3: THE filter() FUNCTION

"""
DEFINITION: filter(predicate_function, iterable)
Filters out items based on a condition function returning True or False.
Returns a filter object (iterator).
"""

mixed_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, mixed_numbers))

# Keep numbers greater than 5
greater_than_five = list(filter(lambda x: x > 5, mixed_numbers))

print(f"\nOriginal List: {mixed_numbers}")
print(f"Filtered Even Numbers: {evens}")
print(f"Filtered Numbers > 5: {greater_than_five}")


# SECTION 4: THE reduce() FUNCTION

"""
DEFINITION: reduce(function, iterable)
Imported from 'functools'. Applies a cumulative operation sequentially across 
items to boil down a sequence into a single cumulative output value.
"""

sample_data = [1, 2, 3, 4, 5]

# Sum up all elements in sequence: (((1 + 2) + 3) + 4) + 5
total_sum = reduce(lambda x, y: x + y, sample_data)

# Find maximum number in a list cumulatively
max_number = reduce(lambda a, b: a if a > b else b, sample_data)

print(f"\nSample Data: {sample_data}")
print(f"Cumulative Sum (reduce): {total_sum}")
print(f"Maximum Number (reduce): {max_number}")