my_list = [1, 2, 3, 4, 5]
s = 0
e = len(my_list) - 1

while(s < e):
    temp = my_list[s]
    my_list[s] = my_list[e]
    my_list[e] = temp
    s += 1
    e -= 1
    
print("Reversed list : ",my_list)