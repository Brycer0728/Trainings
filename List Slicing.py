# List Slicing 

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
# list are mutable
amazon_cart[0] = 'laptop'
# if the line of code above was printed it would print '['laptop, 'sunglasses', 'toys', 'grapes']'
# 'notebooks' is the fisrt piece of data in the list, numerically it is represented by '0' aka 0 index
# by setting the '0' index or 1st piece of data in the list to 'laptop', it changes the list
new_cart = amazon_cart[0:3] # this line changes the original list by only selecting the first 3 pieces of data. Indexes 0, 1, and 2
new_cart[0] = 'gum' # this line of code substitutes the first piece of data in the 'new_cart' variable to 'gum'
print(new_cart) # prints '['gum', 'sunglasses', 'toys']
print(amazon_cart)

copy_cart = amazon_cart[:] # this is a way of copying a list without modifying it

# in line 14, if you get rid of '[0:3]' and just make it to where the line reads 'new_cart = amazon_cart'
# that is completely changing 'amazon_cart' if you follow with something like like 15
# 'amazon_cart' would now print whatever 'new_cart' prints