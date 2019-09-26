# Решение задачи  "Friends" в пайчекио
# Задача: py.checkio.org/mission/friends/
# Автор: M. Batanov, 26.09.19


class Friends:
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True

    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    def names(self):
        sset = set()
        for skobe in self.connections:
            for e in skobe:
                sset.add(e)
        return sset

    def connected(self, name):
        sset = set()
        for skobe in self.connections:
            for e in skobe:
                if name in skobe:
                    sset.add(e)
        if len(sset) > 0:
            sset.remove(name)
        return sset
