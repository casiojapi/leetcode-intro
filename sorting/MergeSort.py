def mergeSort(arr):
    if len(arr) > 1:
        leftArr = arr[:len(arr)//2]  #left half of the array
        rightArr = arr[len(arr)//2:] #right half of the array
        mergeSort(leftArr)
        mergeSort(rightArr)

        i = 0   #left index
        j = 0   #right index
        k = 0   #base array index

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:    #if left index value is smaller than right index value
                arr[k] = leftArr[i]
                i += 1 
            else:                           # if right index value is smaller or equal than left index value
                arr[k] = rightArr[j]
                j += 1
            k +=1
        
        while i < len(leftArr):     # in case the are still values on the left array
            arr[k] = leftArr[i]
            i += 1
            k += 1
        
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1

test = [1, 3, 4, 1, 2,-122, -2,  7 , 4, 5, 2, 1,-2,  6, 11, 2, 44,-80000, -33 , 2 ,1 ,3, 2, 1 , 88, -1, -33, -2, 12]
print(test)
mergeSort(test)
print(test)
