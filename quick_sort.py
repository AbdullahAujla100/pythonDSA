def quickSort(arr,low,high):
    if low < high:
        pivot=partition(arr,low,high)
        quickSort(arr,low,pivot-1)
        quickSort(arr,pivot+1,high)


def partition(arr, low,high):
    piv=arr[low]
    i=low+1
    j=high
    while True:
        while i <=j and arr[i] <= piv:
            i+=1
        while i <=j and arr[j] >= piv:
            j-=1
        if i<=j:
            arr[i],arr[j]= arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]

    return j                



print("==BEFORE-QUICK-SORT==")
myList=[64, 34, 25, 5, 22, 11, 90, 12]
print(myList)
print("==AFTER-QUICK-SORT==")
quickSort(myList,0,len(myList)-1)
print(myList)
