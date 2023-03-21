# string indexes
# the data in strings are stored in a numeric order that starts with 0
# in the variable 'example' A=0, B=1, C=2, D=3, E=4... and so on
# think about the numbers as book shelves 0-7 is a full shelf
example = 'ABCDEFGH'
         # 01234567
print(example[0])
# the example above prints 'A' because it's in the '0' index

print(example[7])
# the example above prints 'H' because it's in the '7' index

# there is a way to grab specific pieces of text in a string using this method and ':' inside of []
# [start:stop:stepover] - this is called STRING SLICING
# 'start' is what index to start at, 'stop' is what index to stop at, and 'stepover' is how many to skip
print(example[0:3])
# the example above prints 'ABC' because I'm telling the computer to print the indexes 0-2, it doesn't print where it's supposed to stop

print(example[1:8])
# the example above prints 'BCDEFGH' because I'm telling the computer to print everyting except the 0 index, which is 'A'

print(example[0:8:2])
# using 'stepover', the example above now prints 'ACEG' because I'm printing the whole string but just stepping over every other number

print(example[1:])
# example above prints 'BCDEFGH'
# leaving a blank space after or before a ':' will just tell the computer to start at the very beginning or go to the end

print(example[:3])
# example above prints 'ABC'
# starts at the very beginning since I don't specify where to start, and stops right before the 3rd index

print(example[-1])
# example above prints 'H'
# using a negative number indicates you want to start backwards, since the '-1' is by itself, we just want to print the very last piece of data in the string

print(example[::-1])
# in the example above it prints 'HGFEDCBA'
# no indication of where to start and stop infront of the colons, and the '-1' indicates we want to start from the back and not stepover any numbers

print(example[::-2])
# in the example above 'HFDB' is printed
# the negative indicates we want to start in reverse order and the '2' tells the computer to skip over every other number