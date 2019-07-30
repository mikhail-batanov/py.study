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
    win, switch = 0, 0
    while not win:
        if switch == 0:
            number = int(input('Ходят крестики, укажите цифру для хода: '))
            s[number-1] = 'X'
            pprint()
            win = check()
            switch = 1
    else:
        number = int(input('Ходят нолики, укажите цифру для хода: '))
        s[number-1] = 'O'
        pprint()
        win = check()
        switch = 0
    if switch == 0:
        print ('Нолики выиграли!')
    else:
        print ('Крестики выиграли!')

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Это поле для игры:')
pprint()
step()
