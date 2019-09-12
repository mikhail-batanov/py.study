# Решение задачи "Pawn Brotherhood" в пайчекио
# Задача: py.checkio.org/ru/mission/pawn-brotherhood/
# Автор: M. Batanov, 12.09.19


def safe_pawns(pawns_set) -> int:
    pawns_list = list(pawns_set)
    temp_array = []
    for i in range(len(pawns_list)):
        temp_array.append((ord(pawns_list[i][0]) - 96)*10 +
                          int(pawns_list[i][1]))
    result, i = 0, 0
    while i < len(temp_array):
        if temp_array[i] - 11 in temp_array or \
          temp_array[i] + 9 in temp_array:
            result = result + 1
        i = i + 1
    return result
    
