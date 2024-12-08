import requests
import json
import pytest
import allure


class TestDeleteCourier:
    @allure.title("Проверяем удаление курьера")
    def test_courier_is_deleted(self, payload):
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'
        login = payload.get("login")
        password = payload.get("password")
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
                                 data={"login": login, "password": password})
        created_courier = response.json()
        courier_id = created_courier['id']
        delete_response = requests.delete("https://qa-scooter.praktikum-services.ru/api/v1/courier/" + str(courier_id))
        assert delete_response.status_code == 200