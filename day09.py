# PYTHON SETS & SET METHODS MASTER SCRIPT 

"""
DEFINITIONS & CORE CONCEPTS:
1. SET: An unordered collection of unique elements enclosed in curly braces `{}`.
2. UNORDERED: Elements do not have a fixed position/index. Indexing `s[0]` throws a TypeError.
3. UNIQUE: Sets automatically eliminate duplicate entries upon creation or modification.
4. IMMUTABLE ELEMENTS: Items within a set must be immutable (e.g., numbers, strings, tuples).
5. EMPTY SET SYNTAX: `{}` creates a dictionary! Use `set()` constructor to create an empty set.
"""

print("CREATING & UNDERSTANDING SETS ")

# Example 1: Automatic Deduplication & Unordered Behavior
numbers_set = {2, 4, 2, 6, 4, 8}
print("Original Set Definition: {2, 4, 2, 6, 4, 8}")
print("Deduplicated Result    :", numbers_set)  # Output will drop extra 2s and 4s

# Example 2: Mixing Data Types
mixed_set = {"CodeWithHarry", 29, 5.9, True, 29}
print("Mixed Set              :", mixed_set)

# Example 3: The Empty Set Trap
empty_dict = {}
empty_set = set()

print("\nType of `{}`    :", type(empty_dict))  # <class 'dict'>
print("Type of `set()` :", type(empty_set))   # <class 'set'>

# Example 4: Iterating over Set items (Since direct indexing is forbidden)
print("\nIterating through set elements:")
for item in mixed_set:
    print(" ->", item)


print("\n SETTHEORY & MATHEMATICAL METHODS ")

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7, 2}

# UNION & UPDATE
# UNION: Combines elements from both sets without altering original sets.
union_set = s1.union(s2)
print("s1.union(s2)             :", union_set)

# UPDATE: Mutates/modifies the caller set in-place with elements of another set.
s1_copy = s1.copy()
s1_copy.update(s2)
print("s1 after .update(s2)     :", s1_copy)

#  INTERSECTION & INTERSECTION_UPDATE 
# INTERSECTION: Returns elements present in BOTH sets.
intersection_set = s1.intersection(s2)
print("\ns1.intersection(s2)      :", intersection_set)

# INTERSECTION_UPDATE: Modifies original set to contain only intersecting items.
s1_copy = s1.copy()
s1_copy.intersection_update(s2)
print("s1 after .intersection_update(s2):", s1_copy)

#  SYMMETRIC DIFFERENCE 
# SYMMETRIC DIFFERENCE: Returns elements in set A or B, but NOT in both (A ∪ B - A ∩ B).
sym_diff = s1.symmetric_difference(s2)
print("\ns1.symmetric_difference(s2):", sym_diff)

#  DIFFERENCE 
# DIFFERENCE: Returns elements present ONLY in caller set (A - B).
diff = s1.difference(s2)
print("s1.difference(s2) [s1 - s2] :", diff)


print("\nSET RELATIONSHIP TESTS ")

cities_a = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities_b = {"Tokyo", "Berlin"}
cities_c = {"London", "Paris"}

# ISDISJOINT: Returns True if sets have NO common elements.
print("Are cities_a & cities_c disjoint? :", cities_a.isdisjoint(cities_c))  # True

# ISSUPERSET: Returns True if main set contains ALL elements of secondary set.
print("Is cities_a a superset of cities_b?:", cities_a.issuperset(cities_b))  # True

# ISSUBSET: Returns True if ALL elements of main set exist in secondary set.
print("Is cities_b a subset of cities_a?  :", cities_b.issubset(cities_a))    # True


print("\n ADDING & REMOVING ELEMENTS ")

fruits = {"Apple", "Banana"}

# ADD: Appends a single item
fruits.add("Cherry")
print("After .add('Cherry')     :", fruits)

# REMOVE vs DISCARD
# REMOVE: Deletes element. Throws KeyError if item does NOT exist.
fruits.remove("Apple")
print("After .remove('Apple')  :", fruits)

# DISCARD: Deletes element. Fails silently (no error) if item does NOT exist.
fruits.discard("Mango")  # Mango is not in set, no error raised!
print("After .discard('Mango') :", fruits)

# POP: Removes and returns an arbitrary element from the set
popped_item = fruits.pop()
print(f"Popped item              : {popped_item}")
print("Set after .pop()         :", fruits)

# CLEAR: Removes all elements from the set (leaving an empty set)
fruits.clear()
print("Set after .clear()       :", fruits)

# DEL: Deletes the set variable entirely from memory
del fruits
# print(fruits)  # Uncommenting this line will raise NameError: name 'fruits' is not defined