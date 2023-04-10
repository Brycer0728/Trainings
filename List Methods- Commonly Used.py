# Other commonly used List Methods
basket = ['a','b','c','d','e']
basket_2 = ['a','x','b','c','d','e','d']

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

# '.sort()' sorts the list, modififes the list, '.sort()' doesn't return anything
basket_2.sort()
# printing 'print(basket_2.sort())' wouldn't return anything
print(basket_2)
# line 23 prints '['a', 'b', 'c', 'd', 'd', 'e', 'x']'

# 'sorted' is like '.sort()' but it returns something, it doesn't modify the list, it creates a new one
print(sorted(basket_2))
# line 28 prints '['a', 'b', 'c', 'd', 'd', 'e', 'x']' because sorted will actually return a value

# '.copy()' allows you to copy a list

# '.reverse()' reverses the order of the list but doesn't sort it. It just reverses the indexs
# since 'basket_2' is still sorted due to line 28, if we reverse the order it will print in a sorted reverse order
basket_2.reverse()
print(basket_2)
# line 36 printed '['x', 'e', 'd', 'd', 'c', 'b', 'a']'