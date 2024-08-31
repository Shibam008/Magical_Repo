def checkPronic(num):
    flag = 0
    for i in range(1, num+1):
        if (i*(i+1)) == num :
            flag = 1
            break 
    if(flag == 1):
        return True
    return False

num = int(input("Enter a number : "))

if(checkPronic(num)):
    print(num, " is a pronic number")
else:
    print(num, " is not a pronic number")