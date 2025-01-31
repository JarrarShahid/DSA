# 1. Understanding How Selection Sort Works
# Selection sort is a simple and intuitive sorting algorithm. The main idea is to divide the list into two parts: the sorted part and the unsorted part.

# Initially, the entire list is unsorted.
# In each iteration, the algorithm finds the smallest element from the unsorted part and swaps it with the first element of the unsorted part, effectively growing the sorted section by one.
# Example: Given [29, 10, 14, 37, 13]

# Pass 1: Find the smallest element (10). Swap it with the first element. [10, 29, 14, 37, 13]
# Pass 2: Find the smallest in the remaining part (13). Swap it with the second element. [10, 13, 14, 37, 29]
# Continue until the list is completely sorted: [10, 13, 14, 29, 37]

# 2. How to Think of Applying the Solution
# To apply the solution, break it down like this:

# Identify the smallest element: Loop through the unsorted portion of the list to find the smallest element.
# Swap the smallest element: Swap it with the first element of the unsorted portion.
# Shrink the unsorted portion: Incrementally reduce the unsorted section by moving to the next index.
# Repeat: Continue until the entire list is sorted.

# 3. Pseudo Code

# Step 1: Start from the first element and iterate until the second last element.
# Step 2: For each position, assume it contains the smallest value.
# Step 3: Look through the unsorted part of the list to find an even smaller element.
# Step 4: If a smaller element is found, swap it with the current element.
# Step 5: Move to the next position and repeat until the entire list is sorted.

def selection_sort(arr):
    # Loop through each element of the list except the last one
    n = len(arr)
    for i in range(n - 1):
        # Assume the current position holds the smallest element
        min_index = i

        # Find the index of the smallest element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update min_index if a smaller element is found

        # Swap the found minimum element with the current element
        # Only swap if min_index has changed to avoid unnecessary swaps
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print(f"Swapped {arr[min_index]} with {arr[i]}: {arr}")  # Debug statement

    return arr

# Example usage
arr = [29, 10, 14, 37, 13]
print("Original Array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted Array:", sorted_arr)
