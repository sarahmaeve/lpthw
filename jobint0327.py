#!/bin/python3

import sys
import os

# Complete the function below.

def  translateToPigLatin(phrase):
    pigge = []
    words = phrase.split()
    for word in words:
        if word[0:1].upper() in ['A', 'E', 'I', 'O', 'U']:
            pigge.append(word + 'way')
        else:
            pigge.append(word[1:] + word[0:1].lower() + 'ay')

    # titlecase first word
    return ' '.join(pigge)

#print(translateToPigLatin('Hello all world'))

f = open(os.environ['OUTPUT_PATH'], 'w')


try:
    _phrase = str(input())
except:
    _phrase = None

res = translateToPigLatin(_phrase)
f.write(res + "\n")

f.close()
