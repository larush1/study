def parse_input():
    n = int(input())
    res = []
    for _ in range(n):
        el_str = input()
        el_arr = list(map(int, el_str.split()))
        res.append(el_arr)
    return res


def first_el_sort(array):
    return array[0]


def merger(a, b):
    if b[0] <= a[1] and b[1] >= a[1]:
        return [a[0], b[1]]
    if b[0] <= a[1] and b[1] <= a[1]:
        return [a[0], a[1]]
    if b[0] > a[1]:
        return False


def clumb_maker(sort_array):
    i = 1
    while i < len(sort_array):
        new_el = merger(sort_array[i-1], sort_array[i])
        if new_el:
            sort_array[i] = new_el
            del sort_array[i-1]
        if not new_el:
            i += 1
    return sort_array


def run():
    inp_arr = parse_input()
    inp_sort = sorted(inp_arr, key=first_el_sort)
    output = clumb_maker(inp_sort)
    for i in output:
        print(*i)

if __name__ == '__main__':
    run()
