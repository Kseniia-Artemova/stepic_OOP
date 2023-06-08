from random import randint, choice  # функция для генерации целых случайных значений в диапазоне [a; b]


class RandomPassword:

    def __init__(self, psw_chars, min_length, max_length):
        if min_length >= max_length:
            raise ValueError("Минимальное значение должно быть меньше максимального!")
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self):
        number_symbols = randint(self.min_length, self.max_length)
        password = ""
        for _ in range(number_symbols):
            password += choice(self.psw_chars)
        return password


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
pw = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [pw() for _ in range(3)]
print(lst_pass)


def get_password(psw_chars, min_length, max_length):
    if min_length > max_length:
        raise ValueError("Минимальное значение должно быть меньше максимального!")

    def combine():
        password = [choice(psw_chars) for _ in range(randint(min_length, max_length))]
        return "".join(password)

    return combine


gp = get_password(psw_chars, min_length, max_length)
gp_2 = get_password("1234567890", 4, 4)
print(gp(), gp(), gp())
print(gp_2(), gp_2(), gp_2())