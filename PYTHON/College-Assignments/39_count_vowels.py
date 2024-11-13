strn = input("Enter a string : ")
cnt = 0
for ch in strn:
    if ch in "aeiou" and "AEIOU":
        cnt += 1
print(f"total number of vowel : {cnt}")