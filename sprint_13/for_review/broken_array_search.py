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
    