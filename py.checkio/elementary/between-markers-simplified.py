# Решение задачи "Between Markers (simplified)" в пайчекио
# Задача: py.checkio.org/mission/between-markers-simplified/
# Автор: M. Batanov, 14.09.19


def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.find(begin)+1:text.find(end)]
