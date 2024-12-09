import requests
import json
import pytest
import allure
from urls import CourierLoginUrls

class TestCourierLogin:
    @allure.title("Проверяем успешный логин курьера")
    def test_login_is_successful(self, payload):
        response = requests.post(CourierLoginUrls.create, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'
        login = payload.get("login")
        password = payload.get("password")
        response = requests.post(CourierLoginUrls.login, data={"login": login, "password": password})
        assert response.status_code == 200 and "id" in response.json()

    @allure.title("Проверяем, что при передаче только логина приходит ошибка")
    def test_login_without_password_returns_error(self, payload):
        response = requests.post(CourierLoginUrls.create, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'
        login = payload.get("login")
        response = requests.post(CourierLoginUrls.login, data={"login": login})
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Проверяем, что при передаче только пароля приходит ошибка")
    def test_login_without_login_returns_error(self, payload):
        response = requests.post(CourierLoginUrls.create, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'
        password = payload.get("password")
        response = requests.post(CourierLoginUrls.login, data={"password": password})
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Проверяем, что без предварительного создания пользователя приходит ошибка, т.к. такого пользователя нет")
    def test_login_nonexistent_user_returns_error(self, payload):
        login = payload.get("login")
        password = payload.get("password")
        response = requests.post(CourierLoginUrls.login, data={"login": login, "password": password})
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

