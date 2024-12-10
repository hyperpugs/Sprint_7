import requests
import json
import pytest
import allure
from data import Url, DataForOrder


class TestCreateOrder:

    @allure.title("Проверяем успешное создание заказа")
    @pytest.mark.parametrize('scooter_color', DataForOrder.scooter_color)
    def test_create_order_with_diff_colors(self, scooter_color):
        order_data = DataForOrder.order_data
        order_data['color'] = scooter_color
        order = requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=order_data)
        assert order.status_code == 201 and 'track' in order.json()
        requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}{order.json()['track']}')
