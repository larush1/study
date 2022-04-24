# 67727271
def binary_for_broken_arr(arr, target, left, right):
    if right < left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[left] <= arr[mid]:
        if target >= arr[left] and target <= arr[mid]:
            right = mid-1
            return binary_for_broken_arr(arr, target, left, right)
        else:
            left = mid+1
            return binary_for_broken_arr(arr, target, left, right)
    else:
        if target >= arr[mid] and target <= arr[right]:
            left = mid+1
            return binary_for_broken_arr(arr, target, left, right)
        else:
            right = mid-1
            return binary_for_broken_arr(arr, target, left, right)


def broken_search(nums, target) -> int:
    return binary_for_broken_arr(nums, target, 0, len(nums) - 1)


# def test():
#     arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
#     assert broken_search(arr, 19) == 0
#     assert broken_search(arr, 21) == 1
#     assert broken_search(arr, 100) == 2
#     assert broken_search(arr, 101) == 3
#     assert broken_search(arr, 1) == 4
#     assert broken_search(arr, 4) == 5
#     assert broken_search(arr, 5) == 6
#     assert broken_search(arr, 7) == 7
#     assert broken_search(arr, 12) == 8
#     nums = [1]
#     assert broken_search(nums, 2) == -1
#     nums = [5, 1]
#     assert broken_search(nums, 1) == 1
#     nums = [3, 6, 7]
#     assert broken_search(nums, 8) == -1


# test()
