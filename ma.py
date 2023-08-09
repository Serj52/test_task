
class MyError(Exception):
    def __str__(self):
        return 'Error text'

class Parent:
    pass

class First(Parent):
    pass

class Second(Parent):
    pass

class A(First):
    def __init__(self):
        self.i = 3
        self._isSecond = 0

    @property
    def isSecond(self):
        return self._isSecond

    @isSecond.setter
    def isSecond(self, new_var):
        if new_var:
            raise AttributeError

    def fnc(self, var):
        if var == 7:
            raise MyError
        return var * 6

    def isFirst(self):
        return 1



