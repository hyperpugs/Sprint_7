import generators

class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'  # Main Url Yandex Scooter
    CREATE_COURIER = 'api/v1/courier'  # Courier account creation handle
    COURIER_LOGIN = 'api/v1/courier/login'  # Courier login handle
    COURIER_DELETE = 'api/v1/courier/'  # Courier Delete handle
    CREATE_ORDER = 'api/v1/orders'  # Order creation handle
    GET_ORDER_LIST = 'api/v1/orders'  # Get order list handle
    ORDER_CANCEL = 'api/v1/orders/cancel?track='  # Order cancel handle
    TRACK_ORDER = '/api/v1/orders/track?t='  # Track order handle

class DataForOrder:
    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-06-06",
        "comment": "Saske, come back to Konoha"
        }
    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]

class DataForRegistration:
    reg_data = [{'password': generators.password_generator(), 'first_name': generators.name_generator()},
                {'login': generators.login_generator(), 'first_name': generators.name_generator()}]
