def countFreq(s, x):
    cnt = 0
    s.casefold()
    for ch in s:
        if ch == x:
            cnt += 1
    return cnt

strn = input("Enter a string : ")
target = input("Enter your target character : ")
ans = countFreq(strn, target)

if ans:
    print("Frequency of given char : ", ans)
else:
    print("Character not found!")
