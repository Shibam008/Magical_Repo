
#! Question :
'''
Write a generator function that yields even numbers up to a specified limit
'''

'''
#* yield keyword is used in generator functions to produce a series of values over time, rather than computing them all at once and returning them in a list, for example.

#* By using yield, you can process large datasets without loading everything into memory at once.
'''

def even_generator(limit):
   for i in range(2, limit+1, 2):
      return i
   
def even_generator_yield(limit):
   for i in range(2, limit + 1, 2):
      yield i
      
#// It will throw an error
# for num in even_generator(10):
#    print(num)

for num in even_generator_yield(10):
   print(num)