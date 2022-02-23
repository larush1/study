from sys import stdout
from time import sleep


def progress_bar(length_bar=50, shift=5, delay=0.1, word='Downloading'):
    """
    Функция для динамического отображения загрузки в консоли.
    Просто для тренировки и учебы :)
    """
    s = ''
    percent_bar = [int(100/length_bar)*i for i in range(length_bar+1)]
    str_percent = [f'{percent}%' for percent in percent_bar]
    stdout.write(word)
    for percent in str_percent:
        s += '.'
        stdout.write(s + percent.rjust(length_bar-len(s)+shift))
        sleep(delay)
        stdout.write('\b'*(length_bar)+'\b'*shift)
    else:
        stdout.write(s)
        stdout.write('Complete' + '\n')


# length_bar = 50     # Длина прогресс бара. Должна быть кратна 5 и меньше 101
# shift = 5           # Сдвиг счетчика процентов врпаво. Должен быть больше 4
# delay = 0.1         # Задержка в секундах
# word = 'Downloading'

progress_bar()
