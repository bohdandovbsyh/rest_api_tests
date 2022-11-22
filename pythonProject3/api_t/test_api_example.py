import time
from http import HTTPStatus
from random import randint

from api_colections.peaople_collection import PeopleAPI
from data.person_data import Person
import json

from waiters import wait_until


def test_get_person_200():
    response = PeopleAPI().get_person(1)
    assert response.status_code == HTTPStatus.OK, f'Status code is not as expected\nActual {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_person_data(create_person):
    expected_person = create_person
    response = PeopleAPI().get_person(1)
    person_data = json.loads(response.text)
    actual_person = Person.from_json(**person_data)
    assert actual_person == expected_person


def test_create_person():
    response = PeopleAPI().create_person({'skin_color': 'black'})


def get_i():
    return randint(0, 25)


def test_wait():
    start = time.time()
    wait_until(lambda: get_i() == 5, message=f'Is not working {get_i()}')
    print('Horray')
    print(time.time() - start)
