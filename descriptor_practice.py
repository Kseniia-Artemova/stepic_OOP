class FloatValue:

    @classmethod
    def verify(cls, value):
        if type(value) is not float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:

    def __init__(self, n, m):
        self.cells = [[Cell(0.0) for _ in range(n)] for _ in range(m)]


if __name__ == '__main__':

    table = TableSheet(5, 3)
    values = list(range(1, 16))
    indx = 0
    for column in table.cells:
        for cell in column:
            cell.value = float(values[indx])
            indx += 1

