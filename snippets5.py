import copy

# various stuff
# deep copy vs shallow copy

list = [ [ ] ] * 5
print(list) # ok
list[0].append(10)
print(list) # this is unexpected
list[1].append(20)
print(list) # more unexpected

## works on a differently constructed nested list so something is up
## with the * operator

hellos = [ ['hello'] ] * 5
print(hellos) # same result
hellos[0].append('goodbye')
print(hellos) # ok ...
print(id(hellos[0]))
print(id(hellos[1]))
# same memory address, these are references
hellos.append(['hello'])
print(id(hellos[5]))
# something new

hellos.append(copy.deepcopy(hellos[0])) # let's deepcopy instead
print(hellos)
hellos[0].append('so long')
print(hellos) # aha, new deepcopy is isolated as is the manual append

helloz = [[]for i in range(0,5)]
# build through list comprehension instead ... will this work?
print(helloz)
helloz[0].append('hello!')
print(helloz)
# hello-lujah

# another shallow copy method
helloy = helloz[:]
helloz[0].append('goodbye!')
print(helloz) # as unexpected
print(helloy) # also should be expected; [:] is not a deepcopy
