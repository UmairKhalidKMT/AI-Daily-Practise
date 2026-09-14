# BIG O: O(n) - Linear Time
# Imagine 5 apples in a box. You pick them up one by one.
# If you have 5 apples, it takes 5 steps. 
# If you have 100 apples, it takes 100 steps. 
# Time grows in a straight line with the size of the list!

apples = ["red apple", "green apple", "yellow apple"]

for apple in apples:
    # We visit every apple once
    print("I ate a", apple)


    ##################################

# BIG O: O(n) - Linear Time (Worst Case)
# You are searching for your favorite toy in a toy box.
# If it's at the very end (or not there at all), you check every single toy once.

toys = ["car", "blocks", "teddy bear", "dinosaur"]

for toy in toys:
    if toy == "teddy bear":
        print("Found my favorite teddy bear!")


    ####################################


# BIG O: O(n²) - Quadratic Time (Slow!)
# Imagine matching 3 shirts with 3 pairs of pants.
# For EVERY single shirt, you try ALL 3 pairs of pants!
# 3 shirts * 3 pants = 9 dynamic outfits.
# If you double the clothes, the work gets FOUR times bigger!

shirts = ["red shirt", "blue shirt"]
pants = ["jeans", "shorts"]

for shirt in shirts:  # First outer loop
    for pant in pants:  # Inner loop runs completely for each shirt
        print("Wearing:", shirt, "with", pant)

    #####################################

# BIG O: O(n) - Still Linear Time!
# Even though we skip every second number (5 steps instead of 10),
# computer scientists still call this O(n) because double the numbers 
# still means double the total work overall!

for number in range(0, 10, 2):  # Count from 0 to 9, jumping by 2
    print("Step count:", number)