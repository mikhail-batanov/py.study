# Заготовка решения py.checkio.org/mission/long-non-repeat/solve/


def non_repeat(line):
    array = []
    for i in range(len(line)):
        temp_line = ''
        for e in range(i, len(line)):
            if line[e] not in temp_line:
                temp_line = temp_line + line[e]
            else:
                array.append(temp_line)
                temp_line = line[e]
            if e == len(line) - 1:
                array.append(temp_line)
    for i in range(len(array)):
        for e in range(len(array)):
            if len(array[i]) > len(array[e]):
                array[i], array[e] = array[e], array[i]
    print(array)
    if len(array) > 0:
        return array[0]
    else:
        return array


non_repeat('abdjwawk')
non_repeat("abcabcffab")
non_repeat("fghfrtyfgh")
non_repeat("w")
non_repeat("aaaaa")
non_repeat("wq")
non_repeat("fghfhy")
