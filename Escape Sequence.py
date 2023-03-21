# escape sequence is adding a '\' before a letter or special charcter to tell python it's apart of the string
# the example "*" is wrong, python thinks the string is only 'It'
# *weather = 'It's sunny'
# the correct way to do it is: added a '\' before the " ' " and the s
weather = 'It\'s sunny'
print(weather)
# the code above prints 'It's sunny'

# '\t' adds a tab spacing
weather = '\t It\'s \"kind of\" sunny'
print(weather)
# the code above prints '   It's "kind of" sunny'

# '\n' adds a new line
weather = '\t It\'s \"kind of\" sunny \n hope you have a good day'
print(weather)
# the code above prints '   It's "kind of" sunny
# hope you have a good day'