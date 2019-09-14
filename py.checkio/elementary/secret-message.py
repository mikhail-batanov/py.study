# Решение задачи "Secret Message" в пайчекио
# Задача: py.checkio.org/ru/mission/secret-message/
# Автор: M. Batanov, 14.09.19


def find_message(text: str) -> str:
    uppercase_letter = [symbol for symbol in text if symbol.isupper()]
    return "".join(uppercase_letter)
