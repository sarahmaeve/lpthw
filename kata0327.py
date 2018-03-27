def expanded_form(num):
    mynum = list(str(num))
    digits = len(mynum) - 1
    output = ''
    for i in mynum:
        if i != '0':
            if digits < len(mynum) - 1:
                output += ' + '
            output += i + '0' * digits
        digits -= 1

    return output

print(expanded_form(12356))
print(expanded_form(7005))
print(expanded_form(900))

# and the optimum / best practice from codekata for study
#
# def expanded_form(n):
#     result = []
#     for a in range(len(str(n)) - 1, -1, -1):
#         current = 10 ** a
#         quo, n = divmod(n, current)
#         if quo:
#             result.append(str(quo * current))
#     return ' + '.join(result)


def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending'
    if arr == sorted(arr, reverse=True):
         return 'yes, descending'
    return 'no'

## in this case kata answer is the same, with an optional sorted(arr)[::-1]
## and if / elif / else instead of if/return clauses

# code along with https://www.youtube.com/watch?v=Nkw6Jg_Gi4w
# swap based sort
def insertion_sort(A):
    for i in range(1, len(A)):
        j = i - 1
        while A[j] > A[j+1] and j >= 0:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1
    return A

print(insertion_sort([4, 5, 12, 8, 2]))


# from his github as the code-along is wrong
# removed unnecessary buffer variable from his version
def insertion_sort3(A):
    for i in range(1, len(A)):
        curNum = A[i]
        # negative ranges and strides are confusing and
        # error prone (like the original video)
        for j in range(i-1, -2, -1):
            # print("{} : {}".format(A[j],curNum))
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                break
        A[j+1] = curNum
    return A


print(insertion_sort3([0, 12, 5, 3, 9, 7, 2, 34, 23, 1]))
