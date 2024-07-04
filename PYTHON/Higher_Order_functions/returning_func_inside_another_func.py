
#* Example 1 
def func():
   def func1(n):
      return n ** 2
   return func1

print( func()(4) )


#* Example 2
def func2(n1):
   def func3(n2):
      return n1 + n2
   return func3

print( func2(8)(5) )