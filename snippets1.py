# Interesting python snippets

# combination for / else construct inside print()
# improvement from comments on https://www.youtube.com/watch?v=VBokjWj_cEA
needle = 'd'
haystack = ['a', 'b', 'c', 'd']
print("Found!" if needle in haystack else "Not Found!")

# extended iterable unpacking
# https://www.python.org/dev/peps/pep-3132/
# more info : https://www.youtube.com/watch?v=SNTZpy0oDB8
cities = ['San Francisco', 'Oakland', 'San Jose', 'Los Angeles']
smallest, *rest, largest = cities
print(f"Smallest city is {smallest}, largest city is {largest}")

# dict comprehensions
# https://stackoverflow.com/questions/209840/map-two-lists-into-a-dictionary-in-python
fruit = ['oranges', 'apples', 'pears', 'strawberries']
prices = [1.25, 1.79, 2.20, 3.30]
# toss in some interesting formatting while I'm here
price_list = {k.title(): "${:,.2f}".format(v) for k,v in zip(fruit, prices)}
print(price_list)

# reverse a list (idiomatic) through slices
# with a stride of -1
a = ['b', 23, 'hamhock', -19, 'camel']
a = a[::-1]

# copy a list through slice notation
# this is faster than list comprehensions or copy()
b = a # b copies the reference to the same list
c = a[:] # c is now a copy
a.append('coracle')
b.append('barbell')
print(f"a:{a}\nb: {b}\nc: {c}")

# https://www.youtube.com/watch?v=OSGv2VnC0go
# use reversed()
colors = ['red', 'green', 'blue', 'yellow']
for color in reversed(colors):
    print(color)

# need index?
# "Whenever you're manipulating indices directly, you're probably doing it wrong."
for i, color in enumerate(colors):
    print(i, '--->', color)

# use .join rather than + for assembling a list of strings
