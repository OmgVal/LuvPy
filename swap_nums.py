a = input('enter value of a= ')
b = input('enter value of b= ')

# you need a temporary variable to swap values (could take any name not just 'temp') -- if you do not provide a temp variable then swap will not work 

temp = a
a=b
b=temp

print('a=', a)
print('b= ' + b)