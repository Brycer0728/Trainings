# type conversion is converting the type of data types
# in the example below we are turning a str into an int
print(type(int(str(100))))
# can also be written like
a = str(100)
b = int(a)
c = type(b)
print(c)
# both sets of code print the same thing 'class 'int''
