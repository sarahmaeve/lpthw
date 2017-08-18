# import random
# import secrets
# print(random.__dir__())


# building a password generator
# give it the length of the password
# return a random string of UC, LC and numbers


import random
# random.choice(seq) -> returns a random element from seq

# """
#
# [X] Include uppercase letters
# [ ] Include lowercase letters
# [X] Include numbers
# [ ] Include symbols (how many?)
# """

# can replace with string constants
# import string
# string.ascii_uppercase et al

UPPERALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERALPHA = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '1234567890'
SYMBOLS = '~`!@#$%^&*()_+={}[]|:";\'<>,.?'


def generate_password(length, optdict):
    """(12, uc, lc, num=3)"""
    output_pwd = ''
    remaining_len = length
    charsetOpts = []
    for k, v in optdict.items():
        if v != '*':
            output_pwd += add_charspace([k], v)
            remaining_len -= v
        else:
            charsetOpts.append(k)
    else:
        if charsetOpts:
            output_pwd += add_charspace(charsetOpts, remaining_len)

    # shuffle output_pwd so that all the minimum chars aren't grouped together
    slist = list(output_pwd)
    random.shuffle(slist)
    shuffled = ''.join(slist)
    return shuffled

# for example:
# num = 3, sym = 1, uc, lc
# num 3 , sym , total - (special) -> remainder charsets
def add_charspace(charsets, length):
    """ arguments : list of character sets in option format
        example: add_charspace([uc, lc], 8)
        example: add_charspace([num], 2)
    """

    pwspace = ''
    pwchunk = ''
    # print((charsets))
    for charset in charsets:
        if charset == 'uc':
            pwspace += UPPERALPHA
        if charset == 'lc':
            pwspace += LOWERALPHA
        if charset == 'num':
            pwspace += NUMBERS
        if charset == 'sym':
            pwspace += SYMBOLS

    for x in range (0, length):
        pwchunk += random.choice(pwspace)

    return pwchunk

# optparse-like : sym=1
myoptions = { 'uc': '*', 'lc': '*', 'num': 3, 'sym': 2 }
print(generate_password(12, myoptions))
