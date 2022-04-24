res = -1


def _broken_search(nums, target, left, right):
    global res
    if nums[left] == target:
        res = left
        return res
    elif nums[right] == target:
        res = right
        return res
    if left >= right:
        return
    mid = (left + right)//2
    _broken_search(nums, target, left, mid)
    _broken_search(nums, target, mid+1, right)


def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    _broken_search(nums, target, left, right)
    return res






# nums = [19, 21, 100, 101, 1, 4, 5, 7, 12]
# nums = [1]

# print(broken_search(nums, 1))
# _broken_search(nums, 100, 0, 8)



# def test():
#     arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
#     assert broken_search(arr, 5) == 6

# test()