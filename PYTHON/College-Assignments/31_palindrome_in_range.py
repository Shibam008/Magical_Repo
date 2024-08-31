def checkPalindrome(num):
    original = num
    ans = 0
    
    while num != 0:
        rem = num % 10
        ans = ans*10 + rem
        num //= 10
    
    if original == ans:
        return True
    return False

def palindromeInRange(r1, r2):
    print(f"palindrom in range {r1} to {r2}")
    for n in range(r1, r2):
        if(checkPalindrome(n)):
            print(n, end = " ")
            
x = int(input("Range from : "))
y = int(input("to : "))

palindromeInRange(x, y)