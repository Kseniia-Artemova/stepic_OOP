class InputDigits:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        string = self.func()
        try:
            return list(map(int, string.split()))
        except ValueError:
            return string


@InputDigits
def input_dg():
    string = input()
    return string


res = input_dg()
print(res)