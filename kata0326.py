def iq_test(numbers):
    odd = 0
    even = 0
    last_odd = 0
    last_even = 0

    for x, y in enumerate(numbers.split(' ')):
        if int(y) % 2 == 0:
            odd += 1
            last_odd = x + 1
        else:
            even += 1
            last_even = x + 1

# incorrect: only need to test for 1 or more than one, and this needs to be
# # outside the for loop
#         if odd > 0 and even > 0:
#             if odd > even:
#                 return last_even
#             elif even < odd:
#                 return last_odd

# so corrected:
   if odd == 1:
        return last_odd
    else:
        return last_even


## The code kata answer
# demonstrating aggregation of booleans
# list comp is a big improvement


# def iq_test(numbers):
#     e = [int(i) % 2 == 0 for i in numbers.split()]
#
#     return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
