
def say_hello(name):
    print("Hello,", name)

say_hello("Ali")
say_hello("Sara")
say_hello("Umair")


def add(a, b):
    print(a + b)

add(2, 3)
add(10, 5)
add(100, 200)


def avg(a, b, c):
    return (a + b + c) / 3

result = avg(10, 20, 30)

print("Average is:", result)


def make_sandwich(bread, filling):
    print("Making a sandwich with", bread)
    print("Filling:", filling)

make_sandwich(bread="brown bread", filling="cheese")


def say_hello(name="Ali"):
    print("Hello,", name)

say_hello()
say_hello("Umair")
say_hello("Sara")