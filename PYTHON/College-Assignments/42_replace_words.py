def replace_word(s, old_word, new_word):
    return s.replace(old_word, new_word)

strn = input("Enter your sentence : ")
old_word = input("Which word do you want to replace ? : ")
new_word = input("to which ? : ")

print(replace_word(strn, old_word, new_word))
    