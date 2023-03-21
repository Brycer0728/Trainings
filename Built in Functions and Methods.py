# built in functions are functions that uses '()' around a data type to perfrom some type of action on that data
greet = 'hellooooo'
print(greet[0:len(greet)])
# the example above prints 'hellooooo', the length functionis being used aboved 'len()'
# we are using a string slice to print the data at the '0' index all the way through the length of greet, which ends up being all the data

print(greet[1:len(greet)])
# the example above prints 'ellooooo'
# since the start of the string slice is the '1' index, it starts with the 'e' in 'hellooooo' and the 'stop' is the full length of the variable 'greet'

# METHODS
# String Methods - "owned by something" methods or actions only strings can perform
# methods have a '.' infront of it ex: '.format()'

quote = 'to be or not to be'

print(quote.upper())
# the example above prints 'TO BE OR NOT TO BE'
# the 'upper' method is capatilizing the whole string within the 'quote' variable

print(quote.replace('be' , 'me'))
# the example above prints 'to me or not to me'
# STRINGS ARE IMMUATBLE, THEY CANNOT BE CHANGED. WE CAN OVERWRITE THEM BUT WE DON'T CHANGE THEM
# doing 'quote.replace()' is creating a new string, we didn't assign the string to anything but we can

quote2 = quote.replace('be' , 'me')
print(quote2)
# we have now assigned the 'replace' method to a variable, created a totally differnt variable/string