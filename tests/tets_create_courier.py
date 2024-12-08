import requests
import json
import pytest
import allure

class TestCreateCourier:

    @allure.title("Проверяем, что курьер успешно создан")
    def test_courier_is_successfully_created(self, payload):
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data = payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title("Проверяем, что нельзя создать дубликат курьера")
    def test_cannot_create_duplicate_courier(self, payload):
        first_courier = payload
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=first_courier)
        assert response.status_code == 201 and response.text == '{"ok":true}'
        second_courier = first_courier
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=second_courier)
        assert response.status_code == 409 and response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Проверяем, что при передаче только имени (без логина и пароля) нельзя создать курьера")
    def test_only_firstname_returns_error(self, payload):
        firstname = payload.get("firstName")
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier",
                                 data={"firstName": firstname})
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверяем, что при передаче только логина и имени (без  пароля) нельзя создать курьера")
    def test_without_password_returns_error(self, payload):
        login = payload.get("login")
        firstname = payload.get("firstName")
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier",
                                 data={"login": login,
                                       "firstName":firstname})
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверяем, что при передаче только имени и пароля(без логина) нельзя создать курьера")
    def test_without_password_returns_error(self, payload):
        password = payload.get("password")
        firstname = payload.get("firstName")
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier",
                                 data={"password": password,
                                       "firstName": firstname})
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для создания учетной записи"

