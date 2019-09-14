# Решение задачи "Three Words" в пайчекио
# Задача: py.checkio.org/mission/three-words/
# Автор: M. Batanov, 14.09.19


def checkio(words: str) -> bool:
    words, n = words.split(' '), 0
    for i in range(len(words)):
        if not words[i].isdigit():
            n = n + 1
            if n == 3:
                return True
        else:
            n = 0
    return False
