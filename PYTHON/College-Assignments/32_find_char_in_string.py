def findChar(strn, target):
    cnt = 0
    for char in strn:
        cnt+=1
        if(char == target):
            print("Target found at index : ",cnt)
            break
    else:
        print("Target not found!")


strn = input("Enter a string : ")
target = input("Enter your target character : ")
findChar(strn, target)
