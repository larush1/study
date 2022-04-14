def twosum_extra_ds(numbers, X):
    # Создаём вспомогательную структуру данных с быстрым поиском элемента.
    previous = set()

    for A in numbers:
        Y = X - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)

    # Если ничего не нашлось в цикле, значит, нужной пары элементов в массиве нет.
    return None, None 

print(twosum_extra_ds([5,2,8,47,24,8,2,1,4], 6))