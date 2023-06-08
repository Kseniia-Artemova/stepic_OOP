class Bag:

    def __init__(self, max_weight):
        self.__max_weight = None
        self.max_weight = max_weight
        self.__things = []
        self.__total_weight = 0

    @property
    def max_weight(self):
        return self.__max_weight

    @max_weight.setter
    def max_weight(self, max_weight):
        if type(max_weight) in (int, float):
            self.__max_weight = max_weight

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.__total_weight + thing.weight <= self.max_weight:
            self.__things.append(thing)
            self.__total_weight += thing.weight

    def remove_thing(self, indx):
        self.__things.pop(indx)
        self.__total_weight -= self.__things[indx].weight

    def get_total_weight(self):
        return self.__total_weight


class Thing:

    def __init__(self, name, weight):
        self.__name = None
        self.name = name
        self.__weight = None
        self.weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if type(weight) in (int, float):
            self.__weight = weight


if __name__ == '__main__':

    bag = Bag(1000)
    bag.add_thing(Thing("Книга по Python", 100))
    bag.add_thing(Thing("Котелок", 500))
    bag.add_thing(Thing("Спички", 20))
    bag.add_thing(Thing("Бумага", 100))
    w = bag.get_total_weight()
    print(w)
    for t in bag.things:
        print(f"{t.name}: {t.weight}")