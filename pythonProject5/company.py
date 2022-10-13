class Company:
    def __init__(self, name, industry):
        self.__name = name
        self.industry = industry

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"This is {self.__name}"
