import requests
import allure
import generators

from data import Url


class TestLoginCourier:

    @allure.title("Проверяем успешный логин курьера")
    def test_successful_courier_login(self, create_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=create_courier[1])
        courier_id = response.json()
        assert response.status_code == 200 and "id" in courier_id

    @allure.title("Проверяем, что без предварительного создания пользователя приходит ошибка")
    def test_unregistered_courier_login(self):
        login_data = {'login': generators.login_generator(), 'password': generators.password_generator()}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', login_data)
        assert response.status_code == 404 and (response.json()["message"] == 'Учетная запись не найдена')

    @allure.title("Проверяем, что при передаче только логина приходит ошибка")
    def test_courier_login_empty_password_error(self, create_courier):
        data_response = {'login': create_courier[2], 'password': ''}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=data_response)
        assert response.status_code == 400 and (response.json()["message"] == "Недостаточно данных для входа")

    @allure.title("Проверяем, что при передаче только пароля приходит ошибка")
    def test_courier_login_empty_login_error(self, create_courier):
        data_response = {'login': '', 'password': create_courier[3]}
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=data_response)
        assert response.status_code == 400 and (response.json()["message"] == "Недостаточно данных для входа")
