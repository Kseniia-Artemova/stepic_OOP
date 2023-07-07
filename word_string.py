class WordString:

    def __init__(self, string=""):
        self._string = string
        self.list_string = string.split()

    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, string):
        self._string = string

    def __len__(self):
        return len(self.list_string)

    def __call__(self, indx):
        return self.list_string[indx]


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")