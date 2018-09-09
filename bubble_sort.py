def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
test = [65,3,76,8,34,5,4,21,33,62]
bubble_sort(test)
print(test)
# O(n^2)