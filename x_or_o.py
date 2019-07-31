def pprint():
    i = 0
    while i < 8:
        print (s[i], s[i+1], s[i+2])
        i = i + 3


def check():
    j = 0
    vect = [[s[0], s[1], s[2]], [s[0], s[4], s[8]], [s[0], s[3], s[6]],
            [s[1], s[4], s[7]], [s[2], s[5], s[8]], [s[2], s[4], s[6]],
            [s[3], s[4], s[5]], [s[6], s[7], s[8]]]
    while j < len(vect):
        if vect[j].count('X') == 3 or vect[j].count('O') == 3:
            return 1
            break
        else:
            j = j + 1


def step():
    win = 0
    while not win:
        switch, ops = 'X', 0
        if not any(e in range(len(s)+1) for e in s):
            print('Ничья')
            exit()
        print('Ходят крестики, укажите цифру для хода:')
        while not ops:
            number = input()
            if number.isdigit():
                number = int(number)
                if number >= 1 and number <= 9:
                    if s[number-1] != 'X' and s[number-1] != 'O':
                        ops = 1
                    else:
                        print('Укажите доступную цифру для хода:')
                else:
                    print('Укажите доступную цифру для хода:')
            else:
                print('Укажите цифру для хода:')
        s[number-1] = switch
        win = check()
        if win:
            switch = 'O'
            continue
        pprint()
        comp_step()
        win = check()
        if win:
            switch = 'X'
    if switch == 'X':
        print('Нолики выиграли!')
    else:
        if switch == 'O':
            print('Крестики выиграли!')


def comp_step():
    j, k = 0, 0
    pars = [[s[0], s[1], s[2]], [s[0], s[4], s[8]], [s[0], s[3], s[6]],
            [s[1], s[4], s[7]], [s[2], s[5], s[8]], [s[2], s[4], s[6]],
            [s[3], s[4], s[5]], [s[6], s[7], s[8]]]
    omni = [[0, 1, 2], [0, 4, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [2, 4, 6],
            [3, 4, 5], [6, 7, 8]]
    while j < len(pars):
        if pars[j].count('X') > 1 and pars[j].count('O') < 1:
            while k < len(pars[j]):
                if pars[j][k] != 'X':
                    s[omni[j][k]] = 'O'
                    print('Ход ноликов:')
                    pprint()
                    return
                k = k + 1
        j = j + 1
    else:
        if s[4] != 'O' and s[4] != 'X':
            s[4] = 'O'
            print('Ход ноликов:')
            pprint()
        else:
            while k < len(s):
                if s[k] != 'X' and s[k] != 'O':
                    s[k] = 'O'
                    print('Ход ноликов:')
                    pprint()
                    return
                k = k + 1

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Это поле для игры:')
pprint()
step()
