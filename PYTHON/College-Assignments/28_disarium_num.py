def checkDisarium(num):
    n = len(str(num))
    original = num
    ans = 0 
    while n != 0 :
        rem = num % 10
        ans += rem ** n
        num //= 10
        n -= 1
    if original == ans :
        return True
    return False

num = int(input("Enter number : "))

if(checkDisarium(num)):
    print(f"{num} is a disarium number")
else:
    print(f"{num} is not a disarium number")