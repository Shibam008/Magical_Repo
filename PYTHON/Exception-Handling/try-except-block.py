
try :
   num = int(input("Enter an integer : "))
   div = 15/num
   print(div)
except :
   print("Wrong input!")
   
   
my_list = [1,2,3,4,5,6,8,9,10]

double = list(map(lambda val : val * 2, my_list))
print(double)

even = list(filter(lambda val : val % 2 == 0, my_list))
print(even)

from functools import reduce
print(reduce(lambda x,y : x if (x > y) else y, my_list))

#* in this code even if we enter a wrong input at first our rest code will run . That's the beauty of exception handling