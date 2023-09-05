########################
###### OPERATORS #######
########################

# +
# -
# / - division will always return a float number (4/2 gives 2.0). if you do not want a float you will use two '//' (called floor division) and this will give you an integer. Anything after the decimal is ignored when doing this.
# * - one star is regular multiplication but double (**) is used for "power of". 
# % - modulus operator gives you what remains ( ex: 5%2 gives you 1)

#####################
### ArithmeticOps ###
#####################
# PEMDAS
    # () -- gives priority to anything inside of it
    # ** -- solved right to left
    # *, /, //, % -- solved Left to Right
    # +, - -- solved Left to Right

# Exercise:
# print( 5 + 2 * 3 - 1 + 10 / 5) # answer is 12.0 -- add () to change your answer to 11.0

# my solution: 
# print( 5 + 2 * (3 - 1) + 10 / 5)

# Exercise 2: calc BMI -- formula is weight/(height * height) (height to the power of 2)
    # weight(kg) is an int and height(m) has to be a float
#my solution: 

weight = int(input('what is your weight using kg: '))
height = float(input('what is your height using meters: '))
print(weight / (height * height))



