# Решение задачи  "Striped Words" в пайчекио
# Задача: py.checkio.org/mission/striped-words/
# Автор: M. Batanov, 21.09.19


def checkio(text):
    vowels, consonants = "AEIOUY", "BCDFGHJKLMNPQRSTVWXZ"
    result, text = 0, text.upper()
    string = ''
    for symbol in text:
        if symbol in vowels or symbol in consonants or symbol in '0123456789':
            string = string + symbol
        else:
            string = string + ' '
    text = string.split(' ')
    for word in text:
        for i in range(len(word) - 1):
            if word[i] in vowels and word[i+1] in consonants:
                if i == len(word) - 2:
                    result = result + 1
                continue
            elif word[i] in consonants and word[i+1] in vowels:
                if i == len(word) - 2:
                    result = result + 1
                continue
            else:
                break
    return result
