# ---------- Linear Search ----------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# ---------- Binary Search (iterative) ----------
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"  low={low}, high={high}, mid={mid}, arr[mid]={arr[mid]}")

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1      # search right half
        else:
            high = mid - 1     # search left half

    return -1




# ---------- Main ----------
if __name__ == "__main__":
    numbers = [3, 8, 12, 25, 31, 47, 60]
    print("List:", numbers)

    print("\nLinear Search for 25:")
    idx = linear_search(numbers, 25)
    print(f"  Found at index {idx}" if idx != -1 else "  Not found")

    print("\nBinary Search for 47:")
    idx = binary_search(numbers, 47)
    print(f"  Found at index {idx}" if idx != -1 else "  Not found")

    print("\nBinary Search for 10:")
    idx = binary_search(numbers, 10)
    print(f"  Found at index {idx}" if idx != -1 else "  Not found")
