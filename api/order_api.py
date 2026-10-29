import requests
import allure

from urls import API as api

class OrderAPI:
    @allure.step("Отправка запроса на оформление заказа")
    def create_order_request(self, ingredient_id, token):
        response = requests.post(api.create_order_api, json = {"ingredients": ingredient_id}, headers = {'Authorization': token})
        return response

    @allure.step("Отправка запроса на оформление заказа без регистрации")
    def create_order_request_without_login(self, ingredient_id):
        response = requests.post(api.create_order_api, json = {"ingredients": ingredient_id})
        return response
    