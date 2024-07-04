
#* Question
'''
Write a decorator that measures the time, a function takes to execute 
'''

import time

def func_timer(func):
   def wrapper(*args, **kwargs):
      start = time.time()
      result = func(*args, **kwargs)
      end = time.time()
      print(f"{func.__name__} ran in {end-start} time")
      return result
   return wrapper      

@func_timer
def exmpl_func(n):
   time.sleep(n)
   
exmpl_func(3)