"""

CONCEPT DEFINITIONS:
- Exception: An unwanted or unexpected event that disrupts the normal flow 
             of a program's execution.
- try block: Wraps code that might raise an exception.
- except block: Catch and handles specific or general errors if raised in 'try'.
- Program Continuity: Using try-except prevents the Python interpreter from
                       crashing/halting when an error occurs.

"""

def generate_multiplication_table():
    user_input = input("Enter a number to generate its table: ")
    
    # Example list to test IndexError
    numbers_list = [10, 20, 30]

    try:
        # 1. Potential ValueError if user enters text instead of a number
        num = int(user_input)
        
        print(f"\n--- Multiplication Table of {num} ---")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
            
        # 2. Potential IndexError if index is out of bounds
        idx = int(input("\nEnter an index to pick from [10, 20, 30] (0-2): "))
        print(f"Value at index {idx} is: {numbers_list[idx]}")

    except ValueError:
        # Triggered if conversion to int fails
        print("\n[Error Handled] Invalid Input! Please enter a valid integer.")

    except IndexError:
        # Triggered if requested index doesn't exist in the list
        print("\n[Error Handled] Index out of range! Valid indices are 0 to 2.")

    except Exception as e:
        # Fallback for any other unanticipated exception
        print(f"\n[Error Handled] An unexpected error occurred: {e}")

    # Notice this line still runs even if the try block produced an error!
    print("\n=> Program execution continues smoothly after handling errors...\n")


"""

CONCEPT DEFINITION:
- finally block: A clause that ALWAYS executes, regardless of whether an 
                 exception occurred or was caught.
- The Return Scenario: Even if a function returns early from inside a 'try' 
                       or 'except' block, the 'finally' block is GUARANTEED 
                       to execute before the function actually exits.

"""

def check_list_index():
    data = [100, 200, 300, 400]
    
    try:
        idx = int(input("Enter an index (0-3): "))
        print(f"Selected item: {data[idx]}")
        
        # Returning early on success
        return 1 

    except IndexError:
        print("[Error] That index doesn't exist!")
        # Returning early on failure
        return 0

    except ValueError:
        print("[Error] Input must be a valid integer!")
        return -1

    finally:
        # Crucial Behavior: This WILL execute even though we hit 'return' above!
        print("[FINALLY BLOCK] This cleanup code ALWAYS runs (even after a 'return')!")


"""

CONCEPT DEFINITION:
- Custom Errors (raise): Manually triggering built-in exceptions (e.g., ValueError)
                        or custom error classes to halt invalid program state.
- Why raise errors? To enforce rules early (fail-fast principle) so invalid inputs 
                    don't propagate down your code causing silent bugs.

"""

def process_user_age():
    user_input = input("Enter your age (between 18 and 100): ")

    # Checking for non-numeric strings
    if not user_input.isdigit():
        # Raise ValueError if conversion isn't possible
        raise ValueError("Invalid input! Age must be a numeric integer.")

    age = int(user_input)

    # Custom Business Rule Validation
    if age < 18 or age > 100:
        # Intentionally halt program execution when outside allowable range
        raise ValueError(f"Age {age} is out of bounds! Must be between 18 and 100.")

    print(f"[Success] Age recorded successfully: {age}")



    


if __name__ == "__main__":
    generate_multiplication_table()
    result = check_list_index()
    print(f"Function returned with code: {result}")

    try:
        process_user_age()
    except ValueError as err:
            # Catching the custom error raised above
        print(f"[Caught Custom Error]: {err}")