def fibonacci(n):
   if(n <= 1):
      return n
   else:
      return fibonacci(n-2) + fibonacci(n-1)

nterms = int(input("How many terms ? : "))

if nterms <= 0:
   print("please enter a positive integer number")
else:
   print("Fibonacci sequence : ")
   for i in range(nterms):
      print(fibonacci(i))