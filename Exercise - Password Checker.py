# Password Checker Exercise
# my answer is below
# username = input('Username: ' )
# password = input('Password: ')
# hidden_pw = '*' * 6

# print(f'{username}, your password {hidden_pw} is {len(password)} letters long.')
# my example above printed 'Brycer, your password ****** is 6 letters long.'
# hidden_pw in my example is a pre-determined value and cannot be changed, shoud be like the 'hidden_pw' in Andrei's answer below

# Andrei's answer is below
username = input('What is your username? ')
password = input('What is your password? ')

#print(f'{username}, your password, {password}, is {len(password)} letters long.')

# to make the code a little more readable you can add a variable for 'len(password)'
# need to add a variable for the 6 '*'s so the password isn't showing

pw_length = len(password)
hidden_pw = '*' * pw_length # this makes it to where 'hidden_pw' is not pre-determined and depends on what the user inputs

print(f'{username}, your password, {hidden_pw}, is {pw_length} characters long.')
# the above line of code prints 'Brycer, your password, *********, is 9 characters long.'