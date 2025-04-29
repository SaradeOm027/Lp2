def selectionSort(arr):
    """
    Sorts an array using the Selection Sort algorithm.
    Time Complexity: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the current position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def main():
    print("=== Selection Sort ===")
    try:
        # Input: space-separated integers
        arr = list(map(int, input("Enter integers separated by spaces: ").strip().split()))
        if not arr:
            print("No elements entered. Exiting.")
            return
        print("Original array:", arr)
        sorted_arr = selectionSort(arr[:])  # Use arr[:] to avoid in-place mutation if needed
        print("Sorted array:  ", sorted_arr)
    except ValueError:
        print("Invalid input! Please enter only integers separated by spaces.")

if __name__ == '__main__':
    main()
