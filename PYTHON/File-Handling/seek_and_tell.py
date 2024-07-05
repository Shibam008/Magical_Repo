
#! f.tell() returns the position of cursor in integer , counting the characters

#! f.seek() we can update/send our cursor to our expected position


with open('new_file2.txt', 'w') as f:
   f.write("hello my name is shibam sadhukhan aiming to become a software developer")
   print(f.tell()) 
   
   
   
with open('new_file2.txt', 'r') as f:
   f.seek(5)             # first it will point cursor in 5th position 
   
   print(f.read(10))   # from that 5th position it will read 10 characters 
   
   print(f.tell())   # now after reading 10 lines our cursor will be updated into (10 + 5) 15th position as our initial position was 5th 
