def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        arr = merge(merge_sort(arr[:m]), merge_sort(arr[m:]))    
    return arr

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
test = [65,3,76,8,34,5,4,21,33,62]
arr = merge_sort(test)
print(arr)