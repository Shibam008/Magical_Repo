def binSearch(arr, x):
    s = 0
    e = len(arr)-1
    
    while(s <= e):
        
        mid = s + (e-s)//2
        
        if(arr[mid] == x):
            return True
        elif(arr[mid] < x):
            s = mid + 1
        else:
            e = mid - 1
            
    return False

arr = [1, 2, 3, 4, 5, 9, 10, 15, 18]
target = int(input("Enter target value : "))

if(binSearch(arr, target)):
    print("Target Found")
else:
    print("Target not found!")
        