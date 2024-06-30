
#* (*args) is used to take infinite arguments
#! it returns tuple data type
#* we can perform all tuple operations 


def sum_all(*args):
   print(args)
   return sum(args)  

def test(*args):
   print(args)
   for i in args:
      print(i ** 2)
   

print(sum_all(1, 2, 3, 4, 5))
print("\n")
test(2, 4, 6, 8)