import time


class GeyserClassic:
    MAX_DATE_FILTER = 100
    INSTRUCTION = {
        1: ("Mechanical", "slot_1"),
        2: ("Aragon", "slot_2"),
        3: ("Calcium", "slot_3")
    }

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def add_filter(self, slot_num, filter):
        slot = self.INSTRUCTION.get(slot_num)
        if slot and slot[0] == str(filter) and self.__dict__[slot[1]] is None:
            setattr(self, slot[1], filter)

    def remove_filter(self, slot_num):
        slot = self.INSTRUCTION.get(slot_num)
        if slot and slot[1]:
            setattr(self, slot[1], None)

    def get_filters(self):
        filters = [slot for slot in self.__dict__.values() if slot]
        return tuple(filters)

    def check_work(self, obj):
        if 0 <= (time.time() - obj.date) <= self.MAX_DATE_FILTER:
            return True
        return False

    def water_on(self):
        filters = self.get_filters()
        if len(filters) == 3 and all(map(self.check_work, filters)):
            return True
        return False


class Filter:

    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f"{self.__class__.__name__}"

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return
        super().__setattr__(key, value)


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


if __name__ == '__main__':
    #
    # my_water = GeyserClassic()
    # my_water.add_filter(1, Mechanical(time.time()))
    # my_water.add_filter(2, Aragon(time.time()))
    # w = my_water.water_on() # False
    # print(w)
    # my_water.add_filter(3, Calcium(time.time()))
    # w = my_water.water_on()  # True
    # print(w)
    # f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
    # my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
    # my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно

    my_water = GeyserClassic()
    my_water.add_filter(1, Mechanical(time.time()))
    my_water.add_filter(2, Aragon(time.time()))

    assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

    my_water.add_filter(3, Calcium(time.time()))
    assert my_water.water_on() == True, "метод water_on вернул False при всех трех установленных фильтрах"

    f1, f2, f3 = my_water.get_filters()
    print(my_water.get_filters())
    assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3,
                                                                                Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"
    print(type(f1), type(f2), type(f3))

    my_water.remove_filter(1)
    assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

    my_water.add_filter(1, Mechanical(time.time()))
    assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

    f1, f2, f3 = my_water.get_filters()
    my_water.remove_filter(1)

    my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
    assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

    f1 = Mechanical(1.0)
    f2 = Aragon(2.0)
    f3 = Calcium(3.0)
    assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

    f1.date = 5.0
    f2.date = 5.0
    f3.date = 5.0

    assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"
