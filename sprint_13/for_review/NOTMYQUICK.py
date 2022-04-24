import random


def sort_key(part_1, part_2):
    if int(part_1[1]) == int(part_2[1]):
        if int(part_1[2]) == int(part_2[2]):
            return part_1[0] < part_2[0]
        return int(part_1[2]) < int(part_2[2])
    return int(part_1[1]) > int(part_2[1])


def partition(array, pivot):
    left = 0
    right = len(array) - 1
    while right > left:
        while sort_key(array[left], pivot):
            left += 1
        while sort_key(pivot, array[right]):
            right -= 1
        array[left], array[right] = array[right], array[left]
    return array[:left], array[left:]


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[random.randint(0, len(array) - 1)]
        left, right = partition(array, pivot)
        return quicksort(left) + quicksort(right)


def get_started():
    participants = int(input())
    results = []
    for _ in range(0, participants):
        results.append(list(map(str, input().strip().split())))
    return results


if __name__ == '__main__':
    part = get_started()
    sorted_results = quicksort(part)
    for result in sorted_results:
        print(result[0])