# exercise 24: More practice
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\t the lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-" * 40)
print(poem)
print("-" * 40)

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))

# its just like with an f"" string
print(f"We'd have {beans} beans. {jars} jars, and {crates} crates.")

# instead of suggested variable = variable / 10
start_point /= 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
# if *formula and the {} interpolation don't match up
# you get IndexError: tuple index out of range
# same error if only referencing list instead of *list
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
