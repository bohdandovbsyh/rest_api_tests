import pytest

from data.person_data import Person


@pytest.fixture()
def create_person():
    return Person()
