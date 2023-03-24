def merge_arrays(arr1, arr2):
    p1, p2, m1 = 0, 0, 0
    merge = [0] * (len(arr1) + len(arr2))
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] <= arr2[p2]:
            merge[m1] = arr1[p1]
            p1+=1
        else:
            merge[m1] = arr2[p2]
            p2+=1
        m1 += 1

    if p1 >= len(arr1):
        while p2 < len(arr2):
            
            merge[m1] = arr2[p2]
            p2+=1
            m1+=1
    else:
        while p1 < len(arr1):
            merge[m1] = arr1[p1]
            p1+=1
            m1+=1 
    return merge

purge = merge_arrays(arr1, arr2)
print(purge)
