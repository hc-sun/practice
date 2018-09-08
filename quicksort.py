def quicksort(arr): # Hoare partition scheme
    quicksort_helper(arr, 0, len(arr)-1)

def quicksort_helper(arr, start, end):
    if start < end:
        index = partition(arr, start, end)
        quicksort_helper(arr, start, index-1)
        quicksort_helper(arr, index+1, end)

def partition(arr, start, end):
    pivot = arr[start]
    leftmark = start + 1
    rightmark = end

    done = False
    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivot:
            leftmark += 1 # value>pivot
        while rightmark >= leftmark and arr[rightmark] >= pivot:
            rightmark -= 1 # value<pivot
        if leftmark > rightmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp
    temp = arr[start]
    arr[start] = arr[rightmark]
    arr[rightmark] = temp
    return rightmark

test = [65,3,76,8,34,5,4,21,33,62]
quicksort(test)
print(test)


# def switch(arr):
#     pivot_index = len(arr) - 1
#     for i in len(arr) - 1:
#         if arr[i] > arr[pivot_index] and i < pivot_index:
#             temp = arr[pivot_index]
#             arr[pivot_index] = arr[i]
#             arr[i] = arr[pivot_index-1]
#             pivot_index -= 1
#             arr[pivot_index] = temp