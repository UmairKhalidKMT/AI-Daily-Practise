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
    sequence = [fibonacci(i) for i in range(terms)]
    print(f"Fibonacci sequence ({terms} terms): {sequence}")


print("\nFibonacci Sequence Output")
print("6th Fibonacci term (n=6):", fibonacci(6))  # Output: 8

print_fibonacci_sequence(8)  