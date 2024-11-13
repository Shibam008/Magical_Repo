strn = input("Enter your paragraph seperated by '.' : \n")
cnt = 0
for ch in strn:
    if ch == '.':
        cnt += 1
        
print("Total lines : ", cnt)
