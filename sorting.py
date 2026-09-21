# ---------- Bubble Sort ----------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"  Pass {i + 1}: {arr}")
        if not swapped:      # no swaps means already sorted
            break
    return arr


# ---------- Merge Sort ----------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------- Quick Sort ----------
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ---------- Main ----------
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11, 90]
    print("Original array:", data)

    print("\nBubble Sort:")
    result = bubble_sort(data.copy())
    print("  Sorted:", result)

    print("\nMerge Sort:")
    print("  Sorted:", merge_sort(data.copy()))

    print("\nQuick Sort:")
    print("  Sorted:", quick_sort(data.copy()))   