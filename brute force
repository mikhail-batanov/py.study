# Решение задачи "Sort Array by Element Frequency" в пайчекио
# Автор - M. Batanov, 11.09.19


def frequency_sort(items):
    t = list(dict.fromkeys(items))
    x = t
    for i in range(len(t)):
        x[i] = items.count(t[i])
    t = list(dict.fromkeys(items))
    for i in range(len(x)-1):
        nx = x[i]
        nt = t[i]
        if nx < x[i+1]:
            x[i] = x[i+1]
            x[i+1] = nx
            t[i] = t[i+1]
            t[i+1] = nt
    result = list('')
    for i in range(len(t)):
        for j in range(x[i]):
            result.append(t[i])
    return result
