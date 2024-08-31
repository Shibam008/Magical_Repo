num = int(input("Enter a number : "))
original = num
ans = 0 

while num != 0:
    rem = num % 10
    ans = ans*10 + rem
    num //= 10

if original == ans :
    print(f"{original} is a palindrom number")
else:
    print(f"{original} is not a palindrom number")

    