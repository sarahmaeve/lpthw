# Fibonacci redone with generator
def fib(num):
    """Given a number, return the Fibonacci sequence from zero to that number"""
    if num < 0:
        raise ValueError("Must be a positive integer.")

    a, b = 0, 1
    # up to and including num
    for x in range(0, num + 1):
        yield(a)
        a, b = b, a + b

for x in fib(1000):
    print(x)
