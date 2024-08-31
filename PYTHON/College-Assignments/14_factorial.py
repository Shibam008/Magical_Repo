def fact(num):
    if num == 0 or num == 1:
        return 1
    return num * fact(num-1)

n = int(input("Enter a positive integer number : "))
ans = fact(n)
print(f"Factorial of {n} = {ans}")