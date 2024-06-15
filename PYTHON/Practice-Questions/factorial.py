def fact(n):
   if  n == 0:
      return 1
   else:
      return n * fact(n-1)

num = int(input("Enter a number : "))
ans = fact(num)
print("Factorial of ",num,"is = ",ans)
