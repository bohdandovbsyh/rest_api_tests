from singlton.singlton_decorator import singleton
from singlton.singlton_metaclass import SingletonMeta


class DbConnector(metaclass=SingletonMeta):

    def __init__(self, db_link, db_password):
        self.db_link = db_link
        self.db_password = db_password


class Human(DbConnector):
    def __init__(self):
        super().__init__(1, 2)


if __name__ == '__main__':
    db_connector_1 = DbConnector('my_db', '123')
    db_connector_2 = DbConnector('789', '563')

    human_1 = Human()
    human_2 = Human()
    print(id(human_1))
    print(id(human_2))
