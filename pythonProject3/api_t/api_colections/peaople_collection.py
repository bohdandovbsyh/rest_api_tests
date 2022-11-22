from api_t.api_colections.base_api import BaseAPI

from api_t.data.person_data import Person


class PeopleAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__person_url = 'api/people'

    def get_person(self, person_id):
        return self.get(f'{self.__person_url}/{person_id}')

    def create_person(self, person_data=None):
        if person_data:
            person = Person()
            person.update_dict(**person_data)
            json_data = person.get_json()
        else:
            json_data = Person().get_json()
        response = self.post(f'{self.__person_url}', body=json_data)
        return response
