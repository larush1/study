# def correct_position(str_num1, str_num2):
#     if len(str_num1) == len(str_num2):
#         return str_num1 > str_num2
#     if len(str_num1) > len(str_num2):
#         str_num2 += str_num2[-1]*(len(str_num1) - len(str_num2))
#         if str_num2 == str_num1:
#             if str_num2[-1] == '0':
#                 return False
#             return False
#         return str_num1 > str_num2
#     else:
#         str_num1 += str_num1[-1]*(len(str_num2) - len(str_num1))
#         if str_num1 == str_num2:
#             if str_num1[-1] == '0':
#                 return True
#             return True
#         return str_num1 > str_num2

def correct_position(str_num1, str_num2):
    a = int(str_num1 + str_num2)
    b = int(str_num2 + str_num1)
    return a > b


def insertion_sort(array, compar):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and compar(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
            array[j] = item_to_insert
    return array


def run():
    _ = input()
    unsorted = list(input().split())
    # inp = '100 10'
    # inp = '336 945 741 532 433 309 685 325 572 24 1000 631 675 831 807 134 473 1000 634 748 587 1000 852 353 262 305 243 27 697 919 906 844 938 670 71 843 803 72 180 781 491 379 590 407 233 498 617 533 28 493 542 1000 521 85 373 646 89 799 787 728 148 38 443 559 426 1000 916 866 1000 1000 610 925 882 888 965 317 104 256 976 9 83 415 244 239 1000 68 305 771 734 571 523 574 1000 495 139 94 757 709 573 412'
    # unsorted = list(inp.split())
    # print(sorted(unsorted))
    out = insertion_sort(unsorted, correct_position)
    print(''.join(out))
    # print(out)


if __name__ == '__main__':
    run()