def fibo(n):
    if n <= 0:
        return "Input should be higher than 0"
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fibo(n-1) + fibo(n-2)

num = int(input("How many terms of fibonacci sequence do you want ? : "))
print(f"Fibonacci sequence upto {num} terms is : ", end = " ")
for i in range(1, num+1):
    ans = fibo(i)
    print(ans, end = " ")