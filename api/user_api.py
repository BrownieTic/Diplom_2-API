import requests
import allure

from urls import API as api

class CreateUserAPI:
    @allure.step("Отправка запроса на создание пользователя")
    def create_user_request(self, data):
        response = requests.post(api.creating_user_api, json = data)
        return response

    @allure.step("Отправка запроса на удаление пользователя")
    def delete_user_request(self, token):
        response = requests.delete(api.delete_user_api, headers = {'Authorization': token})
        return response

class UserLoginAPI:
    @allure.step("Отправка запроса на авторизацию пользователя")
    def login_request(self, data):
        response = requests.post(api.login_api, json = data)
        return response    