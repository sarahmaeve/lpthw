from sys import argv
# red the WYSS section for how to run this
# unpacking argv
# this way it must have precisely three variables :|

script, first, second, third = argv
fourth = input("Let's add a fourth variable: ")
print("The script is called", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)
