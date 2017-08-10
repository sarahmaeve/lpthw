## code kata

# Codewars : complementary DNA strings (7 kyu)
# my answer
def DNA_strand(dna):
    DNA_MATCH = { 'A': 'T', 'T' : 'A', 'C' : 'G', 'G': 'C' }
    complement = ''
    for letter in list(dna):
        complement += DNA_MATCH[letter]

    return complement

# cool other solutions (research)
# string translation
# some versions of python require import of string module
def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

# list comp
pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])

## unrelated odd side-effect: inefficient lowercase-only ROT13 in python
rot13 = str.maketrans("abcdefghijklmnopqrstuvwxyz","nopqrstuvwxyzabcdefghijklm")
message = "hello there"
message.translate(rot13)

# the _actual_ answer
import codecs
codecs.encode('Hello There!', 'rot13')
