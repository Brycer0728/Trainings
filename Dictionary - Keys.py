# Dictionary keys have to be immuatble (something that is unable to change), can't use lists because lists can change
# a key is usually something descriptive, like a string
# whenever you use the same key, the last value overrides the previous one

dictionary = {
    'a' : '123',
    'a' : 'hello'
}
print(dictionary['a']) # prints 'hello' due to line 7 overriding line 6