# creating a program that guesses your age

birth_year = input('What year were you born? ')
age = 2023 - int(birth_year) # had to change birth year into a number using the 'int()' data type, this is type conversion
# used a formated string below to be able to import data into the string, imported data is 'age'
print(f'Your age is: {age}')