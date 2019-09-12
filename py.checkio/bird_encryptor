# Решение задачи "Bird Language" в пайчекио
# Задача: py.checkio.org/ru/mission/bird-language/
# Автор: M. Batanov, 12.09.19


def translate(phrase):
    i, result = 0, ''
    while i < len(phrase):
        result = result + phrase[i]
        if phrase[i].lower() in 'aeiouy':
            i = i + 3
        elif phrase[i].lower() in 'bcdfghjklmnpqrstvwxz':
            i = i + 2
        else:
            i = i + 1
    return result
