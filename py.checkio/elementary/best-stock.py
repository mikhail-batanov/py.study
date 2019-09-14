# Решение задачи "Best Stock" в пайчекио
# Задача: py.checkio.org/ru/mission/best-stock/
# Автор: M. Batanov, 14.09.19


def best_stock(data):
    return max(data, key=data.get)
