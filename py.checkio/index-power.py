# Решение задачи "Index Power" в пайчекио
# Задача: py.checkio.org/mission/index-power/
# Автор: M. Batanov, 14.09.19


def index_power(array: list, n: int) -> int:
    if n > len(array) - 1:
        return -1
    return array[n]**n
