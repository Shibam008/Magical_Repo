x = float(input("Enter first number : "))
y = float(input("Enter second number : "))
oper = input("Which operation do you want to perform ? (+, -, *, /) || Enter choise : ")

if oper == '+':
    res = x + y
    print(f"addition of {x} and {y} is = {res}")
    
elif oper == '-':
    res = x - y
    print(f"subtraction of {x} and {y} is = {res}")
    
elif oper == '*':
    res = x * y
    print(f"multiplication of {x} and {y} is = {res}")
    
elif oper == '/':
    res = x / y
    print(f"division of {x} and {y} is = {res}")
    
else:
    print("Wrong operation entered!")