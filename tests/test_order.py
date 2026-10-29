import allure

from data import Ingredients as ingredient

@allure.feature("Создание заказа")
class TestOrder:
    @allure.story("Успешное создание заказа")
    @allure.title("Оформление заказа с ингредиентами зарегестрированным пользователем")
    def test_order_with_login_and_ingredients_success(self, login_and_delete, request_order_class, ):
        response = request_order_class.create_order_request(ingredient.list_id_ingredients, login_and_delete)
        r = response.json()
        with allure.step("Проверить успешное создание"):
            assert response.status_code == 200
            assert r["success"] == True
            assert r['order']['number'] != None

    @allure.title("Оформление заказа без авторизации")
    def test_order_without_login_and_ingredients_success(self, request_order_class, ):
        response = request_order_class.create_order_request_without_login(ingredient.list_id_ingredients)
        r = response.json()
        with allure.step("Проверить успешное создание"):
            assert response.status_code == 200
            assert r["success"] == True
            assert r['order']['number'] != None

    @allure.title("Оформление пустого заказа зарегестрированным пользователем")
    def test_order_with_login_without_ingredients_error(self, login_and_delete, request_order_class):
        response = request_order_class.create_order_request([], login_and_delete)
        r = response.json()
        with allure.step("Проверить ошибку"):
            assert response.status_code == 400
            assert r["success"] == False
            assert r["message"] == "Ingredient ids must be provided"

    @allure.title("Оформление заказа с неверным хешом ингридиента зарегестрированным пользователем")
    def test_order_with_login_incorrect_ingredients_error(self, login_and_delete, request_order_class):
        response = request_order_class.create_order_request(ingredient.ingredient_id_incorrect, login_and_delete)
        with allure.step("Проверить ошибку"):
            assert response.status_code == 500    
     