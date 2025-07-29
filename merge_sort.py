def merge_sort(merge_list):
    if len(merge_list) <=1:
        return merge_list

    mid = len(merge_list) // 2
    left_half = merge_list[:mid]
    right_half= merge_list[mid:]

    sorted_left= merge_sort(left_half)
    sorted_right=merge_sort(right_half)

    return merge(sorted_left,sorted_right)

def merge(left,right):
    result =[]
    i=j=0

    while i< len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1  
        elif left[i] > right[j]:
            result.append(right[j])
            j+=1
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])  
        j+=1

    return result        

    
print("===BEFORE-MERGE-SORT===")
merge_list=[12,8,9,3,11,5,4]
print(merge_list)

mySortedlist=merge_sort(merge_list)
print("===AFTER-MERGE-SORT===")

print(mySortedlist)