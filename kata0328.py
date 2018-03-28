
# naive solution which falls apart when trying to find "earliest pair"
# prob also way to slow
#
# def sum_pairs(ints, s):
#     low_score = -1
#     target = [-1,-1]
#     for ind, num in enumerate(ints):
#         for x, y in enumerate(ints, ind):
#             if num + y == s:
#                 if target == [-1, -1]:
#                     target = [ind, x]
#                 elif target[0] > ind and target[1] > x:
#                     target = [ind, x]
#
#     if target != [-1,-1]:
#         return [ints[target[0]], ints[target[1]]]
#
#     return None


### code kata best practices solution
# STUDY!
# inner pair => translation : first to populate cache completely
# avoiding "scoring" based on indices which is not how the problem is defined

def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

l1= [1, 4, 8, 7, 3, 15]
l5= [10, 5, 2, 3, 7, 5]
l7= [0, 2, 0]
print(sum_pairs(l1, 8))
print(sum_pairs(l7, 0))
print(sum_pairs(l5, 10))
