# Решение задачи "Popular Words" в пайчекио
# Задача: py.checkio.org/mission/popular-words/
# Автор: M. Batanov, 14.09.19


def popular_words(text: str, words: list) -> dict:
    text = ' ' + text.lower() + ' '
    return {e: text.count(' ' + e + ' ') +
            text.count('\n' + e) + text.count(e + '\n')
            for e in words}
