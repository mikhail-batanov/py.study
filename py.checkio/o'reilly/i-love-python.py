# Решение задачи  "I Love Python!" в пайчекио
# Задача: py.checkio.org/mission/i-love-python/
# Автор: M. Batanov, 15.10.19


import random


def i_love_python():
    variant = random.randint(1, 2)
    print(variant)
    if variant == 1:
        # i love python for its syntax
        return "I love Python!"
    else:
        a, b, c = 'I ', 'love ', 'Python!'
        # for its variable declaration
        return a + b + c
