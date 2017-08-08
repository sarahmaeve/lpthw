# try to do a fibonacci sequence using memoization
# inspired by https://www.youtube.com/watch?v=Qk0zUZW-U_M

from functools import lru_cache

# could also use =none
@lru_cache(maxsize=1000)

def fibonacci(n):
    # n.is_integer didn't work here
    if type(n) != int:
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("Please use a positive integer")

# very verbose structure used in video
    # if n == 1:
    #     return 1
    # elif n == 2:
    #     return 1
    # elif n > 2:
    #     return fibonacci(n-1) + fibonacci(n-2)

    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

for x in range(0,501):
    print(x, fibonacci(x))

# print info on lru_cache
# from https://docs.python.org/3/library/functools.html
print(fibonacci.cache_info())
