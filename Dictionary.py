# Dictionary is a data type in python but it's also a data structure
# Data structure is a way to organize data i.e. list
# Dictionary is an unordered key value pair (not right next to each other)

dictionary = { # 'dictionary' can be named whatever you want in this example
    'a' : 1,
    'b' : 2,
    'x' : 3
}
print(dictionary) # prints '{'a': 1, 'b': 2, 'x': 3}'
print(dictionary['a']) # prints '1' because we are specifing what to print in this dictionary

# you can also include list, booleans, strings in dictionaries as well

dictionary_2 = {
    'a' : [1,2,3],
    'b' : 'hello',
    'x' : True
}
print(dictionary_2) # prints '{'a': [1, 2, 3], 'b': 'hello', 'x': True}'
print(dictionary_2['a'][1]) # prints '2' choosing to print from the list defined by 'a' and the '1' in [] is the specifc index from the list

my_list = [
    {
    'a' : [1,2,3],
    'b' : 'hello',
    'x' : True
},
{
    'a' : [4,5,6],
    'b' : 'hello',
    'x' : True
}
]
print(my_list[1]['b']) # prints 'hello'' the '1' in [] indicates we are pulling from the 2nd dictionary in the list, almost like the 2nd index, the 'b' represents what we want from the dictionary
print(my_list[0]['x']) # prints 'True' tge '0' in [] indicates we are pulling from the 1st index in the list which is the 1st 'dictionary', the 'x' is us asking specifically for what 'x' is defining