def checkArmstrong(num):
    pow = len(str(num))
    original = num
    ans = 0
    
    while num != 0:
        rem = num % 10
        ans += rem ** pow
        num //= 10
    
    if original == ans:
        return True
    else:
        return False
    

num = int(input("Enter a number : "))

if(checkArmstrong(num)):
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not a armstrong number!")