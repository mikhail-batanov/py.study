# Решение задачи "The Most Numbers" в пайчекио
# Задача: py.checkio.org/mission/most-numbers/
# Автор: M. Batanov, 14.09.19


def checkio(*args):
    if len(args) != 0:
        return max(args) - min(args)
    else:
        return 0
