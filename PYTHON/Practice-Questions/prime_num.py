def isPrime(n):
   if(n == 1):
      print("not a prime")
      
   if (n > 1):
      for i in range(2,n):
         if(n % i == 0):
            print("Not prime")
            break
      print("it is prime")
         
         
num = int(input("Enter a number : "))
isPrime(num)
