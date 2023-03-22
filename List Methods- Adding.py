# List Methods- actions that you can use on Lists
basket = [1,2,3,4,5]
list = [1,2,3,4,5]
numbers = [1,2,3,4,5]

# Adding Methods

# Append adds an object to the end of the list
## new_list = basket.append(100)
# if 'new_list" is printed from the example above, it would print none, a method doesn't produce a value
basket.append(100)
# the 'append' method above is adding '100' to the END of the list in the variable 'basket'
new_list = basket
print(new_list) 
print(basket)
# lines 9 and 10 both print '[1,2,3,4,5,100]'

# Insert allows you to add a object anywhere in the list by using the index and the object
list.insert(4, 100) # 4 is the index/where it will be inserted at, 100 is what is being inserted
print(list)
# line of code prints '[1,2,3,4,100,5]' add or inserting the object '100' in the 4th index in this example

# Extend takes an interable ('something you can loop over, you can iterate over') and adds it to the list
numbers.extend([100,101])
print(numbers)