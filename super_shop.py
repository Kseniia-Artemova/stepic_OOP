class SuperShop:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class StringValue:

    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        allowable_len = range(self.min_length, self.max_length + 1)
        if type(value) is str and len(value) in allowable_len:
            setattr(instance, self.name, value)


class PriceValue:

    def __init__(self, max_value):
        self.min_value = 0
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        allowable_value = range(self.max_value + 1)
        if type(value) in (int, float) and value in allowable_value:
            setattr(instance, self.name, value)


class Product:
    name = StringValue(2, 50)
    price = PriceValue(10_000)

    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == '__main__':

    shop = SuperShop("У Балакирева")
    shop.add_product(Product("Курс по Python", 0))
    shop.add_product(Product("Курс по Python ООП", 2000))
    for p in shop.goods:
        print(f"{p.name}: {p.price}")



