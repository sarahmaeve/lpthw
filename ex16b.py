from sys import argv

script, filename = argv

print(f"Contents of {filename}:")
fileh = open(filename)
print(fileh.read(),end='')
fileh.close()
