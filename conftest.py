import pytest

from randomizer import RandomData

from api.user_api import CreateUserAPI
from api.user_api import UserLoginAPI
from api.order_api import OrderAPI

from data import UserData as data

@pytest.fixture(scope="function")
def random_data():
    data = RandomData()
    # генерируем логин, пароль и имя курьера
    login = data.generate_random_string(10)
    password = data.generate_random_string(10)
    name = data.generate_random_string(10)

    # собираем тело запроса
    payload = {
        "email": login+"@yandex.ru",
        "password": password,
        "name": name
    }
    return payload

@pytest.fixture(scope="function")
def request_create_class():
    request = CreateUserAPI()
    return request

@pytest.fixture(scope="function")
def create_user_and_delete(request_create_class, random_data):
    response = request_create_class.create_user_request(random_data)
    token = response.json()["accessToken"]
    yield response
    request_create_class.delete_user_request(token)

@pytest.fixture(scope="function")
def fix_user(request_create_class):
    response = request_create_class.create_user_request(data.USER)
    token = response.json()["accessToken"]
    yield response
    request_create_class.delete_user_request(token)

@pytest.fixture(scope="function")
def request_login_class():
    request = UserLoginAPI()
    return request

@pytest.fixture(scope="function")
def request_order_class():
    request = OrderAPI()
    return request

@pytest.fixture(scope="function")
def login_and_delete(request_create_class, request_login_class, random_data):
    response_create = request_create_class.create_user_request(random_data)
    token = response_create.json()["accessToken"]
    response_login = request_login_class.login_request(random_data)
    yield token
    request_create_class.delete_user_request(token)
