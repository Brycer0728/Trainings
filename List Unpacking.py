# List Unpacking
a,b,c,d, *other, e = [1,2,3,4,5,6,7,8,9]

print(a) # pritns '1'
print(b) # prints '2'
print(c) # prints '3'
print(d) # prints '4'
print(other) # prints '[5, 6, 7, 8, 9]' the remaining items in the list that have not been assigned a variable
print(e) # prints '9' I think it is because 'e' is the last variable so it automatically prints the list item in the list
