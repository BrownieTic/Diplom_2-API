import allure
import pytest

from data import UserData as data

@allure.feature("Регистрация")
class TestCreatUser:
    @allure.story("Успешное создание пользователя")
    @allure.title("Создание нового уникального пользователя с корректными данными")
    def test_create_uniq_new_user_success(self, create_user_and_delete):
        response = create_user_and_delete
        with allure.step("Проверить успешное создание пользователя"):
            assert response.status_code == 200
            assert 'accessToken' in response.json()

    @allure.story("Запрос на создание пользователя с некорректными данными")
    @allure.title("Попытка создания дублированного пользователя")
    def test_create_user_duplicate_error(self, create_user_and_delete, request_create_class, random_data):
        response = request_create_class.create_user_request(random_data)
        r = response.json()
        with allure.step("Проверить ошибку"):
            assert response.status_code == 403
            assert r["success"] == False
            assert r["message"] == "User already exists"

    @allure.story("Запрос на создание пользователя без одного из полей")
    @allure.title("Создание пользователя с полями: {user}")
    @pytest.mark.parametrize('user',[
        {"email": data.USER['email'], "password": data.USER['password']},
        {"email": data.USER['email'], "name": data.USER['name']},
        {"password": data.USER['password'], "name": data.USER['name']}
                                     ])
    def test_create_user_without_one_field_error(self, request_create_class, user):
        response = request_create_class.create_user_request(user)
        r = response.json()
        with allure.step("Проверить ошибку"):
            assert response.status_code == 403
            assert r["success"] == False
            assert r["message"] == "Email, password and name are required fields"

@allure.feature("Авторизация")
class TestLoginUser():
    @allure.story("Успешная авторизация пользователя")
    @allure.title("Авторизация существующего пользователя")
    def test_login_user_true_user_success(self, request_login_class, create_user_and_delete, random_data):
        token = create_user_and_delete.json()["accessToken"]
        response_login = request_login_class.login_request(random_data)
        r = response_login.json()
        with allure.step("Проверить успешную авторизацию"):
            assert response_login.status_code == 200
            assert r["success"] == True
            assert random_data['email'] in r["user"]["email"]
            assert random_data['name'] in r["user"]["name"]

    @allure.story("Попытка авторизации с неккоретными данными")
    @allure.title("Вход в аккаунт с полями: {user}")
    @pytest.mark.parametrize('user',[
        {"email": data.USER['email']*2, "password": data.USER['password']},
        {"email": data.USER['email'], "password": data.USER['password']*2},
        {"password": data.USER['password']},
        {"email": data.USER['email']}
                                     ])
    def test_login_user_false_data_error(self, request_login_class, fix_user, user):
        token = fix_user.json()["accessToken"]
        response_login = request_login_class.login_request(user)
        r = response_login.json()
        with allure.step("Проверить ошибку"):
            assert response_login.status_code == 401
            assert r["success"] == False
            assert r["message"] == "email or password are incorrect"

