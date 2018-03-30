# simple autocomplete exercise
# https://www.codewars.com/kata/5389864ec72ce03383000484/train/python
# return only 5 matches
# match capitalized
# only match beginning for some reason (thus match a slice and not use 'in')
# ignore junk characters (non-alphabetic in this limited case)

import re
def autocomplete(input_, dictionary):
    found = []
    clean_input = re.sub(r'[^a-zA-Z]+', '', input_)
    for word in dictionary:
        if clean_input.upper() == word[:len(clean_input)].upper():
            found.append(word)
            if len(found) == 5:
                return found

    return found


## here's the codewars response for comparison
# things to learn:
# .startswith()
# use of a slice to limit return [:5] instead of a conditional is very slick,
# but possibly computationally expensive ???
# use of .lower(), .upper() and .capitalize() in other solutions
# non-regexp character check using join from list comprehension

def autocomplete(input_, dictionary):
    input_ = ''.join( [ c for c in list(input_) if c.isalpha() ])
    return [ x for x in dictionary if x.lower().startswith(input_.lower()) ][:5]
