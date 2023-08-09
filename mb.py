from ma import Second


class B(Second):
    def __init__(self, var):
        self.var = var
        self.isSecond = 1

    def fnc(self, a, b):
        return a * b * self.var

    def isFirst(self):
        return 0
