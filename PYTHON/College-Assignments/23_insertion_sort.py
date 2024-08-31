arr = [12, 18, 16, 11, 13, 14]
print("Actual array : ", arr)

n = len(arr)
for i in range(0, n-1):
    j = i+1
    while(j > 0 and arr[j] < arr[j-1]):
        temp = arr[j]
        arr[j] = arr[j-1]
        arr[j-1] = temp
        j -= 1
        
print("insertion sort : ", arr)
        
        