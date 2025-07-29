def counting(arr):
    if not arr:
        return arr
    
    max_val= max(arr)
    count=[0]*(max_val+1)
    for num in arr:
        count[num]+=1

    sorted_arr=[]
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_arr.append(i)

    return sorted_arr                
    

arr=[4,5,4,1,1,2,8,7,4,0,3]

counting(arr)
print(counting(arr))