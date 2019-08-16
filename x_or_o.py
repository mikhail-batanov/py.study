class color:
    Red = '\033[91m'
    Green = '\033[92m'
    END = '\033[0m'

def revect():
    return [[s[0], s[1], s[2]], [s[0], s[4], s[8]], [s[0], s[3], s[6]],
            [s[1], s[4], s[7]], [s[2], s[5], s[8]], [s[2], s[4], s[6]],
            [s[3], s[4], s[5]], [s[6], s[7], s[8]]]


def pprint():
    i = 0
    while i < 8:
        print (s[i], s[i+1], s[i+2])
        i = i + 3


def check():
    vect = revect()
    j = 0
    while j < len(vect):
        if vect[j].count(X) == 3 or vect[j].count(O) == 3:
            return 1
            break
        else:
            j = j + 1


def step():
    while 1 == 1:
        if not any(e in range(len(s)+1) for e in s):
            print('Ничья')
            break
        ops = 0
        while not ops:
            number = input(
                'Ход крестиков, укажите доступную цифру для хода: ', )
            if number.isdigit():
                number = int(number)
                if number >= 1 and number <= 9:
                    if s[number-1] != X and s[number-1] != O:
                        ops = 1
        s[number-1] = X
        if check():
            pprint()
            print('Крестики выиграли!')
            break
        comp_step()
        if check():
            print('Нолики выиграли!')
            break


def comp_step():
    j, k = 0, 0
    pars = revect()
    cs = 0
    while j < len(pars):
        if pars[j].count(X) < 1 and pars[j].count(O) > 1 and not cs:
            while k < len(pars[j]):
                if pars[j][k] != O:
                    s[omni[j][k]] = O
                    cs = 1
                    break
                k = k + 1
        j = j + 1
    j, k = 0, 0
    while j < len(pars):
        if pars[j].count(X) > 1 and pars[j].count(O) < 1 and not cs:
            while k < len(pars[j]):
                if pars[j][k] != X:
                    s[omni[j][k]] = O
                    cs = 1
                    break
                k = k + 1
        j = j + 1
    if s[4] == O or s[4] == X and not cs:
        if s[0] != X and s[0] != O and not cs:
            s[0] = O
            cs = 1
        if s[2] != X and s[2] != O and not cs:
            s[2] = O
            cs = 1
        if s[6] != X and s[6] != O and not cs:
            s[6] = O
            cs = 1
        if s[8] != X and s[8] != O and not cs:
            s[8] = O
            cs = 1
    if s[4] != O and s[4] != X and not cs:
        s[4] = O
        cs = 1
    while k < len(s):
        if s[k] != X and s[k] != O and not cs:
            s[k] = O
            cs = 1
            break
        k = k + 1
    print('Ход ноликов:')
    pprint()

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
omni = [[0, 1, 2], [0, 4, 8], [0, 3, 6],
        [1, 4, 7], [2, 5, 8], [2, 4, 6],
        [3, 4, 5], [6, 7, 8]]
X = color.Green + 'X' + color.END
O = color.Red + 'O' + color.END
print('Это поле для игры:')
pprint()
step()
