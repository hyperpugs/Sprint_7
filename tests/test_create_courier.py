import requests
import pytest
import allure
from data import  Url, DataForRegistration


class TestsCreateNewCourier:

    @allure.title("Проверяем, что курьер успешно создан")
    def test_creation_courier_success(self, generate_courier_data):
        registration = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=generate_courier_data[0])
        assert registration.status_code == 201 and (registration.json() == '{"ok":true}')

    @allure.title("Проверяем, что нельзя создать дубликат курьера")
    def test_creation_courier_clone_error(self, create_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier[0])
        assert response.status_code == 409 and (response.json() == 'Этот логин уже используется. Попробуйте другой.')

    @allure.title( "Проверяем, что без передачи логина или пароля  нельзя создать курьера")
    @pytest.mark.parametrize('data_setup', DataForRegistration.reg_data)
    def test_creation_courier_deficit_data_error(self, data_setup):
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', data_setup)
        assert response.status_code == 400 and (response.json() == 'Недостаточно данных для создания учетной записи')
