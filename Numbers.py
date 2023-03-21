# int and float data types
# int is a number (1,2,3,4)
# float is a floating point number - a number with a decimal point
print(2 + 4) # brackets are saying perform the action '+' on the data types '2' and '4'
print(2 - 4)
print(2 * 4)
print(2 / 4)

# (type(x)) can decipher what data type was used for 'x' -
# the example below prints "class 'int'"
print(type(2 + 4)) 
# the example below prints "class 'float'" because it is printing a decimal number
print(type(2 / 4))

# double multiply
print(2 ** 3)

# double divide - gets rounded down to an integer
# example below will print '0' instead of .5
print(2 // 4)

# modulo is the integer(whole number) that remains after the division
# example below prints '1', 4 goes into 5 once, so 1 remains
print(5 % 4)
# since 4 can go into 8 evenly, there is no remainig number so the example will print '0'
print(8 % 4)
# 4 goes into 9 twice(8), the number 1 remains so that is what the example below will print
print(9 % 4)

# math functions
# example below is the 'round' math funcion where it rounds the data down or up
# example below will print '3'
print(round(3.1))

# example below is 'absolute value' means no negative numbers
# example below will print '20'
print(abs(-20))

# bin is a function that prints the binary form of a number (1s and 0s)
# example below will print '0b101' the '0b' is just python identifying its a binary number
print(bin(5))