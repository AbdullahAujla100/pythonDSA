def insertion(arr):
    n=len(arr)
    for i in range(1,n):
        key= arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key




arr=[20,30,10,5,1,40]
print(arr)
insertion(arr)
print(f"INSERTED-ARRAy{arr}")
