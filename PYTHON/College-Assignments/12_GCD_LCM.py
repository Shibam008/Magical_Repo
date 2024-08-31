def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a*b//gcd(a, b)

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

gcdAns = gcd(num1, num2)
lcmAns = lcm(num1, num2)

print(f"GCD = {gcdAns} and LCM = {lcmAns}")