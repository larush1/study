from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    if len(first_number) > len(second_number):
        second_number = '0'*(len(first_number)-len(second_number)) + second_number
    else:
        first_number = '0'*(len(second_number)-len(first_number)) + first_number
    result = ''
    is_bin = '0'
    for i in reversed(range(len(first_number))):
        if first_number[i] + second_number[i] + is_bin == '000':
            result = '0' + result
            is_bin = '0'
        elif first_number[i] + second_number[i] + is_bin in ('010', '100', '001',):
            result = '1' + result
            is_bin = '0'
        elif first_number[i] + second_number[i] + is_bin in ('110', '101', '011',):
            result = '0' + result
            is_bin = '1'
        else:
            result = '1' + result
            is_bin = '1'
    if is_bin == '1':
            result = '1' + result
    return result


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))

# first_number = '11001'
# second_number = '10111100'
# print(get_sum(first_number, second_number))