# Bubble Sort

# How it functions:

# 1. Go through the list, checking one item at a time.
# 2. Compare each item with the one next to it.
# 3. If the item is bigger than the next one, swap them so the bigger one goes last.
# 4. Do this for as many times as there are items in the list.

# To use the Bubble Sort in a program, you need:

# 1. A list of numbers that you want to sort.
# 2. A loop inside the program that goes through the list and swaps numbers if the first one is bigger than the next one. This loop should get shorter each time it runs.
# 3. A loop outside that controls how many times the inner loop should run. If the list has n items, this loop should run n-1 times.

def bubble_sort(arr):
    n = len(arr)  # Get the length of the list
    for i in range(n-1):  # Outer loop: repeat the process n-1 times
        for j in range(n-i-1):  # Inner loop: compare adjacent elements
            if arr[j] > arr[j+1]:  # If the current element is greater than the next one
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap them
    return arr  # Return the sorted list


my_array = [64, 34, 25, 12, 22, 11, 90, 5]
new_array = [10,9,8,7,6,5,4,3,2,1]

print(bubble_sort(my_array))
print(bubble_sort(new_array))
