## This is the text editor interface.
## Anything you type or change here will be seen by the other person in real time.

# input: array of intergers
# output: boolean, true if and only if 3 separate cells sum to 0
# [1, 1, 1] => false
# [0, 0, 0] => true

# [0, 1, 2, -5, 8, -1]

# lower = [ i for i in myarray if i <= 0 ]
# upper = [ i for i in myarray if i > 0 ]
# zeros = lower.index(0)

# for num in upper:
#     if zeros:
#         if lower.index(-num):
#             return True

myarray = [0, 1, 0]
myarray = [0, 1, 2, -5, 8, -1]
for index, num in enumerate(myarray): # index = 0
    for index2, number2 in enumerate(myarray[index+1:]): # number2 iterate through [1, 0]
        for number3 in myarray[index2+2:]: # number iterate from [0]
            if num + number2 + number3 == 0:
                # return [num, number2, number3]
                print('True')

else:
    print('False')
