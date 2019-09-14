# Решение задачи "First Word (simplified)" в пайчекио
# Задача: py.checkio.org/mission/first-word-simplified/
# Автор: M. Batanov, 14.09.19


def first_word(text: str) -> str:
    text = text + ' '
    return text[:text.find(' ')]
