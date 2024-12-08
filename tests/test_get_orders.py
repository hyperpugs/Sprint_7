import requests
import json
import pytest
import allure

class TestGetOrders:
    @allure.title("Проверяем успешное получение списка заказов по id курьера")
    def test_get_order_list_returns_body(self, payload):
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'
        login = payload.get("login")
        password = payload.get("password")
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
                                 data={"login": login, "password": password})
        created_courier = response.json()
        courier_id = created_courier['id']
        params = {"courierId" : courier_id}
        response = requests.get("https://qa-scooter.praktikum-services.ru/api/v1/orders", params=params)
        assert response.status_code == 200 and "orders" in response.text


