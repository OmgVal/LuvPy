# print(len('Zayn Malik')) #Len() function only works with a string 
# print(len(12345)) #returns a TypeError for int
# print(len('12345')) #works because its a string

# length = len('Zayn Malik')
# print('your name has ' + length + ' characters') # TypeError because "length" returns an int and you can only concatenate same datatypes
# Correct way: use str() function to convert variable(length)
# print('your name has ' + str(length) + ' characters') 

# if you are not sure what datatype you have use type() function
# print(type(length)) # code prints: <class 'int'>

# Other types of conversion functions:
    # int()
    # float()
    # str()

############################
####### CONVERSIONS ########
############################

# print(10 + 10) 
# print('10' + '10')
# print(int('10') + int('10')) #conversion 
# print(10 + float('10')) # float conversion

# incorrect way to convert
# name = 'chloe'
# print(10 + int(name)) #ValueError: invalid literal for int() with base 10: 'chloe'

# Exercise: take input from user and add it to a number
# my solution:
# num1 = int(input('Hello, please give me the 1st number:'))
# num2 = int(input('Hello, please give me the 2nd number:'))
# answer = num1 + num2
# print(str(num1) + " + " + str(num2) + ' = ' + str(answer))

# Jenny's Solution:
num1 = input('enter 1st num:')
num2 = input('enter 2nd num:')

# sum = num1 + num2

# # This is wrong because the input it receives is a string automatically. When you concatenate it returns the two inputs next to each other and does not actually add 2 integers. Datatype remained as a str the entire time. 
# print(sum)

# Correct way is to convert data into an int
sum = int(num1) + int(num2)
print(sum)
