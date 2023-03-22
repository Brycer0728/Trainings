# List Methods Removing
basket = [1,2,3,4,5]
list = [1,2,3,4,5]
nums = [1,2,3,4,5]
digits = [1,2,3,4,5]
object = [1,2,3,4,5]

# Pop 'pops off' anything at the end of the list
basket.pop()
print(basket)
# example above printed '[1, 2, 3, 4]' 'popped off' the 5 at the end
list.pop(0) # the number in the '()' tells you what INDEX to 'pop off'
print(list)
# example above prints '[2,3,4,5]
# Pop returns a value
new_list = digits.pop(4)
print(new_list)
# example above prints '5' since 'pop' returns a value of the number that is being removed

# Remove method allows you to remove a specific value
nums.remove(3)
print(nums)
# example above prints [1,2,4,5] '3' is removed since it was specific in the method

# Clear removes everything in the list
object.clear()
print(object)
# example above prints '[]' it cleared everything in the list