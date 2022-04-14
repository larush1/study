def build_matryoshka(size, n):
    if n >= 1:
        print(f"Создаём низ матрёшки размера {size}.")
        build_matryoshka(size - 1, n - 1)
        print(f"Создаём верх матрешки размера {size}.")
    else:
        return


def stairs_builder(n):
    if n == 0:
        return
    print('построена 1 ступенька')
    print(f"Осталось построить {n} ступеней.")
    stairs_builder(n - 1)


def as_binary_string(n):
    if n < 0:
        return "-" + as_binary_string(-n)
    if n == 0 or n == 1:
        return str(n)
    last_digit = n % 2
    return as_binary_string(n // 2) + str(last_digit) 

def printBin(n):
    # if n < 0:
    #     print('-', end='')
    #     return printBin(-n)
    if n == 0:
        return
    printBin(n // 2)
    print(n%2, end='')

def printBin2(n):
    if n == 0 or n == 1:
        return str(n)
    return printBin2(n // 2) + str(n % 2)
# build_matryoshka(4, 3)
# stairs_builder(10)
# print(as_binary_string(50))
# printBin(20)
print(printBin2(47))