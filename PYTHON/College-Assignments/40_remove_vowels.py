def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return "".join([ch for ch in s if ch not in vowels])

s = input("Enter a string : ")
print("Output : ",remove_vowels(s))

        
    