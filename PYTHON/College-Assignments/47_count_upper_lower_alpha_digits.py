# count uppercase, lowercase, alphabets, numbers
def count(s):
    up = 0
    low = 0
    alpha = 0
    digit = 0
    for ch in s:
        if ch.isupper():
            up += 1
        if ch.islower():
            low += 1
        if ch.isalpha():
            alpha += 1
        if ch.isnumeric():
            digit += 1
    print(f"Uppercase - {up}, Lowercase - {low}, Numbers - {digit}, Alphabets - {alpha}")
    
s = input("Enter string : ")
count(s)