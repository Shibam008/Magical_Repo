def convertBinary(num):
   if num > 1:
      convertBinary(num//2)
   print(num % 2, end='')

dec = int(input("Enter decimal number : "))
convertBinary(dec)