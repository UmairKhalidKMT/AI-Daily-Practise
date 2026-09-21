# 1. CREATING A LIST & MIXED DATA TYPES
marks = [10, 20, 35, "Harry", True, 45, 50, 60]
print("Original List:", marks)
print("Type of list:", type(marks))

# 2. POSITIVE AND NEGATIVE INDEXING
print("\n--- Indexing ---")
print("First Element (Index 0):", marks[0])  # Output: 10
print("Fourth Element (Index 3):", marks[3]) # Output: "Harry"

# Negative Indexing
# Formula: len(marks) + negative_index => 8 + (-3) = Index 5
print("Negative Index [-3]:", marks[-3])     # Output: 45

# 3. CHECKING MEMBERSHIP (using 'in')
print("\n--- Membership Check ---")
if "Harry" in marks:
    print("Yes, 'Harry' is present in the list!")
else:
    print("No, not found.")

# 4. LIST SLICING AND JUMP INDEXING [start : end : step]
print("\n--- Slicing ---")
# Slice from Index 1 to 5 (Index 5 excluded)
print("Slicing [1:5]:", marks[1:5]) 

# Jump Index (Step = 2)
# Takes every 2nd element within the range 1 to 7
print("Slice with Step [1:7:2]:", marks[1:7:2])

# Default boundaries (Omitting start/end defaults to 0 and len(marks))
print("Default Slice [:]:", marks[:])

# 5. LIST COMPREHENSION (Dynamic List Generation)
print("\n--- List Comprehension ---")
# Generate squares of numbers 0 through 4
squares = [i * i for i in range(5)]
print("Squares:", squares)

# Generate list with conditional logic (Only even numbers)
even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers (0-9):", even_numbers)



