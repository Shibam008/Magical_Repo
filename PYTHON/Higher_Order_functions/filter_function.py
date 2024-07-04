# filter( func , iterable)

#* Qn -> Given a list of word, print all the words whose length is greater than or equal 4 


#* Example 1
words = ["Ram", "Joy", "Shibam", "Anik"]
ans = list(filter(lambda word : len(word) >= 4, words))
print(ans)


#* Example 2
nums = [10, 15, 14, 81, 65, 32, 64]
res = list(filter(lambda val : val % 2 == 0, nums))
print(res)