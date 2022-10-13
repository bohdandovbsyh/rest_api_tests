from typing import Type


class Column:
    def __init__(self, name: str, column_type: Type):
        self.__name = name
        self.__column_type = column_type
        self.__value = None

    def __set__(self, instance, value):
        print(instance)
        self.__value = value

    def __get__(self, instance, value):
        print(instance)
        return self.__value


class Table:
    id = Column('id', str)
    name = Column('name', str)


if __name__ == '__main__':
    table = Table()
    table.id = '1'
    table.name = 'John'

    print(table.id)
    print(table.name)
