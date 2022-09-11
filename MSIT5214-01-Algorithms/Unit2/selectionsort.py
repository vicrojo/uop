import random

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


# This function runs n times the generation of a random numbers list and then sorts
# the values with the selection sort algorithm

def test_selection_sort(n):
    for i in range(n):
        print("Test #" + str(i + 1))
        unordered_array = random.sample(range(1, 1000), 10)
        print("Unordered Array: " + str(unordered_array))
        print("Ordered Array: " + str(selection_sort(unordered_array)))


# Number of tests to execute
TEST_TIMES = 5
test_selection_sort(TEST_TIMES)
