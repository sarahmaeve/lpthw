from sys import argv

# unpack argv and collect the filename
# in the future, is it better to refer to argv[1]?
script, filename = argv

# documentation : default read-only equivalent to open(file, mode='r')
txt = open(filename)

print(f"Here's your file {filename}:")
# print contents to the screen in one blob
print(txt.read())
# added in second part: close fd
txt.close()

# informational: if you use txt.read again, you'll get
# ValueError: I/O operation on closed file.

# not a great way to do this.
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()

# in the future, error handling??
