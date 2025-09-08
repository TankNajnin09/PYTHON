# === SEARCHING FUNCTIONS ===

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
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
    return -1

# === SORTING FUNCTIONS ===

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    def _quick_sort(items, low, high):
        if low < high:
            pi = partition(items, low, high)
            _quick_sort(items, low, pi - 1)
            _quick_sort(items, pi + 1, high)

    def partition(items, low, high):
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)

# === MAIN PROGRAM ===

def main(arr):
    while True:
        print("\n====== MENU ======")
        
        print("1. Linear Search")
        print("2. Binary Search (Array must be sorted)")
        print("3. Selection Sort")
        print("4. Bubble Sort")
        print("5. Insertion Sort")
        print("6. Merge Sort")
        print("7. Quick Sort")
        print("8. Display Array")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            x = int(input("Enter value to search: "))
            index = linear_search(arr, x)
            print(f"Element found at index: {index}" if index != -1 else "Element not found.")
        elif choice == '2':
            x = int(input("Enter value to search: "))
            sorted_arr = sorted(arr)  # Binary search needs sorted array
            index = binary_search(sorted_arr, x)
            print(f"Sorted Array: {sorted_arr}")
            print(f"Element found at index: {index}" if index != -1 else "Element not found.")
        elif choice == '3':
            selection_sort(arr)
            print("Array sorted using Selection Sort.",arr)
        elif choice == '4':
            bubble_sort(arr)
            print("Array sorted using Bubble Sort.",arr)
        elif choice == '5':
            insertion_sort(arr)
            print("Array sorted using Insertion Sort.",arr)
        elif choice == '6':
            merge_sort(arr)
            print("Array sorted using Merge Sort.",arr)
        elif choice == '7':
            quick_sort(arr)
            print("Array sorted using Quick Sort.",arr)
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
print("Enter array")
arr = list(map(int, input("Enter elements separated by space: ").split()))

#if __name__ == "__main__":
main(arr)
