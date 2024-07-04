
#* Key feature or point about lambda function :
'''
   1. One line
   2. No return value
   3. Not Reuseable
   4. No name required
   5. require only input and logic **
   6. No syntax
   7. Annonymous Function **
'''


#* Example 1  -------------

exmpl = lambda num : num ** 2
print( exmpl(8) )


#* Example 2  --------------------

def operation(a, b, func):
   return func(a, b)

print( operation(5, 8, lambda a, b : a + b))
print( operation(5, 8, lambda a, b : a * b))


#* Example 3  -----------------

strn = "My name is Shibam"
check = lambda strn : 'a' in strn
print( check(strn) ) 