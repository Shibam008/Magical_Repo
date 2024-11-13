strn = input("Enter a string : ")
total_words = list(strn.split())
max_word_len = 0

for word in total_words:
    x = len(word)
    if x > max_word_len:
        max_word_len = x
        
print(f"Length of the maximum word '{word}' is = {x}")
        
