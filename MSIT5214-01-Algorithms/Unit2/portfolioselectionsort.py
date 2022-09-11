# Implementation of the Selection Sort Algorithm

def selection_sort(array):
    n = len(array)
    for i in range(n):
        # Setting the first element of the unsorted array is the one with minimum value.
        minimum = i

        for j in range(i+1, n):
            if (array[j] < array[minimum]):
                # Updating the position of minimum array element if a smaller array element is found.
                minimum = j

        # Swapping the minimum element with the first element of the unsorted array part.
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp

    return array


unordered_array = [64, 35, 12, 22, 11]
print("Unordered Array: " + str(unordered_array))
print("Ordered Array: " + str(selection_sort(unordered_array)))
