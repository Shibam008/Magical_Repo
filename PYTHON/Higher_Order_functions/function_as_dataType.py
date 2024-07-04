def func(n):
   return n ** 2

square = func
print(type(square))
print( square(4) )

my_list = [1, 3, 4, square]
print(my_list[-1])
ans = my_list[-1](5)
print(ans)