tup = (44, 88, 99, 100, 'umair')
# tup[4] = 'taimoor'  # TypeError: tuples are immutable
print(tup)

countries_tuple = ("Spain", "France", "Germany", "Italy", "Portugal")

countries = list(countries_tuple)
countries.append("Greece")
print("List after appending Greece:", countries)

refcountry = countries          # alias — same object!
refcountry.append("Austria")
print("Original list via countries:", countries)   # shows Austria too

countrycopy = countries.copy()  # independent copy
countrycopy[0] = "Sweden"
print("Modified copy:", countrycopy)
print("Original list unchanged:", countries)

countries_tuple = tuple(countries)  # now really a tuple
print("Tuple after conversion:", countries_tuple)


# OPERATIONS & METHODS ON TUPLES

# 1. TUPLE IMMUTABILITY & INDIRECT MODIFICATION WORKAROUND
countries = ("Spain", "Italy", "India", "England", "Germany")
print("Original Tuple:", countries)

# Steps to alter a tuple:
# Step a: Convert tuple to a mutable list
temp_list = list(countries)

# Step b: Modify the list (add/remove items)
temp_list.append("Russia")       # Add item
temp_list.pop(2)                # Remove item at index 2 ("India")
temp_list[1] = "Finland"         # Change item at index 1 ("Italy" -> "Finland")

# Step c: Convert list back to tuple
countries = tuple(temp_list)
print("Modified Tuple:", countries)

# 2. CONCATENATING TUPLES (Creates a brand-new tuple)
tuple1 = (0, 1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("\nConcatenated Tuple (+):", combined_tuple)

# 3. TUPLE METHODS
num_tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2, 4, 3)

# count(): Counts total occurrences of an item
three_count = num_tuple.count(3)
print(f"\nNumber 3 appears {three_count} times in num_tuple.")

# index(): Finds the index of an element
first_index = num_tuple.index(3)
print("First index of 3:", first_index)

# index(element, start, end): Finds index within a sliced range
# Searches for '3' starting from index 4 up to index 8
sliced_index = num_tuple.index(3, 4, 8)
print("Index of 3 between index 4 and 8:", sliced_index)

# len(): Returns total items in tuple
print("Length of num_tuple:", len(num_tuple))