# LPTHW continues with the basics: while loops

# i = 0
# numbers = []
#
# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)
#
#     i += 1
#
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")
#
# print("The numbers: ")
#
# for num in numbers:
#     print(num)

def kludge(threshold, skip):
    i = 0
    numbers = []
    while i < threshold:
        numbers.append(i)
        i += skip

    print("The numbers:")

    for num in numbers:
        print(num)

def kludge_range(thresh, skip):
    numbers = range(0,thresh,skip)

    print("The numbers:")

    for num in numbers:
        print(num)

kludge_range(100,3)
