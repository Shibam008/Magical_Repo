def abecederian(w , a):
    for i in w:
        print(i + a , end =' ')
word = input("Please enter a word : ")
add = input("Enter Which you add with each letter of given word : ")
abecederian(word,add)