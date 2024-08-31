def linearSearch(arr, x):
    for i in arr:
        if i == x:
            return True
    else:
        return False
    
arr = [5, 8, 6, 9, 2, 3]
target = int(input("Enter target value : "))

if(linearSearch(arr, target)):
    print("Target found")
else:
    print("Target not found!")

    