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




# LIST METHODS & MUTATION


numbers = [12, 45, 1, 6, 11, 45, 2]
print("Initial List:", numbers)

# 1. APPEND: Add element to end of the list
numbers.append(7)
print("After append(7):", numbers)

# 2. SORT & REVERSE SORT
numbers.sort()
print("Sorted (Ascending):", numbers)

numbers.sort(reverse=True)
print("Sorted (Descending):", numbers)

# 3. REVERSE: Reverse the current elements order
numbers.reverse()
print("Reversed List:", numbers)

# 4. INDEX & COUNT
print("\n--- Index & Count ---")
print("Index of first 45:", numbers.index(45))
print("Count of 45 in list:", numbers.count(45))

# 5. INSERT: Insert element at specific index (Index, Value)
numbers.insert(1, 999)  # Inserts 999 at Index 1
print("After insert(1, 999):", numbers)

# 6. COPY vs REFERENCE (Crucial Python concept)
print("\n--- Copy vs Reference ---")
# Incorrect copy (Creates a reference pointer to the same memory block)
ref_list = numbers
ref_list[0] = 0
print("Original List modified by ref_list change:", numbers)

# Correct copy (Creates a brand-new independent copy)
# You cannot copy a list simply by typing list2 = list1 (= assignment will use reference) , because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
clean_list = numbers.copy()
clean_list[0] = 777
print("Original List after clean_list change:", numbers)
print("Copied List:", clean_list)

# 7. EXTEND & CONCATENATION
print("\n--- Merging Lists ---")
extra_items = [100, 200, 300]

# Option A: Extend (Mutates original list)
numbers.extend(extra_items)
print("After extend():", numbers)

# Option B: Concatenation using '+' (Creates a new merged list)
list_a = [1, 2, 3]
list_b = [4, 5, 6]
merged_list = list_a + list_b
print("Concatenated List (+):", merged_list)

umair=[1,2,3,4,'taimoor',5]
umair.append('ali')
umair.insert(1,'hafeez')
