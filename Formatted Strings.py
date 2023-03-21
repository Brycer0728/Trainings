# formatted strings - f string is the prefered way to do a formatted string
# adding a 'f' before a string turns it into a formatted string
# putting variables or integers in curly brackets '{}', allows for the data to be imported into the string
name = 'Johnny'
age = 55

print(f'Hi {name}. Congrats on turning {age} today')
# the 'f' in front of the start of the string turns this into a formatted string

# '.format' does the same thing
print('Hi {}. Congrats on turning {} today'.format('Johnny', '55'))

# below is a '.format' using variables
print('Hi {}. Congrats on turning {} today'.format(name, age))

# below is an example of having either the string or variables in a specific order (starts with 0)
print('Hi {1}. Congrats on turning {0} today'.format(name, age))
# the example above prints 'Hi 55. Congrats on turning Johnny today' because 'name' is 0 and 'age' is 1
# another example of using a variable and it's data for a string
print('Hi {new_name}. Congrats on turning {age} today'.format(new_name='Sally', age=100))
# example above prints 'Hi Sally. Congrats on turning 100 today'