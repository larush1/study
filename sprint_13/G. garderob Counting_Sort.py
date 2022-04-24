def counting_sort0(array, k):
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1
    index = 0
    for value in range(k):
        for amount in range(counted_values[value]):
            array[index] = value
            index += 1
    return array


def counting_sort(array, k):
    counted_values = [0] * k
    res = []
    for value in array:
        counted_values[value] += 1
    for value in range(len(counted_values)):
        res += [value] * counted_values[value]
    return res


def run():
    _ = input()
    inp = list(map(int, input().split()))
    # inp = [0, 2, 1, 2, 0, 0, 1]
    k = 3
    print(*counting_sort(inp, k))


if __name__ == '__main__':
    run()
