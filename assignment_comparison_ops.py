# assignment op "=" needs a var/container on the left side(a = 5). you cannot have the value on the left(5 = a).
# Shorthand Ops:
    #Operator	Shorthand	Expression	Description
    # +=	x+=y	x = x + y	Adds 2 numbers and assigns the result to left operand.
    # -=	x-= y	x = x -y	Subtracts 2 numbers and assigns the result to left operand.
    # *=	x*= y	x = x*y	Multiplies 2 numbers and assigns the result to left operand.
    # /=	x/= y	x = x/y	Divides 2 numbers and assigns the result to left operand.   
    # %=	x%= y	x = x%y	Computes the modulus of 2 numbers and assigns the result to left operand.
    # **=	x**=y	x = x**y	Performs exponential (power) calculation on operators and assign value to the equivalent to left operand.
    # //=	x//=y	x = x//y	Performs floor division on operators and assign value to the left operand.

# Another short var assignment option is:
    # a, b, c = 5, 6, 7

# a, b = 4, 3
# c = a + b
# a += 2
# c += a
# print(c)

a = 5
print(a == 5) # True
print(a <= 5) # True
print(a < 5) # False
print((a + 1) != 6) # False

# exercise