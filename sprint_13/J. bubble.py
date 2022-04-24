def bubble_sort(arr):
    sort_arr = sorted(arr)
    if arr == sort_arr:
        print(*arr)
    else:
        for i in range(len(arr)-1):
            if arr != sort_arr:
                for j in range(len(arr)-1-i):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                print(*arr)

def run():
    # _ = input()
    # unsorted = list(map(int, input().split()))
    inp = '4 3 9 2 1'
    unsorted = list(map(int, inp.split()))
    bubble_sort(unsorted)


if __name__ == '__main__':
    run()