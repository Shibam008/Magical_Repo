
#* Concept of serialization and deserialization
'''
   Serialization and deserialization, also known as pickling and unpickling in Python, are processes used to convert complex data structures(dict, list, tuple), such as objects or data collections, into a format that can be easily stored or transmitted and then reconstructed later
   
   
   Object serialization is the process of converting state of an object into byte stream. This byte stream can further be stored in any file-like object such as a disk file or memory stream. It can also be transmitted via sockets etc. Deserialization is the process of reconstructing the object from the byte stream.
   
   
   *  text,python object --> byte  = Serialization
   *  byte --> python object = Deserialization
   *  byte stream --> JSON format
   #! import json
   *  will be creating files with .json extension
   *  json.dump()  --> used in serialization
   *  json.load()  --> used in deserialization / (even we can read/print file data)
'''

# Specially we can't store complex data structures into a file without using this concept, even if we are able to store using type casting to str() we can't read that data from file . That's why this concept comes and very useful.

   
   
   
#! Example what should not be done
#---------------------------------------------------------------------
my_dict = {
   'name' : 'Shibam',
   'age' : 19,
   'town' : 'Gobardanga'
}

#* We can't store dictionary as it is that's the drawback
# with open('new_file.txt','w') as file:
#    file.write(my_dict)

#* typecasting dict to str 
with open('new_file.txt','w') as file:
   file.write(str(my_dict))

# with open('new_file.txt','r') as file:
#    print(file.read())
#    print(file.read(my_dict))
#---------------------------------------------------------------





#! Example what should actually be done
#--------------------------------------------------

import json

new_dict = {
   'name' : 'Shibam',
   'age' : 19,
   'town' : 'Gobardanga',
   'pin' : 743273
}

with open('test.json','w') as file:
   json.dump(new_dict, file, indent = 4)

with open('test.json','r') as file:
   data = json.load(file)
   print(data)
#--------------------------------------------------
   
   


