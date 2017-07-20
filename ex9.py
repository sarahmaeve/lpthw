# Moar printing

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
# can add end='' as the last argument even with other args
print("Here are the months: ", months, end='\n\n')

# combining

print("Here are the days: ", days, "and here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes
We'll be able to type as much as we like.
Even 4 lines if we want, or 5 or 6.
""")
