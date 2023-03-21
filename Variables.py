# variables store information that can be used in our programs/code
# example below is if someone took an IQ test and  scored a 190, the variable 'iq' is 190
# assigning the value (190 in the example) to the variable is called binding
iq = 190
# best practices for variables are listed below
# snake_case
# start with lowercase or underscore
# letters, numbers, underscores
# case sensitive
# don't overwrite keywords
# end of list

# variables can be reassigned
user_age = iq/4
# example above prints '47.5' because 190 is bound to 'iq' 190/4 equals 47.5
print(user_age)

# constants never change in a program, the value never changes
# constants need to be in all capital leters
PI = 3.14

# to rapidly assign values to variables, list the variables and values with commas in between
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)