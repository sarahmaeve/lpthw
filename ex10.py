# let's review escape sequences

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
format_cat = "Endert {}"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

cat_block = '''
Once, the cat said:
"Behold, I am the cat."
Then it went back to sleep.
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(cat_block)
print(format_cat.format('\tkatze\n'))
