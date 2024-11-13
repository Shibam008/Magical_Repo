def countFrequency(strn, x):
    cnt = 0
    for ch in strn:
        if(ch == x):
            cnt += 1
    return cnt

strn = input("Enter string : ")
target = input("Enter target : ")
ans = countFrequency(strn, target)
print(ans)