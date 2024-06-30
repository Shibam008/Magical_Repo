

#* Question : 
''' 
create a function that accepts any number of keyword arguments and prints them in the format 
key : value
'''

def print_kwargs(**kwargs):
   for key, value in kwargs.items():
      print(f"{key}: {value}")

print_kwargs(name = "Shibam", age = 18, city = "Gobardanga")
print_kwargs(name = "Anik", age = 20, city = "Barasat")
print_kwargs(name = "Shovan", age = 18, vill = "Bankura")