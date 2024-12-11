import requests
import allure
from data import Url


class TestOrdersList:

    @allure.title("Проверяем успешное получение списка заказов")
    def test_successful_get_order_list(self):
        response = requests.get(f'{Url.MAIN_URL}{Url.GET_ORDER_LIST}')
        assert response.status_code == 200 and 'orders' in response.json()
