from typing import List


def find_distances(house_nums: List[str]) -> List[int]:
    distances = [0] * len(house_nums)
    left_zero_index = - float("inf")
    for index in range(len(house_nums)):
        if house_nums[index] == '0':
            left_zero_index = index
        else:
            distances[index] = index - left_zero_index
    right_zero_index = float("inf")
    for index in range(len(house_nums) - 1, -1, -1):
        if house_nums[index] == '0':
            right_zero_index = index
        else:
            distances[index] = min(right_zero_index - index, distances[index])
    return distances


if __name__ == '__main__':
    # _ = input()
    # nums = input().split()
    # print(*find_distances(nums))
    # assert find_distances([0, 1, 4, 9, 0]) == [0, 1, 2, 1, 0]
    # assert find_distances([0, 7, 9, 4, 8, 20]) == [0, 1, 2, 3, 4, 5]
    # print(*find_distances(['0', '1', '4', '9', '0']))
    # print(*find_distances(['0', '7', '9', '4', '8', '20']))
    print(*find_distances(['7', '9', '4', '8', '20', '0']))