# kata here: https://www.codewars.com/kata/5375f921003bf62192000746/train/python
# my solution

def abbreviate(s):
    import re
    ab = []
    for word in re.split('([^A-Za-z])', s):
        if len(word) > 3:
            word = word[0:1] + str(len(word) - 2) + word[-1]
        ab.append(word)
    return ''.join(ab)


### code kata top solution for study

import re

regex = re.compile('[a-z]{4,}', re.IGNORECASE)

def replace(match):
    word = match.group(0)
    return word[0] + str(len(word) - 2) + word[-1]

def abbreviate(s):
    return regex.sub(replace, s)

## lessons:
# word[0] fine instead of word[0:1] slice
# study more regex patterns
# from my solution: using () to also grab the delimiter used in split()
