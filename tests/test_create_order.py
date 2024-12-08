import requests
import json
import pytest
import allure
from urls import OrderUrls


class TestCreateOrder:
    colors = ["", '"color": ["BLACK"]', '"color": ["GREY"]', '"color": ["BLACK", "GREY"]']
    @allure.title("Проверяем успешное создание заказа со всеми обязательными полями и разными комбинациями цветов")
    @pytest.mark.parametrize("color", colors)
    def test_order_is_created(self, order_data, color):
        order_data += color
        order_data = json.dumps(order_data)
        response = requests.post(OrderUrls.order, data=order_data)
        assert response.status_code == 201 and "track" in response.json()