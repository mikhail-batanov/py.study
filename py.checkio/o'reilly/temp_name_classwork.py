# Заготовка для решения задачи пайчекио
# Разбираю логику работы классов и методов
# В методах "names" и "connected" есть не разобранная ошибка

class Friends:


    def __init__(self, connections):
        self.connections = list(connections)


    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections = self.connections.append(connection)
            return True

    
    def remove(self, connection):
        if connection in self.connections:
            self.connections.remove(connection)
            return True
        else:
            return False

    
    def names(self):
        sset = set()
        print(type(sset))
        for skobe in self.connections:
            for e in skobe:
                sset.add(e)
        return sset


    def connected(self, name):
        sset = set()
        print(self.connections, type(self.connections))
        for skobe in self.connections:
            for e in skobe:
                if name in skobe:
                    sset.add(e)
        sset.remove(name)
        print(sset, type(sset))
        return sset


letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
digit_friends = Friends([{"1", "2"}, {"3", "1"}])
f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
f.remove({"sophia", "pilot"})
f.names()
f.connected("sophia")
Q = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
Q.connected("a")
Q.add({"a", "d"})
Q.connected("a")
Q.remove({"a", "d"})
Q.connected("a")
