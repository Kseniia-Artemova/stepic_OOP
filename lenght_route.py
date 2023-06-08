from math import sqrt, pow


class LineTo:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:

    def __init__(self, *args):
        self.lines = [*args]

    def get_path(self):
        return self.lines

    def get_length(self):
        route = 0
        if self.lines:
            x0, y0 = 0, 0
            for line in self.lines:
                x1, y1 = line.x, line.y
                route += sqrt(pow((x1 - x0), 2) + pow((y1 - y0), 2))
                x0, y0 = line.x, line.y

        return route

    def add_line(self, line):
        self.lines.append(line)


if __name__ == '__main__':

    p = PathLines(LineTo(1, 2))
    print(p.get_length())  # 2.23606797749979
    p.add_line(LineTo(10, 20))
    p.add_line(LineTo(5, 17))
    print(p.get_length())  # 28.191631669843197
    m = p.get_path()
    print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

    h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
    print(h.get_length())  # 71.8992593599813

    k = PathLines()
    print(k.get_length())  # 0
    print(k.get_path())  # []