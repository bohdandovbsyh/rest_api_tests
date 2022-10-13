class Park:
    def __init__(self):
        self.__square = 1000
        self.__banches = 100
        self.__fontance = 50

    def __call__(self, is_open):
        if is_open:
            print(f'{self.__class__.__name__} is Opened')
        else:
            print(f'{self.__class__.__name__} is Closed')


if __name__ == '__main__':
    park = Park()
    park(False)
