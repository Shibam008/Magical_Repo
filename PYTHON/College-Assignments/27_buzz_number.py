def checkBuzz(num):
    n = len(str(num))
    digit = str(num)
    if(num % 7 == 0 or digit[n-1] == '7'):
        return True
    else:
        return False
    
num = int(input("Enter a number : "))

if(checkBuzz(num)):
    print(f"{num} is a BUZZ number")
else:
    print(f"{num} is not a BUZZ number!")