# Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
new_array = [10,9,8,7,6,5,4,3,2,1]

print(bubble_sort(my_array))
print(bubble_sort(new_array))
