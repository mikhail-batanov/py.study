# Решение задачи "Absolute Sorting" в пайчекио
# Задача: py.checkio.org/ru/mission/absolute-sorting/
# Автор: M. Batanov, 14.09.19


def checkio(numbers_array: tuple) -> list:
    numbers_array = list(numbers_array)
    for i in range(len(numbers_array)):
        for j in range(len(numbers_array)):
            if abs(numbers_array[i]) < abs(numbers_array[j]):
                numbers_array[i], numbers_array[j] = \
                    numbers_array[j], numbers_array[i]
    return numbers_array
