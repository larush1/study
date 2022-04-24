# № 67751048

# Компаратор для стандартной сортировки Pytnon
# было интересно какие результаты покажет Контест
# Быстро! и памяти использовано совсем немного больше :)
# № этой посылки со стандартной сортировкой - 67750246

# class TupleComparator(tuple):
#     def __lt__(self, other):
#         if self[1] == other[1]:
#             if self[2] == other[2]:
#                 return self[0] < other[0]
#             return self[2] < other[2]
#         return self[1] > other[1]

from random import randint


def key_competition_results(p1, p2):
    if p1[1] == p2[1]:
        if p1[2] == p2[2]:
            return p1[0] < p2[0]
        return p1[2] < p2[2]
    return p1[1] > p2[1]


def effective_partition(arr, pivot):
    left = 0
    right = len(arr) - 1
    while right > left:
        while key_competition_results(arr[left], pivot):
            left += 1
        while key_competition_results(pivot, arr[right]):
            right -= 1
        arr[left], arr[right] = arr[right], arr[left]
    return arr[:left], arr[left:]


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[randint(0, len(arr) - 1)]
        left, right = effective_partition(arr, pivot)
        return quick_sort(left) + quick_sort(right)


def parser():
    amount_participants = int(input())
    list_of_participants = []
    for _ in range(amount_participants):
        participant = input().split()
        listview_participant = list(
            map(lambda x: int(x) if x.isdigit() else x, participant))
        list_of_participants.append(listview_participant)
    return list_of_participants


if __name__ == '__main__':
    participants = parser()
    # sorted_participants = sorted(participants, key=TupleComparator)
    sorted_participants = quick_sort(participants)
    for p in sorted_participants:
        print(p[0])
