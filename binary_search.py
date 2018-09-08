def binary_search(arr, element):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if element < arr[mid]:
            right = mid - 1
        elif element > arr[mid]:
            left = mid + 1
        else:
            return True
    return False
# O(log(n))