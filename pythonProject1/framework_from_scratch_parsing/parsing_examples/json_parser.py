import json
import requests


# request_obj = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?status=available')

# pets_json = request_obj.json()
#
# print(pets_json[0]['id'])

# pets_json = json.loads(request_obj.text)
# print(pets_json)
# print(pets_json[0]['category'])

# my_dict = {'a': None, 'b': True}
#
# convert_to_json = json.dumps(my_dict)
# print(convert_to_json)
#
# print(json.loads(convert_to_json))

class UserData:
    def __init__(self, **kwargs):
        self.user_name = 'Admin'
        self.user_password = 'Admin123'
        self.is_active = True

    def get_dict(self):
        return self.__dict__


user_data = UserData().get_dict()
to_json = json.dumps(user_data)
print(to_json)
c = 0
