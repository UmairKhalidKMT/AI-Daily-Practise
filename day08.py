def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)

print(factorial(5))
print(factorial(3))


# Fibonacci Sequence

def fibonacci(n: int) -> int:
    """Returns the n-th Fibonacci number using recursion.
    
    Formula: F(n) = F(n-1) + F(n-2)
    Base Cases: F(0) = 0, F(1) = 1
    """
    # Base Cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive Step: Sum of previous two Fibonacci numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci_sequence(terms: int):
    """Prints the entire Fibonacci sequence up to 'terms' count."""
    sequence = [fibonacci(i) for i in range(terms)]
    print(f"Fibonacci sequence ({terms} terms): {sequence}")


print("\n--- Fibonacci Sequence Output ---")
# Getting the 6th Fibonacci term (0-indexed: 0, 1, 1, 2, 3, 5, 8)
print("6th Fibonacci term (n=6):", fibonacci(6))  # Output: 8

# Print complete sequence for first 8 terms
print_fibonacci_sequence(8)  # Output: [0, 1, 1, 2, 3, 5, 8, 13]