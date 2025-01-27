def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found


arr = [1, 6, 8, 9, 3, 7, 5, 2]
arr.sort()  # Sorting the array
print("Sorted Array:", arr)

target = 7
result = binarySearch(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found.")
