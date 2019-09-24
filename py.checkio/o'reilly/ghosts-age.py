# Решение задачи  "Ghosts Age" в пайчекио
# Задача: py.checkio.org/mission/ghosts-age/
# Автор: M. Batanov, 24.09.19


def checkio(opacity):
    fibonachi, starting_point = [0, 1], 10000
    for i in range(0, 100):
        fibonachi.append(fibonachi[i]+fibonachi[i+1])
    for i in range(5000):
        if i in fibonachi:
            starting_point = starting_point - i
        else:
            starting_point = starting_point + 1
        if starting_point == opacity:
            return i
