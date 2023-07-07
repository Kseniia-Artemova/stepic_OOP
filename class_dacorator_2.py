# https://stepik.org/lesson/701987/step/11?auth=login&unit=702088

class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            result = list(map(self.render, value.split()))
            return result
        return wrapper


class RenderDigit:

    def __call__(self, string: str):
        try:
            return int(string)
        except ValueError:
            return


@InputValues(RenderDigit())
def input_dg():
    return input()


print(input_dg())