from typing import List

def get_nearest_zeros(numbers: List[str]) -> List[str]:
    nearest_zeros = len(numbers)*[0]
    zero_count = 0
    was_first_zero = 0
    for i in range(len(numbers)):
        if numbers[i] == '0':
            zero_count = 0
            was_first_zero = 1
        elif was_first_zero == 0:
            nearest_zeros[i] = 1
            continue
        else:
            zero_count +=1
            nearest_zeros[i] = zero_count
    zero_count = 0
    working = 0
    for i in reversed(range(len(numbers))):
        if nearest_zeros[i] == 0:
            zero_count = 0
            working = 1
            continue
        else:
            zero_count +=1
        if not nearest_zeros[i] == zero_count and working == 1:
            nearest_zeros[i] = zero_count
            if nearest_zeros[i-1] == zero_count:
                working = 0
                continue
            if nearest_zeros[i-1] == zero_count + 1:
                nearest_zeros[i] = zero_count
                working = 0
    return map(str, nearest_zeros)

def read_input() -> List[str]:
    _ = input()
    numbers = input().strip().split()
    return numbers

if __name__ == '__main__':
    print(' '.join(get_nearest_zeros(read_input())))

    # numbers = []
    # for i in range(1000000):
    #     numbers += [str(i)]
    # numbers[1875] = '0'
    # numbers[500000] = '0'
    # numbers += ['0']
    # print(' '.join(get_nearest_zeros(numbers)))
    # print(' '.join(get_nearest_zeros([9,9,9,9,9,0,9,9,9,9,0,9,9,9,9,9,0,0,0,1,0])))