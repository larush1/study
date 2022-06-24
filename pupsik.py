bad = ['b1', 'b2', 'b3']
good = ['g1', 'g2', 'g3']


def filter(text):
    text = text.split()
    res = []
    for word in text:
        if word in good:
            res.append('good')
        elif word in bad:
            res.append('bad')
        else:
            res.append('com')
    if 'good' not in res:
        return 'Нет!'
    if 'bad' not in res:
        return 'Да!'
    return 'Нет!'


assert filter('b1 g1') == 'Нет!'
assert filter('a s') == 'Нет!'
assert filter('b1 s') == 'Нет!'
assert filter('a g1') == 'Да!'
