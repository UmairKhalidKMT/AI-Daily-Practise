"""
=============================================================================
DEFINITION & CONCEPTS:
- Dictionary: An ordered collection (Python 3.7+) of key-value pairs enclosed 
  in curly brackets `{}`.
- Keys: Unique, immutable data types (strings, ints, tuples).
- Values: Any data type, can be duplicated.
- Time Complexity: Fast lookup O(1) average case using internal hashing/indexes.
=============================================================================
"""

# CREATING A DICTIONARY

employee_ids = {
    344: "Harry",
    567: "Neha",
    678: "Zakir",
    56: "Shubham"
}

user_info = {
    "name": "Karan",
    "age": 19,
    "eligible": True
}

print("Employee Dictionary:", employee_ids)


# ACCESSING VALUES & SAFE ACCESS
# Approach A: Square Bracket Notation dict[key]
# Throws KeyError if key does NOT exist!
print("Direct Lookup:", user_info["name"])  # Output: Karan

# Approach B: Safe Lookup with .get(key)
# Returns None (or default value) if key does NOT exist — prevents app crash!
print("Safe Lookup (Existing Key):", user_info.get("name"))     # Output: Karan
print("Safe Lookup (Missing Key):", user_info.get("address"))   # Output: None


# ACCESSING KEYS & VALUES SEPARATELY
# .keys() returns a view object of all dictionary keys
print("\nAll Keys:", user_info.keys())

# .values() returns a view object of all dictionary values
print("All Values:", user_info.values())


# ITERATING OVER A DICTIONARY
# Iterating over Keys and fetching Values manually:
print("\n--- Iterating via Keys ---")
for key in user_info.keys():
    print(f"Key: {key} | Value: {user_info[key]}")

# Iterating over (Key, Value) Pairs using .items():
# .items() returns tuple pairs (key, value) which can be unpacked cleanly
print("\n--- Iterating via Items (Key-Value Pairs) ---")
for key, value in user_info.items():
    print(f"The value corresponding to '{key}' is: {value}")