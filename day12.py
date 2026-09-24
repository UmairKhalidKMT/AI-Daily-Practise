"""

CONCEPT DEFINITION:
- Ternary Operator (Shorthand if-else): A concise syntax to evaluate conditions
  and return values in a single line.
- Syntax: <result_if_true> if <condition> else <result_if_false>
- Best Used For: Simple variable assignments or inline string formatting.

"""

def demonstrate_shorthand_if_else():
    a = 330
    b = 3300

    # 1. Simple Variable Assignment based on Condition
    # Reads as: Assign "A is greater" if a > b, otherwise "B is greater or equal"
    status = "A is greater" if a > b else "B is greater or equal"
    print(f"Comparison Status: {status}")

    # 2. Inline Evaluation inside print statement
    print("A is larger") if a > b else print("B is larger or equal")

    # 3. Chained Ternary Operator (Elif Equivalent)
    # Note: Keep chained expressions short; complex logic hurts code readability.
    result = "A is greater" if a > b else ("A equals B" if a == b else "B is greater")
    print(f"Chained Evaluation: {result}")


"""

CONCEPT DEFINITION:
- enumerate(): Explains the enumerate() built-in function, which tracks both the index and the value simultaneously while iterating over a sequence (list, tuple, string, etc.)
- Benefits: Avoids writing messy counter variables (e.g., i = 0, i += 1) inside for loops.
            Returns Unpacked Tuples: Yields (index, item) pairs on every loop iteration.

"""

def process_marks_demo():
    marks = [12, 56, 32, 98, 45, 1, 4]

    print("--- Traditional Approach (Manual Index Counter) ---")
    index = 0
    for mark in marks:
        print(f"Index {index}: Mark = {mark}")
        if index == 3:
            print("--> Found target score at index 3!")
        index += 1  # Easy to forget to increment or place in the wrong block!

    print("\n--- Pythonic Approach (using enumerate) ---")
    # enumerate() automatically yields (index, value) pairs
    for idx, mark in enumerate(marks):
        print(f"Index {idx}: Mark = {mark}")
        if idx == 3:
            print("--> Found target score at index 3!")



    


if __name__ == "__main__":
    demonstrate_shorthand_if_else()
    process_marks_demo()