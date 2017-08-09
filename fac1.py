# first factorial
# based on CoderByte question

def FirstFactorial(num):
    """Assuming between 1 - 20, all positive int"""
    if num <= 2:
        return num

    return num * FirstFactorial(num - 1)


print(FirstFactorial(2))
print(FirstFactorial(8))
print(FirstFactorial(20))
