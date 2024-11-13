# return ascii value of each first character of a string

def findAscii(s):
    word_list = list(s.split())
    for word in word_list:
        print(f"ASCII value of '{word[0]}' -> {ord(word[0])}")

s = input("Enter string : ")
findAscii(s)