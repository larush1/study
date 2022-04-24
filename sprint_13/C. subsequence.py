def is_subsequence(s, t):
    last_index = 0
    for el_s in s:
        el_index = t.find(el_s, last_index)
        if el_index == -1:
            return False
        else:
            el_index += 1
            last_index = el_index
    return True


def run():
    s = input()
    t = input()
    # s = 'abbbbc'
    # t = 'aasgasgasgbb'
    print(is_subsequence(s, t))


if __name__ == '__main__':
    run()
