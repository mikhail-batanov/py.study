# Решение задачи  "Boolean Algebra" в пайчекио
# Задача: py.checkio.org/mission/boolean-algebra/
# Автор: M. Batanov, 21.09.19


def boolean(x, y, operation):
    if operation == 'conjunction':
        return min(x, y)
    if operation == 'disjunction':
        return max(x, y)
    if operation == 'implication':
        return x - y <= 0
    if operation == 'exclusive':
        return max(x, y) - min(x, y)
    if operation == 'equivalence':
        return not (max(x, y) - min(x, y))
