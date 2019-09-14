# Решение задачи "Even the Last" в пайчекио
# Задача: py.checkio.org/mission/even-last/
# Автор: M. Batanov, 14.09.19


def checkio(array):
    result, i = 0, 0
    if len(array) > 0:
        while i < len(array):
            result = result + array[i]
            i = i + 2
        result = result * array[len(array)-1]
    return result
