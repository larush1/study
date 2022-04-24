def binary_search(arr, x, left, right):
    mid = (left + right) // 2
    while arr[mid] != x:
        if len(arr[left:right]) != 1:
            if arr[mid] > x:
                right = mid
                mid = (left + right) // 2
            elif arr[mid] < x:
                left = mid
                mid = (left + right) // 2
        else:
            return -1
    return mid

# print(binary_search([1,2,3,4,5,6,7,8], 4,0,8))
# print(can_bye_bike([1,2,3,4,5,6,7,8], 4,0,8))
# print(can_bye_bike([1,7,7,7,7,7,7,8], 9,     0,8))


def can_bye_bike(arr, x, left, right, last_ok=-1):
    mid = (left + right) // 2
    if arr[mid] >= x:
        last_ok = mid
        right = mid
    else:
        left = mid + 1
    if right <= left:
        return last_ok
    else:
        return can_bye_bike(arr, x, left, right, last_ok)


_ = input()
inp = input()
x = int(input())
arr = list(map(int, inp.split()))
bicycle = can_bye_bike(arr, x, 0, len(arr))
if bicycle != -1:
    bicycle += 1
bicycle_x2 = can_bye_bike(arr, x*2, 0, len(arr))
if bicycle_x2 != -1:
    bicycle_x2 += 1
print(bicycle, bicycle_x2)
