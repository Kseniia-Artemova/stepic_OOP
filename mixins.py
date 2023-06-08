class Employee:

    def __init__(self, name):
        super().__init__()
        self.name = name


class MixinLog:
    ID = 1

    def __init__(self):
        self.id = self.ID
        print(self.__class__)
        self.__class__.ID += 1

    def order_log(self):
        print(f"{self.id}-й сотрудник")


class Developer(Employee, MixinLog):
    pass


dev_1 = Developer("Pasha")
dev_1.order_log()
dev_2 = Developer("Lesha")
dev_2.order_log()
dev_3 = Developer("Ksu")
dev_3.order_log()
print(Developer.__mro__)