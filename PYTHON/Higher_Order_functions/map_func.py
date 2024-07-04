
#! Usecase
'''
   when we have to apply any condition in entire list item.
   example : if we want to return square of every element present in a list
'''

# map( func, iterable )

#* Example 1
my_list = [4, 5, 6, 7]
ans = list(map(lambda elem : elem ** 2, my_list))
print(ans)

#* Example 2
words = ["mango", "apple", "banana", "orange"]
ans1 = list(map(lambda word : word.capitalize(), words))
print(ans1)