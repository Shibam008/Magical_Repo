
#! for using this reduce func we first have to import 

#* Key points :
'''
   1. It always uses only two variables (like two pointer approach)
   2. unlike map and filter we can directly print the result
   3. usecses : a) biggest num in list  b) sum of elements etc
'''
from functools import reduce

nums = [1, 5, 8, 9, 21, 50]
print( reduce(lambda x,y : x+y, nums)) # sum 

print( reduce(lambda x,y : x if (x > y) else y, nums)) # largest elem

