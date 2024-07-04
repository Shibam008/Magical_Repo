def add(a, b):
   return a + b

def mul(a, b):
   return a * b

def operation(a, b, func):
   return func(a, b)


print( operation(5, 8, add) )

# we will see some optimized example using lambda function
   