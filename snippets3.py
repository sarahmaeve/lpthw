### codewars exercise 7 kyu

def remove_smallest(numbers):
    # better than if len(numbers) > 0
    if numbers:
        numbers.remove(min(numbers))
    return numbers

print(remove_smallest([1,2, 3, 5, 6]))


### my first answer to exercism isogram question
### mostly due to a need to pass through all non-letter chars
### (spaces and hyphens)
def is_isogram(word):
    alpha_chars = [i for i in set(word.lower()) if i.isalpha()]
    alpha_words = [i for i in list(word.lower()) if i.isalpha()]
    return bool( len(alpha_chars) == len(alpha_words) )


### little regex hacking
myRegex = re.compile(r'(\d\d\d)?-?(\d\d\d)-(\d\d\d\d)')
test = myRegex.search('blah: 403-0532')
# unpack groups() tuple
area_code, prefix, suffix = test.groups()


# hackerrank string challenge: swap case of a string
# built on a lot of similar exercises
# of course this has apparently been superceded by str.swapcase() -- lol

import string
def swap_case(s):
    return s.translate(str.maketrans(string.ascii_letters, string.ascii_uppercase + string.ascii_lowercase ))
