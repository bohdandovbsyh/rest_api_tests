import requests

from api_t.config_file import BASE_URL, API_KEY


class BaseAPI:
    def __init__(self):
        self.__base_url = BASE_URL
        self.__user = 'Admin'
        self._headers = {'Content-Type': 'application/json', 'api-key': API_KEY}
        self.__request = requests

    def get(self, url, headers=None, params=None):
        print('FROM Base API')
        if headers is None:
            headers = self._headers
        response = self.__request.get(f'{self.__base_url}/{url}', params=params, headers=headers)
        return response

    def post(self, url, body=None, headers=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.post(f'{self.__base_url}/{url}', json=body, headers=headers, params=params)
        return response

    def delete(self):
        ...

    def put(self):
        ...

    def patch(self):
        ...
