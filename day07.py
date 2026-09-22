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