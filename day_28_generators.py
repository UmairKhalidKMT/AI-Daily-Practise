"""
================================================================================
CONCEPT DEFINITIONS:
1. Generator: A special type of function in Python that returns an iterator using 
   the `yield` keyword instead of `return`.
2. On-the-Fly Generation: Generators compute and yield values one at a time only 
   when requested, rather than storing an entire sequence in memory at once.
3. Lazy Evaluation: The evaluation of expressions is delayed until their values 
   are actually needed, significantly saving memory and improving performance for large datasets.
================================================================================
"""

# ==============================================================================
# SECTION 1: CREATING AND USING A BASIC GENERATOR
# ==============================================================================

def number_generator(limit: int):
    """A generator function that yields numbers up to a specified limit."""
    print("--- Generator execution started ---")
    current = 1
    while current <= limit:
        # yield pauses the function, saves its state, and returns the current value
        yield current
        current += 1


print("--- Testing Generator in VS Code ---")
# Instantiating the generator (does NOT run the function body yet)
gen = number_generator(3)
print(f"Generator Object: {gen}\n")

# Requesting values one by one using the built-in next() function
print(f"First value (next): {next(gen)}")
print(f"Second value (next): {next(gen)}")
print(f"Third value (next): {next(gen)}")

# Calling next() again when no values are left raises a StopIteration exception:
# print(next(gen)) # Uncommenting this will raise StopIteration


# ==============================================================================
# SECTION 2: ITERATING OVER A GENERATOR USING A FOR LOOP
# ==============================================================================

print("\n--- Iterating through a Generator with a For Loop ---")
# For loops automatically handle generator iteration and StopIteration exceptions
for number in number_generator(5):
    print(f"Generated Number: {number}")