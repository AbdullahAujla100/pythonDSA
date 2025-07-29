def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]





arr=[64, 34, 25, 12, 22, 11, 90, 5]
print ("==BEFORE-SORTING==")
print(arr)
print ("==ATFER-SORTING==")
bubbleSort(arr)
print(arr)

