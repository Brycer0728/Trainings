# Common List Patterns

# 'range' allows you to generate a list quickly
# range(x,y) x = where to start for the list, and y = where to stop
# you can also just put a number, 'range(100)' and it will start at and go to 99
print(list(range(1,101)))
# line 6 prints every number starting with 1 and ending with 100
print(list(range(51)))
# line 9 prints every number starting with 0 and ending with 50
# since there wasn't a specified number that we should start with, it just defaults to 0

# '.join()' combines lists into a string
new_sentence = ' '.join(['hi', 'my','name', 'is', 'Bryce'])
print(new_sentence)
# line 14 prints 'hi my name is Bryce'