# "More Printing"
# this exercise says "do not skip"
# so it should be extra tedious

print("Mary had a little lamb.")
# direct substitution
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10 ) # what'd that do?
# A: repeat the character ten times

# typing or command->return practice
# put a collection of characters in variables in order to reassemble them
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. Try removing it to see what happens
# A: if removed: SyntaxError: keyword can't be an expression
# an arg for the print() function? yes, example end='!'
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# assemble characters, but do not end the first print statement with a newline
# end the print statement with a space ' ' (if no end= , they follow each other)
print(end7 + end8 + end9 + end10 + end11 + end12)
