class Book:
    
    book_attr = {"title": str, "author": str, "pages": int, "year": int}

    def __init__(self, title: str = "", author: str = "", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in self.book_attr and type(value) != self.book_attr[key]:
            print(key, type(value), self.book_attr[key])
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)


if __name__ == '__main__':

    book = Book("Python ООП", "Сергей Балакирев", 22, 2022)
    print(book.__annotations__)
