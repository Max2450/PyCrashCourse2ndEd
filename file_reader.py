"""Chapter 10 class for reading the pi_digits.txt file."""
#with is used to automatically close the opened file once it is no longer needed.

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    #extra blank line would appear without rstrip because read() returns an empty string at the end of files.

#alternately, we can use loops to read each line
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        #extra blank lines appear after each line due to print() also adding newlines

#with only allows access to the file object returned by open() within the with block, but we can store the contents.
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

