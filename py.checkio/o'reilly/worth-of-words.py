# Решение задачи  "Worth of Words" в пайчекио
# Задача: py.checkio.org/mission/worth-of-words/
# Автор: M. Batanov, 19.09.19


def worth_of_words(words):
    words_price = [0 for e in words]
    pricelist = {'eaionrtlsu': 1, 'dg': 2, 'bcmp': 3, /
                 'fhvwy': 4, 'k': 5, 'jx': 8, 'qz': 10}
    for i in range(len(words)):
        for symbol in words[i]:
            for position in pricelist:
                if symbol in position:
                    words_price[i] = words_price[i] + pricelist.get(position)
    return words[words_price.index(max(words_price))]
