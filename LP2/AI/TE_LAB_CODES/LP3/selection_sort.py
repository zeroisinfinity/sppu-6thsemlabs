# ============================================================
# QUESTION:
# Implement Greedy Algorithm using Selection Sort
# to sort elements in ascending order.
# ============================================================


# ============================================================
# EXPLANATION:
#
# Selection Sort is a simple sorting algorithm
# based on the Greedy approach.
#
# It selects the smallest element from the
# unsorted part and places it at the correct position.
#
# Steps:
# 1. Assume first element is minimum.
# 2. Compare it with remaining elements.
# 3. Find smallest element.
# 4. Swap with first position.
# 5. Repeat for remaining list.
#
# Time Complexity:
# Best Case = O(n²)
# Worst Case = O(n²)
# ============================================================


# ============================================================
# EXPLANATION WITH EXAMPLE:
#
# Consider array:
# [64, 25, 12, 22, 11]
#
# Step 1:
# Find minimum → 11
# Swap with first element
#
# [11, 25, 12, 22, 64]
#
# Step 2:
# Find minimum from remaining → 12
#
# [11, 12, 25, 22, 64]
#
# Step 3:
# Find minimum → 22
#
# [11, 12, 22, 25, 64]
#
# Final Sorted Array:
# [11, 12, 22, 25, 64]
# ============================================================


# ======================
# SELECTION SORT PROGRAM
# ======================

def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:

                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Driver Code

arr = [64, 25, 12, 22, 11]

print("Sorted Array:", selection_sort(arr))