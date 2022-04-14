# from typing import List, Tuple

# def get_sum(number_list: List[int], k: int) -> List[int]:
#     number = int(''.join(number_list))
#     output = number + k
#     return ' '.join(str(output))

# def read_input() -> Tuple[List[int], int]:
#     n = int(input())
#     number_list = list(input().strip().split())
#     k = int(input())
#     return number_list, k

# number_list, k = read_input()
# print(" ".join(map(str, get_sum(number_list, k))))

from typing import List, Tuple

def get_sum(number_list: List[int], k: List[int]) -> List[int]:
    if len(number_list) > len(k):
        k = [0]*(len(number_list)-len(k)) + k
    else:
        number_list = [0]*(len(k)-len(number_list)) + number_list
    result = [0]*len(number_list)
    is_ten = 0
    for i in reversed(range(len(number_list))):
            if number_list[i] + k[i] + is_ten > 9:
                result[i] = number_list[i] + k[i] + is_ten - 10
                is_ten = 1
            else:
                result[i] = number_list[i] + k[i] + is_ten
                is_ten = 0
    if is_ten == 1:
        result = [1] + result
    return result

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = list(map(int, str(input())))
    return number_list, k

number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))

# print(read_input())
# print(get_sum(['1', '2', '0', '0'], 34))
# print(get_sum(['9', '5'], 17))
# print(get_sum([1, 2, 0, 9], [1, 4, 0]))
# print(get_sum([9, 9, 9, 9], [9, 9, 9, 9]))