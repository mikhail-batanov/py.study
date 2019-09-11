# Решение задачи "Time Converter (24h to 12h)" в пайчекио
# Автор - M. Batanov, 11.09.19


def time_converter(time):
    hours = int(time[0] + time[1])
    result = time[2:5]
    if hours > 11:
        if hours != 12:
            hours = hours - 12
        result = str(hours) + result + ' p.m.'
    else:
        if hours == 0:
            hours = 12
        result = str(hours) + result + ' a.m.'
    return result
