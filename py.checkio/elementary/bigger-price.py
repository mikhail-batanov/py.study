# Решение задачи  "Bigger Price" в пайчекио
# Задача: py.checkio.org/mission/bigger-price/
# Автор: M. Batanov, 14.09.19


def bigger_price(limit: int, data: list) -> list:
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i].get('price') > data[j].get('price'):
                data[i], data[j] = data[j], data[i]
    return data[0:limit]
