

#* When we use 'r' mode , check if the file exists. Else you will get an error.

file = open('new_file.txt', 'r')
#count_line = 0
while True:
   #count_line += 1
   data = file.readline()
   if data == '':
      break
   #print(count_line)
   print(data)
   

