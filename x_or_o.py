# Крестики-нолики на питоне, задача в целях обучения
# Автор - M. Batanov
# Первым этапом написания был вывод поля игры и ход игрока
# Второй этап - ход компьютера, создание репозитория на github
# Третий этап - добавление цвета в консоли, улучшение "ИИ"
# Четвертый этап - переписать игру в ООП
# Пятый этап - игра по сети, не войдет в текущий файл

class field:
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win_coordinates = [[0, 1, 2], [0, 4, 8], [0, 3, 6],
                       [1, 4, 7], [2, 5, 8], [2, 4, 6],
                       [3, 4, 5], [6, 7, 8]]
    X = '\033[92m' + 'X' + '\033[0m'
    O = '\033[91m' + 'O' + '\033[0m'
    # '\033[92m' - зеленый цвет
    # '\033[91m' - красный цвет
    # '\033[0m' - конец цвета

    def win_vectors(self):
        return [[field.board[0], field.board[1], field.board[2]],
                [field.board[0], field.board[4], field.board[8]],
                [field.board[0], field.board[3], field.board[6]],
                [field.board[1], field.board[4], field.board[7]],
                [field.board[2], field.board[5], field.board[8]],
                [field.board[2], field.board[4], field.board[6]],
                [field.board[3], field.board[4], field.board[5]],
                [field.board[6], field.board[7], field.board[8]]]

    def board_output(self):
        i = 0
        while i < 8:
            print(field.board[i], field.board[i + 1], field.board[i + 2])
            i = i + 3


class check:
    def win(self):
        vect = field.win_vectors(0)
        j = 0
        while j < len(vect):
            if vect[j].count(field.X) == 3 or vect[j].count(field.O) == 3:
                if vect[j].count(field.X) == 3:
                    print('Крестики выиграли!')
                if vect[j].count(field.O) == 3:
                    print('Нолики выиграли!')
                return True
            else:
                j = j + 1
        else:
            return False

    def draw(self):
        while 1 == 1:
            if not any(e in range(len(field.board) + 1) for e in field.board):
                return True
            else:
                return False

    def move(self):
        number = self
        if number.isdigit():
            number = int(number)
            if number >= 1 and number <= 9:
                if field.board[number - 1] != field.X\
                        and field.board[number - 1] != field.O:
                    return True
        else:
            return False


class step:
    def player(self):
        while 1 == 1:
            if check.draw(0):
                print('Ничья.')
                break
            number = input(
                'Ход крестиков, укажите доступную цифру для хода: ', )
            while not check.move(number):
                number = input(
                    'Ход крестиков, укажите доступную цифру для хода: ', )
            number = int(number)
            field.board[number - 1] = field.X
            if check.draw(0):
                field.board_output(0)
                print('Ничья.')
                break
            if check.win(0):
                field.board_output(0)
                break
            step.computer(0)
            if check.win(0):
                break

    def computer(self):
        j, k = 0, 0
        pars = field.win_vectors(0)
        cs = 0
        while j < len(pars):
            if pars[j].count(field.X) < 1 \
                    and pars[j].count(field.O) > 1 and not cs:
                while k < len(pars[j]):
                    if pars[j][k] != field.O:
                        field.board[field.win_coordinates[j][k]] = field.O
                        cs = 1
                        break
                    k = k + 1
            j = j + 1
        j, k = 0, 0
        while j < len(pars):
            if pars[j].count(field.X) > 1 \
                    and pars[j].count(field.O) < 1 and not cs:
                while k < len(pars[j]):
                    if pars[j][k] != field.X:
                        field.board[field.win_coordinates[j][k]] = field.O
                        cs = 1
                        break
                    k = k + 1
            j = j + 1
        if field.board[0] == field.X and field.board[8] == field.X \
                and field.board[1] != field.O \
                and field.board[1] != field.X and not cs:
            field.board[1] = field.O
            cs = 1
        if field.board[2] == field.X and field.board[6] == field.X \
                and field.board[7] != field.O \
                and field.board[7] != field.X and not cs:
            field.board[7] = field.O
            cs = 1
        if field.board[4] == field.O or field.board[4] == field.X and not cs:
            if field.board[0] != field.X \
                    and field.board[0] != field.O and not cs:
                field.board[0] = field.O
                cs = 1
            if field.board[2] != field.X \
                    and field.board[2] != field.O and not cs:
                field.board[2] = field.O
                cs = 1
            if field.board[6] != field.X \
                    and field.board[6] != field.O and not cs:
                field.board[6] = field.O
                cs = 1
            if field.board[8] != field.X \
                    and field.board[8] != field.O and not cs:
                field.board[8] = field.O
                cs = 1
        if field.board[4] != field.O \
                and field.board[4] != field.X and not cs:
            field.board[4] = field.O
            cs = 1
        print('Ход ноликов:')
        field.board_output(0)


print ('Это поле для игры:')
field.board_output(0)
step.player(0)
