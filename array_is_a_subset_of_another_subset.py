def isSubset(arr1, arr2):
    hash = {}
    for i in arr1:
        hash[i] = i

    for j in arr2:
        if not (j in hash):
            return False
    
    return True

arr1 = [11,1,13,21,3,7]
arr2 = [11,3,7,1]

print(isSubset(arr1,arr2))  # TRUE