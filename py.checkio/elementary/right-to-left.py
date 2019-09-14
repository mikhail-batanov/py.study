# Решение задачи "Right to Left" в пайчекио
# Задача: py.checkio.org/mission/right-to-left/
# Автор: M. Batanov, 14.09.19


def left_join(phrases):
    phrases = list(phrases)
    result = ''
    for phrase in phrases:
        result = result + phrase.replace('right', 'left') + ','
    result = result[:len(result)-1]
    return result
