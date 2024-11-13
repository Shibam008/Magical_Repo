def findChar(s, x):
    idx = -1
    s.casefold()
    for ch in s:
        idx += 1
        if ch == x:
            print("Character found at index :",idx)
            break
    else:
        print("Character not found!")
        

s = input("Enter a string : ")
target = input("what char do you want to find ? Enter char : ")
findChar(s, target)

    
    