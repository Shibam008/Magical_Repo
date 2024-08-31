def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    return True

def primesInRange(r1, r2):
    for n in range(r1, r2+1):
        if (isPrime(n)):
            print(n, end = " ")
            
x = int(input("Enter starting of range : "))
y = int(input("Enter ending of the range : "))

primesInRange(x,y)

