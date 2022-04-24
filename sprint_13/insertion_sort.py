from math import nan


def insertion_sort(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j-1]:
            array[j] = array[j-1]
            j -= 1
            array[j] = item_to_insert
            print(f'step {i}, sorted {i+1} elements: {array}') 

insertion_sort([12, 5, 1, 4, nan, 9, 3, 6])