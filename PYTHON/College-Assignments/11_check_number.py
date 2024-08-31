def checkNumber(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative Number")
    elif num == 0:
        print("It's Zero")

num = int(input("Enter a number : "))
checkNumber(num)
