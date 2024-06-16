def armstrong(num):
   size = len(str(num))
   ans = 0
   original = num 
   
   while num != 0:
      lastDigit = num % 10
      ans += lastDigit ** size
      num //= 10
      
   if ans == original:
      print("it is a armstrong number")
   else:
      print("Not an armstrong")
      
      
n = int(input("Enter a number : "))
armstrong(n)      

      