# Заготовка для решения задачи пайчекио
# Разбираю логику работы классов и методов
# В методах "names" и "connected" есть не разобранная ошибка

class Friends:


    def __init__(self, connections):
        self.connections = list(connections)
        print('Мои связи: ', type(self.connections), self.connections)
        for e in self.connections:
            print(e, type(e))


    def add(self, connection):
        if connection in self.connections:
            return True
        else:
            self.connections = self.connections.append(connection)
            return False

    
    def remove(self, connection):
        if connection in self.connections:
            self.connections = self.connections.remove(connection)
            return True
        else:
            return False

    
    def names(self):
        sset = set()
        print(type(sset))
        for skobe in self.connections:
            for e in skobe:
                sset = sset.add(e)
        return sset


    def connected(self, name):
        sset = set()
        for skobe in self.connections:
            for e in skobe:
                if name in skobe:
                    sset = sset.add(e)
        sset = sset.remove(name)
        return sset


letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
digit_friends = Friends([{"1", "2"}, {"3", "1"}])
f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
f.names()
