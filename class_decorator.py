class HandlerGET:

    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        method = request.get("method", "GET")
        information = self.func(request)
        return f"{method}: {information}" if method == 'GET' else None


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


if __name__ == '__main__':
    res = contact({"method": "GET", "url": "contact.html"})
    print(res)

    res_1 = contact({"url": "contact.html"})
    print(res_1)

    res_2 = contact({"method": "POST", "url": "contact.html"})
    print(res_2)