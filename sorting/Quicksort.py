def quicksort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    pivot = arr.pop()
    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
        
    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

test = [5, 2, 1, 5, 2,-1, -33, 22, 1,2, 3,5, 2, -2 ,433, -999221, 76, 6, 3]
print(test)
sorted = quicksort(test)
print(sorted)
