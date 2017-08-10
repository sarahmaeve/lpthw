# print Fibonacci sequence without memoization

def fib(num):
    """ Given a number, print the Fibonacci sequence for that number"""
    if num < 0:
        raise ValueError("Must be a positive integer.")

    a, b = 0, 1
    for x in range(0, num + 1):
        print(a)
        a, b = b, a + b


fib(500)
