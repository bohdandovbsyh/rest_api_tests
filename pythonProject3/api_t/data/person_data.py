import json


class Person:
    def __init__(self, **kwargs):
        self.name = 'Luke Skywalker' if 'name' not in kwargs.keys() else kwargs['name']
        self.height = '172' if 'height' not in kwargs.keys() else kwargs['height']
        self.mass = '77' if 'mass' not in kwargs.keys() else kwargs['mass']
        self.hair_color = 'blond' if 'hair_color' not in kwargs.keys() else kwargs['hair_color']
        self.skin_color = 'fair' if 'skin_color' not in kwargs.keys() else kwargs['skin_color']

    @classmethod
    def from_json(cls, **kwargs):
        return cls(**kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_dict(self):
        return self.__dict__

    def update_dict(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_json(self):
        return json.dumps(self.__dict__)
