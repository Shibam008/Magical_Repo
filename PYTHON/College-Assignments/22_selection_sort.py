arr = [5, 7, 8, 1, 3, 2, 4]
print("Actual array : ", arr)

n = len(arr)
for i in range(0, n-1):
    minIdx = i
    for j in range(i+1, n):
        if(arr[j] < arr[minIdx]):
            minIdx = j
    temp = arr[i]
    arr[i] = arr[minIdx]
    arr[minIdx] = temp
    
print("Selection sort : ", arr)