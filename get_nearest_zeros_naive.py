from typing import List

def get_nearest_zeros_naive(numbers: List[int]) -> List[str]:
    nearest_zeros = len(numbers)*[0]
    count = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            nearest_zeros[i] = 0
            continue
        if 0 in numbers[i:len(numbers)]:
            for j in range(i, len(numbers)):
                if numbers[j] == 0:
                    from_right = count
                    count = 0
                    break
                else:
                    count += 1
        else:
            count += 1
            nearest_zeros[i] = count
            continue

        if 0 in numbers[0:i+1]:
            for j in reversed(range(0, i+1)):
                    if numbers[j] == 0:
                        from_left = count
                        count = 0
                        break
                    else:
                        count += 1
        else:
            from_left = from_right
        nearest_zeros[i] = from_right if from_right < from_left else from_left
    return map(str, nearest_zeros)

def read_input() -> List[int]:
    _ = input()
    numbers = list(map(int, input().strip().split()))
    return numbers

# numbers = read_input()
# print(' '.join(get_nearest_zeros_naive(numbers)))


numbers = []
for i in range(10000):
    numbers += [i]
numbers[500] = 0
numbers[999] = 0
numbers += [0]
print(' '.join(get_nearest_zeros_naive(numbers)))


# print(' '.join(get_nearest_zeros_naive([9,9,9,9,9,0,0,11,1,1,1,1,0,1,1,1,1,1])))
