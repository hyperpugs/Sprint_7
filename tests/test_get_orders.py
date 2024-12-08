import requests
import json
import pytest
import allure
from urls import CourierLoginUrls, OrderUrls

class TestGetOrders:
    @allure.title("Проверяем успешное получение списка заказов по id курьера")
    def test_get_order_list_returns_body(self, payload):
        response = requests.post(CourierLoginUrls.create, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'
        login = payload.get("login")
        password = payload.get("password")
        response = requests.post(CourierLoginUrls.login, data={"login": login, "password": password})
        created_courier = response.json()
        courier_id = created_courier['id']
        params = {"courierId" : courier_id}
        response = requests.get(OrderUrls.order, params=params)
        assert response.status_code == 200 and "orders" in response.text