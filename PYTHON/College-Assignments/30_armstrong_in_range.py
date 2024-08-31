def checkArmstrong(num):
    pow = len(str(num))
    original = num
    ans = 0
    
    while num != 0:
        rem = num % 10
        ans += rem ** pow
        num //= 10
    
    if(original == ans):
        return True
    return False

def armstrongInRange(r1, r2):
    print(f"amrstrong numbers in range {r1} to {r2} are : ")
    for n in range(r1, r2+1):
        if(checkArmstrong(n)):
            print(n, end = " ")
            
x = int(input("Range from : "))
y = int(input("to : "))

armstrongInRange(x, y)
