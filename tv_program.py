class TVProgram:

    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        if isinstance(tl, Telecast):
            self.items.append(tl)

    def remove_telecast(self, indx):
        for i in range(len(self.items)):
            if self.items[i].uid == indx:
                self.items.pop(i)
                return


class Telecast:

    def __init__(self, uid, name, duration):
        self.uid = uid
        self.name = name
        self.duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, uid):
        if type(uid) is int and uid > 0:
            self.__id = uid
        else:
            self.__id = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = None

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        if type(duration) is int and duration >= 0:
            self.__duration = duration
        else:
            self.__duration = None


if __name__ == '__main__':
    pr = TVProgram("Первый канал")
    pr.add_telecast(Telecast(1, "Доброе утро", 10000))
    pr.add_telecast(Telecast(2, "Новости", 2000))
    pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
    for t in pr.items:
        print(f"{t.name}: {t.duration}")
        print(t.__dict__)