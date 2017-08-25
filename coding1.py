# coding exercise from interview
# this works but I feel it can be done in a much better way

def char_count(sentence):
    activeChar = ''
    activeCount = 0
    revised = ''
    for x in range(len(sentence)):
        if sentence[x] != activeChar:
            if activeChar:
                revised += activeChar + str(activeCount)
            activeChar = sentence[x]
            activeCount = 1
        else:
            activeCount += 1
    else:
        if activeChar:
            revised += activeChar + str(activeCount)

    return revised


sentence = 'aaabbcccdabcc'
print(char_count(sentence))
