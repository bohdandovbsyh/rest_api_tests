class Hobby:
    def __init__(self, name):
        self.__name = name

    def __call__(self, _class):
        _class.hobby = self.__name
        return _class
