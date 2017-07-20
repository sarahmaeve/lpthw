# this appears to be an old programmer joke
# from many t-shirts

# format strings directly outside of a print() statement
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# no difference in using single or double quotes here
y = f'Those who know {binary} and those who {do_not}.'

# print these preformatted strings
print(x)
print(y)

# you also can substitute them inside other print() calls
print(f"I said: {x}")
print(f"I also said: '{y}'")

# first direct use of boolean in these exercises?
hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"

# use of string.format() to substitute for {}
# if adding extra {} results in IndexError
print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

# string concat
print(w + e)
