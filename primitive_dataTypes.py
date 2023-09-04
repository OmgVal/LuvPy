# Data types are known as classes and the Variable you create are known as instance/objects of those Classes

# var_1 = 3
# the function type() can be used to figure out the type of variable being used
# print(type(var_1))
# when you run this code it will return:
    # <class 'int'> -- class type is an integer
    # other class(data) types:
        # int
        # float
        # string
        # boolean
# an integer can be any length you want:
# var = 12344626625546352727
# with no prefix this long number is considered a decimal(base 10) number

# Number System prefixes (starts with zero):
    # Binary: 0b or 0B
    # Octal: 0o or 0O
    # Hexadecimal: 0x or 0X

# var_1 = 0o123
# var_2 = 0x123
# var_3 = 123

# #octal
# print(var_1)
# #hexadecimal
# print(var_2)
# print(var_3)

# #check types
# print(type(var_1))
# print(type(var_2))
# print(type(var_3))

# name_1 = 'Zayn Malik'
# name_2 = 'Harry Styles'
# a = 12

# # # type: string
# # print(type(name_1))

# # get strings index/key value using brackets []
# # @ index 4 you have a space "zayn malik" so you will receive "space"/nothing back
# # print(name_1[4])

# # concatenating
# print(name_1 + name_2)

# # you can only concatenate str (not "int") to str -- you will have to convert the datatypes both into STR before concatenating 
# print(name_2 + a)

# you can use backslash to "skip" the special meaning of something
# print('Jenny\'s \'lectures \'')
# print('Hello \\n World!') #\n means new line but you can cancel it by adding a backslash to it to void its meaning 

# #you can print string multiple times using * (multiplication symbol)
# print(5 * 'Jenny\'s \'lectures \'')

###################
##### BOOLEAN #####
###################

# var = True # You must us a Capital "T"/"F" to keep the datatype as Boolean
a = 1
b = 2
var = a > b #check if this is true or false
print(var)
print(type(var))

