# string immutability - describes how you can't reassign part of a string
selfish = '01234567'
        #  01234567

#selfish[0] = '8'

#print(selfish)
# example above prints ''str' object does not support item assignment'
# the string can be fully changed but you can't alter any of the values in the string

selfish = selfish + '8'

print(selfish)
# the example above prints '012345678'
# 8 is added to the end of the string, "a whole new shelf space is created for us to use the new string"