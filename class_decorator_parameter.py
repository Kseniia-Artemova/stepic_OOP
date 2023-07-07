class Handler:

    def __init__(self, methods=("GET",)):
        self.methods = methods

    def __call__(self, func, *args, **kwargs):
        self.func = func

        def wrapper(request):
            method = request.get("method", "GET")
            if method not in self.methods:
                return None
            return getattr(self, method.lower())(request)

        return wrapper

    def get(self, request):
        return f"GET: {self.func(request)}"

    def post(self, request):
        return f"POST: {self.func(request)}"


@Handler(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"


if __name__ == '__main__':
    res = contact({"method": "GET", "url": "contact.html"})
    print(res)

    res_1 = contact({"url": "contact.html"})
    print(res_1)

    res_2 = contact({"method": "POST", "url": "contact.html"})
    print(res_2)

    res_3 = contact({"method": "DEL", "url": "contact.html"})
    print(res_3)

    assert hasattr(Handler, 'get') and hasattr(Handler, 'post'), "класс Handler должен содержать методы get и post"


    @Handler(methods=('GET', 'POST'))
    def contact2(request):
        return "контакты"

    print(contact2({"method": "POST"}))
    assert contact2({"method": "POST"}) == "POST: контакты", "декорированная функция вернула неверные данные"
    assert contact2({"method": "GET"}) == "GET: контакты", "декорированная функция вернула неверные данные"
    assert contact2({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
    assert contact2(
        {}) == "GET: контакты", "декорированная функция вернула неверные данные при указании пустого словаря"


    @Handler(methods=('POST'))
    def index(request):
        return "index"


    assert index({"method": "POST"}) == "POST: index", "декорированная функция вернула неверные данные"
    assert index({"method": "GET"}) is None, "декорированная функция вернула неверные данные"
    assert index({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"