# Решение задачи  "Cipher Map" в пайчекио
# Задача: py.checkio.org/mission/cipher-map2/
# Автор: M. Batanov, 20.09.19


def recall_password(cipher_grille, ciphered_password):
    result, cipher_grille = '', list(cipher_grille)
    c = [['.', '.', '.', '.'] for e in cipher_grille]
    for e in range(len(cipher_grille)):
        for i in range(len(cipher_grille)):
            for j in range(len(cipher_grille[i])):
                if cipher_grille[i][j] == 'X':
                    result = result + ciphered_password[i][j]
        for i in range(len(c)):
            for j in range(len(c[i])):
                c[i][j] = cipher_grille[len(cipher_grille[i])-j-1][i]
        for i in range(len(c)):
            for j in range(len(c[i])):
                if j == 0:
                    cipher_grille[i] = c[i][j]
                else:
                    cipher_grille[i] = cipher_grille[i] + c[i][j]
    return result
