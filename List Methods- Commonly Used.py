# Other commonly used List Methods
basket = ['a','b','c','d','e']

# Index is used to find where a value is in the list
# print(basket.index(x, y, z))
# x = value that we are looking for
# y = is where to put an index value to start your search in the list
# z = is where to put an index value to end your search in the list
print(basket.index('d', 0, 4))
# example above prints '3', in the list 'd' is at the 3rd index

print(basket.count('d'))
# line 12 prints '1' because 'd' only shows up in basket once
# '.count()' is used to see how many times something shows up in a list

# the keyword 'in' lets you know if something is present in another thing
print('b' in 'basketball')
# line 17 prints 'True" because the letter 'b' shows up in basketball