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
