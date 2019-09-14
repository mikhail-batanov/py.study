# Решение задачи "Digits Multiplication" в пайчекио
# Задача: py.checkio.org/ru/mission/digits-multiplication/
# Автор: M. Batanov, 14.09.19


def checkio(number: int) -> int:
    multiplication, numb = 1, list(str(number))
    for element in numb:
        if int(element) != 0:
            multiplication = multiplication * int(element)
    return multiplication
