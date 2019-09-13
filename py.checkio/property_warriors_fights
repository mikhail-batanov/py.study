# Решение задачи "The Warriors" в пайчекио
# Задача: py.checkio.org/ru/mission/the-warriors/
# Автор: M. Batanov, 13.09.19


class Warrior:
    health = 50
    attack = 5

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Knight(Warrior):
    attack = Warrior.attack + 2


def fight(unit_1, unit_2):
    while unit_1.health > 0 and unit_2.health > 0:
        unit_2.health = unit_2.health - unit_1.attack
        if unit_2.health > 0:
            unit_1.health = unit_1.health - unit_2.attack
        else:
            return True
    else:
        return False
