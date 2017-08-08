# exercise 21: function returns, because that would be cool

def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a,b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# a puzzle for extra credit, type it in anyway
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# 35 + (75 - (180 * (50 / 2)))
print("That becomes: ", what, "Can you do it by hand?")

# additional exercise
# 20 * (3 + (27 / (6 - 2))
test = multiply(20, add(3, divide(27, subtract(6, 2))))
print("Additional exercise is: ", test)
