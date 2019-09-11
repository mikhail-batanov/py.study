# Решение задачи "Caesar Cipher (encryptor)" в пайчекио
# Автор - M. Batanov, 11.09.19


def to_encrypt(text, delta):
    t = ''
    for i in range(len(text)):
        if text[i] != ' ':
            x = ord(text[i]) + delta
            if x > 122:
                x = x - 26
            if x < 97:
                x = x + 26
            t = t + chr(x)
        else:
            t = t + text[i]
    return t
